import matplotlib.pyplot as plt

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

