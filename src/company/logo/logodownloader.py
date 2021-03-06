import requests
import uuid
import imghdr
import os
from src.config.config import config
from os.path import abspath, join
from urlparse       import urlparse
from logoexception  import LogoException

class LogoDownloader(object):

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
    def download(url):
        imagedata               = LogoDownloader.requestExternalImageOverHTTP(url)
        extension               = LogoDownloader.determineExtension(imagedata)
        pathToStoreLogoIn       = LogoDownloader.generatePathForImage(extension) 
        pathToWhereLogoIsStored = LogoDownloader.writeTo(pathToStoreLogoIn, imagedata)
        return pathToWhereLogoIsStored

    @staticmethod
    def determineExtension(imageData):
        allowedExtensions = ['png', 'jpeg', 'gif']
        extension = imghdr.what(None, h = imageData)
        if extension in allowedExtensions:
            return extension
        else:
            raise LogoException('Illegal file extension.')

    @staticmethod
    def writeTo(path, imageData):
        with open(path, 'wb') as handle:
            handle.write(imageData)
        return path 

    @staticmethod
    def isDownloadable(logoPath):
        url = urlparse(logoPath) 
        return 'http' in url.scheme

    @staticmethod
    def generatePathForImage(extension = None):
        pathConfigSaysToStoreLogosIn = config.get('company_logo', 'location')
        uniqueFilenameForLogo        = LogoDownloader.generateUniqueFilename(extension)
        pathToStoreLogoIn            = abspath(join(pathConfigSaysToStoreLogosIn, uniqueFilenameForLogo))
        return pathToStoreLogoIn
