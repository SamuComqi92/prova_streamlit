import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Set up Streamlit app
st.title("3D Surface Plot")
color_filter = st.selectbox("Color Filter", ["None", "Cool", "Hot"])
title_filter = st.text_input("Title Filter", "Surface Plot")

# Filter the color
if color_filter == "Cool":
    cmap = 'cool'
elif color_filter == "Hot":
    cmap = 'hot'
else:
    cmap = 'viridis'

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap=cmap)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(title_filter)

# Render the plot using Streamlit
st.pyplot(fig)