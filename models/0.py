from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'SloeCoach'
settings.subtitle = 'Ginuine coaching'
settings.author = 'Sloen Ranger'
settings.author_email = 'sloe@sloecoach.com'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'postgres://postgres:postgres@localhost:5432/sloecoach'
settings.security_key = 'd0f678bd-baa8-4a2a-a081-fa7ae62cf726'
settings.email_server = 'logging'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
