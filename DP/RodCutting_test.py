import unittest
from RodCutting import *

class RodCuttingTestCase(unittest.TestCase):
    def setUp( self ):
        self.price_table = [ (1,1), (2,5), (3,8), (4,9), (5,10), (6,17), (7, 17), (8,20), (9,24), (10,30) ]

        self.test_data = [ ( 1, 1, [1] ), ( 2, 5, [2] ), ( 3, 8, [3] ), ( 4, 10, [2,2] ), ( 5, 13, [2, 3] ), ( 6, 17, [6] ), (7 , 18, [1,6]), (8, 22, [2,6]), (9, 25, [3,6]), (10, 30, [10])  ]
    
        self.solution = Solution()

    def test_top_down( self ):
        for l, p, s in self.test_data:
            p0, s0 = self.solution.rod_cutting_top_down( self.price_table, l )
            self.assertEqual( p, p0 )
            self.assertListEqual( s, s0 )

    def test_bottom_up( self ):
        for l, p, s in self.test_data:
            p0, s0 = self.solution.rod_cutting_bottom_up( self.price_table, l )
            self.assertEqual( p, p0 )
            self.assertListEqual( s, s0 )
    

rodCuttingTestSuit = unittest.TestSuite()
rodCuttingTestSuit.addTest( RodCuttingTestCase("test_top_down") )
rodCuttingTestSuit.addTest( RodCuttingTestCase("test_bottom_up") )

runner = unittest.TextTestRunner()
runner.run( rodCuttingTestSuit )
