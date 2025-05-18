import matplotlib.pyplot as plt
import numpy as np
import plot_2dim_data as pd

np.random.seed(42)
x_train = np.random.rand(20) * 17
y_train = 2.7 * x_train + 13.75 + np.random.rand(20) * 10
m = len(x_train)

print("Data Table")
print(f"feature : target")
for i in range(0, m):
    print(f"{x_train[i]} : {y_train[i]}")

pd.plot_data(x_train, y_train, "some feature", "some target", "Feature vs Target")

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

for epoch in range(epochs + 1):
    dw, db = _compute_the_gradients(x_train, y_train, w, b)
    loss = _get_loss(x_train, y_train, w, b)
    loss_history.append(loss)
    if epoch % 10 == 0 or epoch == epochs - 1:
        pd.plot_data_and_model(
            x_train,
            y_train,
            _get_predictions(x_train, w, b),
            "some feature",
            "some target",
            "Feature vs Target",
            f"Prediction w = {w:.2f}, b = {b:.2f}",
        )
    print(f"Epoch {epoch}: Loss = {loss:.4f}, w = {w:.4f}, b = {b:.4f}")
    w = w - learning_rate * dw
    b = b - learning_rate * db


final_loss = _get_loss(x_train, y_train, w, b)
loss_history.append(final_loss)
print(f"Final loss after training: {final_loss:.4f}")
print(f"Model: y = {w}x + {b}")

# Plot loss curve after training
plt.figure(figsize=(8, 5))
plt.plot(range(epochs), loss_history, label="Loss")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error (Loss)")
plt.title("Loss Curve")
plt.legend()
plt.grid(True)
plt.show()
