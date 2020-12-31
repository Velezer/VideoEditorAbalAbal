from moviepy.editor import *
from setup import *


clip1 = VideoFileClip(SOURCE_PATH1)
clip2 = VideoFileClip(SOURCE_PATH2)
final = concatenate_videoclips([clip1, clip2])

final.write_videofile(filename=OUTPUT_MP4_PATH, codec='libx264')
