

import logging

import sloecoach.db.record_template
import sloecoach.iplugin

LOGGER = logging.getLogger("module.sloecoach.plugins.db_record_basic")
LOGGER.setLevel(logging.DEBUG)


class _ItemLoader(sloecoach.db.record_template.RecordTemplate):

    def handle_field_not_found(self, field_name):
        record_auto_name = "auto_%s" % self.field_name_to_record_name(field_name)
        record_value = self.record.get(record_auto_name)
        return record_auto_name, record_value

    def filter_missing_fields(self, missing_fields):
        if not self.record.get("audio_channels"):
            missing_fields = [x for x in missing_fields if not x.startswith("audio_")]

        return missing_fields


class DbRecordBasic(sloecoach.iplugin.IPlugin):

    def update_item(self, db, record):
        LOGGER.debug("Updating item %s", record)

        record_template = _ItemLoader(db, db.scitem, record)

        record_template.enter()


    def update_item_not(self, db, record):
        LOGGER.debug("Updating item %s", record)

        db_record = {}

        unused_from_record = set(record.keys())
        unused_from_record.remove("type")

        missing_fields = []

        for field_name in db.scitem.fields:
            if field_name.startswith("f_"):
                record_name = field_name[2:]
                record_value = record.get(record_name)
                if record_value is not None:
                    unused_from_record.remove(record_name)
                else:
                    record_auto_name = "auto_%s" % record_name
                    record_value = record.get(record_auto_name)
                    if record_value is not None:
                        unused_from_record.remove(record_auto_name)
                    else:
                        missing_fields.append(record_name)

                db_record[field_name] = record_value

        if unused_from_record or missing_fields:
            if not record.get("audio_channels"):
                missing_fields = [x for x in missing_fields if not x.startswith("audio_")]
            message = []
            if unused_from_record:
                message.append("Unused from record: %s" % ", ".join(unused_from_record))
            if missing_fields:
                message.append("Fields missing from record: %s" % ", ".join(missing_fields))
            if message:
                LOGGER.debug("; ".join(message))



        db.scitem.insert(**db_record)
        db.commit()
        pass




    METADATA = dict(
        update_methods=dict(item=update_item)
    )
    TYPE="db_record"
