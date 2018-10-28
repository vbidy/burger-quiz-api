'''
Created on 18 septembre 2018

This is the main class to launch to run the CUBE Ops OC tools

@author: ddegar25
'''

import logging
from cube.ops.tools.utils import progutils
from cube.ops.tools.configmanager.programconf import ProgramConfiguration
from cube import app,socketio
from cube.ops.tools.configmanager.watcher import ConfigWatcher

logger = logging.getLogger()

if __name__ == "__main__":
    # Handle mandatory arguments
    #args = progutils.parseArguments()
    #configFile = vars(args)['config_file']
    #logConfigFile = vars(args)['log_file']
    #
    ## Configure the whole program (logging, external config files, singletons, ...)
    #progutils.configureLogging(logConfigFile)
    #progutils.pgconf = ProgramConfiguration(configFile)
    #
    ## Start secondary threads
    #configWatcher = ConfigWatcher(configFile)
    #configWatcher.start()
    
    # Launch the Flask app server
    socketio.run(app,port=8080)
    #app.run(host='0.0.0.0', port=8080)
