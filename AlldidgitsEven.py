# your code goes here
def evenDigitsOnly(n):
    y = str(n)
    y.split()
    x = [int(i) for i in y if int(i)%2==0]
    return len(x) == len (y)
		    
		        
print evenDigitsOnly(642386)
