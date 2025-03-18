import matplotlib.pyplot as plt
import numpy as np
def generate_pentagon(center=(0, 0), radius=1):
    angle = np.linspace(0, 2 * np.pi, 6)[:-1]
    x = center[0] + radius * np.cos(angle)
    y = center[1] + radius * np.sin(angle)
    return np.column_stack((x, y))
original_pentagon = generate_pentagon(center=(0, 0), radius=1)
scale_x = 4
scale_y = 4
scaling_matrix = np.array([[scale_x, 0], [0, scale_y]])
scaled_pentagon = np.dot(original_pentagon, scaling_matrix)
plt.figure()
plt.plot(np.append(original_pentagon[:, 0], original_pentagon[0, 0]),
         np.append(original_pentagon[:, 1], original_pentagon[0, 1]), 'bo-', label='Original Pentagon')
plt.plot(np.append(scaled_pentagon[:, 0], scaled_pentagon[0, 0]),
         np.append(scaled_pentagon[:, 1], scaled_pentagon[0, 1]), 'ro-', label='Scaled Pentagon')
plt.title("2D Scaling Transformation (Pentagon)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
