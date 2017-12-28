import matplotlib.pyplot as plt
import numpy as np

# Print chart of the function (in range <0; length-1>)
# assuming that index is the argument of function

plt.plot([0, 5, 1, 6, 2, 7, 3, 8, 4, 9])
# plt.show()

# Print chart of the function with given two vectors:
# first are function arguments
# second are results for arguments

plt.plot([1, 4, 5], [5, 6, 7])
# plt.show()

# It's also possible to configure chart style:
# Line types:
# -      - solid line
# :      - point line
# -.     - dot-line line
# --     - dashed line

# Solid line:
plt.plot([1, 4, 5], [5, 6, 7], '-')
# plt.show()

# Point line
plt.plot([1, 4, 5], [5, 6, 7], ':')
# plt.show()

# Dot line
plt.plot([1, 4, 5], [5, 6, 7], '-.')
# plt.show()

# Dashed line
plt.plot([1, 4, 5], [5, 6, 7], '--')
# plt.show()

# Yellow line:
plt.plot([1, 4, 5], [5, 6, 7], 'y')
# plt.show()

# Magenta line
plt.plot([1, 4, 5], [5, 6, 7], 'm')
# plt.show()

# Cyan line
plt.plot([1, 4, 5], [5, 6, 7], 'c')
# plt.show()

# Red line
plt.plot([1, 4, 5], [5, 6, 7], 'r')
# plt.show()

# Green line
plt.plot([1, 4, 5], [5, 6, 7], 'g')
# plt.show()

# Blue line
plt.plot([1, 4, 5], [5, 6, 7], 'b')
# plt.show()

# White line
plt.plot([1, 4, 5], [5, 6, 7], 'w')
# plt.show()

# Black line
plt.plot([1, 4, 5], [5, 6, 7], 'k')
# plt.show()

# Creating chart with symbols instead of lines:
# Dots line
plt.plot([1, 4, 5], [5, 6, 7], '.')
# plt.show()

# Circles line
plt.plot([1, 4, 5], [5, 6, 7], 'o')
# plt.show()

# X line
plt.plot([1, 4, 5], [5, 6, 7], 'x')
# plt.show()

# + line
plt.plot([1, 4, 5], [5, 6, 7], '+')
# plt.show()

# * line
plt.plot([1, 4, 5], [5, 6, 7], '*')
# plt.show()

# s line
plt.plot([1, 4, 5], [5, 6, 7], 's')
# plt.show()

# diamond line
plt.plot([1, 4, 5], [5, 6, 7], 'd')
# plt.show()

# down triangle line
plt.plot([1, 4, 5], [5, 6, 7], 'v')
# plt.show()

# up triangle line
plt.plot([1, 4, 5], [5, 6, 7], '^')
# plt.show()

# left triangle line
plt.plot([1, 4, 5], [5, 6, 7], '<')
# plt.show()

# right triangle line
plt.plot([1, 4, 5], [5, 6, 7], '>')
# plt.show()

# pentagon line
plt.plot([1, 4, 5], [5, 6, 7], 'p')
# plt.show()

# hexagon line
plt.plot([1, 4, 5], [5, 6, 7], 'h')
# plt.show()

# There can be multiple charts printed using single plot.
# In that case they are represented as triples:
# ([arguments], [function results for those arguments], 'string configuration')
plt.plot([1, 2], [3, 4], 'r^', [0, 1], [4, 5], 'bv')
# plt.show()

# It is possible to pass only function results - in that case arguments are indexes of function results
# and the chart is printed using standard, black line:
plt.plot([1, 2], 'yo', [0, 1])
# plt.show()

# Chart is also configurable using keyword arguments:
plt.plot([1, 2], [3, 4], linestyle='dashed', marker='o', color='green')
# plt.show()

# Set vertical and horizontal limits of plot:
plt.plot([1, 2], [3, 4])
plt.xlim(2, 4)
plt.ylim(4, 8)
# plt.show()

# Set chart title and labels for each axis:
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('chart title')
# plt.show()

# Window parameters are also configurable:
# figsize - (vertical size in inches, horizontal size in inches)
plt.figure(figsize=(4, 6), dpi=100)
# plt.show()

plt.xticks([1, 2, 3])
plt.yticks(np.linspace(2, 4, 10))
# plt.show()

# Configure axis:
ax = plt.gca()
# Don't print right frame
ax.spines['right'].set_color('none')
# Don't print bottom frame
ax.spines['bottom'].set_color('none')
# Set ticks position to be under the x axis
ax.xaxis.set_ticks_position('bottom')
# Set ticks position to be on the right of the y axis
ax.yaxis.set_ticks_position('right')
# Set bottom border to the center
ax.spines['top'].set_position(('data', 0))
# Set bottom border to the center
ax.spines['left'].set_position(('data', 0))
# Set x ticks to range <-1, 1>
plt.xticks(np.linspace(-1, 1, 5), np.linspace(-1, 1, 5))
# Set y ticks to range <-1, 1>
plt.yticks(np.linspace(-1, 1, 5), np.linspace(-1, 1, 5))
# plt.show()

# Show function charts, i.e. sin/cos functions:
v1 = np.linspace(-10, 10, 500)
x1 = np.sin(v1)
plt.plot(v1, x1, 'rd', label='sin')
v2 = np.linspace(-10, 10, 500)
x2 = np.cos(v2)
plt.plot(v2, x2, 'gv', label='cos')
plt.legend('upper right')
# Set font size:
plt.rc('font', size=10)
plt.title('Test')
# plt.show()

# Add single highlighted point on chart:
v = np.linspace(-0, 3, 1000)
y = np.sin(v)
plt.plot(v, y, 'r-')
plt.scatter([v[500]], [y[500]], color='green')
# plt.show()

# Linear chart
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

plt.plot(x, y)
plt.grid(True)
plt.yscale('linear')
# plt.show()

# Logarithmic chart
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

plt.plot(x, y)
plt.grid(True)
plt.yscale('log')
plt.show()

# The same as previous chart
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

plt.semilogy(x, y)
plt.show()
