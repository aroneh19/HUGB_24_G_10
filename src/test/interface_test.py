import unittest

from app.server.interface import SystemInterface

class TestInterface(unittest.TestCase):

    def setUp(self):
        """Set up function that is called prior to every test. 
           There are similar functions for cleaning up (tearDown)
           and for setting up/cleaning up before/after the test suite as a whole (setUpClass/tearDownClass)."""
           
        self.my_iface = SystemInterface()

    def test_an_operation_without_params(self):
        ret = self.my_iface.an_operation_without_params()
        self.assertTrue(not ret is None)
        self.assertTrue('msg' in ret.keys())
        self.assertEqual(ret['msg'], 'Operation successful')
