# -- coding: utf-8 --
from __future__ import unicode_literals
from GeneralArsenal.Chronicler import info, debug, error, warning
import requests
import json


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"
__description__ = ""


debug('Debug message')
info('Info message')
error('Error message')
warning('Warning message')


resp = requests.get('http://localhost:9333/json')
debug(resp.content)
debug(type(resp.content))
debug(resp.content.decode())
debug(type(resp.content.decode()))

# debug(json.load(resp.json))
