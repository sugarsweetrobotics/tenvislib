import os, sys, yaml, time
from tenvis import *

import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        param = yaml.load(open('setting.yaml', 'r'))
        self.tenvis = Tenvis(**param)
        pass

    def test_get_camera_params(self):
        must_keys = ['resolution', 'brightness', 'contrast',
                     'mode', 'flip']

        d = self.tenvis.get_camera_params()
        for k in must_keys:
            self.assertTrue(k in d.keys())

    def test_get_params(self):
        must_keys = ['id', 'sys_ver', 'app_ver', 'alias', 'now', 'tz', 
                     'ntp_enable', 'ntp_svr', 
                     'ip', 'mask', 'gateway', 'dns', 'port']
        d = self.tenvis.get_params()
        for k in must_keys:
            self.assertTrue(k in d.keys())

    def test_get_status(self):
        must_keys = ['id', 'sys_ver', 'app_ver', 'alias', 'now', 'tz', 
                     'alarm_status', 'ddns_status', 'ddns_host',
                     'oray_type', 'upnp_status',
                     'p2p_status', 'p2p_local_port',
                     'msn_status']
        d = self.tenvis.get_status()
        for k in must_keys:
            self.assertTrue(k in d.keys())

    def test_camera_control_QVGA(self):
        self.tenvis.camera_control(resolution=self.tenvis.QVGA)
        time.sleep(1)
        self.assertEqual(self.tenvis.get_camera_params()['resolution'], 
                         str(self.tenvis.QVGA))

    def test_camera_control_VGA(self):
        self.tenvis.camera_control(resolution=self.tenvis.VGA)
        time.sleep(1)
        self.assertEqual(self.tenvis.get_camera_params()['resolution'], 
                         str(self.tenvis.VGA))


if __name__ == '__main__':
    print 'Starting Tenvis Test'
    unittest.main()
    """
    camera_control_test(t)
    sys.exit(1)

    print t.get_status()
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
    """
