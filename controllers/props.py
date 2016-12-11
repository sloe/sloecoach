

def index():
    return dict()

def items():
    grid = SQLFORM.grid(db.scitem)
    return dict(grid=grid)

def primacy():
    grid = SQLFORM.grid(db.scprimacy)
    return dict(grid=grid)

def worth():
    grid = SQLFORM.grid(db.scworth)
    return dict(grid=grid)
