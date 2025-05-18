import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x_train = np.random.rand(20) * 17
y_train = 2.7 * x_train + 13.75 + np.random.rand(20) * 10
m = len(x_train)

w = 0.0
b = 0.0
learning_rate = 0.01
epochs = 100


def _get_predictions(x, w, b):
    return w * x + b


def _get_error(x, y, w, b):
    return _get_predictions(x, w, b) - y


def _get_loss(x, y, w, b):
    return np.mean((_get_predictions(x, w, b) - y) ** 2)


def _compute_the_gradients(x, y, w, b):
    _error_ = _get_error(x, y, w, b)
    w_grad = 2 * np.mean(_error_ * x)
    b_grad = 2 * np.mean(_error_)
    return (w_grad, b_grad)


loss_history = []
plot_epochs = []
plot_predictions = []

for epoch in range(epochs):
    dw, db = _compute_the_gradients(x_train, y_train, w, b)
    loss = _get_loss(x_train, y_train, w, b)
    loss_history.append(loss)

    # Save model predictions every 10 epochs + last epoch
    if epoch % 10 == 0 or epoch == epochs - 1:
        plot_epochs.append(epoch)
        plot_predictions.append(_get_predictions(x_train, w, b))

    print(f"Epoch {epoch}: Loss = {loss:.4f}, w = {w:.4f}, b = {b:.4f}")
    w = w - learning_rate * dw
    b = b - learning_rate * db

final_loss = _get_loss(x_train, y_train, w, b)
print(f"Final loss after training: {final_loss:.4f}")
print(f"Model: y = {w}x + {b}")

# Plot combined figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left plot: Data points and model predictions at select epochs
ax1.scatter(x_train, y_train, color="blue", label="Training Data")
colors = plt.cm.viridis(np.linspace(0, 1, len(plot_epochs)))

for idx, epoch in enumerate(plot_epochs):
    ax1.plot(x_train, plot_predictions[idx], color=colors[idx], label=f"Epoch {epoch}")

ax1.set_xlabel("some feature")
ax1.set_ylabel("some target")
ax1.set_title("Feature vs Target and Model Predictions")
ax1.legend()

# Right plot: Loss curve
ax2.plot(range(epochs), loss_history, color="red", label="Loss (MSE)")
ax2.set_xlabel("Epoch")
ax2.set_ylabel("Mean Squared Error (Loss)")
ax2.set_title("Loss Curve")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
