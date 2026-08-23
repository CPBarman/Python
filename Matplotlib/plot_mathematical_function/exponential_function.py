#================================================================================================#
#                                   Exponential Function
#================================================================================================#
# Mathematical Form:
#
# y = eˣ
#
# NumPy:
#
# np.exp(x)
# → Calculates eˣ
#
# Exponential Growth:
#
# y = np.exp(x)
#
# Exponential Decay:
#
# y = np.exp(-x)
#================================================================================================#




#================================================================================================#
# Structure-1: Exponential Function
#------------------------------------------------------------------------------------------------#
# Exponential Function:
#
# y = eˣ
#
# Statement:
# An exponential function is a mathematical function in which
# the variable x appears in the exponent.
#
# Structure:
# y = np.exp(x)
#
# np.exp(x) → Calculates e raised to the power of x
#
#================================================================================================#

#Example-1: 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)

y = np.exp(x)

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Exponential Function: y = eˣ")

plt.grid()

plt.show()


#================================================================================================#
# Structure-2: Exponential Function with Coefficient
#------------------------------------------------------------------------------------------------#
# Mathematical Form:
#
# y = aeˣ
#
# Structure:
# y = a * np.exp(x)
#
# a → Coefficient
#================================================================================================#

#Example-1: 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)

a = 2

y = a * np.exp(x)

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Exponential Function: y = 2eˣ")

plt.grid()

plt.show()

#Example-2: 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)

growth = np.exp(x)
decay = np.exp(-x)

plt.plot(x, growth, label="Growth: eˣ")
plt.plot(x, decay, label="Decay: e⁻ˣ")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Exponential Growth and Decay")

plt.legend()
plt.grid()

plt.show()