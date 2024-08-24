# -- coding: utf-8 --
from __future__ import unicode_literals
from Chronicler import info, debug, error, warning
import requests
from websockets.sync.client import connect


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"
__description__ = ""


class EsablishingConnectionToTarget():
    def __init__(self) -> None:
        self.webSocketObject = None
    
    def run(self):
        appDebugInfo = self._getRequest(9333)
        webSocketURL = self._getWebSocketDebuggerUrl(appDebugInfo, 'carapp_updatecenterlite')
        if webSocketURL: self._openWebSocketConnection(webSocketURL)
        self._closeWebSocketCconnection()

    def _getRequest(self, port=9333):
        try:
            appDebugInfo = requests.get('http://localhost:' + str(port) + '/json').json()
        except Exception as _fail:
            error(_fail)
        finally:
            # debug(self.appDebugInfo)
            return appDebugInfo

    def _getWebSocketDebuggerUrl(self, appDebugInfo, carapp_name='carapp_updatecenterlite') -> str:
        devToolsCred = next((devToolsDict for devToolsDict in appDebugInfo if devToolsDict['title']==carapp_name), None)
        if devToolsCred:
            return devToolsCred['webSocketDebuggerUrl']
        debug('Not found')
    
    def _openWebSocketConnection(self, webSocketURL):
        self.webSocketObject = connect(webSocketURL)
    
    def _closeWebSocketCconnection(self):
        self.webSocketObject.close()

    def _sshOpen(self):
        ...
    
    def _sshClose(self):
        ...


if __name__ == '__main__':
    test = EsablishingConnectionToTarget()
    test.run()
