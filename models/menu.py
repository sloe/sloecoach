response.title = "Sloecoach"
response.subtitle = "Ginuine coaching"
response.meta.author = ""
response.meta.keywords = ""
response.meta.description = ""

import sloecoach.db.stack
stack_title, stack_menu = sloecoach.db.stack.make_stack_menu(db, session.stack_id)

response.menu = [
    (T("Index"), False, URL("default", "index"),[]),
    (stack_title, False, None, stack_menu),

    (T("Configuration"), False, None, [
        (T("Stacks"), False, URL("config", "stacks"), [])
    ]),
    (T("Properties"), False, None, [
        (T("Albums"), False, URL("props", "albums"), []),
        (T("Items"), False, URL("props", "items"), []),
        (T("Primacies"), False, URL("props", "primacy"), []),
        (T("Worths"), False, URL("props", "worth"), [])
    ]),
    (T("Tasks"), False, None, [
        (T("Read data tree"), False, URL("task", "readtree"), []),
        (T("Read primary footage"), False, URL("task", "readprimary"), [])
    ])
]
