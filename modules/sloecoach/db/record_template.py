
import logging

LOGGER = logging.getLogger("module.sloecoach.db.record_template")
LOGGER.setLevel(logging.DEBUG)

class RecordTemplate(object):
    def __init__(self, db, target_db, record):
        self.db = db
        self.target_db = target_db
        self.record = record
        self.used = False


    def init_db_record(self):
        self.db_record = {}


    def init_unused_from_record(self):
        self.unused_from_record = set(self.record.keys())
        if "type" in self.unused_from_record:
            self.unused_from_record.remove("type")


    def init_missing_fields(self):
        self.missing_fields = []


    def filter_field_name(self, field_name):
        return field_name.startswith("f_")


    def field_name_to_record_name(self, field_name):
        return field_name[2:]


    def handle_field_not_found(self, field_name):
        return None, None


    def handle_db_field(self, field_name):
        record_name = self.field_name_to_record_name(field_name)
        consumed_record_name = record_name
        record_value = self.record.get(record_name)
        if record_value is None:
            consumed_record_name, record_value = self.handle_field_not_found(field_name)

        if record_value is None:
            self.missing_fields.append(record_name)
        else:
            self.unused_from_record.remove(consumed_record_name)

        return record_value


    def iterate_db_fields(self):
        for field_name in self.target_db.fields:
            if self.filter_field_name(field_name):
                self.db_record[field_name] = self.handle_db_field(field_name)


    def adjust_db_fields(self):
        pass


    def filter_unused_from_record(self, unused_from_record):
        return unused_from_record


    def filter_missing_fields(self, missing_fields):
        return missing_fields


    def _get_object_name(self):
        name_fields = ("f_name", "f_leafname", "f_uuid")
        name = "<unknown>"
        for name_field in name_fields:
            name = self.db_record.get(name_field)
            if name:
                break
        return name


    def generate_log_message(self, unused_from_record, missing_fields):
        message = []
        if unused_from_record or missing_fields:
            name = self._get_object_name()

            if unused_from_record:
                unused_from_record = self.filter_unused_from_record(self.unused_from_record)
            if missing_fields:
                missing_fields = self.filter_missing_fields(self.missing_fields)

            if unused_from_record:
                message.append("Unused from record for %s \"%s\": %s" % (self.NAME, name, ", ".join(sorted(unused_from_record))))
            if missing_fields:
                message.append("Fields missing from record for %s \"%s\": %s" % (self.NAME, name, ", ".join(sorted(missing_fields))))
        return message


    def output_log_message(self, message):
        if message:
            LOGGER.debug(";\n  ".join(message))


    def update_or_insert_item(self):
        item_uuid = self.db_record.get("f_uuid")
        if not item_uuid:
            raise Exception("UUID missing from record item %s" % self.db_record)
        else:
            existing_row = self.db(self.target_db.f_uuid == item_uuid).select(for_update=True).first()
            if not existing_row:
                self.target_db.insert(**self.db_record)
            else:
                fpn_fields = [x for x in self.target_db.fields if x.startswith("f_fpn_")]
                is_match = True
                for fpn_field in fpn_fields:
                    existing_value = existing_row.get(fpn_field)
                    new_value = self.db_record.get(fpn_field)
                    if not existing_value or existing_value != new_value:
                        LOGGER.debug("Fingerprint mismatch for %s, existing %s != new %s", fpn_field, existing_value, new_value)
                        is_match = False
                        break

                if is_match:
                    pass # Match, so update not required
                else:
                    existing_row.update_record(**self.db_record)



    def commit_db(self):
        self.db.commit()


    def enter(self):
        if self.used:
            raise Exception("RecordTemplate reentered.  Object is single use")
        self.used = True

        self.init_db_record()
        self.init_unused_from_record()
        self.init_missing_fields()
        self.iterate_db_fields()
        self.adjust_db_fields()
        message = self.generate_log_message(self.unused_from_record, self.missing_fields)
        self.output_log_message(message)
        self.update_or_insert_item()
        self.commit_db()
