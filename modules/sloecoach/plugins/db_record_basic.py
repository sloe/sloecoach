

import logging

import sloecoach.db.record_template
import sloecoach.iplugin

LOGGER = logging.getLogger("module.sloecoach.plugins.db_record_basic")
LOGGER.setLevel(logging.DEBUG)


class _TreeLoader(sloecoach.db.record_template.RecordTemplate):
    NAME="<not set>"

    def __init__(self, db, target_db, record, dir_subpath):
        sloecoach.db.record_template.RecordTemplate.__init__(self, db, target_db, record)
        self.dir_subpath = dir_subpath


    def adjust_db_fields(self):
        _db = self.db

        # Derive primacy and worth from the path
        split_subpath = self.dir_subpath.split("/")
        if len(split_subpath) == 1:
            primacy_name, worth_name, subtree = split_subpath[0], None, None
        elif len(split_subpath) == 2:
            primacy_name, worth_name, subtree = split_subpath[0], split_subpath[1], None
        else:
            primacy_name, worth_name, subtree = split_subpath[0], split_subpath[1], split_subpath[2:]

        if primacy_name and worth_name:
            for count in range(2):
                primacy_row = _db(_db.scprimacy.f_name == primacy_name).select(_db.scprimacy.id).first()
                worth_row = _db(_db.scworth.f_name == worth_name).select(_db.scworth.id).first()

                if primacy_row and worth_row:
                    break

                if count > 0:
                    raise Exception("Unknown primacy ('%s') or worth ('%s')" % (primacy_name, worth_name))
                # Shouldn't be missing so make sure basic configuration is in the database
                import sloecoach.db.ensure_basis
                sloecoach.db.ensure_basis.ensure_basis(_db)

            self.db_record.update(dict(
                f_primacy=primacy_row.id,
                f_worth=worth_row.id,
                f_subtree=subtree
            ))
        else:
            self.db_record.update(dict(
                f_primacy=None,
                f_worth=None,
                f_subtree=None
            ))


class _AlbumLoader(_TreeLoader):
    NAME = "album"

    def __init__(self, db, target_db, record, dir_subpath):
        _TreeLoader.__init__(self, db, target_db, record, dir_subpath)


    def filter_missing_fields(self, missing_fields):
        removeables = ("capture_device", "capture_info", "event_time", "event_title",
                       "location", "order", "primacy", "sitetag", "source_album_uuid",
                       "subevent_title", "subtree", "tags", "worth")
        missing_fields = [x for x in missing_fields if x not in removeables]

        return missing_fields


class _GenSpecLoader(sloecoach.db.record_template.RecordTemplate):
    NAME = "genspec"

    def __init__(self, db, target_db, record, dir_subpath):
        sloecoach.db.record_template.RecordTemplate.__init__(self, db, target_db, record)



class _ItemLoader(_TreeLoader):
    NAME = "item"

    def __init__(self, db, target_db, record, dir_subpath):
        _TreeLoader.__init__(self, db, target_db, record, dir_subpath)


    def handle_field_not_found(self, field_name):
        record_auto_name = "auto_%s" % self.field_name_to_record_name(field_name)
        record_value = self.record.get(record_auto_name)
        return record_auto_name, record_value


    def filter_missing_fields(self, missing_fields):
        removeables = ("common_id", "primacy", "subtree", "worth")
        missing_fields = [x for x in missing_fields if x not in removeables]
        if not self.record.get("audio_channels"):
            missing_fields = [x for x in missing_fields if not x.startswith("audio_")]

        return missing_fields


class _OutputSpecLoader(sloecoach.db.record_template.RecordTemplate):
    NAME = "outputspec"

    def __init__(self, db, target_db, record, dir_subpath):
        sloecoach.db.record_template.RecordTemplate.__init__(self, db, target_db, record)


class _PlaylistLoader(_TreeLoader):
    NAME = "playlist"

    def __init__(self, db, target_db, record, dir_subpath):
        _TreeLoader.__init__(self, db, target_db, record, dir_subpath)

    def filter_missing_fields(self, missing_fields):
        removeables = ("selector_genspec_name", "primacy", "subtree", "worth")
        missing_fields = [x for x in missing_fields if x not in removeables]

        return missing_fields


class _RemoteItemLoader(_TreeLoader):
    NAME = "remoteitem"

    def __init__(self, db, target_db, record, dir_subpath):
        _TreeLoader.__init__(self, db, target_db, record, dir_subpath)


    def filter_missing_fields(self, missing_fields):
        removeables = ("primacy", "subtree", "worth")
        missing_fields = [x for x in missing_fields if x not in removeables]

        return missing_fields


class _RemotePlaylistLoader(_TreeLoader):
    NAME = "remoteplaylist"

    def __init__(self, db, target_db, record, dir_subpath):
        _TreeLoader.__init__(self, db, target_db, record, dir_subpath)


    def filter_missing_fields(self, missing_fields):
        removeables = ("primacy", "subtree", "worth")
        missing_fields = [x for x in missing_fields if x not in removeables]

        return missing_fields


class _TransferSpecLoader(sloecoach.db.record_template.RecordTemplate):
    NAME = "transferspec"

    def __init__(self, db, target_db, record, dir_subpath):
        sloecoach.db.record_template.RecordTemplate.__init__(self, db, target_db, record)


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
            ("junk", "Junk footage where loss is not important")):
            db.scworth.update_or_insert(db.scworth.f_name == name, f_name=name, f_description=description)

        db.commit()


    def update_album(self, db, record, dir_subpath):
        record_template = _AlbumLoader(db, db.scalbum, record, dir_subpath)
        record_template.enter()


    def update_genspec(self, db, record, dir_subpath):
        record_template = _GenSpecLoader(db, db.scgenspec, record, dir_subpath)
        record_template.enter()


    def update_item(self, db, record, dir_subpath):
        record_template = _ItemLoader(db, db.scitem, record, dir_subpath)
        record_template.enter()


    def update_outputspec(self, db, record, dir_subpath):
        record_template = _OutputSpecLoader(db, db.scoutputspec, record, dir_subpath)
        record_template.enter()


    def update_playlist(self, db, record, dir_subpath):
        record_template = _PlaylistLoader(db, db.scplaylist, record, dir_subpath)
        record_template.enter()


    def update_remoteitem(self, db, record, dir_subpath):
        record_template = _RemotePlaylistLoader(db, db.scremoteitem, record, dir_subpath)
        record_template.enter()


    def update_remoteplaylist(self, db, record, dir_subpath):
        record_template = _RemotePlaylistLoader(db, db.scremoteplaylist, record, dir_subpath)
        record_template.enter()


    def update_transferspec(self, db, record, dir_subpath):
        record_template = _TransferSpecLoader(db, db.sctransferspec, record, dir_subpath)
        record_template.enter()


    METADATA = dict(
        update_methods=dict(
            album=update_album,
            genspec=update_genspec,
            item=update_item,
            outputspec=update_outputspec,
            playlist=update_playlist,
            remoteitem=update_remoteitem,
            remoteplaylist=update_remoteplaylist,
            transferspec=update_transferspec
        )
    )
    TYPE="db_record"
