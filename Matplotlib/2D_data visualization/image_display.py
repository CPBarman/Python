#================================================================================================#
#                              2D Data Visualization
#================================================================================================#
#
# 1. Image Display
#    ├── plt.imshow()
#    ├── cmap
#    └── Colorbar
#
# 2. Contour Plot
#    ├── plt.contour()
#    ├── plt.contourf()
#    └── Contour Levels
#
# plt.imshow(data)
# → Displays a 2D array as an image
#
# cmap="..."
# → Controls how values are represented by colors
#
# plt.colorbar()
# → Shows the relationship between colors and values
#================================================================================================#




#================================================================================================#
# Structure-1: Image Display using plt.imshow()
#------------------------------------------------------------------------------------------------#
# plt.imshow()
#
# Statement:
# The plt.imshow() function is used to display data as
# an image.
#
# Each value in a 2D array can be represented using
# a different color.
#
# Structure:
# plt.imshow(data)
#
# data → A 2D array or image data
#================================================================================================#

#Example-1: Displaying a 2D Array
import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

plt.imshow(data)

plt.show()


#================================================================================================#
# Structure-2: Image Display with Colormap
#------------------------------------------------------------------------------------------------#
# plt.imshow(data, cmap="colormap_name")
#
# Statement:
# The cmap parameter is used to specify the colormap
# for displaying numerical values as colors.
#
# Structure:
# plt.imshow(data, cmap="viridis")
#================================================================================================#

#Structure-2: imshow() with Colormap
import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

plt.imshow(data, cmap="viridis")

plt.show()


#================================================================================================#
# Structure-3: Image Display with Colorbar
#------------------------------------------------------------------------------------------------#
# plt.imshow(data, cmap="...")
# plt.colorbar()
#
# Statement:
# The colorbar shows the relationship between the colors
# in the image and the numerical values of the data.
#================================================================================================#

#Example
import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

plt.imshow(data, cmap="viridis")

plt.colorbar()

plt.title("2D Data Visualization")

plt.show()