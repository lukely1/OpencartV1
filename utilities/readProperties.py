import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + '/configurations/config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = (config.get('commonInfo', 'baseURL'))  # get url from config.ini
        return url

    @staticmethod
    def getUseremail():
        username = (config.get('commonInfo', 'email'))  # get username from config.ini
        return username

    @staticmethod
    def getPassword():
        password = (config.get('commonInfo', 'password'))  # get pwd from config.ini
        return password

# Testing above methods - optional Code
# print(ReadConfig.getApplicationURL())
# print(ReadConfig.getUseremail())
