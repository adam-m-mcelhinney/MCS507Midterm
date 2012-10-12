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
stir[(0,0)]=1

n=5
k=1
for i  in range(5):
    coeff=-(i-1)
    key=tuple(i,1)
    if stir.has_key(key):
        stir[key]
