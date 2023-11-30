import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [0, 1, 2, 3, 4, 5],
    [10, 11, 12, 13, 14, 15],
    [20, 21, 22, 23, 24, 25],
    [30, 31, 32, 33, 34, 35],
    [40, 41, 42, 43, 44, 45],
    [50, 51, 52, 53, 54, 55],
])

fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(data)

ax.grid()

ax.set_xlabel("Значення")
ax.set_ylabel("Рівень")

plt.show()