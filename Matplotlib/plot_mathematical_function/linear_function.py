#================================================================================================#
#                                   Linear Function
#================================================================================================#
#
#
#================================================================================================#




#================================================================================================#
# Structure-1: Linear Function
#------------------------------------------------------------------------------------------------#
# Linear Function:
#
# y = mx + c
#
# Statement:
# A linear function represents a straight-line relationship
# between x and y.
#
# m → Slope
# c → Y-intercept
#
# Structure:
# y = m*x + c
#
#================================================================================================#

#Example-1: 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y = 2*x + 1

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Function: y = 2x + 1")

plt.grid()

plt.show()

#Example-2: 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y1 = 2*x + 1
y2 = -x + 3

plt.plot(x, y1, label="y = 2x + 1")
plt.plot(x, y2, label="y = -x + 3")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Functions")

plt.legend()
plt.grid()

plt.show()