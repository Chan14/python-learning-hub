import matplotlib.pyplot as plt
import numpy as np
import plot_2dim_data as pd

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic training data
x_train = np.random.rand(20) * 17
y_train = 2.7 * x_train + 13.75 + np.random.rand(20) * 10

# Display the data table
print("Data Table\nfeature : target")
for x, y in zip(x_train, y_train):
    print(f"{x:.4f} : {y:.4f}")

# Initial plot
pd.plot_data(x_train, y_train, "some feature", "some target", "Feature vs Target")

# Hyperparameters
w, b = 0.0, 0.0
learning_rate = 0.01
epochs = 100


def predict(x, w, b):
    """Return the predicted y values."""
    return w * x + b


def compute_loss(x, y, w, b):
    """Compute mean squared error."""
    return np.mean((predict(x, w, b) - y) ** 2)


def compute_gradients(x, y, w, b):
    """Compute gradients of the loss with respect to w and b."""
    error = predict(x, w, b) - y
    dw = 2 * np.mean(error * x)
    db = 2 * np.mean(error)
    return dw, db


# Training loop
loss_history = []

for epoch in range(epochs + 1):
    dw, db = compute_gradients(x_train, y_train, w, b)
    w -= learning_rate * dw
    b -= learning_rate * db
    loss = compute_loss(x_train, y_train, w, b)
    loss_history.append(loss)
    print(f"Epoch {epoch:3d}: Loss = {loss:.4f}, w = {w:.4f}, b = {b:.4f}")

    if epoch % 10 == 0 or epoch == epochs:
        # print(f"Epoch {epoch:3d}: Loss = {loss:.4f}, w = {w:.4f}, b = {b:.4f}")
        pd.plot_data_and_model(
            x_train,
            y_train,
            predict(x_train, w, b),
            "some feature",
            "some target",
            "Feature vs Target",
            f"Prediction w = {w:.2f}, b = {b:.2f}",
        )


# Final model info
print(f"\nFinal loss after training: {loss_history[-1]:.4f}")
print(f"Trained Model: y = {w:.4f}x + {b:.4f}")

# Plot the loss curve
plt.figure(figsize=(8, 5))
plt.plot(range(epochs + 1), loss_history, label="Loss")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error (Loss)")
plt.title("Loss Curve")
plt.legend()
plt.grid(True)
plt.show()
