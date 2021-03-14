from math import sqrt as _sqrt

_upper_limit = 100
PI = 0

for k in range(0, _upper_limit+1):
    PI += ((-1)**k)/((3**k)*(2*k+1))
    
PI *= _sqrt(12) 