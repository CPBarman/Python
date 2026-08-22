#================================================================================================#
#                       PART-8: Advanced Plot Customization / Styling
#================================================================================================#
#
# 1. Axis Limits
#    ├── set_xlim()
#    └── set_ylim()
#
# 2. Tick Customization
#    ├── set_xticks()
#    └── set_yticks()
#
# 3. Tick Parameters
#    └── tick_params()
#
# 4. Spine Customization
#    └── ax.spines[]
#
# 5. Grid Customization
#    └── ax.grid()
#
# 6. Plot Style
#    └── plt.style.use()
#
#================================================================================================#



#================================================================================================#
# Structure-1: X-axis Limits
#------------------------------------------------------------------------------------------------#
# ax.set_xlim()
#
# Statement:
# The ax.set_xlim() method is used to set the visible
# range of values on the X-axis.
#
# Structure:
# ax.set_xlim(min, max)
#
# min → Minimum X-axis value
# max → Maximum X-axis value
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_xlim(0, 6)

plt.show()


#================================================================================================#
# Structure-2: Y-axis Limits
#------------------------------------------------------------------------------------------------#
# ax.set_ylim()
#
# Statement:
# The ax.set_ylim() method is used to set the visible
# range of values on the Y-axis.
#
# Structure:
# ax.set_ylim(min, max)
#
# min → Minimum Y-axis value
# max → Maximum Y-axis value
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_ylim(0, 12)

plt.show()


#================================================================================================#
# Structure-4: Y-axis Tick Positions
#------------------------------------------------------------------------------------------------#
# ax.set_yticks()
#
# Statement:
# The ax.set_yticks() method is used to specify the
# positions of ticks on the Y-axis.
#
# Structure:
# ax.set_yticks(values)
#
# values → Tick positions
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_yticks([0, 2, 4, 6, 8, 10])

plt.show()

#================================================================================================#
# Structure-5: Tick Parameters
#------------------------------------------------------------------------------------------------#
# ax.tick_params()
#
# Statement:
# The ax.tick_params() method is used to customize
# the appearance of ticks and tick labels.
#
# Structure:
# ax.tick_params(...)
#
# Common Parameters:
# axis      → "x", "y", or "both"
# direction → Tick direction
# length    → Tick length
# width     → Tick width
# labelsize → Tick label size
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.tick_params(axis="both")

plt.show()

#================================================================================================#
# Structure-6: Tick Direction
#------------------------------------------------------------------------------------------------#
# ax.tick_params(direction="...")
#
# Statement:
# The direction parameter is used to control
# the direction of the ticks.
#
# Common Values:
# "in"   → Ticks point inward
# "out"  → Ticks point outward
# "inout" → Ticks point both inward and outward
#
# Structure:
# ax.tick_params(direction="in")
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.tick_params(direction="in")

plt.show()


#================================================================================================#
# Structure-7: Tick Length
#------------------------------------------------------------------------------------------------#
# ax.tick_params(length=value)
#
# Statement:
# The length parameter is used to control
# the length of the ticks.
#
# Structure:
# ax.tick_params(length=value)
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.tick_params(length=8)

plt.show()

#================================================================================================#
# Structure-8: Tick Width
#------------------------------------------------------------------------------------------------#
# ax.tick_params(width=value)
#
# Statement:
# The width parameter is used to control
# the thickness of the ticks.
#
# Structure:
# ax.tick_params(width=value)
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.tick_params(width=2)

plt.show()


#================================================================================================#
# Structure-9: Tick Label Size
#------------------------------------------------------------------------------------------------#
# ax.tick_params(labelsize=value)
#
# Statement:
# The labelsize parameter is used to control
# the size of the tick labels.
#
# Structure:
# ax.tick_params(labelsize=value)
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.tick_params(labelsize=14)

plt.show()

#================================================================================================#
# Structure-10: X-axis Tick Parameters
#------------------------------------------------------------------------------------------------#
# ax.tick_params(axis="x", ...)
#
# Statement:
# axis="x" applies the tick customization only
# to the X-axis.
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.tick_params(
    axis="x",
    direction="in",
    length=8,
    width=2,
    labelsize=12
)

plt.show()