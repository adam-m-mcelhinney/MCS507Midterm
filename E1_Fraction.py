"""
MCS 507 Midterm
Exercise 1

1. Consider a real number x. Let i be the integer part of x and let f be the fractional part of x. If f is zero,
then the continued fraction representation of x is [i]. Otherwise, the continued fraction representation
of x is [i,L], where L is the continued fraction representation of 1/f.

Write Python code to compute the continued fraction representation of a real number with an iterator.
Each step of the iterator gives the next element in the list of convergents. Calling the next() n times
in a list comprehension gives the first n convergents in the continued fraction representation.
If the continued fraction terminates (e.g.: x = 2.25 = 9/4 has the continued fraction representation
[2, 4]), then the iterator needs to trigger an exception the third time the method next() is invoked.
The real number x may be given as a Python float or as a multiprecision float (as defined by
sympy.mpmath).


Notes:
1. Having issue with rounding. See n=2.45 and wikipedia page
https://en.wikipedia.org/wiki/Continued_fraction#Calculating_continued_fraction_representations

THINK THIS MAY BE BROKEN!


"""
from math import floor
from sympy import mpmath
from sympy import nsimplify
#import sympy as sy
import fractions

class cont_fract():
    """
    Continued fraction expansion iterator
    """

    def __init__(self,n):
        
        self.n=n
        self.count=0
        self.q=self.n
        self.rep=[]
        

    def __iter__(self):
        #self.next()
        return self.rep

    def __str__(self):
        """
        Returns the current state of the iterator
        """
        s=" Number:" + str(self.n)
        s=s+'\n Number of evaluations:' + str(self.count)
        s= s+ '\n Latest fractional value: ' + str(self.q)
        s=s+ '\n All functional evaluations: ' + str(self.rep)
        #s=str(self.rep)
        return s

    def __repr__(self):
        """
        Defines the representation. 
        """
        return self.__str__()

    
        

    def fract(self,n):
        """
        Does one iterations of continued fraction expansion
        """
        from math import floor
        try:
            i=floor(n)
        except TypeError:
            print 'No more expansions'
            #pass
            return None,None 
        #print i
        f=n-i
        #print f
        #tol=.0001
        #r=1/nsimplify(f, tolerance=tol)
        try:
            r=1/float(f)
            print r
            self.count=self.count+1
        #print self.count
        except ZeroDivisionError:
            print 'No more expansions'
            r=''
        return r,i

    def next(self):

        try:
            print self.q
            self.q,self.i=self.fract(self.q)
            print 'i'+str(self.i)
            self.rep.append(self.i)
            #print q
            #print self.count
            return self.rep[self.count-1]
        except TypeError:
            return
             
        

            
    
if __name__=="__main__":

##    n=3.245
##    t=cont_fract(n)
##    #print t
##    #print t.next()
##    y=[t.next() for i in range(5)]
##    print y

    n2=2.25
    t2=cont_fract(n2)
    x=[t2.next() for i in range(4)]
    print x
    #print t2.next()
##    from math import sqrt
##    q=sqrt(2)
##    t3=cont_fract(q)
##    y=[t3.next() for i in range(5)]
##    print y
