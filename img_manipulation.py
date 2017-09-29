# -*- coding: utf-8 -*-

from PIL import Image


size_750x300 = 750,300
#
img = Image.open('blog/img/maxresdefault.jpg')



img.thumbnail(size_750x300)
width = img.size[0]
height = img.size[1]
img_cropped = img.crop(
    (
        0,
        50,
        width,
        height-50
    )
)
img_cropped.save('blog/img/750x300/venv.png')
