
from gluon.storage import Storage

def readtree():
    import sloecoach.db.session
    stack_row = sloecoach.db.session.get_stack_row(db, session)
    if not stack_row:
        redirect(URL('select', 'stack', vars=dict(redirect=URL())))

    import sloecoach.db.despatcher

    despatchable = sloecoach.db.despatcher.Despatchable(
        api_name="readtree",
        spec = Storage(
            stack_row=stack_row
        )
    )

    sloecoach.db.despatcher.Despatcher.execute(db, despatchable)

    return dict()
