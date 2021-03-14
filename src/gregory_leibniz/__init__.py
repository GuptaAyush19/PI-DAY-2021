_upper_limit = 100
PI = 0

for k in range(0, _upper_limit+1):
    PI += ((-1)**k)/(2*k+1)
    
PI = 4*PI