
import sloecoach.task.readtree

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
