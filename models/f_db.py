

g_treenode_items = (
    Field('uuid', length=64)
)

db.define_table(
    'scitem',
    g_treenode_items,
    Field("leafname", comment="Leafname (filename) of item"),
    Field("name", comment="Primary name of item"),
    Field("common_id", comment="IDs of related items in common ID format"),
    Field("audio_bit_rate", 'double', comment="Audio bit rate (bits per second)"),
    Field("audio_channels", 'integer', comment="Number of audio channels"),
    Field("audio_codec_name", comment="Name of audio codec"),
    Field("audio_duration", 'double', comment="Duration of audio track(s) (seconds)"),
    Field("audio_nb_frames", 'integer', comment="Number of audio frames"),
    Field("audio_sample_fmt", comment="Audio sample format"),
    Field("audio_sample_rate", 'double', comment="Audio sample rate (samples per second)"),
    Field("video_avg_frame_rate", comment="Video frame rate (frames per second)"),
    Field("video_bit_rate", 'double', comment="Video bit rate (bits per second)"),
    Field("video_codec_name", 'double', comment="Name of video codec"),
    Field("video_duration", 'double', comment="Duration of video track(s) (seconds)"),
    Field("video_format_long_name", comment="Name of video format, long"),
    Field("video_format_name", comment="Name of video format, short"),
    Field("video_height", 'integer', comment="Height of video (pixels)"),
    Field("video_level", comment="Level of video codec"),
    Field("video_nb_frames", 'integer', comment="Number of video frames"),
    Field("video_pix_fmt", comment="Video pixel format"),
    Field("video_size", 'integer', comment="Video size (bytes)"),
    Field("video_width", 'integer', comment="Width of video (pixels)")
)


db.define_table(
    'scstack',
    Field("name", comment="Primary name of stack"),
    Field("infopath", comment="Path to root directory of info file tree"),
    Field("videopath", comment="Path to root directory of video file tree")
)
