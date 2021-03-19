import configparser
config = configparser.RawConfigParser()
config.read("C:\mygit-hub_projects\ruttl_QA\Configuration\config.py")

class ReadConfig:
    @staticmethod
    def getURL():
        url= config.get('BASEURL')
        return url