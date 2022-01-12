from sympy import *
#knowledge = And((Not(rain)>> hagrid),Or(hagrid, dumbledore),Not(And(hagrid, dumbledore)), dumbledore )
#print(knowledge)
""" If it didn’t rain, Harry visited Hagrid today.
Harry visited Hagrid or Dumbledore today, but not both.
Harry visited Dumbledore today."""

from sympy.logic import SOPform
from sympy import symbols
from sympy.logic import simplify_logic
from sympy.logic.inference import satisfiable
from sympy.abc import X, Y, Z
from sympy import S

X = X = Symbol("It is raining.")  # rain
Y = Symbol("Harry visited Hagrid")  # hagrid
Z = Symbol("Harry visited Dumbledore")  # dumbeldore

b=  (Z | Y) & (Implies(~X, Y)) & ~(Z & Y) & Z
print(" harry visited dumbeldore and it is raining and not visited hagrid ")
simplify_logic(b)
satisfiable(b)

b=  (Z | Y) & (X>>~Y) & ~(Z & Y) & Y
print("harry visited hagrid and not visited dumbledore and it is not raining ")
simplify_logic(b)

b=  (Z | Y) & (X >> ~Y) & ~(Z & Y) & X
print("It is raining today so harry visited dumbledore and not hagrid")
simplify_logic(b)

