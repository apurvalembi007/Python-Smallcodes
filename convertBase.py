def conversion(n, base):
    if n<1:
    	return [0]
    output = []
    while n:
    	output.append(n%base)
    	n = n/base
    return "".join(map(str,output[::-1]))
    
    
    
print conversion(13, 2)