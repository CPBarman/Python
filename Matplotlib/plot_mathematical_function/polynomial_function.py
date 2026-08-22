#================================================================================================#
#                                   Polynomial Function
#================================================================================================#
## Polynomial:
# y = aₙxⁿ + ... + a₂x² + a₁x + a₀
#
# Python:
# y = 2*x**3 - 3*x**2 + x + 5
#
# NumPy:
# np.polyval(coefficients, x)
#
# Degree:
# → Highest power of x
#
#==============================
#
#================================================================================================#




#================================================================================================#
# Structure-1: Polynomial Function
#------------------------------------------------------------------------------------------------#
# Polynomial Function:
#
# y = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₂x² + a₁x + a₀
#
# Statement:
# A polynomial function consists of powers of x
# with constant coefficients.
#
# Example:
# y = 2x³ - 3x² + x + 5
#
#================================================================================================#

#Example-1:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y = x**3

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Function: y = x³")

plt.grid()

plt.show()

#================================================================================================#
# Structure-2: General Polynomial Function
#------------------------------------------------------------------------------------------------#
# Statement:
# A polynomial function can contain multiple powers
# of x with different coefficients.
#
# Structure:
# y = a*x**3 + b*x**2 + c*x + d
#================================================================================================#

#Example-1:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)

y = 2*x**3 - 3*x**2 + x + 5

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Function")

plt.grid()

plt.show()


#Example-2:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)

a = 2
b = -3
c = 1
d = 5

y = a*x**3 + b*x**2 + c*x + d

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Function")

plt.grid()

plt.show()



#================================================================================================#
# Structure-3: np.polyval()
#------------------------------------------------------------------------------------------------#
# np.polyval(coefficients, x)
#
# Statement:
# The np.polyval() function evaluates a polynomial
# at given values of x.
#
# Structure:
# np.polyval([a, b, c, d], x)
#
# For:
# y = ax³ + bx² + cx + d
#
#================================================================================================#

#Example-1
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)

coefficients = [2, -3, 1, 5]

y = np.polyval(coefficients, x)

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial using np.polyval()")

plt.grid()

plt.show()


