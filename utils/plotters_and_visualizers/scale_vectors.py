import numpy as np
from IPython.display import display
from ipywidgets import FloatSlider, interact
from plot_vectors import plot_vectors_2d_plotly, plot_vectors_3d_plotly

# Define your original vector
original_vec = np.array([2, 1, 4])  # For 2D
# original_vec = np.array([1, 2, 3]) # For 3D


def plot_scaled_vector(scale_factor):
    scaled_vec = scale_factor * original_vec
    print(f"Scaled Vector: {scaled_vec}")
    # Choose the appropriate plotting function based on dimension
    if len(original_vec) == 2:
        plot_vectors_2d_plotly(
            [original_vec, scaled_vec], title=f"Scaled Vector (Scale: {scale_factor})"
        )
    else:
        plot_vectors_3d_plotly(
            [original_vec, scaled_vec], title=f"Scaled Vector (Scale: {scale_factor})"
        )


# Create a slider for the scale factor
scale_slider = FloatSlider(min=-3, max=3, step=0.1, value=1, description="Scale Factor")

# Link the slider to the plotting function
# In a Jupyter notebook, this will create an interactive plot
interact(plot_scaled_vector, scale_factor=scale_slider)
# (Uncomment the above line and run in Jupyter to see it in action)
