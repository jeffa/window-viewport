import unittest
from window.viewport import viewport

class TestLoad(unittest.TestCase):

    def test_defaults(self):
        w2v = viewport()
        self.assertIsInstance( w2v, viewport, 'object is instance of class' )

if __name__ == '__main__':
    unittest.main()
