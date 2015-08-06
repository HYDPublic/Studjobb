# -*- coding: utf-8 -*-
import time
import os
import requests
import uuid
from ConfigParser import SafeConfigParser
from urlparse     import urlparse
from dimensions   import dimensions

class LogoException(Exception):
    pass

class Logo(object):

    @staticmethod
    def configLocation():
         return os.path.abspath(os.path.join(__file__, '..', '..', '..', 'config'))

    @staticmethod
    def pathToStoreFromConfig():
        config = SafeConfigParser()
        config.read(Logo.configLocation())
        return config.get("company_logo", "location")
        
    @staticmethod
    def generatePathForImage(extension = None):
        pathConfigSaysToStoreLogosIn = Logo.pathToStoreFromConfig()
        uniqueFilenameForLogo = Logo.generateUniqueFilename(extension)
        pathToStoreLogoIn = os.path.abspath(os.path.join(pathConfigSaysToStoreLogosIn, uniqueFilenameForLogo))
        return pathToStoreLogoIn

    @staticmethod
    def generateUniqueFilename(extension = None):
        uniqueHash = uuid.uuid4().urn[9:]
        if extension:
            return uniqueHash + '.' + extension
        else:
            return uniqueHash
    @staticmethod
    def requestExternalImageOverHTTP(url):
        response = requests.get(url, stream = True)
        if not response.ok:
            raise LogoException("Could not download image.")

        # Gather chunks in memory
        chunks = ""
        for chunk in response.iter_content(1024):
            chunks += chunk
        return chunks

    @staticmethod
    def downloadFromURL(url):
        imagedata = Logo.requestExternalImageOverHTTP(url)
        extension = Logo.getExtensionFromURL(url)
        pathToStoreLogoIn = Logo.generatePathForImage(extension) 
        Logo.writeTo(pathToStoreLogoIn, imagedata)
        return True

    @staticmethod
    def writeTo(path, imageData):
        with open(path, 'wb') as handle:
            handle.write(imageData)
        return True

    @staticmethod
    def getExtensionFromURL(url):
        path = urlparse(url).path
        if path.endswith('.png'): return 'png'
        if path.endswith('.gif'): return 'gif'
        if path.endswith('.jpg'): return 'jpg'

    @staticmethod
    def isURL(logoPath):
        url = urlparse(logoPath) 
        return 'http' in url.scheme

    @staticmethod
    def doesNotExist(logoPath):
        return os.path.isfile(logoPath) == False

    @staticmethod
    def isTooWide(width):
        return width > 500

    @staticmethod
    def isTooHigh(height):
        return height > 500
    
    @staticmethod
    def isValid(logoPath):
        if Logo.doesNotExist(logoPath):
            raise LogoException('Logo does not exist.')
        
        try:
            # Try to parse image dimensions
            width, height = dimensions(logoPath)[:2]
        except NotImplementedError:
            raise LogoException("Could not parse logo format.")

        if Logo.isTooWide(width):
            raise LogoException("Logo is too wide.")
        elif Logo.isTooHigh(height):
            raise LogoException("Logo is too high.")

        return True
