
import os

from gluon.storage import Storage

def readtree():
    import sloecoach.db.session
    stack_row = sloecoach.db.session.get_stack_row(db, session)
    if not stack_row:
        redirect(URL('select', 'stack', vars=dict(redirect=URL())))

    import sloecoach.db.despatcher
    import sloecoach.selector

    selector = sloecoach.selector.Selector(
        basename_filters_allow_only=stack_row.f_filter_metafile.split(',')
    )

    despatchable = sloecoach.db.despatcher.Despatchable(
        api_name="readtree",
        spec = Storage(
            metadata_root_path=stack_row.f_infopath,
            name=stack_row.f_name,
            selector=selector
        )
    )

    sloecoach.db.despatcher.Despatcher.execute(db, despatchable)

    return dict()
