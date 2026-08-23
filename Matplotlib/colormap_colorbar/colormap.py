#================================================================================================#
#                                        Colormaps
#------------------------------------------------------------------------------------------------#
#
# "viridis"
# → A smooth range of colors
#
# "plasma"
# → Bright color transition
#
# "inferno"
# → Dark-to-bright color transition
#
# "magma"
# → Dark-to-light color transition
#
# "coolwarm"
# → Useful for comparing low and high values
#
#================================================================================================#




#================================================================================================#
# Structure-1: Colormap
#------------------------------------------------------------------------------------------------#
# Colormap
#
# Statement:
# A colormap is a collection or range of colors that is used
# to represent different numerical values visually.
#
# In Matplotlib, colormaps are commonly used to map numerical
# data values to different colors.
#================================================================================================#


#================================================================================================#
# Structure-2: Using cmap
#------------------------------------------------------------------------------------------------#
# cmap
#
# Statement:
# The cmap parameter is used to specify which colormap
# should be used for visualizing numerical data.
#
# Structure:
# plt.scatter(x, y, c=values, cmap="colormap_name")
#
# c    → Numerical values used to determine colors
# cmap → Name of the colormap
#================================================================================================#

#Example-1: Colormap with Scatter Plot
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

plt.show()

