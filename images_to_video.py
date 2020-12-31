from setup import *
from moviepy.editor import *

PICT_EXTENSION = '.jpg'
FPS = 24

directory = sorted(os.listdir(WORK_DIR))  # file list in the directory
# print(directory)
clips = [ImageClip(os.path.join(WORK_DIR, filename)).set_duration(1 / FPS)
         for filename in directory
         if filename.endswith(PICT_EXTENSION)]

video = concatenate(clips, method="compose")
video.write_videofile(OUTPUT_MP4_PATH, fps=FPS, codec='libx264')
