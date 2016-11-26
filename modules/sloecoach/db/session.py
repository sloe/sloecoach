

def get_stack_row(db, session):
    stack_id = session.stack_id
    stack_row = db(db.scstack.id == stack_id).select().first()
    return stack_row



