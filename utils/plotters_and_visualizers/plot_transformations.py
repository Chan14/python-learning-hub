# Example of a 2D Transformation
import numpy as np
import plotly.graph_objects as go
from IPython.display import display
from ipywidgets import Checkbox, FloatSlider, interact
from plot_vectors import plot_vectors_2d_plotly, plot_vectors_3d_plotly

# Original vector and standard basis vectors
original_vec_2d = np.array([2, 1])
standard_basis_2d = [np.array([1, 0]), np.array([0, 1])]


def plot_transformed_2d(m11, m12, m21, m22, show_grid):
    transformation_matrix_2d = np.array([[m11, m12], [m21, m22]])

    transformed_vec_2d = transformation_matrix_2d @ original_vec_2d
    transformed_basis_2d = [transformation_matrix_2d @ b for b in standard_basis_2d]

    print(f"Transformation Matrix:\n{transformation_matrix_2d}")
    print(f"Original Vector: {original_vec_2d}")
    print(f"Transformed Vector: {transformed_vec_2d}")

    plot_vectors_2d_plotly(
        [original_vec_2d, transformed_vec_2d],
        show_transformed_grid=show_grid,
        basis_vectors=transformed_basis_2d,
        title="2D Linear Transformation",
    )


# Create sliders for the matrix elements and a toggle for the grid
# sliders = [
#     FloatSlider(min=-2, max=2, step=0.1, value=1, description=f'm{i+1}{j+1}')
#     for i in range(2) for j in range(2)
# ]
# grid_toggle = widgets.Checkbox(value=False, description='Show Transformed Grid')

# # In a Jupyter notebook, this will create an interactive plot
# # interact(plot_transformed_2d, m11=sliders[0], m12=sliders[1], m21=sliders[2], m22=sliders[3], show_grid=grid_toggle);
# (Uncomment the above lines and run in Jupyter to see it in action)


# Example of a 3D Transformation
# (Similar structure to 2D, but with a 3x3 matrix and 3 basis vectors)
# Define the original vector and standard basis vectors
original_vec_3d = np.array([1, 2, 3])
standard_basis_3d = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]


# This is the function that will be called by the ipywidgets `interact`
def plot_transformed_3d(m11, m12, m13, m21, m22, m23, m31, m32, m33, show_grid):
    """
    Applies a 3D linear transformation and plots the original vector,
    the transformed vector, and optionally the transformed grid.

    Args for sliders:
        m_ij (float): Elements of the 3x3 transformation matrix.
        show_grid (bool): Flag to show or hide the transformed grid.
    """

    transformation_matrix_3d = np.array(
        [[m11, m12, m13], [m21, m22, m23], [m31, m32, m33]]
    )

    transformed_vec_3d = transformation_matrix_3d @ original_vec_3d
    transformed_basis_3d = [transformation_matrix_3d @ b for b in standard_basis_3d]

    print(f"Transformation Matrix:\n{transformation_matrix_3d}")
    print(f"Original Vector: {original_vec_3d}")
    print(f"Transformed Vector: {transformed_vec_3d}")

    plot_vectors_3d_plotly(
        [original_vec_3d, transformed_vec_3d],
        show_transformed_grid=show_grid,
        basis_vectors=transformed_basis_3d,
        title="3D Linear Transformation",
    )


# Similar interactive setup as 2D with 9 sliders for the 3x3 matrix
# (Uncomment and set up sliders/toggle in Jupyter for interactive use)
# Create sliders for the matrix elements and a toggle for the grid
# We use a default range for the matrix elements to allow for common transformations
sliders = {
    "m11": FloatSlider(min=-2, max=2, step=0.1, value=1, description="m11"),
    "m12": FloatSlider(min=-2, max=2, step=0.1, value=0, description="m12"),
    "m13": FloatSlider(min=-2, max=2, step=0.1, value=0, description="m13"),
    "m21": FloatSlider(min=-2, max=2, step=0.1, value=0, description="m21"),
    "m22": FloatSlider(min=-2, max=2, step=0.1, value=1, description="m22"),
    "m23": FloatSlider(min=-2, max=2, step=0.1, value=0, description="m23"),
    "m31": FloatSlider(min=-2, max=2, step=0.1, value=0, description="m31"),
    "m32": FloatSlider(min=-2, max=2, step=0.1, value=0, description="m32"),
    "m33": FloatSlider(min=-2, max=2, step=0.1, value=1, description="m33"),
    "show_grid": Checkbox(value=False, description="Show Transformed Grid"),
}

# Use ipywidgets.interact to create the interactive controls
print(
    "Adjust the sliders below to see the effect of linear transformations on the 3D vector."
)
print("The blue vector is the original, and the orange vector is the transformed one.")
print("Check 'Show Transformed Grid' to visualize how the entire space is transformed.")
interact(plot_transformed_3d, **sliders)
