# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(len_a,len_b,len_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    invalid = False
    if not(isinstance(len_a,int) or not isinstance(len_b,int) or not isinstance(len_c,int)):
        invalid = True

    # require that the input values be >= 0 and <= 200
    if not invalid and len_a> 200 or len_b > 200 or len_c > 200:
        invalid = True
    if not invalid and len_a<= 0 or len_b <= 0 or len_c <= 0:
        invalid = True

    if invalid:
        return 'InvalidInput'
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (len_a>= (len_b + len_c)) or (len_b >= (len_a+ len_c)) or (len_c >= (len_a+ len_b)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if len_a== len_b and len_b == len_c:
        return 'Equilateral'
    if (((len_a* len_a) + (len_b * len_b)) == (len_c * len_c)
    or ((len_a*len_a) + (len_c*len_c)) == (len_b*len_b)
    or ((len_b*len_b) +(len_c*len_c)) == (len_a*len_a)):
        return 'Right'
    if (len_a!= len_b) and (len_b != len_c) and (len_a!= len_c):
        return 'Scalene'
    return 'Isoceles'
