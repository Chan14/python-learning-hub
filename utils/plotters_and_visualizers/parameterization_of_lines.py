import matplotlib.pyplot as plt
import numpy as np


def get_2d_vector(prompt):
    """
    Prompts the user to input a 2D vector and returns it as a NumPy array.

    Args:
        prompt (str): The message displayed to the user for input.

    Returns:
        numpy.ndarray: A 1D NumPy array representing the 2D vector [x, y].

    Raises:
        ValueError: If the input is not in the expected 'x,y' format.
    """
    while True:
        try:
            vec_str = input(prompt)
            x, y = map(float, vec_str.split(","))
            return np.array([x, y])
        except ValueError:
            print(
                "Invalid input. Please enter two numbers separated by a comma (e.g., '1,2')."
            )


def get_2d_point(prompt, v_direction):
    """
    Prompts the user to input a 2D coordinate point, ensuring it does not lie
    on a line passing through the origin with the given direction vector.

    Args:
        prompt (str): The message displayed to the user for input.
        v_direction (numpy.ndarray): The 2D direction vector of the line
                                     to check against (e.g., for L1).

    Returns:
        numpy.ndarray: A 1D NumPy array representing the 2D point [x, y].
    """
    while True:
        p = get_2d_vector(prompt)
        # Check if p lies on the line L1(t) = t * v_direction
        # This is done by checking if the '2D cross product' (determinant) is zero.
        # For vectors a=(ax,ay) and b=(bx,by), the 2D cross product is ax*by - ay*bx.
        # If it's zero, the vectors are collinear.
        if np.isclose(p[0] * v_direction[1] - p[1] * v_direction[0], 0, atol=1e-9):
            print(
                "The point you entered lies on the first line. Please enter a point not on this line."
            )
        else:
            return p


