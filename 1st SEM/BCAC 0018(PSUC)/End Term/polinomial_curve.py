# Importing required library
import numpy as np
import matplotlib.pyplot as plt

# Creating x axis with range and y
# Function for Plotting polinomial Graph
x = np.arange(0, 5*np.pi, 0.1)
y = x**2+2*x+1

# Plotting Graph
plt.plot(x, y, color='green')
plt.show()
