

import logging

import sloecoach.db.record_template
import sloecoach.iplugin

LOGGER = logging.getLogger("module.sloecoach.plugins.db_record_basic")
LOGGER.setLevel(logging.DEBUG)


class _ItemLoader(sloecoach.db.record_template.RecordTemplate):

    def __init__(self, db, target_db, record, dir_subpath):
        sloecoach.db.record_template.RecordTemplate.__init__(self, db, db.scitem, record)
        self.dir_subpath = dir_subpath


    def handle_field_not_found(self, field_name):
        record_auto_name = "auto_%s" % self.field_name_to_record_name(field_name)
        record_value = self.record.get(record_auto_name)
        return record_auto_name, record_value


    def adjust_db_fields(self):
        _db = self.db
        split_subpath = self.dir_subpath.split("/")
        primacy_name, worth_name, subtree = split_subpath[0], split_subpath[1], split_subpath[2:]

        for count in range(2):
            primacy_row = _db(_db.scprimacy.f_name == primacy_name).select(_db.scprimacy.id).first()
            worth_row = _db(_db.scworth.f_name == worth_name).select(_db.scworth.id).first()

            if primacy_row and worth_row:
                break

            if count > 0:
                raise Exception("Unknown primacy ('%s') or worth ('%s')" % (primacy_name, worth_name))
            import sloecoach.db.ensure_basis
            sloecoach.db.ensure_basis.ensure_basis(_db)

        self.db_record.update(dict(
            f_primacy=primacy_row.id,
            f_worth=worth_row.id,
            f_subtree=subtree
        ))


    def filter_missing_fields(self, missing_fields):
        removeables = ("primacy", "subtree", "worth")
        missing_fields = [x for x in missing_fields if x not in removeables]
        if not self.record.get("audio_channels"):
            missing_fields = [x for x in missing_fields if not x.startswith("audio_")]

        return missing_fields


class DbRecordBasic(sloecoach.iplugin.IPlugin):

    def ensure_basis(self, db):
        LOGGER.info("Ensuring that basic entries are present in database")

        for name, description in (
            ("capture", "Captured footage"),
            ("primary", "Pristine footage used for generating releaseable (final) footage"),
            ("final", "End product footage for distribution")):
            db.scprimacy.update_or_insert(db.scprimacy.f_name == name, f_name=name, f_description=description)

        for name, description in (
            ("precious", "Footage that cannot be recreated"),
            ("derived", "Footage that can be recreated, typically derived from other footage"),
            ("junk", "Junk footage where loos is not important")):
            db.scworth.update_or_insert(db.scworth.f_name == name, f_name=name, f_description=description)

        db.commit()


    def update_item(self, db, record, dir_subpath):
        LOGGER.debug("Updating item %s", record)
        record_template = _ItemLoader(db, db.scitem, record, dir_subpath)
        record_template.enter()


    METADATA = dict(
        update_methods=dict(item=update_item)
    )
    TYPE="db_record"
