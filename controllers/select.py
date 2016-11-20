
def stack():
    return dict(message="Please select a stack")


def stacksetdefault():
    if request.args:
        stack_id = int(request.args[0])
        stack_row = db(db.scstack.id == stack_id).select().first()
        if stack_row:
            session.stack_id = stack_id
            session.flash = "Selected stack '{f_name}'".format(**stack_row)
        else:
            raise HTTP(404, "Stack ID {0} not found".format(stack_id))

    if request.vars.redirect:
        redirect(request.vars.redirect)
    else:
        redirect(URL(c="default", f="index"))
