
import logging
LOGGER = logging.getLogger("sloecoach.create")
LOGGER.setLevel(logging.DEBUG)

def album():


    grid_field_names = (
        "f_name",
        "f_title",
        "f_event_title",
        "f_event_time",
        "f_location",
        "f_subtree",
        "f_uuid"
    )

    grid_fields = []
    for grid_field_name in grid_field_names:
        grid_field = getattr(db.scalbum, grid_field_name)
        if not grid_field:
            raise Exception("Field not in DB: %s" % grid_fileld_name)
        grid_fields.append(grid_field)

    grid_links = [dict(header="Use as template", body=lambda row: A("Use as template", _href=URL(vars=dict(templateuuid=row.f_uuid))))]

    grid_query = db.scalbum.f_event_title != None

    grid = SQLFORM.grid(
        grid_query,
        fields=grid_fields,
        links = grid_links,
        orderby=db.scalbum.f_subtree)

    form_field_exclude_names = [
        "f_uuid",
        "id"
    ]

    form_field_names = []
    for form_field_name in db.scalbum.fields:
        if not form_field_name.startswith("f_") or form_field_name.startswith("f_fpn_"):
            form_field_exclude_names.append(form_field_name)
        elif form_field_name not in form_field_exclude_names:
            form_field_names.append(form_field_name)

    class __IS_UNIQUE_NAME(object):
        def __init__(self, error_message="Event named {} already exists"):
            self.error_message = error_message

        def __call__(self, value):
            if db(db.scalbum.f_name == value).select().first():
                return value, self.error_message.format(value)
            else:
                return value, None

    db.scalbum.f_name.requires = __IS_UNIQUE_NAME()

    form = SQLFORM(db.scalbum,
                   fields=form_field_names)

    form_template_uuid = request.vars.templateuuid
    if form_template_uuid:
        template_row = db(db.scalbum.f_uuid == form_template_uuid).select().first()
        if template_row:
            for k, v in template_row.as_dict().iteritems():
                if k not in form_field_exclude_names:
                    form.vars[k] = v

    form.vars.f_supremacy = "DB"

    def __form_onvalidation(_form):
        import sloecoach.uuidfactory
        _form.vars.f_uuid = sloecoach.uuidfactory.UuidFactory.create_uuid("ALBUM")

    if form.process(onvalidation=__form_onvalidation).accepted:
        session.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'

    return dict(grid=grid,
                form=form)


def event():
    return album()
