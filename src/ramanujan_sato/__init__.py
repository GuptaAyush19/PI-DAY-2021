from math import sqrt as _sqrt
from math import factorial as _fact

# pi = {n*sk}^{-1}
n = _sqrt(8)/(99**2)
sk = 0

for k in range(5):
    sk += ((_fact(4*k))/(_fact(k)**4))*((26390*k+1103)/(396**(4*k)))
    
PI = 1/(n*sk)