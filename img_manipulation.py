# -*- coding: utf-8 -*-

from PIL import Image


size_750x300 = (750, 300)
#
img = Image.open('blog/img/maxresdefault.jpg')
img.thumbnail(size_750x300)
img.save('blog/img/750x300/venv.png')
