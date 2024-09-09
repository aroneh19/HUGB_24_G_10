import unittest

from app.server.interface import SystemInterface

class TestInterface(unittest.TestCase):

    def setUp(self):
        """Set up function that is called prior to every test. 
           There are similar functions for cleaning up (tearDown)
           and for setting up/cleaning up before/after the test suite as a whole (setUpClass/tearDownClass)."""
           
        self.my_iface = SystemInterface()

    def test_an_operation_without_params (self):
        """This is an actual unit test: It only tests the unit (function), without any of the Flask stuff before it.
           The assertions check that the return value is not of type None, has a key "msg", and contains the defined
           String as a message. Change any of the assertions to check if you can fail the test!"""

        ret = self.my_iface.an_operation_without_params()
        self.assertTrue(not ret is None)
        self.assertTrue('msg' in ret.keys())
        self.assertEqual(ret['msg'], 'Operation an_operation_without_params not yet implemented')