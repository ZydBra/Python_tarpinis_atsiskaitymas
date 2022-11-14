# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos

# Kitų failų ir žemiau esančio kodo nekeiskite

from modules.numbers.numbers import *
from modules.math.multiplication import multiplication
from modules.math.subtraction import substraction
from modules.math.division import division as divivsion
from modules.math.composition import composition as addition

a = addition(one, four)
b = divivsion(four, two)
c = substraction(three, two)
d = multiplication(five, two)

print(a)
print(b)
print(c)
print(d)
