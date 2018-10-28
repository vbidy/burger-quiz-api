# -*- coding: utf-8 -*-

'''
Created on 18 mai 2018

@author: ddegar25
'''
import threading
import logging
import os
import time
from cube.ops.tools.configmanager.programconf import ProgramConfiguration
from cube.ops.tools.utils import progutils

class ConfigWatcher(threading.Thread):
    '''
    This handler will be used to watch configuration file changes and 
    reload the configuration if needed.
    '''
    _configFile = None
    _logger = None
    
    '''
    This thread checks whether configuration file has changed.
    The check is performed once per hour
    '''
    def __init__(self, configFile):
        '''
        Constructor
        '''
        threading.Thread.__init__(self) # Mandatory when using threading !!!
        self._configFile = configFile
        self._logger = logging.getLogger("Configuration Watcher")
    
    def run(self):
        '''
        The process that is called when the thread is started
        '''
        self._logger.info("Thread started and running.")
        # Watch for config file changes and when there are updates, reload the config 
        if os.path.exists(self._configFile):
            cachedStamp = os.stat(self._configFile).st_mtime
            while True:
                if os.path.exists(self._configFile):
                    stamp = os.stat(self._configFile).st_mtime
                    # File has changed, do something
                    if stamp != cachedStamp:
                        self._logger.info("Found that the configuration file has changed. Previous timestamp was: " 
                                          + str(cachedStamp) + ". New one is " + str(stamp) + ". Reloading configuration.")
                        cachedStamp = stamp
                        progutils.pgconf = ProgramConfiguration(self._configFile)
                time.sleep(3600)