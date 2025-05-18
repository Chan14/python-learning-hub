import matplotlib.pyplot as plt
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Generate synthetic training data
x_train = np.random.rand(20) * 17
y_train = 2.7 * x_train + 13.75 + np.random.rand(20) * 10

# Hyperparameters
w, b = 0.0, 0.0
learning_rate = 0.01
epochs = 100


def predict(x, w, b):
    """Return the model's predictions."""
    return w * x + b


def compute_loss(x, y, w, b):
    """Compute mean squared error loss."""
    return np.mean((predict(x, w, b) - y) ** 2)


def compute_gradients(x, y, w, b):
    """Compute gradients with respect to w and b."""
    error = predict(x, w, b) - y
    dw = 2 * np.mean(error * x)
    db = 2 * np.mean(error)
    return dw, db


# Training loop
loss_history = []
plot_epochs = []
plot_predictions = []

for epoch in range(epochs):
    dw, db = compute_gradients(x_train, y_train, w, b)
    w -= learning_rate * dw
    b -= learning_rate * db
    loss = compute_loss(x_train, y_train, w, b)
    loss_history.append(loss)

    # Save predictions every 10 epochs and at last epoch
    if epoch % 10 == 0 or epoch == epochs - 1:
        plot_epochs.append(epoch)
        plot_predictions.append(predict(x_train, w, b))

    print(f"Epoch {epoch:3d}: Loss = {loss:.4f}, w = {w:.4f}, b = {b:.4f}")


# Final results
print(f"\nFinal loss after training: {loss:.4f}")
print(f"Trained model: y = {w:.4f}x + {b:.4f}")

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left: Data points and model predictions
ax1.scatter(x_train, y_train, color="blue", label="Training Data")
colors = plt.cm.viridis(np.linspace(0, 1, len(plot_epochs)))

for idx, epoch in enumerate(plot_epochs):
    sorted_idx = np.argsort(x_train)
    ax1.plot(
        x_train[sorted_idx],
        plot_predictions[idx][sorted_idx],
        color=colors[idx],
        label=f"Epoch {epoch}",
    )

ax1.set_xlabel("Some Feature")
ax1.set_ylabel("Some Target")
ax1.set_title("Feature vs Target and Model Predictions")
ax1.legend()

# Right: Loss curve
ax2.plot(range(epochs), loss_history, color="red", label="Loss (MSE)")
ax2.set_xlabel("Epoch")
ax2.set_ylabel("Mean Squared Error")
ax2.set_title("Loss Curve")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
