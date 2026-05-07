# Importing required library
import numpy as np
import matplotlib.pyplot as plt

# Creating x axis with range and y
# Function for Plotting polinomial Graph
x = np.arange(0, 5*np.pi, 0.1)
y = np.exp(x)

# Plotting Graph
plt.plot(x, y, color='green')
plt.show()