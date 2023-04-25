#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:25:33 2023

@author: tobibrosch
"""
#Imports
import math

#Code
#Eingabe 
x = float(input("Wähle x="))
tol = float(input("Wähle tol="))
#Variables
i=0
k=0
sin_xexact = math.sin(x)
sin_xcalc = 0
error = 1
i=0
while error > tol:
    sin_xcalc=sin_xcalc+(-1)**(i)*(x**(2*i+1))/math.factorial(2*i+1)
    i=i+1
    print("Summand=", i)
    error = abs(sin_xcalc-sin_xexact)
    print("|", sin_xcalc, "-" , sin_xexact, "|=", error)
print("Ab dem", i, "-Summanden, ist die Differenz zwischen exaktem Wert und approximierten Wert <", tol)