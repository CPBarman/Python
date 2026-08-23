#================================================================================================#
#                                   Logarithmic Function
#================================================================================================#
# Natural Logarithm:
#
# np.log(x)
# → ln(x)
#
# Base-10 Logarithm:
#
# np.log10(x)
# → log₁₀(x)
#
# Important:
#
# x > 0
#
# Logarithmic functions increase slowly as x increases.
#
#================================================================================================#




#================================================================================================#
# Structure-30.5: Logarithmic Function
#------------------------------------------------------------------------------------------------#
# Logarithmic Function:
#
# y = log(x)
#
# Statement:
# A logarithmic function is a mathematical function that
# represents the logarithm of x.
#
# Structure:
# y = np.log(x)
#
# np.log(x) → Calculates the natural logarithm of x
#
#================================================================================================#

#Example-1: 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 100)

y = np.log(x)

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Logarithmic Function: y = ln(x)")

plt.grid()

plt.show()

#================================================================================================#
# Structure-2: Base-10 Logarithm
#------------------------------------------------------------------------------------------------#
# np.log10(x)
#
# Statement:
# The np.log10() function calculates the logarithm
# of x with base 10.
#
# Mathematical Form:
#
# y = log₁₀(x)
#
# Structure:
# y = np.log10(x)
#================================================================================================#

#Example-1:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 100, 100)

y = np.log10(x)

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Logarithmic Function: y = log₁₀(x)")

plt.grid()

plt.show()

#Example-2: Comparing Different Logarithmic Functions
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 100)

y1 = np.log(x)
y2 = np.log10(x)

plt.plot(x, y1, label="ln(x)")
plt.plot(x, y2, label="log₁₀(x)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparison of Logarithmic Functions")

plt.legend()
plt.grid()

plt.show()