response.title = "Sloecoach"
response.subtitle = "Ginuine coaching"
response.meta.author = ''
response.meta.keywords = ''
response.meta.description = ''
response.menu = [
    (T('Index'), False, URL('default','index'),[]),
    (T('Configuration'), False, None, [
        (T('Stacks'), False, URL('config','stacks'), [])
    ]),
    (T('Properties'), False, None, [
        (T('Item properties'), False, URL('props','items'), [])
    ]),
    (T('Tasks'), False, None, [
        (T('Read primary footage'), False, URL('task','readprimary'), [])
    ])
]
