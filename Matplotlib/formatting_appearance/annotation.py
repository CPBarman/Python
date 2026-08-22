#================================================================================================#
#                                        Annotate
#------------------------------------------------------------------------------------------------#
#
# plt.annotate("text", xy=(x, y))
# → Adds annotation to a specific point
#
# xy
# → Point being annotated
#
# xytext
# → Position of the annotation text
#
# arrowprops
# → Controls the annotation arrow
#
# arrowstyle
# → Controls arrow style
#
#================================================================================================#




#================================================================================================#
# Structure-1: Annotation
#------------------------------------------------------------------------------------------------#
# plt.annotate()
#
# Statement:
# The plt.annotate() function is used to add explanatory
# text to a specific point on a plot.
#
# It can also use an arrow to point to a specific
# data point.
#
# Structure:
# plt.annotate("text", xy=(x, y))
#
# text → Annotation text
# xy   → Coordinate of the point being annotated
#================================================================================================#

#Example-1: Basic Annotation
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.annotate(
    "Important Point",
    xy=(3, 6)
)

plt.show()

#================================================================================================#
# Structure-2: Annotation with Arrow
#------------------------------------------------------------------------------------------------#
# plt.annotate("text", xy=(x, y), xytext=(x, y),
#              arrowprops=dict(...))
#
# Statement:
# The xy parameter specifies the point being annotated,
# while xytext specifies the position of the annotation text.
#
# arrowprops is used to control the arrow.
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.annotate(
    "Important Point",
    xy=(3, 6),
    xytext=(4, 8),
    arrowprops=dict(arrowstyle="->")
)

plt.show()




#================================================================================================#
# Structure-3: Arrow Style
#------------------------------------------------------------------------------------------------#
# arrowprops=dict(arrowstyle="->")
#
# Statement:
# The arrowstyle parameter is used to control
# the style of the annotation arrow.
#
# Common Arrow Styles:
#
# "->"  → Simple arrow
# "<-"  → Reverse arrow
# "<->" → Double-headed arrow
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.annotate(
    "Maximum Point",
    xy=(5, 10),
    xytext=(3, 8),
    arrowprops=dict(arrowstyle="->")
)

plt.show()