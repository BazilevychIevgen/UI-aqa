# -- coding: utf-8 --
from __future__ import unicode_literals
from GeneralArsenal.Chronicler import log
import requests
import json


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"
__description__ = ""


log.debug('Debug message')
log.info('Info message')
log.error('Error message')
log.warning('Warning message')


resp = requests.get('http://localhost:9333/json')
log.debug(resp.content)
log.debug(type(resp.content))
log.debug(resp.content.decode())
log.debug(type(resp.content.decode()))

# log.debug(json.load(resp.json))
