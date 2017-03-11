
import logging
import uuid

LOGGER = logging.getLogger("module.sloecoach.uuidfactory")
LOGGER.setLevel(logging.DEBUG)


class UuidFactory(object):

    PREFIX_DICT = dict(
        ALBUM="02"
    )


    @classmethod
    def create_uuid(cls, obj_type=None):
        new_uuid = str(uuid.uuid4())
        prefix = cls.PREFIX_DICT.get(obj_type, None)

        if prefix:
            return prefix + new_uuid[len(prefix):]
        else:
            return new_uuid
