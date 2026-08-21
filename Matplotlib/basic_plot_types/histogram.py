#================================================================================================#
#                                           Histogram
#================================================================================================#




#================================================================================================#
# Structure-1: Histogram
#------------------------------------------------------------------------------------------------#
# plt.hist(data)
#
# Statement:
# The plt.hist() function is used to create a histogram.
#
# A histogram is used to show the frequency distribution
# of numerical data.
#
# Structure:
# plt.hist(data)
#
# data → Numerical data
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt
marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75,
         78, 80, 82, 85, 88, 90, 92, 95]

plt.hist(marks)
plt.show()


#================================================================================================#
# Structure-3: Bins
#------------------------------------------------------------------------------------------------#
# plt.hist(data, bins=value)
#
# Statement:
# The bins parameter determines the number of intervals
# into which the data is divided.
#
# Structure:
# plt.hist(data, bins=number)
#
# bins → Number of intervals
#================================================================================================#

#Example-1
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75,
         78, 80, 82, 85, 88, 90, 92, 95]

plt.hist(marks, bins=5)

plt.show()


