# area(quarter circle):area(square) = pi/4
from random import random as _random
from math import sqrt as _sqrt

class QuarterCircle:
    def __init__(self):
        self._grid = []
        
    def _fill_grid(self):
        for point in range(0, 100):
            self._grid.append(self._random_point())
    
    @staticmethod
    def _dist(point:tuple) -> float:
        return _sqrt((point[0]**2)+(point[1]**2)) 
    
    @staticmethod
    def _random_point() -> tuple:
        return (_random(), _random())
        
    @property
    def PI(self):
        self._fill_grid()
        _count = 0
        for point in self._grid:
            if self._dist(point)<1:
                _count += 1
        return (_count/len(self._grid))*4
    
pi_sum = 0
    
for i in range(0, 100):
    pi_sum += QuarterCircle().PI
    
PI = pi_sum/100 