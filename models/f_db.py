

g_treenode_items = (
    Field("f_uuid", length=64)
)

db.define_table(
    'scitem',
    g_treenode_items,
    Field("f_leafname", comment="Leafname (filename) of item"),
    Field("f_name", comment="Primary name of item"),
    Field("f_common_id", comment="IDs of related items in common ID format"),
    Field("f_audio_bit_rate", 'double', comment="Audio bit rate (bits per second)"),
    Field("f_audio_channels", 'integer', comment="Number of audio channels"),
    Field("f_audio_codec_name", comment="Name of audio codec"),
    Field("f_audio_duration", 'double', comment="Duration of audio track(s) (seconds)"),
    Field("f_audio_nb_frames", 'integer', comment="Number of audio frames"),
    Field("f_audio_sample_fmt", comment="Audio sample format"),
    Field("f_audio_sample_rate", 'double', comment="Audio sample rate (samples per second)"),
    Field("f_video_avg_frame_rate", comment="Video frame rate (frames per second)"),
    Field("f_video_bit_rate", 'double', comment="Video bit rate (bits per second)"),
    Field("f_video_codec_name", 'double', comment="Name of video codec"),
    Field("f_video_duration", 'double', comment="Duration of video track(s) (seconds)"),
    Field("f_video_format_long_name", comment="Name of video format, long"),
    Field("f_video_format_name", comment="Name of video format, short"),
    Field("f_video_height", 'integer', comment="Height of video (pixels)"),
    Field("f_video_level", comment="Level of video codec"),
    Field("f_video_nb_frames", 'integer', comment="Number of video frames"),
    Field("f_video_pix_fmt", comment="Video pixel format"),
    Field("f_video_size", 'integer', comment="Video size (bytes)"),
    Field("f_video_width", 'integer', comment="Width of video (pixels)")
)


db.define_table(
    'scstack',
    Field("f_name", comment="Primary name of stack"),
    Field("f_infopath", comment="Path to root directory of info file tree"),
    Field("f_videopath", comment="Path to root directory of video file tree")
)
