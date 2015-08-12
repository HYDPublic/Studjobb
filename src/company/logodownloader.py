import requests
import uuid
import os

from urlparse       import urlparse
from logoexception  import LogoException
from logo           import LogoException
from logoconfig     import LogoConfig

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
        extension               = LogoDownloader.getExtensionFromURL(url)
        pathToStoreLogoIn       = LogoDownloader.generatePathForImage(extension) 
        pathToWhereLogoIsStored = LogoDownloader.writeTo(pathToStoreLogoIn, imagedata)
        return pathToWhereLogoIsStored

    @staticmethod
    def writeTo(path, imageData):
        with open(path, 'wb') as handle:
            handle.write(imageData)
        return path 

    @staticmethod
    def getExtensionFromURL(url):
        path = urlparse(url).path
        if path.endswith('.png'): return 'png'
        if path.endswith('.gif'): return 'gif'
        if path.endswith('.jpg'): return 'jpg'

    @staticmethod
    def isDownloadable(logoPath):
        url = urlparse(logoPath) 
        return 'http' in url.scheme

    @staticmethod
    def generatePathForImage(extension = None):
        pathConfigSaysToStoreLogosIn = LogoConfig.pathToStore()
        uniqueFilenameForLogo        = LogoDownloader.generateUniqueFilename(extension)
        pathToStoreLogoIn            = os.path.abspath(os.path.join(pathConfigSaysToStoreLogosIn, uniqueFilenameForLogo))
        return pathToStoreLogoIn