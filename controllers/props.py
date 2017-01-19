

def index():
    return dict()

def albums():
    grid = SQLFORM.grid(db.scalbum)
    return dict(grid=grid)

def genspecs():
    grid = SQLFORM.grid(db.scgenspec)
    return dict(grid=grid)

def items():
    grid = SQLFORM.grid(db.scitem)
    return dict(grid=grid)

def outputspecs():
    grid = SQLFORM.grid(db.scoutputspec)
    return dict(grid=grid)

def playlists():
    grid = SQLFORM.grid(db.scplaylist)
    return dict(grid=grid)

def primacy():
    grid = SQLFORM.grid(db.scprimacy)
    return dict(grid=grid)

def remoteitems():
    grid = SQLFORM.grid(db.scremoteitem)
    return dict(grid=grid)

def remoteplaylists():
    grid = SQLFORM.grid(db.scremoteplaylist)
    return dict(grid=grid)

def transferspecs():
    grid = SQLFORM.grid(db.sctransferspec)
    return dict(grid=grid)

def worth():
    grid = SQLFORM.grid(db.scworth)
    return dict(grid=grid)
