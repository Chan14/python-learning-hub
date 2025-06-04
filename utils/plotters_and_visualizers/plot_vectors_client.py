import numpy as np
from plot_vectors import plot_vectors_2d_plotly, plot_vectors_3d_plotly

# Example Usage:

# 2D Vectors
vec_2d_1 = np.array([2, 3])
vec_2d_2 = np.array([-1, 4])
plot_vectors_2d_plotly([vec_2d_1, vec_2d_2], title="My 2D Vectors")

# 3D Vectors
vec_3d_1 = np.array([1, 2, 3])
vec_3d_2 = np.array([-2, 1, 4])
plot_vectors_3d_plotly([vec_3d_1, vec_3d_2], title="My 3D Vectors")
