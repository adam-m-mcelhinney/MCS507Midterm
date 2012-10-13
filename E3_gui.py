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

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exercise 4

The adjacency matrix A of a graph of n vertices is a symmetric n-by-n matrix, defined as follows:
if the vertices i and j are connected by an edge, then Ai,j = 1, and otherwise: Ai,j = 0.
We say that two vertices i and j are connected by a path of length m if one can go from i to j by
walking along m edges. To denote a path, we list the vertices connected by the edges along the path.
A path of length m is a list of m+ 1 vertices.

Extend the GUI of the previous question with two entry widgets where the user can enter two vertices i
and j. Add an extra button to the GUI. When the user presses that extra button an animation starts.
The animation draws all paths of length at most n that connect the two vertices i and j. Every vertex
in the path should be visited only once, i.e.: the path has no loops.

https://en.wikipedia.org/wiki/Adjacency_matrix

"""


from Tkinter import *
import numpy as np
from random import randint
from math import sin, cos, pi


class adjacency():
    """
    GUI to allow users to create adjacency matrics
    """
    def __init__(self,wdw,dimension):
        """
        """
        wdw.title("Create Adjacency")
        self.dim = dimension # dimension of the canvas
        self.c = Canvas(wdw,width=self.dim,\
                        height=self.dim,bg ='white')
        self.c.grid(row=0,column=0,columnspan=2)
        
        # Add button
        self.b0 = Button(wdw,text='Add Random Matrix'\
                         ,command=self.plot_all)
        self.b0.grid(row=1,column=1)
        # Entry widget for num points
        self.n = Entry(wdw)
        self.n.grid(row=2,column=1)
        

        # Entry widgets for user to specify specific points
        self.i = Entry(wdw)
        self.i.grid(row=3,column=1)
        self.j = Entry(wdw)
        self.j.grid(row=4,column=1)

        
        ## Radius of points
        self.radius=4
        ## Scale of points
        self.mag=300
        self.center=self.dim/2.


    def fun(self):
        """
        Functions to calculate the coordinates
        """
        n=int(self.n.get())
        x_f=lambda z: cos((2.*z*pi)/n)
        y_f=lambda z: sin((2.*z*pi)/n)
        return x_f, y_f

    def label_points(self,x,y,label):
        """
        Places a given label on point x and y
        """
        
        self.c.create_text(x,y,anchor=SW,text=label)
        self.c.update()




    def create_mat(self):
        """
        Creates an n*n random symmetric matrix
        """
        n=int(self.n.get())
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
                        
        return A


    def draw_point(self,x,y,tag=1):
        """
        Draws a circle centered at x,y with radius =r.
        Tag=1 means label the points with the coordinates
        """

        x_f,y_f=self.fun()

        r=self.radius
        

        ## Plot the points
        ## x_c means "x-centered"
        x_c=x_f(x)*self.mag+self.center
        y_c=y_f(x)*self.mag+self.center


        self.c.create_oval(x_c-r,y_c-r,x_c+r,y_c+r,outline='red',fill='red',tags='dot')
        self.c.update()

        if tag==1:
            tag='Point '+str(x)
            self.label_points(x_c,y_c,tag)

            

            

            
        

    def plot_coordinates(self):
        """
        Plots the points on the unit circle
        """        
        
        n=int(self.n.get())        
        ## Plot the points
        for i in range(n):
            self.draw_point(i,i)

    def plot_line(self,x0,x1,y0,y1, color=''):
        """
        Draws a line between points (x0,y0) and (x1,y1)
        """
        x_f,y_f=self.fun()
        X0=x_f(x0)*self.mag+self.center
        X1=x_f(x1)*self.mag+self.center
        Y0=y_f(y0)*self.mag+self.center
        Y1=y_f(y1)*self.mag+self.center
        if color=='':
            self.c.create_line(X0,Y0,X1,Y1)
        else:
            self.c.create_line(X0,Y0,X1,Y1,color)
        self.c.update

    def plot_edges(self):
        """
        Plot the edges per the adjacency matrix
        """
        n=int(self.n.get())
        A=self.create_mat()
        self.A=A
        print A
        for i in range(n):
            for j in range(n):
                if (A[i][j]!=0 and i!=j):
                    self.plot_line(i,j,i,j)

    def plot_all(self):
        """
        Plots stuff
        """
        self.plot_coordinates()
        self.plot_edges()
        self.adj_list()

    def adj_list(self):
        """
        Creates an adjacency list
        """
        #print self.A
        list=[]
        for i in range(len(A)):
            r=[]
            for j in range(len(A)):
                print A[i][j]
                if A[i][j]==1:
                    r.append(j)
            list.append(r)
            

        
        
        
        
    
def main():
    top = Tk()      
    dimension = 800
    show = adjacency(top,dimension)
    top.mainloop()



if __name__ == "__main__": main()
