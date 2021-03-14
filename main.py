from sys import path
path.append("./src")

PI = 3.141592653589793238

import gregory_leibniz
import madhava
import newton
import quarter_circle
import ramanujan_sato
import sqrt_g
import taylor_series
import twenty_two_by_7

def diff(module_pi):
    return round(PI-float(module_pi), 4)

def diff_perc(module_pi):
    return round(diff(module_pi)/PI*100, 4)

def nprint(mod):
    print(mod.__name__+f" pi = {mod.PI}", f"diff = {diff(mod.PI)}", f"preci = {diff_perc(mod.PI)}", sep=", ", end="\n")

print("APPROX PI =", PI)
nprint(gregory_leibniz)
nprint(madhava)
nprint(newton)
nprint(quarter_circle)
nprint(ramanujan_sato)
nprint(sqrt_g)
nprint(taylor_series)
nprint(twenty_two_by_7)