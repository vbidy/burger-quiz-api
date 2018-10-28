'''
Created on 19 avr. 2018

@author: ddegar25
'''
import logging
import os
import json


class ProgramConfiguration(object):
    '''
    Class used to handle and maintain all parameters of this program (timeouts, some other values...
    '''
    _config = None
    _configDir = None
    _logger = logging.getLogger()

    def __init__(self, configFilePath):
        '''
        Constructor
        '''
        if os.path.exists(configFilePath):
            self._configDir = os.path.dirname(configFilePath)
            with open(configFilePath, 'rt') as f:
                self._config = json.load(f)
        else:
            raise Exception("Could not load config file " + configFilePath)
    
    def readEndecaCountriesFile(self):
        '''
        Try to read an existing file wich contains a previously computed list of Endeca apps installed per country
        Return the content of the file as a dict object if exists or None otherwise
        '''
        fileName = "toto"
        countriesFile = os.path.join(self._configDir, fileName)
        if os.path.exists(countriesFile):
            with open(countriesFile, 'rt') as f:
                return json.load(f)
        else:
            return None

    def saveEndecaCountriesFile(self, fileContent):
        '''
        Save the content given in parameter in a file for future readings
        '''
        fileName = "toto"
        countriesFile = os.path.join(self._configDir, fileName)
        with open(countriesFile, 'wt') as f:
            json.dump(fileContent, f, indent = 2)
