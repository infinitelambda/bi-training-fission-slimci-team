from pathlib import Path
import os
from log import MyLogger
from functools import wraps
from datetime import datetime
import argparse

import sys

WHO = os.environ['GITHUB_ACTOR']
MY_GITHUB_SECRET = os.environ['my_github_secret']


logger = MyLogger(log_file='sample.log', log_path='logs', name=__name__)


def modified_files():
    '''sample code to return modified files'''
    lf = []
    for root, dirs, files in os.walk('.', topdown=False):
        lf.extend([os.path.join(root, name) for name in files])
    return lf



if __name__ == '__main__':
    logger.debug('Starting Python action')
    logger.debug(f'user: {WHO}\n using: {MY_GITHUB_SECRET}')
    with open('modified_files.txt','r') as f:
        lf = f.read()
    print(lf)
    lf = lf.replace('"','').replace('\n','').replace("'",'')
    lf = lf.split(' ')
    lf = list(filter(lambda x: 'yml' in x or 'yaml' in x, lf))
    print(lf)
    if not lf:
        logger.debug('There were no modified files, using sample code')
        lf = modified_files()

