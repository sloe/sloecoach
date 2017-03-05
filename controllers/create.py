

def album():



    grid_field_names = [
        "f_name",
        "f_title",
        "f_event_title",
        "f_event_time",
        "f_location",
        "f_subtree",
        "f_uuid"
    ]

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

    form = SQLFORM(db.scalbum)

    form_template_uuid = request.vars.templateuuid
    if form_template_uuid:
        template_row = db(db.scalbum.f_uuid == form_template_uuid).select().first()
        if template_row:
            for k, v in template_row.iteritems():
                if k not in ("id", "f_uuid") and not k.startswith("f_fpn_"):
                    form.vars[k] = v

    if form.process().accepted:
        session.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'

    return dict(grid=grid,
                form=form)


def event():
    return album()
