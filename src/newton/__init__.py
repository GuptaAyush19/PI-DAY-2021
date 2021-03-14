from math import sqrt as _sqrt

_series = ((5*(2**5))**-1)+((28*(2**7))**-1)+((72*(2**9))**-1)

#NOTE: Only 3 terms are used in this approximation because
#the other terms are too big to be computed
PI = ((3*_sqrt(3))/4) + 2 - _series