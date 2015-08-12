import PIL
from PIL import Image
import os

from logoexception  import LogoException

class LogoRescaler(object):

    @staticmethod
    def rescale(path = None, newPath = None, width = None, height = None):
        img = Image.open(path)

        if height is None and width is not None:
            basewidth = width
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize))

        if width is None and height is not None:
            baseheight = height 
            hpercent = (baseheight / float(img.size[1]))
            wsize = int((float(img.size[0]) * float(hpercent)))
            img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
        
        if newPath is not None:
            path = newPath
        
        LogoRescaler.save(img, path)

    @staticmethod
    def save(img, path):
        img.save(path)
