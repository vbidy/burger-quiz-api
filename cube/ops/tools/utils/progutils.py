'''
Created on 18 mai 2018

@author: ddegar25
'''
import os
import json
import logging.config
import argparse

memoEnvApps = None
countryDic = None
pgconf = None

def configureLogging(logConfigFile):
    """
    Setup logging configuration
    """
    if os.path.exists(logConfigFile):
        with open(logConfigFile, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
        
# Parse arguments function
def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config-file',
                        required=True,
                        help="External configuration file (JSON format)")
    parser.add_argument('-l', '--log-file',
                        required=True,
                        help="External logging configuration file (JSON format)")
    return parser.parse_args()
