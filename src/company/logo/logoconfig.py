import os
from ConfigParser import SafeConfigParser

class LogoConfig(object):

    @staticmethod
    def configLocation():
         return os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', 'config'))

    @staticmethod
    def urlToLogosFromConfig():
        config = SafeConfigParser()
        config.read(LogoConfig.configLocation())
        return config.get("company_logo", "url")

    @staticmethod
    def pathToStore():
        config = SafeConfigParser()
        config.read(LogoConfig.configLocation())
        return config.get("company_logo", "location")

