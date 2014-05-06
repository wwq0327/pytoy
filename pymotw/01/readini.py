# -*- coding: utf-8 -*-

from ConfigParser import ConfigParser
import os

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'approachrc.ini')

config = ConfigParser()
config.read([filename])

url = config.get('portal', 'url')

print url
