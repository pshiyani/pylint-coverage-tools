"""
SSW_567
Author: Priyankaben Shiyani
Project Description: Triangle Classification Implementation
"""


def classify_triangle(tri_a, tri_b, tri_c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle and this function will
    tell us whether the triangle is scalene,isosceles, equilateral or right triangle
    """
    try:
        tri_a = float(tri_a)
        tri_b = float(tri_b)
        tri_c = float(tri_c)
    except ValueError:
        raise ValueError("Every side of triangle has to be a number!")
    else:
        [tri_a, tri_b, tri_c] = sorted([tri_a, tri_b, tri_c])
        if (tri_a > 0 and tri_b > 0 and tri_c > 0):
            if (tri_a + tri_b > tri_c) and \
                (tri_b + tri_c > tri_a) and \
                (tri_a + tri_c > tri_b):
                if round(((tri_a ** 2) + (tri_b ** 2)), 2) == round((tri_c ** 2), 2):
                    if tri_a == tri_b or tri_b == tri_c or tri_c == tri_a:
                        return 'Right Isosceles Triangle'
                    else:
                        return 'Right Scalene Triangle'
                elif tri_a == tri_b == tri_c:
                    return "Equilateral Triangle"
                elif tri_a == tri_b or tri_a == tri_c or tri_b == tri_c:
                    return "Isosceles Triangle"
                else:
                    return "Scalene Triangle"
            else:
                return "This is not a triangle"
        else:
            return "A triangle should have positive side"