def onclick(event):
    """
    Handles the click event on the matplotlib plot.
    When a point is clicked on the first line, it calculates and draws
    the corresponding point on the parallel line, along with explanatory vectors.

    Args:
        event (matplotlib.backend_bases.MouseEvent): The event object
                                                     containing click coordinates.
    """
    global selected_point_on_line1, line_p1_to_p2, vec_op1, vec_p_p2, vec_op2, vec_op

    # Clear previous dynamic lines and vectors from the plot for a fresh drawing
    if selected_point_on_line1:
        selected_point_on_line1.remove()
    if line_p1_to_p2:
        line_p1_to_p2.remove()
    if vec_op1:
        vec_op1.remove()
    if vec_p_p2:
        vec_p_p2.remove()
    if vec_op2:
        vec_op2.remove()
    if vec_op:
        vec_op.remove()

    # Ensure the click was within the axes area
    if event.inaxes != ax:
        return

    click_x, click_y = event.xdata, event.ydata

    # Find the parameter 't' for the closest point on Line 1 to the click.
    # This is achieved by projecting the clicked point onto the line defined by vector 'v'.
    # The formula for scalar projection of a point (x,y) onto a vector v: t = ( (x,y) . v ) / ||v||^2
    # Where '.' is the dot product and '||v||^2' is the squared magnitude of v.
    t_closest = np.dot(np.array([click_x, click_y]), v) / np.dot(v, v)

    P1 = t_closest * v  # Point on Line 1 (t * v)

    # Corresponding point on Line 2 (p + t * v)
    P2 = p + t_closest * v

    # Plot the selected point on Line 1
    (selected_point_on_line1,) = ax.plot(
        P1[0], P1[1], "co", markersize=8, label=r"$P_1 = t \cdot v$"
    )
    ax.text(P1[0] + 0.1, P1[1] + 0.1, r"$P_1$", fontsize=10, color="cyan")
    ax.text(P2[0] + 0.1, P2[1] + 0.1, r"$P_2$", fontsize=10, color="purple")

    # Draw the translation line (P1 to P2) as a dashed magenta line
    (line_p1_to_p2,) = ax.plot(
        [P1[0], P2[0]],
        [P1[1], P2[1]],
        "m:",
        linewidth=1.5,
        label="Translation (vector p)",
    )

    # Draw vectors to illustrate vector addition:
    # 1. Vector from origin (O) to P1 (t * v)
    vec_op1 = ax.quiver(
        0,
        0,
        P1[0],
        P1[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="orange",
        width=0.005,
        label=r"$\vec{OP_1}$",
    )
    # 2. Vector from point p to P2 (this vector is effectively P1, translated)
    vec_p_p2 = ax.quiver(
        p[0],
        p[1],
        P2[0] - p[0],
        P2[1] - p[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="green",
        width=0.005,
        label=r"$\vec{pP_2}$ (parallel to $\vec{OP_1}$)",
    )
    # 3. Vector from origin (O) to P2 (the resultant vector O + P1 + p)
    vec_op2 = ax.quiver(
        0,
        0,
        P2[0],
        P2[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="purple",
        width=0.005,
        label=r"$\vec{OP_2} = \vec{p} + \vec{OP_1}$",
    )
    # 4. Vector from origin (O) to point p (the translation vector itself)
    vec_op = ax.quiver(
        0,
        0,
        p[0],
        p[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="red",
        width=0.007,
        alpha=0.7,
        label=r"$\vec{p}$",
    )

    ax.legend(
        loc="upper right", fontsize="small"
    )  # Update legend to include new labels
    fig.canvas.draw_idle()  # Redraw the canvas to show changes


# --- Main Script ---
if __name__ == "__main__":
    """
    This script visualizes line parameterization on parallel lines and vector addition
    in a 2D plot using matplotlib.

    It prompts the user for:
    1. A 2D vector 'v' which defines the direction of the lines.
    2. A 2D point 'p' which serves as the translation vector for the second line.

    The script then plots:
    - Line 1: Passing through the origin (0,0) with direction 'v' ($L_1(t) = t \cdot v$).
    - Line 2: Parallel to Line 1, passing through point 'p' ($L_2(t) = p + t \cdot v$).

    Users can click on Line 1 to select a point. Upon clicking, the script dynamically shows:
    - The selected point on Line 1 ($P_1$).
    - The corresponding translated point on Line 2 ($P_2 = p + P_1$).
    - A dashed line connecting $P_1$ and $P_2$ to illustrate the translation.
    - Vectors from the origin to $P_1$, from $p$ to $P_2$, from the origin to $P_2$,
      and from the origin to $p$, to clearly demonstrate the geometric interpretation
      of vector addition ($P_2 = p + P_1$).
    """

    # --- 1. Input Vector v ---
    v = get_2d_vector("Enter a 2D vector (e.g., '1,2'): ")

    # --- 2. Input Point p ---
    p = get_2d_point(
        "Enter a 2D coordinate p (e.g., '3,-1') not on the first line: ", v
    )

    # --- 3. Setup Plot ---
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Line Parameterization and Parallel Lines with Vector Addition")

    # Set reasonable limits based on input vectors to ensure visibility
    # We add 1.5 multiplier to provide some padding around the vectors.
    max_abs_coords = np.max(np.abs(np.concatenate((v, p))))
    plot_limit = max(max_abs_coords * 1.5, 5)  # Ensure at least 5 for smaller vectors
    ax.set_xlim([-plot_limit, plot_limit])
    ax.set_ylim([-plot_limit, plot_limit])

    # Plot origin and point p as static elements
    ax.plot(0, 0, "ko", markersize=6, label="Origin (0,0)")
    ax.text(0.1, 0.1, "O", fontsize=12)
    ax.plot(p[0], p[1], "ro", markersize=6, label="Point p")
    ax.text(p[0] + 0.1, p[1] + 0.1, "p", fontsize=12, color="red")

    # --- 4. Define and Plot Lines ---
    # Generate parameter 't' values for drawing the lines
    t_values = np.linspace(
        -3, 3, 400
    )  # From -3 to 3 times the vector 'v' for line extent

    # Line 1: L1(t) = t * v
    line1_points = np.array([t_values * v[0], t_values * v[1]]).T
    ax.plot(
        line1_points[:, 0],
        line1_points[:, 1],
        "b-",
        linewidth=2,
        label=r"$L_1(t) = t \cdot \vec{v}$",
    )

    # Line 2: L2(t) = p + t * v
    line2_points = np.array([p[0] + t_values * v[0], p[1] + t_values * v[1]]).T
    ax.plot(
        line2_points[:, 0],
        line2_points[:, 1],
        "g--",
        linewidth=2,
        label=r"$L_2(t) = \vec{p} + t \cdot \vec{v}$",
    )

    ax.legend(loc="upper right")  # Initial legend for static elements

    # Global variables to store plot elements that will be updated dynamically
    selected_point_on_line1 = None
    line_p1_to_p2 = None
    vec_op1 = None
    vec_p_p2 = None
    vec_op2 = None
    vec_op = None  # Ensure vec_op is initialized for clearing if it's drawn in onclick

    # Connect the click event to the onclick function
    cid = fig.canvas.mpl_connect("button_press_event", onclick)

    plt.show()
