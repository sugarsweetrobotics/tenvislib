import httplib
import base64
import string


class Request():
    def __init__(host, username, password):
        self.__auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        self.__webservie = httplib.HTTP(host)


def request(host, url, username, password, message=''):
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

    vars = res.split(';')
    dict = {}
    for var in vars:
        print var.split()
        key, val = var.split()[1].split('=')
        dict[key] = val
    print dict
    return dict
    """
var id='00656E527CC2';
var sys_ver='Ver 1.8';
var app_ver='Ver 1.7.22';
var alias='IPCamera';
var now=1395800231;
var tz=-28800;
var alarm_status=0;
var ddns_status=200;
var ddns_host='mytenvis.org';
var oray_type=0;
var upnp_status=4;
var p2p_status=0;
var p2p_local_port=25414;
var msn_status=0;
"""
