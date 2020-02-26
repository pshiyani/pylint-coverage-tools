"""
SSW_567
Author: Priyankaben Shiyani
Project Description: Triangle Classification Implementation
"""
def Classify_triangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle and this function will 
    tell us whether the triangle is scalene,isosceles, equilateral or right triangle
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        raise ValueError("Each side of triangle has to be a number!")
    else:
        [a, b, c] = sorted([a, b, c]) 
        """sum of two side should be > then third side"""
        if (a > 0 and b > 0 and c > 0): 
            if (a + b > c) and (b + c > a) and (a + c > b):  
                if round(((a ** 2) + (b ** 2)), 2) == round((c ** 2), 2):
                    """check triangle is Right Isosceles or Right Scalene"""
                    if a == b or b == c or c == a:  
                        return 'Right Isosceles Triangle'
                    elif a != b and b != c and a != c:  
                        return 'Right Scalene Triangle'
                    """ check if triangle is Equilateral"""
                elif a == b == c:
                    return "Equilateral Triangle" 
                    """ check triangle is Isosceles or Scalene """
                elif a == b or a == c or b == c:
                    return "Isosceles Triangle"  
                else:
                    return "Scalene Triangle"  
            else:
                return "This is not a triangle"  
        else:
            return "A triangle should have positive side"