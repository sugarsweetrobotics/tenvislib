import Image
import httprequest
import StringIO

class Tenvis:


    def __init__(self, host, username, password):

        #self.__ipaddress = ipaddress
        #self.__port = port
        #self.__host = '%s:%s' % (ipaddress, port)
        self.__host = host
        self.__user = username
        self.__password = password


    def get_status(self):
        reply = httprequest.request(self.__host,
                                    '/get_status.cgi',
                                    self.__user,
                                    self.__password)

        statuscode, statusmessage, header = reply.getreply()
        res = reply.getfile().read()

        # print "Response: ", statuscode, statusmessage
        # print "Headers: ", header
        # print 'Content: ', res
        dict = {}
        for var in [s.strip() for s in res.split(';') if len(s.strip()) > 0]:
            key, value = var[var.find('var ') + len('var '):].split('=')
            if value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            dict[key] = value
        return dict


    def videostream(self):
        reply = httprequest.request(self.__host,
                                    '/videostream.cgi',
                                    self.__user,
                                    self.__password)

        statuscode, statusmessage, header = reply.getreply()
        self.__videostream = reply.getfile()


    def update(self):
        
        while True:
            data = self.__videostream.readline()  
            #print data
            if data[0:15] == 'Content-Length:':  
                count = int(data[16:])  
                s = self.__videostream.read(count)      
                while s[0] != chr(0xff):  
                    s = s[1:]       
                    
                p = StringIO.StringIO(s)  
                # p.getvalue()
                return Image.open(p)
