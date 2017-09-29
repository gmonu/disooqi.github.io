# -*- coding: utf-8 -*-

from PIL import Image


size_750x300 = 16,16
#
img = Image.open('img/ico/blog-icon.gif')



img.thumbnail(size_750x300)
width = img.size[0]
height = img.size[1]
# img_cropped = img.crop(
#     (
#         0,
#         50,
#         width,
#         height-50
#     )
# )
img.save('img/ico/blog-icon_16x16.gif')
