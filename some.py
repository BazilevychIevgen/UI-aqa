# -- coding: utf-8 --
from __future__ import unicode_literals
from GeneralArsenal.Chronicler import info, debug, error, warning
import requests
from websockets.sync.client import connect


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"
__description__ = ""


"""
debug('Debug message')
info('Info message')
error('Error message')
warning('Warning message')
"""


def getWebSocketDebuggerUrl(carapp_name='carapp_updatecenterlite', port=9333):
    appDebugInfo = requests.get('http://localhost:' + str(port) + '/json').json()
    # debug(appDebugInfo)

    devToolsCred = next((devToolsDict for devToolsDict in appDebugInfo if devToolsDict['title']==carapp_name), None)
    if devToolsCred:
        return devToolsCred['webSocketDebuggerUrl']
    debug('Not found')


if __name__ == '__main__':
    webSocketURL = getWebSocketDebuggerUrl('carapp_updatecenterlite')
    webSocketObject = connect(webSocketURL)
