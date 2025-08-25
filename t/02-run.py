import unittest
from math import sin
#import window.viewport
from window.viewport import viewport

class TestLoad(unittest.TestCase):

    def test_defaults(self):
        w2v = viewport( world_bounds=(0, 1, 0, 1), view_bounds=(9, 0, 0, 9))
        self.assertEqual( w2v.Dx(.5), 4.5, 'correct Dx()' )
        self.assertEqual( int(w2v.Dy(.6)), 3, 'correct Dy()' )

        x = 0
        y = sin(x)
        self.assertEqual( int(w2v.Dx(x)), 0, 'correct Dx() sin wave 1/5' )
        self.assertEqual( int(w2v.Dy(y)), 9, 'correct Dy() sin wave 1/5' )

        x = 0.1
        y = sin(x)
        self.assertEqual( int(w2v.Dx(x)), 0, 'correct Dx() sin wave 2/5' )
        self.assertEqual( int(w2v.Dy(y)), 8, 'correct Dy() sin wave 2/5' )

        x = 0.2
        y = sin(x)
        self.assertEqual( int(w2v.Dx(x)), 1, 'correct Dx() sin wave 3/5' )
        self.assertEqual( int(w2v.Dy(y)), 7, 'correct Dy() sin wave 3/5' )

        x = 0.3
        y = sin(x)
        self.assertEqual( int(w2v.Dx(x)), 2, 'correct Dx() sin wave 4/5' )
        self.assertEqual( int(w2v.Dy(y)), 6, 'correct Dy() sin wave 4/5' )

        x = 0.4
        y = sin(x)
        self.assertEqual( int(w2v.Dx(x)), 3, 'correct Dx() sin wave 5/5' )
        self.assertEqual( int(w2v.Dy(y)), 5, 'correct Dy() sin wave 5/5' )

if __name__ == '__main__':
    unittest.main()
