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
stir={}


def check_zero(n,k):
    """
    Computes the Stirling value
    """
    if (n==0 and k==0):
        stir[(0,0)]=1
    elif(n<=0 or k<=0):
        stir[(n,k)]=0

        
def stirling(n,k):
    """
    Computes the Stirling number n,k and saves to a dictionary
    """    
    
    key=(n,k)
    print 'key:'+str(key)+str(stir.has_key(key))
    # Check if we already have this value
    if stir.has_key(key):
        return stir[key]
    # Check if n<=0 or k<=0
    check_zero(n,k)



        
    # Check to see if we have the c(n-1,k) and c(n-1,k-1) keys
    key1=(n-1,k)
    key2=(n-1,k-1)
    check_zero(n-1,k)
    check_zero(n-1,k-1)
    print 'key1:'+str(key1)+':'+str(stir.has_key(key1))
    print 'key2:'+str(key2)+':'+str(stir.has_key(key2))
    
    # If we do not have they keys, compute the Stirling value for the next two keys    
    while(stir.has_key(key1)==False):
            stirling(n-1,k)

    while(stir.has_key(key2)==False):
            stirling(n-1,k-1)

    # If we have the keys, compute the Stirling value
    if (stir.has_key(key1) and stir.has_key(key2)):
        A=stir[(n-1,k)]
        B=stir[(n-1,k-1)]
        stir[(n,k)]=-(n-1)*A+B
        #pass
        #print A, B 
        print 'Stirling value computed:'+str((n,k))
        #return stir[(n,k)]

       
        
        
    



if __name__=="__main__":
    #print stirling(0,0)
    #print stirling(1,1)
    #print stirling(2,1)
    #print stirling(3,2)
    #print stirling(5,3)
    #print stirling(9,9)
    print stirling(9,4)

    # Compare with wikipedia
    # https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind
    #(9,9)=1
    # stir[(9,9)]=1
    # (9,4)=67284
    # stir[(9,4)]=-67284
    
