import unittest
from myproperty import A

class ATest(unittest.TestCase):
    def test_get_x(self):
        a = A()
        a.x = 5
        self.assertEquals(a.x, 5)
    def test_del_x(self):
        a = A()
        a.x = 5
        del a.x
        self.assertFalse(a.x==None)

if __name__ == '__main__':
    unittest.main()
