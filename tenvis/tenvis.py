
import httprequest

class Tenvis:


    def __init__(self, ipaddress, port, username, password):

        self.__ipaddress = ipaddress
        self.__port = port
        self.__host = '%s:%s' % (ipaddress, port)
        self.__user = username
        self.__password = password


    def get_status(self):
        httprequest.request(self.__host,
                            '/get_status.cgi',
                            self.__user,
                            self.__password)


