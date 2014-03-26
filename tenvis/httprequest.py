import httplib
import base64
import string


class Request():
    def __init__(host, username, password):
        self.__auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        self.__webservie = httplib.HTTP(host)


def request(host, url, user, password, message=''):
    url = "/get_status.cgi"
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
    # get the response
    statuscode, statusmessage, header = webservice.getreply()
    print "Response: ", statuscode, statusmessage
    print "Headers: ", header
    res = webservice.getfile().read()
    print 'Content: ', res
