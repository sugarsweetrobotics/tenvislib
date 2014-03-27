import os, sys
from tenvis import *


if __name__ == '__main__':
    print 'Starting Tenvis Test'
    t = Tenvis(sys.argv[1], sys.argv[2], sys.argv[3])
    print t.get_status()
    t.camera_control()
    t.videostream()
    b = t.update()
    b.show()

    sys.exit(1)
    print t.get_camera_params()
    raw_input('enter')


    t.videostream()
    b = t.update()
    b.show()

    print t.get_camera_params()
    raw_input('enter')
