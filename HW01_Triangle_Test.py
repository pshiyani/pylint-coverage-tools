"""
SSW_567
Author - Priyankaben Shiyani
Project Description:Triangle Classification Testing
"""
#import math
import unittest 
from HW01_Triangle import Classify_triangle

class TestTriangles(unittest.TestCase):
    def test_incorrect_inputs(self):
        """verify if function raises the exception properly when the input is incorrect"""
        with self.assertRaises(ValueError):
            Classify_triangle( 1, 1, 'hello')
            Classify_triangle('A', 'B', 'C')
            Classify_triangle('a', 'b', 'c')

    def test_not_triangle(self):
        """In this test function will tell us this is a right triangle or not"""
        self.assertEqual(Classify_triangle(0, 0, 0), 'A triangle should have positive side')
        self.assertEqual(Classify_triangle(10.10, 10.10, -10.10), 'A triangle should have positive side')
        self.assertNotEqual(Classify_triangle(3, 4, 5), 'This is not a triangle')
        self.assertEqual(Classify_triangle(-1, -2, -3), 'A triangle should have positive side')
        self.assertEqual(Classify_triangle(1, 1, 3), 'This is not a triangle')

    def test_equilateral(self):
        """In this test function will tell us if the triangle is equilateral or not"""
        self.assertEqual(Classify_triangle(1, 1, 1), 'Equilateral Triangle')
        self.assertEqual(Classify_triangle(11.1, 11.1, 11.1), 'Equilateral Triangle')
        self.assertNotEqual(Classify_triangle(10.11, 10.11, 10.111), 'Equilateral Triangle')
    
    def test_right_scalene(self):
        """In this test function will tell us if the triangle is right scalene or not"""
        self.assertEqual(Classify_triangle(3, 5, 4), 'Right Scalene Triangle')
        self.assertEqual(Classify_triangle(3, 4, 5), 'Right Scalene Triangle')
        self.assertNotEqual(Classify_triangle(5, 4, 7), 'Right Scalene Triangle')

    def test_scalene(self):
        """In this test function will tell us if the triangle is scalene or not"""
        self.assertEqual(Classify_triangle(3, 4, 6), 'Scalene Triangle')
        self.assertNotEqual(Classify_triangle(3 * (2 ^ 64), 4 * (2 ^ 64), 5 * (2 ^ 64)),
                            'Scalene Triangle')
        self.assertEqual(Classify_triangle(10, 20, 12), 'Scalene Triangle')
        
        
    def test_right_isosceles(self):
        """In this test function will tell us if the triangle is right isosceles or not"""
        self.assertEqual(Classify_triangle(1, 1, 2 ** 0.5), 'Right Isosceles Triangle')
        self.assertNotEqual(Classify_triangle(3, 5, 5), 'Right Isosceles Triangle')
        self.assertEqual(Classify_triangle(3, 3, 4.242640687119285146), 'Right Isosceles Triangle')

    def test_isosceles(self):
        """In this test function will tell us if the triangle is isosceles or not"""
        self.assertEqual(Classify_triangle(5, 5, 6), 'Isosceles Triangle')
        self.assertNotEqual(Classify_triangle(3, 4, 5), 'Isosceles Triangle')
        self.assertEqual(Classify_triangle(20, 20, 20), 'Equilateral Triangle')
        self.assertEqual(Classify_triangle(10, 10, 8), 'Isosceles Triangle')
        self.assertEqual(Classify_triangle(4, 4, 4.000000000000001), 'Isosceles Triangle')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)