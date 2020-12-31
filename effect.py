from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx
from setup import *

clip = VideoFileClip(SOURCE_MP4_PATH)
clip = clip.fx(vfx.rotate, 45)

clip.write_videofile(filename=OUTPUT_MP4_PATH, codec='libx264')
