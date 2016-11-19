

def index():
    return dict()

def items():
    grid = SQLFORM.grid(db.scitem)
    return dict(grid=grid)
