
from gluon import current
from gluon.html import URL

def make_stack_menu(db, current_stack_id):
    stack_row = db(db.scstack.id == current_stack_id).select().first()
    if stack_row:
        stack_title = current.T("Stack [{f_name}]").format(**stack_row)
    else:
        stack_title = current.T("Stack [None selected]")

    stack_menu = []
    stack_rows = db(db.scstack.id > 0).select()

    for i, stack_row in enumerate(stack_rows):
        stack_menu.append((stack_row.f_name, False, URL(c="select", f="stacksetdefault", args=[stack_row.id], vars=dict(redirect=URL())), []))
        if i > 20:
            # TODO: Untested
            stack_menu.append(("More...", False, URL(c="select", f="stack"), []))
            break

    return stack_title, stack_menu
