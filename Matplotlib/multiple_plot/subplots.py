#================================================================================================#
#                                      Subplots
#
# 1. plt.subplot()      → Creates/activates a subplot
# 2. Rows and Columns   → Controls subplot layout
# 3. Plot Position      → Selects subplot position
# 4. plt.subplots()     → Creates Figure and Axes
# 5. Multiple Plots     → Displays multiple graphs in one Figure
#================================================================================================#




#================================================================================================#
# Structure-1: Subplots
#------------------------------------------------------------------------------------------------#
# plt.subplot()
#
# Statement:
# The plt.subplot() function is used to create multiple
# plots within a single figure.
#
# Structure:
# plt.subplot(rows, columns, index)
#
# rows    → Number of rows
# columns → Number of columns
# index   → Position of the current plot
#================================================================================================#

#Example-1
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# First Plot
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Linear")

# Second Plot
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Quadratic")

plt.show()



#Example-2:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# First Plot
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title("Linear")

# Second Plot
plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title("Quadratic")

plt.show()


#================================================================================================#
# Structure-3: plt.subplots()
#------------------------------------------------------------------------------------------------#
# plt.subplots()
#
# Statement:
# The plt.subplots() function is used to create a figure
# and one or more Axes objects for multiple plots.
#
# Structure:
# fig, ax = plt.subplots(rows, columns)
#
# fig → Figure object
# ax  → Axes object(s)
#================================================================================================#

#Example-1: 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

fig, ax = plt.subplots(1, 2)

ax[0].plot(x, y1)
ax[0].set_title("Linear")

ax[1].plot(x, y2)
ax[1].set_title("Quadratic")

plt.show()

