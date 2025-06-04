import numpy as np
import plotly.graph_objects as go


def plot_vectors_2d_plotly(
    vectors, show_transformed_grid=False, basis_vectors=None, title="2D Vector Plot"
):
    """
    Plots 2D vectors using Plotly.

    Args:
        vectors (list of np.array): A list of 2D numpy arrays representing the vectors.
        show_transformed_grid (bool): If True, plots a grid based on the basis_vectors.
        basis_vectors (list of np.array, optional): A list of two 2D numpy arrays
                                                    representing the basis vectors (e.g., [[1,0],[0,1]]).
                                                    Required if show_transformed_grid is True.
        title (str): The title of the plot.
    """
    fig = go.Figure()

    # Plot each vector
    for i, vec in enumerate(vectors):
        fig.add_trace(
            go.Scatter(
                x=[0, vec[0]],
                y=[0, vec[1]],
                mode="lines+markers",
                name=f"Vector {i+1}",
                line=dict(width=2),
                marker=dict(size=8),
            )
        )

    # Add origin marker
    fig.add_trace(
        go.Scatter(
            x=[0],
            y=[0],
            mode="markers",
            marker=dict(size=5, color="black"),
            name="Origin",
        )
    )

    # Plot transformed grid if requested
    if show_transformed_grid:
        if (
            basis_vectors is None
            or len(basis_vectors) != 2
            or basis_vectors[0].shape != (2,)
            or basis_vectors[1].shape != (2,)
        ):
            raise ValueError(
                "basis_vectors must be a list of two 2D numpy arrays when show_transformed_grid is True."
            )

        # Generate grid points based on transformed basis vectors
        grid_range = 5  # Extend grid for better visualization
        transformed_grid_x = []
        transformed_grid_y = []

        for i in range(-grid_range, grid_range + 1):
            for j in range(-grid_range, grid_range + 1):
                point = i * basis_vectors[0] + j * basis_vectors[1]
                transformed_grid_x.append(point[0])
                transformed_grid_y.append(point[1])

        # Plot grid points as a scatter plot (can be styled as desired)
        fig.add_trace(
            go.Scatter(
                x=transformed_grid_x,
                y=transformed_grid_y,
                mode="markers",
                marker=dict(size=2, color="lightgray"),
                name="Transformed Grid",
            )
        )

        # Optionally, plot the transformed basis vectors themselves
        for i, b_vec in enumerate(basis_vectors):
            fig.add_trace(
                go.Scatter(
                    x=[0, b_vec[0]],
                    y=[0, b_vec[1]],
                    mode="lines",
                    name=f"Basis Vector {i+1}",
                    line=dict(width=2, dash="dash"),
                )
            )

    fig.update_layout(
        title=title,
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        xaxis_range=[-5, 5],  # Adjust limits as needed
        yaxis_range=[-5, 5],
        hovermode="closest",
        showlegend=True,
        template="plotly_white",
        xaxis=dict(gridcolor="lightgray", zerolinecolor="lightgray"),
        yaxis=dict(gridcolor="lightgray", zerolinecolor="lightgray"),
    )

    fig.show()


def plot_vectors_3d_plotly(
    vectors, show_transformed_grid=False, basis_vectors=None, title="3D Vector Plot"
):
    """
    Plots 3D vectors using Plotly.

    Args:
        vectors (list of np.array): A list of 3D numpy arrays representing the vectors.
        show_transformed_grid (bool): If True, plots a grid based on the basis_vectors.
        basis_vectors (list of np.array, optional): A list of three 3D numpy arrays
                                                    representing the basis vectors (e.g., [[1,0,0],[0,1,0],[0,0,1]]).
                                                    Required if show_transformed_grid is True.
        title (str): The title of the plot.
    """
    fig = go.Figure()

    # Plot each vector
    for i, vec in enumerate(vectors):
        fig.add_trace(
            go.Scatter3d(
                x=[0, vec[0]],
                y=[0, vec[1]],
                z=[0, vec[2]],
                mode="lines+markers",
                name=f"Vector {i+1}",
                line=dict(width=4),
                marker=dict(size=4),
            )
        )

    # Add origin marker
    fig.add_trace(
        go.Scatter3d(
            x=[0],
            y=[0],
            z=[0],
            mode="markers",
            marker=dict(size=5, color="black"),
            name="Origin",
        )
    )

    # Plot transformed grid if requested
    if show_transformed_grid:
        if (
            basis_vectors is None
            or len(basis_vectors) != 3
            or basis_vectors[0].shape != (3,)
            or basis_vectors[1].shape != (3,)
            or basis_vectors[2].shape != (3,)
        ):
            raise ValueError(
                "basis_vectors must be a list of three 3D numpy arrays when show_transformed_grid is True."
            )

        grid_range = 3  # Extend grid for better visualization
        transformed_grid_x = []
        transformed_grid_y = []
        transformed_grid_z = []

        # Generate grid points based on transformed basis vectors
        for i in range(-grid_range, grid_range + 1):
            for j in range(-grid_range, grid_range + 1):
                for k in range(-grid_range, grid_range + 1):
                    point = (
                        i * basis_vectors[0]
                        + j * basis_vectors[1]
                        + k * basis_vectors[2]
                    )
                    transformed_grid_x.append(point[0])
                    transformed_grid_y.append(point[1])
                    transformed_grid_z.append(point[2])

        fig.add_trace(
            go.Scatter3d(
                x=transformed_grid_x,
                y=transformed_grid_y,
                z=transformed_grid_z,
                mode="markers",
                marker=dict(size=1.5, color="lightgray", opacity=0.3),
                name="Transformed Grid",
            )
        )

        # Optionally, plot the transformed basis vectors themselves
        for i, b_vec in enumerate(basis_vectors):
            fig.add_trace(
                go.Scatter3d(
                    x=[0, b_vec[0]],
                    y=[0, b_vec[1]],
                    z=[0, b_vec[2]],
                    mode="lines",
                    name=f"Basis Vector {i+1}",
                    line=dict(width=3, dash="dash"),
                )
            )

    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title="X-axis",
            yaxis_title="Y-axis",
            zaxis_title="Z-axis",
            xaxis=dict(range=[-5, 5], gridcolor="lightgray", zerolinecolor="lightgray"),
            yaxis=dict(range=[-5, 5], gridcolor="lightgray", zerolinecolor="lightgray"),
            zaxis=dict(range=[-5, 5], gridcolor="lightgray", zerolinecolor="lightgray"),
            aspectmode="cube",  # Ensures equal scaling for better intuition
        ),
        hovermode="closest",
        showlegend=True,
        template="plotly_white",
    )

    fig.show()
