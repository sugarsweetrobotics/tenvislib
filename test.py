from tenvis import *


if __name__ == '__main__':
    print 'Starting Tenvis Test'
    t = Tenvis('192.168.1.200', 7777, 'admin', 'admin')
    print t.get_status()
