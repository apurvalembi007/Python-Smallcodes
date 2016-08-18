
# Spiral traversal of matrix COde 

def SprialMatrix(A,row,col):
    #dr = Direction 0 =(Left to right) 1= (Top to bottom) 2 = (right to left <--) 3 = (bottom to top)
	#T=top, B=Bottom,L=left,R=right
	                 
	T,L= 0,0
	B,R= row-1,col-1
	dr = 0 
	
	while(T<=B and L<=R):
	
		if (dr == 0):
			for i in range(L,R+1):
				print A[T][i],
		T= T+1
		dr = 1
			
		if (dr == 1):
			for i in range(T,B+1):
				print A[i][R],
		R= R-1
		dr = 2
		
		if (dr == 2):
			for i in range(R,L-1,-1):
				print A[B][i],
		B= B-1
		dr = 3
		
		if (dr == 3):
			for i in range(B,T-1,-1):
				print A[i][L],
		L= L+1
		dr = 0
	
A=[
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
   ]  
row = len(A)
col = len(A[0])

# function call	
SprialMatrix(A,row,col)
