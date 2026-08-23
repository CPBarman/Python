#================================================================================================#
#                                Saving Figures
#================================================================================================#
#
# 1. Saving Figures
#    └── plt.savefig()
#
# 2. Figure Resolution
#    └── dpi
#
#================================================================================================#





#================================================================================================#
# Structure-1: Saving Figures
#------------------------------------------------------------------------------------------------#
# plt.savefig()
#
# Statement:
# The plt.savefig() function is used to save the current
# figure as an image or document file.
#
# Structure:
# plt.savefig("filename.extension")
#
# filename  → Name of the file
# extension → File format
#
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("My First Saved Figure")

plt.savefig("my_plot.png")

plt.show()


