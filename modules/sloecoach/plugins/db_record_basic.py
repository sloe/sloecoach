
import sloecoach.iplugin

import logging

LOGGER = logging.getLogger("module.sloecoach.plugins.db_record_basic")
LOGGER.setLevel(logging.DEBUG)

class DbRecordBasic(sloecoach.iplugin.IPlugin):

    def update_item(self, db, record):
        LOGGER.debug("Updating item %s", record)

        db_record = {}

        for field, value in record.iteritems():
            if field != "type":
                db_field_name = "f_%s" % field
                db_field = db.scitem.get(db_field_name)
                if not db_field:
                    db_field_name = "f_%s" % field.replace("auto_", "")
                    db_field = db.scitem.get(db_field_name)
                db_record[db_field_name] = value

        db.scitem.insert(**db_record)
        db.commit()
        pass




    METADATA = dict(
        update_methods=dict(item=update_item)
    )
    TYPE="db_record"
