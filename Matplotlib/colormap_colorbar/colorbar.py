#================================================================================================#
#                                Colormaps and Colorbar Summary 
#------------------------------------------------------------------------------------------------#
#
# cmap
# → Specifies a colormap
#
# c=values
# → Uses numerical values to determine colors
#
# plt.colorbar()
# → Displays the relationship between colors and values
#
# Example:
#
# plt.scatter(x, y, c=values, cmap="viridis")
# plt.colorbar()
#
#================================================================================================#




#================================================================================================#
# Structure-1: Colorbar
#------------------------------------------------------------------------------------------------#
# Colorbar
#
# Statement:
# A colorbar is used to show the relationship between
# colors and numerical values in a colormap.
#
# It helps us understand what each color represents.
#================================================================================================#



#================================================================================================#
# Structure-2: Adding a Colorbar
#------------------------------------------------------------------------------------------------#
# plt.colorbar()
#
# Statement:
# The plt.colorbar() function is used to add a colorbar
# to a plot that uses a colormap.
#
# Structure:
# plt.colorbar()
#================================================================================================#

#Example-2: Colormap with Colorbar
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

values = np.random.rand(50)

plt.scatter(
    x,
    y,
    c=values,
    cmap="viridis"
)

plt.colorbar()

plt.show()