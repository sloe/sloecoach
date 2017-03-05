
import sloecoach.task.readtree
import sloecoach.task.writetree

from gluon.storage import Storage

class Despatchable(Storage):
    def __init__(self, api_name, spec):
        self.api_name = api_name
        self.spec = spec




class Despatcher(object):

    @classmethod
    def execute(self, db, cache, despatchable):
        if despatchable.api_name == 'readtree':
            sloecoach.task.readtree.readtree(db, cache, despatchable.spec)
        elif despatchable.api_name == 'writetree':
            sloecoach.task.writetree.writetree(db, cache, despatchable.spec)

