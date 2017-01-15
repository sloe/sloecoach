

g_treenode_items = (
    Field("f_fpn_filehash", comment="SHA256 of the file backing this item", length=64),
    Field("f_fpn_filepath", comment="Path of file backing this item, within the stack"),
    Field("f_fpn_filesize", "bigint", comment="Size of file backing this item"),
    Field("f_fpn_filemtime", "datetime", comment="Timestamp of file backing this item"),
    Field("f_uuid", comment="Unique identifer", length=64, notnull=True, unique=True)
)


db.define_table(
    'scprimacy',
    Field("f_name", comment="Name of primacy"),
    Field("f_description", comment="Description")
)


db.define_table(
    'scworth',
    Field("f_name", comment="Name of worth"),
    Field("f_description", comment="Description")
)

db.define_table(
    'scalbum',
    Field("f_name", comment="Primary name of item"),

    Field("f_capture_device", comment="Device (camera, etc.) used to capture footage"),
    Field("f_capture_info", comment="Capture details (frame rate, resolution, etc.)"),
    Field("f_event_time", comment="Time of event (free form for display)"),
    Field("f_event_title", comment="Main title for event"),
    Field("f_location", comment="Geographic location of event"),
    Field("f_order", 'double', comment="Tags relevant to the site"),
    Field("f_primacy", "reference scprimacy", comment="Primacy"),
    Field("f_sitetag", comment="Tags relevant to the site"),
    Field("f_source_album_uuid", comment="Source album identifier", length=64),
    Field("f_subevent_title", comment="Subtitle for event"),
    Field("f_subtree", comment="Subtree string"),
    Field("f_tags", comment="Tags relevant to this album"),
    Field("f_title", comment="Title of album"),
    Field("f_worth", "reference scworth", comment="Worth"),
    *g_treenode_items
)


db.define_table(
    'scitem',
    Field("f_leafname", comment="Leafname (filename) of item"),
    Field("f_name", comment="Primary name of item"),
    Field("f_common_id", comment="IDs of related items in common ID format"),
    Field("f_audio_bit_rate", 'double', comment="Audio bit rate (bits per second)"),
    Field("f_audio_channels", 'integer', comment="Number of audio channels"),
    Field("f_audio_codec_name", comment="Name of audio codec"),
    Field("f_audio_duration", 'double', comment="Duration of audio track(s) (seconds)"),
    Field("f_audio_nb_frames", 'bigint', comment="Number of audio frames"),
    Field("f_audio_sample_fmt", comment="Audio sample format"),
    Field("f_audio_sample_rate", 'double', comment="Audio sample rate (samples per second)"),
    Field("f_primacy", "reference scprimacy", comment="Primacy"),
    Field("f_subtree", comment="Subtree string"),
    Field("f_video_avg_frame_rate", comment="Video frame rate (frames per second)"),
    Field("f_video_bit_rate", 'double', comment="Video bit rate (bits per second)"),
    Field("f_video_codec_name", comment="Name of video codec"),
    Field("f_video_duration", 'double', comment="Duration of video track(s) (seconds)"),
    Field("f_video_format_long_name", comment="Name of video format, long"),
    Field("f_video_format_name", comment="Name of video format, short"),
    Field("f_video_height", 'integer', comment="Height of video (pixels)"),
    Field("f_video_level", comment="Level of video codec"),
    Field("f_video_nb_frames", 'bigint', comment="Number of video frames"),
    Field("f_video_pix_fmt", comment="Video pixel format"),
    Field("f_video_size", 'bigint', comment="Video size (bytes)"),
    Field("f_video_width", 'integer', comment="Width of video (pixels)"),
    Field("f_worth", "reference scworth", comment="Worth"),
    *g_treenode_items
)


db.define_table(
    'scstack',
    Field("f_name", comment="Primary name of stack"),
    Field("f_filter_metafile", comment="Filter to select metadata files", default=".ini"),
    Field("f_infopath", comment="Path to root directory of info file tree"),
    Field("f_videopath", comment="Path to root directory of video file tree")
)
