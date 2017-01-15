
import sloecoach.iplugin

import ConfigParser
import datetime
import hashlib
import logging
import os

LOGGER = logging.getLogger("module.sloecoach.plugins.io_record_ini")
LOGGER.setLevel(logging.DEBUG)

class IoRecordIni(sloecoach.iplugin.IPlugin):
    METADATA = dict(
        format_names=["INI file"],
        read_extensions=[".ini"],
        write_extensions=[".ini"]
    )
    TYPE="io_record"


    @staticmethod
    def io_record_read_fp_fingerprint(ini_fp):
        fstat = os.fstat(ini_fp.fileno())
        ini_data = {}
        ini_data["fpn_filesize"] = fstat.st_size
        ini_data["fpn_filemtime"] = datetime.datetime.fromtimestamp(fstat.st_mtime).replace(microsecond=0)
        ini_data["fpn_filehash"] = hashlib.sha256(ini_fp.read()).hexdigest()
        return ini_data


    @staticmethod
    def io_record_read_fp(ini_fp):
        parser = ConfigParser.RawConfigParser()
        parser.readfp(ini_fp)
        ini_data = {}
        for section in parser.sections():
            ini_data[section] = {}
            for item_name, value in parser.items(section):
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                ini_data[section][item_name] = value

        return ini_data


    @classmethod
    def io_record_read_file_fingerprint(cls, dir_path, dir_subpath, filename):
        filepath = os.path.join(dir_path, dir_subpath, filename)
        with open(filepath) as fp:
            ini_data = cls.io_record_read_fp_fingerprint(fp)
            ini_data["fpn_filepath"] = "/".join((dir_subpath, filename))

        return ini_data


    @classmethod
    def io_record_read_file(cls, dir_path, dir_subpath, filename):
        filepath = os.path.join(dir_path, dir_subpath, filename)
        with open(filepath) as fp:
            ini_data = cls.io_record_read_fp(fp)

        return ini_data
