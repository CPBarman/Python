#================================================================================================#
#                                   Quadratic Function
#================================================================================================#
##
# General Form:
# y = ax² + bx + c
#
# Basic Example:
# y = x²
#
# Python:
# y = x**2
#
# NumPy:
# y = np.square(x)
#
# Graph:
# → Parabola
#
# a > 0 → Opens upward
# a < 0 → Opens downward
#
#================================================================================================#





#================================================================================================#
# Structure-1: General Quadratic Function
#------------------------------------------------------------------------------------------------#
# Statement:
# A general quadratic function has the form:
#
# y = ax² + bx + c
#
# Structure:
# y = a*x**2 + b*x + c
#================================================================================================#

#Example-1:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

a = 2
b = 3
c = 1

y = a*x**2 + b*x + c

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic Function: y = 2x² + 3x + 1")

plt.grid()

plt.show()


#================================================================================================#
# Structure-2: Quadratic Function using np.square()
#------------------------------------------------------------------------------------------------#
# np.square(x)
#
# Statement:
# The np.square() function returns the square
# of each element of an array.
#
# Structure:
# y = np.square(x)
#================================================================================================#

#Example-1: 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y = x**2

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic Function: y = x**2")

plt.grid()

plt.show()


#Example-2:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y = np.square(x)

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic Function: y = x²")

plt.grid()

plt.show()