import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y1 = x**2
y2 = np.sqrt(x)


fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Subplot bên trái: y = x^2
axes[0].plot(x, y1, color='blue')
axes[0].set_title("Đồ thị y = x^2")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")


axes[1].plot(x, y2, color='green')
axes[1].set_title("Đồ thị y = √x")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")

plt.tight_layout()
plt.show()
