from moviepy.editor import *
from setup import SOURCE_PATH1, SOURCE_PATH2, OUTPUT_PATH, OUTPUT_MP4_PATH


clip1 = VideoFileClip(SOURCE_PATH1)
clip2 = VideoFileClip(SOURCE_PATH2)
final = concatenate_videoclips([clip1, clip2])

final.write_videofile(filename=OUTPUT_MP4_PATH, codec='libx264')
