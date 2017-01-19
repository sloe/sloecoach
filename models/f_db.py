

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
    Field("f_name", comment="Primary name of album"),

    Field("f_capture_device", comment="Device (camera, etc.) used to capture footage"),
    Field("f_capture_info", comment="Capture details (frame rate, resolution, etc.)"),
    Field("f_event_time", comment="Time of event (free form for display)"),
    Field("f_event_title", comment="Main title for event"),
    Field("f_location", comment="Geographic location of event"),
    Field("f_order", comment="Ordering used within this album"),
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
    'scgenspec',
    Field("f_name", comment="Primary name of genspec"),
    Field("f_aftereffects_outputcomp", comment="After Effects output composition"),
    Field("f_aftereffects_outputfilename", comment="After Effects output filename"),
    Field("f_aftereffects_outputmodule", comment="After Effects output module"),
    Field("f_aftereffects_project", comment="After Effects output project"),
    Field("f_gen_type", comment="GenSpec type"),
    Field("f_input_conformed_frame_rate", comment="Frame rate to assume for input before processing"),
    Field("f_output_description", comment="Description of output"),
    Field("f_output_extension", comment="File extension of output file"),
    Field("f_output_frame_rate", comment="Frame rate of output"),
    Field("f_output_frames_per_input_frame", comment="Number of output frames per input frame"),
    Field("f_output_note", comment="Notes"),
    Field("f_output_short_description", comment="Short form description"),
    Field("f_output_suffix", comment="Output suffix"),
    Field("f_priority", 'double', comment="Priority when processing"),
    Field("f_speed_factor", comment="Ratio of playback speed output/input"),

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
    'scoutputspec',
    Field("f_name", comment="Primary name of outputspec"),

    Field("f_genspec_name", comment="Name of genspec to use to create output"),
    Field("f_glob_include", comment="Glob expression to select input"),
    Field("f_output_path", comment="Path for output"),
    Field("f_priority", 'double', comment="Priority when processing"),
    *g_treenode_items
)


db.define_table(
    'scplaylist',
    Field("f_name", comment="Primary name of playlist"),
    Field("f_primacy", "reference scprimacy", comment="Primacy"),
    Field("f_priority", 'double', comment="Priority when processing"),
    Field("f_selector_genspec_name", comment="Selector to apply to genspec"),
    Field("f_subtree", comment="Subtree string"),
    Field("f_title", comment="Item title"),
    Field("f_transfer_type", comment="Type of transfer"),
    Field("f_youtube_description", comment="Youtube description"),
    Field("f_youtube_privacy", comment="Youtube privacy"),
    Field("f_youtube_tags", comment="Youtube tags, comma separated"),
    Field("f_youtube_title", comment="Youtube title"),
    Field("f_worth", "reference scworth", comment="Worth"),
    *g_treenode_items
)


db.define_table(
    'scremoteitem',
    Field("f_name", comment="Primary name of item"),
    Field("f_common_id", comment="IDs of related items in common ID format"),
    Field("f_description", comment="Description"),
    Field("f_primacy", "reference scprimacy", comment="Primacy"),
    Field("f_remote_id", comment="ID of remote item"),
    Field("f_remote_url", comment="URL of remote item"),
    Field("f_subtree", comment="Subtree string"),
    Field("f_title", comment="Title of remote item"),
    Field("f_worth", "reference scworth", comment="Worth"),
    *g_treenode_items
)


db.define_table(
    'scremoteplaylist',
    Field("f_name", comment="Primary name of playlist"),

    Field("f_common_id", comment="IDs of related items in common ID format"),
    Field("f_description", comment="Description"),
    Field("f_primacy", "reference scprimacy", comment="Primacy"),
    Field("f_remote_id", comment="ID of remote playlist"),
    Field("f_remote_url", comment="URL of remote playlist"),
    Field("f_subtree", comment="Subtree string"),
    Field("f_title", comment="Title of remote playlist"),
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


db.define_table(
    'sctransferspec',
    Field("f_name", comment="Primary name of transfer spec"),

    Field("f_priority", 'double', comment="Priority when processing"),
    Field("f_selectors", comment="Selector to choose items"),
    Field("f_transfer_type", comment="Type of transfer"),
    Field("f_youtube_category", comment="Youtube category"),
    Field("f_youtube_description", comment="Youtube description"),
    Field("f_youtube_privacy", comment="Youtube privacy"),
    Field("f_youtube_tags", comment="Youtube tags, comma separated"),
    Field("f_youtube_title", comment="Youtube title"),
    *g_treenode_items
)