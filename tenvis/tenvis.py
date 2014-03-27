import Image
import httprequest
import StringIO

class Tenvis:


    def __init__(self, host, username, password):
        self.__host = host
        self.__user = username
        self.__password = password

    def __value_to_dict(self, val):
        dic = {}
        for var in [s.strip() for s in val.split(';') if len(s.strip()) > 0]:
            key, value = var[var.find('var ') + len('var '):].split('=')
            if value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            dic[key] = value
        return dic

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
        reply = self.__post('/get_camera_params.cgi')
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
        reply = self.__post('/videostream.cgi')
        statuscode, statusmessage, header = reply.getreply()
        self.__videostream = reply.getfile()

    UP = 0
    STOP_UP = 1
    DOWN = 2
    STOP_DOWN = 3
    LEFT = 4
    STOP_LEFT = 5
    RIGHT = 6
    STOP_RIGHT = 7
    CENTER = 25
    VERTICAL_PATROL = 26
    STOP_VERTICAL_PATROL = 27
    HORIZONTAL_PATROL = 28
    STOP_HORIZONTAL_PATROL = 29
    IO_OUTPUT_HIGH = 94
    IO_OUTPUT_LOW = 95
    
    def decoder_control(self, command):
        """
        0 up 
        1 Stop up
        2 down
        3 Stop down
        4 left
        5 Stop left
        6 right
        7 Stop right
        25 center
        26 Vertical patrol
        27 Stop vertical patrol
        28 Horizon patrol
        29 Stop horizon patrol
        94 IO output high
        95 IO output low
        """
        url = url + '?command=%s' % command
        reply = httprequest.request(self.__host,
                                url, 
                               self.__user,
                               self.__password)
        statuscode, statusmessage, header = reply.getreply()
        if statuscode != 200:
            print ' - Requesting %s failed: %s' % (url, statusmessage)
        return reply
        
    def __set_param(self, url, param, value):
        url = url + '?param=%s&value=%s' % (param, value)
        reply = httprequest.set(self.__host,
                                url, 
                               self.__user,
                               self.__password,
                               param, value)
        statuscode, statusmessage, header = reply.getreply()
        if statuscode != 200:
            print ' - Requesting %s failed: %s' % (url, statusmessage)
        return reply

    QVGA = 8
    VGA = 32

    FIFTY_HELZ = 0
    SIXTY_HELZ = 1
    OUTDOOR = 2
    
    FLIP_DEFAULT = 0
    FLIP = 1
    MIRROR = 2
    FLIP_MIRROR = 3

    def camera_control(self, resolution=-1, brightness=-1, contrast=-1, mode=-1, flip_mirror=-1):
        """
        camera_control.cgi

        @param resolution 8:QVGA 32:VGA
        @param brightness 0-255
        @param contrast 0-6
        @param mode  0: 50Hz 1: 60Hz 2: Outdoor
        @param flip_mirror 0: default 1: flip 2: mirror 3: flip + mirror
        """
        reply = None
        if not resolution < 0:
            reply = self.__set_param('/camera_control.cgi', 0, resolution)
        if not brightness < 0:
            reply = self.__set_param('/camera_control.cgi', 1, brightness)
        if not contrast < 0:
            reply = self.__set_param('/camera_control.cgi', 2, contrast)
        if not mode < 0:
            reply = self.__set_param('/camera_control.cgi', 3, mode)
        if not flip_mirror < 0:
            reply = self.__set_param('/camera_control.cgi', 4, flip_mirror)
        return reply
            
    def update(self):
        """
        Update video image
        @return Image.Image (PIL) object 
        """
        while True:
            data = self.__videostream.readline()  
            if data[0:15] == 'Content-Length:':  
                count = int(data[16:])  
                s = self.__videostream.read(count)      
                while s[0] != chr(0xff):  
                    s = s[1:]       
                    
                p = StringIO.StringIO(s)  
                return Image.open(p)

    
