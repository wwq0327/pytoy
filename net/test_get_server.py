import unittest
from get_server import get_server_name

class GetServerTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://www.baidu.com'

    def test_get_server_name(self):
        _s = get_server_name(self.url)
        self.assertEqual(_s, 'BWS/1.1')

if __name__ == '__main__':
    unittest.main()
