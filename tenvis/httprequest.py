import httplib
import base64
import string


class Request():
    def __init__(host, username, password):
        self.__auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        self.__webservie = httplib.HTTP(host)


def request(host, url, username, password, message=''):
    # base64 encode the username and password
    auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    webservice = httplib.HTTP(host)
    # write your headers
    webservice.putrequest("POST", url)
    webservice.putheader("Host", host)
    webservice.putheader("User-Agent", "Python http auth")
    webservice.putheader("Content-type", "text/html; charset=\"UTF-8\"")
    webservice.putheader("Content-length", "%d" % len(message))
    # write the Authorization header like: 'Basic base64encode(username + ':' + password)
    webservice.putheader("Authorization", "Basic %s" % auth)
 
    webservice.endheaders()
    webservice.send(message)
    return webservice
    # get the response

def get(host, url, username, password):
    auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    webservice = httplib.HTTP(host)
    webservice.putrequest('GET', url)
    webservice.putheader('Authorization', 'Basic %s' % auth)
    h.endheaders()
    
