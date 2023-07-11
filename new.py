# HI Adam
#make gif py python

from PIL import Image, ImageDraw
import glob

frames = []
imgs = glob.glob('adam1.jpeg')

for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)


frames[0].save(
    'my.gif' , format='GIF' , append_images=frames[1:],save_all=True, duration=300, loop=0
