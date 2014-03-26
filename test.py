import os, sys
from tenvis import *


if __name__ == '__main__':
    print 'Starting Tenvis Test'
    t = Tenvis(sys.argv[1], sys.argv[2], sys.argv[3])
    print t.get_status()
    t.videostream()
    b = t.update()
    b.show()
    raw_input('enter')
