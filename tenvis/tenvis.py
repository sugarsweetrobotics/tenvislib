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

    def __value_to_dict(self, val):
        dict = {}
        for var in [s.strip() for s in val.split(';') if len(s.strip()) > 0]:
            key, value = var[var.find('var ') + len('var '):].split('=')
            if value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            dict[key] = value
        return dict

    def __post(self, url):
        return httprequest.request(self.__host,
                                   url,
                                   self.__user,
                                   self.__password)

    def get_status(self):
        """
        HTTP request for get_status.cgi 
        @return Dictionary of tenvis status
        """
        reply = self.__post('/get_status.cgi')
        statuscode, statusmessage, header = reply.getreply()
        res = reply.getfile().read()
        return self.__value_to_dict(reply.getfile().read())

    def get_params(self):
        """
        HTTP request for get_params.cgi 
        @return Dictionary of tenvis status
        """
        reply = self.__post('/get_params.cgi')
        statuscode, statusmessage, header = reply.getreply()
        return self.__value_to_dict(reply.getfile().read())

    def get_camera_params(self):
        """
        HTTP request for get_camera_params.cgi 
        @return Dictionary of tenvis status
        """
        reply = self.__post('/get_params.cgi')
        statuscode, statusmessage, header = reply.getreply()
        return self.__value_to_dict(reply.getfile().read())

    def get_misc(self):
        """
        HTTP request for get_misc.cgi 
        @return Dictionary of tenvis status
        """
        reply = self.__post('/get_misc.cgi')
        statuscode, statusmessage, header = reply.getreply()
        return self.__value_to_dict(reply.getfile().read())

    def videostream(self):
        """
        Start Video Streaming
        """
        reply = self.__post('videostream.cgi')
        statuscode, statusmessage, header = reply.getreply()
        self.__videostream = reply.getfile()

    def __est_param(self, url, param, value):
        reply = httprequest.set(self.__host,
                               url,
                               self.__user,
                               self.__password,
                               param, value)
        statuscode, statusmessage, header = reply.getreply()
        if statuscode != 200:
            # failed
            print statusmessage
        return reply

    def camera_control(self, resolution=8, brightness=127, contrast=3, mode=0, flip_mirror=0):
        """
        camera_control.cgit

        @param resolution 8:QVGA 32:VGA
        @param brightness 0-255
        @param contrast 0-6
        @param mode  0: 50Hz 1: 60Hz 2: Outdoor
        @param flip_mirror 0: default 1: flip 2: mirror 3: flip + mirror
        """
        reply = self.__set_param('camera_control.cgi', 0, resolution)
        reply = self.__set_param('camera_control.cgi', 1, brightness)
        reply = self.__set_param('camera_control.cgi', 2, constrast)
        reply = self.__set_param('camera_control.cgi', 3, mode)
        reply = self.__set_param('camera_control.cgi', 4, flip_mirror)

    def update(self):
        """
        Update video image
        @return Image.Image (PIL) object 
        """
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
