from __future__ import division
import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def newton_rapshon_method(x,f,fd,maxiter): 
	# x0--------> Valor inicial 
	# f---------> Funcion 
	# fd--------> Derivada de la funcion 
	# maxiter---> Numero de recursiones 
    
    for n in range(maxiter):
        x = x - f(x)/fd.evalf(subs={'x':x})
    return x
	 
	 
if __name__ == '__main__': 
    maxiter = 4                     # Numero de recursiones 
    x0 = 1
    x = symbols('x')                          # Valor inicial de la recursion 
    f = lambda x: ln(x) - x + 4      # Definiendo la funcion  
    fd = f(x).diff(x)               # La derivada de la funcion
    print (float(newton_rapshon_method(6,f,fd,maxiter)))
