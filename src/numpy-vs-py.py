import sys
import numpy as np

# Loc class representing a vector in 3D space
class Loc:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

# Facet class composed of three Loc objects
class Facet:
	def __init__(self, loc1, loc2, loc3):
		self.loc1 = loc1
		self.loc2 = loc2
		self.loc3 = loc3

# Grid representing a grid of Facet objects
class Grid:
	def __init__(self, rows, cols):
		self.grid = [[None] * cols for _ in range(rows)]


# NumPy array equivalent
rows = 4
cols = 750
facet_dtype = np.dtype([
	('loc1', np.float64, (3,)),
	('loc2', np.float64, (3,)),
	('loc3', np.float64, (3,))
])
np_grid = np.empty((rows, cols), dtype=facet_dtype)

# Get memory usage of custom Python grid structure
custom_python_size = sys.getsizeof(Grid(rows, cols).grid)
facet_size = sys.getsizeof(Facet) + 3 * sys.getsizeof(Loc)
custom_python_total_size = custom_python_size + (rows * cols * facet_size)

# Get memory usage of NumPy array equivalent
np_array_size = np_grid.nbytes

# Print comparison
print("Memory Usage Comparison:")
print("Custom Python Grid Structure:")
print("- Grid Size: {} bytes".format(custom_python_size))
print("- Facet Object: {} bytes".format(facet_size))
print("- Total Size: {} bytes".format(custom_python_total_size))
print()
print("NumPy Array Equivalent:")
print("- Array Size: {} bytes".format(np_array_size))
