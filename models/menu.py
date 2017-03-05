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
    (T("Create"), False, None, [
        (T("Event"), False, URL("create", "event"), [])
    ]),
    (T("Configuration"), False, None, [
        (T("Stacks"), False, URL("config", "stacks"), [])
    ]),
    (T("Properties"), False, None, [
        (T("Albums"), False, URL("props", "albums"), []),
        (T("GenSpecs"), False, URL("props", "genspecs"), []),
        (T("Items"), False, URL("props", "items"), []),
        (T("OutputSpecs"), False, URL("props", "outputspecs"), []),
        (T("Playlists"), False, URL("props", "playlists"), []),
        (T("Primacies"), False, URL("props", "primacy"), []),
        (T("Remote Items"), False, URL("props", "remoteitems"), []),
        (T("Remote Playlists"), False, URL("props", "remoteplaylists"), []),
        (T("TransferSpecs"), False, URL("props", "transferspecs"), []),
        (T("Worths"), False, URL("props", "worth"), [])
    ]),
    (T("Tasks"), False, None, [
        (T("Read data tree"), False, URL("task", "readtree"), []),
        (T("Read primary footage"), False, URL("task", "readprimary"), []),
        (T("Write data tree"), False, URL("task", "writetree"), [])
    ])
]
