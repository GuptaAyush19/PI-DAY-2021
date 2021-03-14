# Pi Day 2021
<img src="./images/nasa.jpg" width=100% alt="NASA Pi Challenge">

Pi Day is an annual celebration of the mathematical constant π. Celebrated on March 14th (3/14) around the world, pi (Greek letter “π”) is the symbol used in mathematics to represent a constant — the ratio of the circumference of a circle to its diameter — which is approximately 3.14159.

It has been a tradition to calculate the approximate value of π on this day using physics experiments and computers. We will be using python, mathematical formulas proved by renowned mathematicians and physics simulator.

## Approximation of π

* Generating random numbers between 0 and 1, using it to create a quarter circle and calculating its area
* Gregory-Leibniz series
* Madhava of Sangamagrama
* Newton's Approximation of π
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

## Download Source Code
To download the source code using git enter this command in your system's terminal
```
git clone https://github.com/GuptaAyush19/PI-DAY-2021.git
```

If you do not have _git_ installed download the zip file from [here]().

## Execute the program
To run this python program, open terminal and enter
```
python main.py
```

This will be the expected output
```
APPROX PI = 3.141592653589793
gregory_leibniz pi = 3.1514934010709914, diff = -0.0099, preci = -0.3151
madhava pi = 3.141592653589794, diff = -0.0, preci = -0.0
newton pi = 3.292481961083404, diff = -0.1509, preci = -4.8033
quarter_circle pi = 3.1244000000000005, diff = 0.0172, preci = 0.5475
ramanujan_sato pi = 3.141592653589793, diff = 0.0, preci = 0.0
sqrt_g pi = 3.132091952673165, diff = 0.0095, preci = 0.3024
taylor_series pi = 3.141592653589793, diff = 0.0, preci = 0.0
twenty_two_by_7 pi = 3.142857142857143, diff = -0.0013, preci = -0.0414
```
*NOTE: quarter_circle uses random numbers so the output may differ each time you run the program.* 