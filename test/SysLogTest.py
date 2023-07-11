import unittest
from app.SysLogger import SysLogger


class SysLoggerTest(unittest.TestCase):

    def setUp(self):
        self.tst = SysLogger("firefox", 5, 2)

    def test_not_raise_error(self):
        self.assertRaises(TypeError, SysLogger.start_monitoring, "firefox", 1, 2)

    def test_not_raise_error_with_no_sampling(self):
        self.assertRaises(TypeError, SysLogger.start_monitoring, "firefox", 10)

    def test_raise_error_sampling(self):
        self.assertRaises(TypeError, SysLogger.start_monitoring, "firefox", 1, "two")

    def test_raise_error_period(self):
        self.assertRaises(TypeError, SysLogger.start_monitoring, "firefox", "1", 2)

    def test_raise_error_name(self):
        self.assertRaises(TypeError, SysLogger.start_monitoring, 370, 1, 3)


if __name__ == '__main__':
    unittest.main()
