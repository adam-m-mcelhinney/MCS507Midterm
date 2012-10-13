"""
path test
"""


import numpy as np
from random import randint
from numpy import asmatrix
import itertools

n=4
A=np.zeros((n,n))
for i in range(n):
            for j in range(n):
                v=randint(0,1)
                A[i][j]=v
                A[j][i]=v



### Create adjanceny list
##path={}
##for i in range(n):
##    keys=[]
##    print 'Level: '+str(i)
##    for j in range(n):
##        #print A[i][j]
##        if A[i][j]==1:
##            keys.append(j)
##        print keys
##    path[i]=keys

# Create adjanceny list
L={}
for i in range(n):
    keys=[]
    print 'Level: '+str(i)
    for j in range(n):
        #print A[i][j]
        if A[i][j]==1:
            keys.append(j)
        print keys
    L[i]=keys

def find_all_paths(graph, start, end, path=[]):
    """
    Need to modify this code
    http://www.python.org/doc/essays/graphs.html
    """
    path = path + [start]
    if start == end:
            return [path]
    if not graph.has_key(start):
            return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
			
        
#print find_all_paths(path,0,1)
print find_all_paths(L,0,1)



def find_paths(adj, start, end, path=[]):
    """
    Gets list of all paths given an adjancency list in the form of a dictionary
    Modified from:
        --http://www.python.org/doc/essays/graphs.html
        --http://search.cpan.org/~cavasquez/Paths-Graph-0.02/Graph.pm
    
    """
    # Add the starting point to the path
    print type(path)
    print type(start)
    print type([start])
    path = path + [start]
    # If the starting point is the end, then we don't need to do anything
    if start == end:
            return [path]
    # If the adjacency list doesn't have the have starting point, stop
    if not adj.has_key(start):
            return []
    # Define a list paths, to hold the unique paths
    paths = []
    # Node represents any point in the adjacency list
    # Go through each one
    for node in adj[start]:
        # If we havent seen this node, repeat the function
        if node not in path:
            newpaths = find_paths(adj, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


print find_all_paths(L,0,1)			
        
print find_paths(L,0,1)    


##### Old crap

               ##S
##path=[]
##for i in range(len(A)):
##            # Put the starting value
##            r=[i]
##            for j in range(len(A)):
##                print A[i][j]
##                if A[i][j]==1:
##                    r.append(j)
##            path.append(r)
##
##start=0
##end=3
####print path[start]
####for  i in range(len(path[start])):
####    print path[start]
####    if start==end:
####        pass
####    else:
####        for j in range(len(path[start])):
####            print j
####exhaus=[]
####print path[start]    
####for i in range(len(path[start])):
####    print path[start][i]
####    print i
####    for j in range(len(path[i])):
####        exhaus.append(path[j])
##
####for i in range(len(A[start])):
####    print A[start][i]
####    # Check if that element connects
####    if A[start][i]==1:
####        e.append(
####        for j in range(len(A[start][i])):
##p=[]
##y=0
##route=[]
##
####for i in range(len(A[start])):
####    print '1. from row start='+str(start)+ ' to col i=' + str(i)+' ='+str(A[start][i])
####    if A[start][i]!=0:
####        route.append([start])#
####        route[y].append(i)
####        y=y+1
####        
####    for j in range(len(A[i])):
####            print '2. from row i='+str(i)+ ' to col j=' + str(j)+' ='+str(A[i][j])
####            #if A[i][j]!=0:
####            for k in range(len(A[k])):
####                    print '3: from row j='+str(j)+', to col k='+str(k)+' ='+ str(A[j][k])
####m={}
####move=[[start] for i in range(n**n)]
####moves=[]
####s=[i for i in range(n)]
####for i in range(n):
####    moves.append(list(itertools.permutations(s,i)))
####for i in range(len(move)):
####
####for i in range(n**n):
####        #for j in range(n):
####        while(j<=n):
####            for k in range(n):
####                print str(start)+','+str(j)+','+str(k)
####            j=j+1
####move=[[start] for i in range(n**n)]
####
####i=n
####while(i>0):
####    print i
####    for i in range(n):
####        for j in range((n**i)/n):
####            print '0'
####            #i=i-1
####        
