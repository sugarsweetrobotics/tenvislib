
import httprequest

class Tenvis:


    def __init__(self, ipaddress, port, username, password):

        self.__ipaddress = ipaddress
        self.__port = port
        self.__host = '%s:%s' % (ipaddress, port)
        self.__user = username
        self.__password = password


    def get_status(self):
        reply = httprequest.request(self.__host,
                                    '/get_status.cgi',
                                    self.__user,
                                    self.__password)
        statuscode, statusmessage, header = reply.getreply()
        print "Response: ", statuscode, statusmessage
        print "Headers: ", header
        res = reply.getfile().read()
        print 'Content: ', res
        dict = {}
        for var in [s.strip() for s in res.split(';') if len(s.strip()) > 0]:
            key, value = var[var.find('var ') + len('var '):].split('=')
            if value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            dict[key] = value
        return dict



