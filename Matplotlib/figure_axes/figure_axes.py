#================================================================================================#
#                                   Figure and Axes
#================================================================================================#
#
# 1. Figure
#    └── plt.figure()
#
# 2. Axes
#    └── fig.add_axes()
#
# 3. Figure and Axes together
#    └── plt.subplots()
#
# 4. Axes Methods
#    ├── ax.plot()
#    ├── ax.set_xlabel()
#    ├── ax.set_ylabel()
#    ├── ax.set_title()
#    ├── ax.grid()
#    └── ax.legend()
#
# 5. Multiple Axes
#    └── plt.subplots(rows, columns)
#
#================================================================================================#




#================================================================================================#
# Structure-1: Figure
#------------------------------------------------------------------------------------------------#
# plt.figure()
#
# Statement:
# The plt.figure() function is used to create a new Figure.
#
# A Figure is the overall container or canvas that holds
# one or more plots.
#
# Structure:
# fig = plt.figure()
#
# fig → Figure object
#================================================================================================#

#Example-1: 
import matplotlib.pyplot as plt
fig = plt.figure()
plt.show()


#================================================================================================#
# Structure-2: Figure Size
#------------------------------------------------------------------------------------------------#
# plt.figure(figsize=(width, height))
#
# Statement:
# The figsize parameter is used to set the width and height
# of a Figure.
#
# Structure:
# fig = plt.figure(figsize=(width, height))
#
# width  → Figure width in inches
# height → Figure height in inches
#================================================================================================#

#Example-1: 
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 5))
plt.show()

#================================================================================================#
# Structure-3: Axes
#------------------------------------------------------------------------------------------------#
# fig.add_axes()
#
# Statement:
# An Axes is the actual plotting area inside a Figure
# where data is displayed.
#
# Structure:
# ax = fig.add_axes([left, bottom, width, height])
#
# ax → Axes object
#================================================================================================#

#Example-1: 
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
plt.show()


#================================================================================================#
# Structure-4: Plot Using Figure and Axes
#------------------------------------------------------------------------------------------------#
# ax.plot(x, y)
#
# Statement:
# The ax.plot() method is used to create a line plot
# inside an Axes object.
#
# Structure:
# fig = plt.figure()
# ax = fig.add_axes([...])
# ax.plot(x, y)
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y)
plt.show()

#================================================================================================#
# Structure-5: Figure and Axes using plt.subplots()
#------------------------------------------------------------------------------------------------#
# plt.subplots()
#
# Statement:
# The plt.subplots() function is used to create a Figure
# and one or more Axes objects together.
#
# Structure:
# fig, ax = plt.subplots()
#
# fig → Figure object
# ax  → Axes object
#================================================================================================#

#Example-1: 
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.show()

#================================================================================================#
# Structure-6: Plot using Axes Object
#------------------------------------------------------------------------------------------------#
# ax.plot(x, y)
#
# Statement:
# The ax.plot() method is used to create a line plot
# inside the Axes object.
#
# Structure:
# fig, ax = plt.subplots()
# ax.plot(x, y)
#================================================================================================#

#Example-1: 
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


#================================================================================================#
# Structure-7: Figure Size using plt.subplots()
#------------------------------------------------------------------------------------------------#
# plt.subplots(figsize=(width, height))
#
# Statement:
# The figsize parameter is used to set the width and height
# of the Figure.
#
# Structure:
# fig, ax = plt.subplots(figsize=(width, height))
#================================================================================================#

#Example-1: 
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 5))

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

ax.plot(x, y)
plt.show()

#================================================================================================#
# Structure-8: Multiple Axes
#------------------------------------------------------------------------------------------------#
# plt.subplots(rows, columns)
#
# Statement:
# The plt.subplots() function can create multiple Axes
# arranged in rows and columns.
#
# Structure:
# fig, ax = plt.subplots(rows, columns)
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2)
plt.show()

#Example-2:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

fig, ax = plt.subplots(1, 2)

ax[0].plot(x, y1)
ax[1].plot(x, y2)

plt.show()


