# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    

    #------Right triangle Test Cases-----------
    def test_RightTriangleA(self): 
       self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
       
    def test_RightTriangleB(self):
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')

    def test_RightTriangleC(self):
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a Right triangle')


    #---Invalid Input Test Cases-----
    
        #----input value greater than 200----
    def test_InvalidInputA(self):
        self.assertEqual(classifyTriangle(201,190,200),'InvalidInput','201,190,200 is an Invalid Input')

    def test_InvalidInputB(self):
        self.assertEqual(classifyTriangle(200,201,200),'InvalidInput','200,201,200 is an Invalid Input')

    def test_InvalidInputC(self):
        self.assertEqual(classifyTriangle(190,200,201),'InvalidInput','190,200,201 is an Invalid Input')

        #----input value less than or equal to zero----
    def test_InvalidInputD(self):
        self.assertEqual(classifyTriangle(0,190,200),'InvalidInput','0,190,200 is an Invalid Input')

    def test_InvalidInputE(self):
        self.assertEqual(classifyTriangle(200,0,200),'InvalidInput','200,0,200 is an Invalid Input')

    def test_InvalidInputF(self):
        self.assertEqual(classifyTriangle(190,200,-1),'InvalidInput','190,200,-1 is an Invalid Input')

        #----input value not an instance of type int----
    def test_InvalidInputG(self):
        self.assertEqual(classifyTriangle('190',200,0),'InvalidInput',"'190',200,0 is an Invalid Input")

    def test_InvalidInputH(self):
        self.assertEqual(classifyTriangle(3,"two",5),'InvalidInput',"3,'two',5 is an Invalid Input")

    def test_InvalidInputI(self):
        self.assertEqual(classifyTriangle(3,2,4.1),'InvalidInput',"3,2,4.1 is an Invalid Input")
        
    #-----NotATriangle test cases------------------
    def test_NotATriangleA(self):
        self.assertEqual(classifyTriangle(2,4,6),'NotATriangle','2,4,6 is not a valid triangle')
    
    def test_NotATriangleB(self):
        self.assertEqual(classifyTriangle(2,4,1),'NotATriangle','2,4,1 is not a valid triangle')

    def test_NotATriangleC(self):
        self.assertEqual(classifyTriangle(11,4,6),'NotATriangle','11,4,6 is not a valid  triangle')

    #-----Equilateral triangle test cases--------
    def test_EquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_EquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral','200,200,200 should be equilateral')
    
    def test_EquilateralTrianglesC(self): 
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral','100,100,100 should be equilateral')

    #-----Scalene triangle test cases------------
    def test_ScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(3,6,4),"Scalene","3,6,4 should be scalene")


    #----Isoceles triangle test cases-----------
    def test_IsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(3,4,3),"Isosceles","3,4,3 should be isosceles")

    def test_IsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(5,4,4),"Isosceles","5,4,4 should be isosceles")
    
    def test_IsoscelesTrianglesC(self):
        self.assertEqual(classifyTriangle(3,3,2),"Isosceles","3,3,2 should be isosceles")
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

