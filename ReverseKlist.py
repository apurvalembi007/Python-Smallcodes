
# http://www.geeksforgeeks.org/reverse-an-array-in-groups-of-given-size/

# Reverse an array in groups of given size
# Given an array, reverse every sub-array formed by consecutive k elements.

# Examples:
	
# Input: 
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3
# Output:  
# [3, 2, 1, 6, 5, 4, 9, 8, 7]

# Input: 
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 5
# Output:  
# [5, 4, 3, 2, 1, 8, 7, 6]

# Input: 
# arr = [1, 2, 3, 4, 5, 6]
# k = 1
# Output:  
# [1, 2, 3, 4, 5, 6]

def ReverseTillK(A,n,k):
	C = [i for i in A[:k]]
	C = C[::-1]
	for x in A[k:n]:
		C.append(x)
	return C
	
A = [1,2,3,4,5]  
n = len(A)
k = 3

# output[]= [3,2,1,4,5]
print ReverseTillK(A,n,k)
