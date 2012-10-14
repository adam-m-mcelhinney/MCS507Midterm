"""
MCS 507 Midterm
Exercise 2

The Stirling numbers of the first kind c(n, k) satisfy the recurrence
c(n, k) = −(n − 1)c(n − 1, k) + c(n − 1, k − 1), for n >= 1 and k >= 1,
with the initial conditions that c(n, k) = 0 if n <= 0 or k <= 0
, except c(0, 0) = 1.

Write a Python class stirling that exports the method c, to compute c(n, k). Any object of the class
stirling stores internally a dictionary that has as keys the tuples (n, k) and values the corresponding
Stirling numbers for all tuples computed in the recurrence for the input values for n and k.

Every value for c(n, k) that is computed in the recurrence is stored in the internal dictionary. In each
call of the method c, the internal dictionary is consulted to see if the values for the given (n, k) have
not yet been already computed. If already computed, then the value in the dictionary is returned,
otherwise, the computed value is stored in the dictionary.

"""

# Define a dictionary

class Stirling():

    def __init__(self):
        # Define dictionary
        self.stir={}

    def __str__(self):
        return str(self.stir)

    
    def __repr__(self):
        """
        Defines the representation.
        """
        return self.__str__()


    def check_zero(self,n,k):
        """
        Ensure the Stirling value is not zero or the special case (0,0)=1
        """
        if (n==0 and k==0):
            self.stir[(0,0)]=1
        elif(n<=0 or k<=0):
            self.stir[(n,k)]=0

        
    def c(self,n,k,verbose=''):
        """
        Computes the Stirling number n,k and saves to a dictionary
        """    
        
        key=(n,k)
        if verbose!='':
            print 'key:'+str(key)+str(self.stir.has_key(key))
        # Check if we already have this value
        if self.stir.has_key(key):
            return self.stir[key]
        # Check if n<=0 or k<=0
        self.check_zero(n,k)



            
        # Check to see if we have the c(n-1,k) and c(n-1,k-1) keys
        key1=(n-1,k)
        key2=(n-1,k-1)
        self.check_zero(n-1,k)
        self.check_zero(n-1,k-1)
        if verbose!='':
            print 'key1:'+str(key1)+':'+str(self.stir.has_key(key1))
            print 'key2:'+str(key2)+':'+str(self.stir.has_key(key2))
        
        # If we do not have they keys, compute the Stirling value for the next two keys    
        while(self.stir.has_key(key1)==False):
                self.c(n-1,k)

        while(self.stir.has_key(key2)==False):
                self.c(n-1,k-1)

        # If we have the keys, compute the Stirling value
        if (self.stir.has_key(key1) and self.stir.has_key(key2)):
            A=self.stir[(n-1,k)]
            B=self.stir[(n-1,k-1)]
            self.stir[(n,k)]=-(n-1)*A+B
            #pass
            #print A, B
            if verbose!='':
                print 'Stirling value computed:'+str((n,k))
                return self.stir[(n,k)]

       
        
        
    



if __name__=="__main__":
    t=Stirling()
    #t.c(5,4)
    t.c(5,5)
    #print t

    
