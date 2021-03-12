<img src="images/nasa.jpg" width=100% alt="NASA Pi Challenge"></img>

Pi Day is an annual celebration of the mathematical constant π. Celebrated on March 14th (3/14) around the world, pi (Greek letter “π”) is the symbol used in mathematics to represent a constant — the ratio of the circumference of a circle to its diameter — which is approximately 3.14159.

It has been a tradition to calculate the approximate value of π on this day using physics experiments and computers. We will be using python, mathematical formulas proved by renowned mathematicians and physics simulator.

## Approximation of π

* Archimedes’ approximation (polygon method)
* Eulers’ identity _e<sup>iπ</sup>-1=0_
* Generating random numbers between 0 and 1, using it to create a quarter circle and calculating its area
* Gregory-Leibniz series
* Madhava of Sangamagrama
* Ramanujan-Sato series
* Square root of _g_ (acceleration due to gravity on Earth)
* Trigonometric Ratios ie Taylor series
* Divide Twenty-two by seven
 
## Limitations of using Python
Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. For example, the decimal fraction
```
0.125
```
has value 1/10 + 2/100 + 5/1000, and in the same way the binary fraction
```
0.001
```
has value 0/2 + 0/4 + 1/8. These two fractions have identical values, the only real difference being that the first is written in base 10 fractional notation, and the second in base 2.

Unfortunately, most decimal fractions cannot be represented exactly as binary fractions. A consequence is that, in general, the decimal floating-point numbers you enter are only approximated by the binary floating-point numbers actually stored in the machine.

Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine. On most machines, if Python were to print the true decimal value of the binary approximation stored for 0.1, it would have to display

```
>>> 0.1
0.1000000000000000055511151231257827021181583404541015625
```
Read more about this error [here](https://docs.python.org/3/tutorial/floatingpoint.html).
