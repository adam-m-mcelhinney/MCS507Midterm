"""
MCS 507 Midterm
Exercise 3

The adjacency matrix A of a graph of n vertices is a symmetric n-by-n matrix, defined as follows:
if the vertices i and j are connected by an edge, then Ai,j = 1, and otherwise: Ai,j = 0.

Write code for a GUI with Tkinter with an entry widget, one button and a canvas. In the entry widget
the user can give the number n of vertices. Each time the user presses the button, a random adjacency
matrix of dimension n is generated and the corresponding graph is drawn on the canvas.

Place the vertices on the unit circle in the plane, i.e.: vertex k has coordinates (cos(2k*pi/n), sin(2k*pi/n)).
For every edge as defined by A, draw the line segment between the vertices connected by the edge.


https://en.wikipedia.org/wiki/Adjacency_matrix

"""

import numpy as np
from random import randint
from math import sin, cos, pi
import matplotlib.pyplot as plt

##
##def num_elements(n):
##    """
##    Calculates the number of unique entries in an n*n symmetric matrix
##    """
##    [i for i in range(n+1)]
##    for i in range(n):
        


#def create_mat(n):
"""
Creates a synmmetric n*n matrix with 0 or 1 as elements
"""
n=10

A=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        v=randint(0,1)
        A[i][j]=v
        A[j][i]=v

# verify symmetric
if sum(sum(np.transpose(A)-A))!=0:
    print ' Warning: Matrix not symmetric!'
else:
    print 'Matrix symmetric'

# calc coordinates
# verify these functions
x_f=lambda z: cos((2*z*pi)/n)
y_f=lambda z: sin((2*z*pi)/n)
x=[x_f(i)for i in range(n)]
y=[y_f(i)for i in range(n)]


#p1=plt.plot(x,y, linewidth=2.0)


# plot lines
for i in range(n):
    for j in range(n):
        if (A[i][j]!=0 and i!=j):
            x_lin=[x_f(i),x_f(j)]
            x2=[i,j]
            #print x2
            #print x_lin
            y_lin=[y_f(i),y_f(j)]
            y2=[i,j]
            #print y2
            #print y_lin
            p=plt.plot(x_lin,y_lin, linewidth=2.0)
p1=plt.plot(x,y, 'ro')
plt.show()

