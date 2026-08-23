#================================================================================================#
#                              2D Data Visualization
#================================================================================================#
#
# 1. Contour Plot
#    ├── plt.contour()
#    ├── plt.contourf()
#    └── Contour Levels
#

# Mathematical Form:
# Z = f(X, Y)
#
# np.meshgrid()
# → Creates coordinate grids from x and y values
#
# plt.contour(X, Y, Z)
# → Creates contour lines
#
# plt.contourf(X, Y, Z)
# → Creates filled contour regions
#
# levels
# → Controls contour levels
#
# cmap
# → Controls colors
#
# plt.colorbar()
# → Shows the relationship between colors and Z values

#================================================================================================#





#================================================================================================#
# Structure-1: Basic Contour Plot
#------------------------------------------------------------------------------------------------#
# plt.contour()
#
# Statement:
# The plt.contour() function is used to create contour
# lines representing different levels of a 2D function or
# dataset.
#
# Structure:
# plt.contour(X, Y, Z)
#
# X → X-coordinate values
# Y → Y-coordinate values
# Z → Function or data values
#
#================================================================================================#

#Example-1: Basic Contour Plot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

plt.contour(X, Y, Z)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Contour Plot")

plt.show()



#================================================================================================#
# Structure-2: Contour Levels
#------------------------------------------------------------------------------------------------#
# levels
#
# Statement:
# The levels parameter is used to control the number
# or specific values of contour levels.
#
# Structure:
# plt.contour(X, Y, Z, levels=value)
#
#================================================================================================#

#Example-2:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

plt.contour(X, Y, Z, levels=10)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Contour Plot with 10 Levels")

plt.show()


#================================================================================================#
# Structure-3: Specific Contour Levels
#------------------------------------------------------------------------------------------------#
# levels=[value1, value2, value3, ...]
#
# Statement:
# A list of values can be used to specify the exact
# contour levels to be displayed.
#
# Structure:
# plt.contour(X, Y, Z, levels=[...])
#================================================================================================#

#Example-1:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

plt.contour(
    X,
    Y,
    Z,
    levels=[5, 10, 15, 20]
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Contour Plot with Specific Levels")

plt.show()

#================================================================================================#
# Structure-4: Filled Contour Plot
#------------------------------------------------------------------------------------------------#
# plt.contourf()
#
# Statement:
# The plt.contourf() function is used to create a contour
# plot with filled colors between contour levels.
#
# Structure:
# plt.contourf(X, Y, Z)
#
# X → X-coordinate values
# Y → Y-coordinate values
# Z → Function or data values
#
#================================================================================================#

#Example-3: Filled Contour Plot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

plt.contourf(X, Y, Z)

plt.colorbar()

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Filled Contour Plot")

plt.show()


#================================================================================================#
# Structure-5: Contour Plot with Colormap
#------------------------------------------------------------------------------------------------#
# plt.contourf(X, Y, Z, cmap="...")
#
# Statement:
# The cmap parameter is used to control the colors
# used in a filled contour plot.
#
# Structure:
# plt.contourf(X, Y, Z, cmap="viridis")
#================================================================================================#

#Example-1: Contour Plot with Colormap
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

plt.contourf(
    X,
    Y,
    Z,
    cmap="viridis"
)

plt.colorbar()

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Contour Plot with Colormap")

plt.show()


#Example: Contour Lines & Filled Colors
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

plt.contourf(X, Y, Z, cmap="viridis")

plt.contour(X, Y, Z)

plt.colorbar()

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Contour Plot with Lines and Colors")

plt.show()