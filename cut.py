from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from setup import *

ffmpeg_extract_subclip(SOURCE_MP4_PATH, 0*60+29, 0*60+40, targetname=OUTPUT_MP4_PATH)

