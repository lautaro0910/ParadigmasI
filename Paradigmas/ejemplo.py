import numpy as np
import matplotlib.pyplot as plt

# Crear valores para X y Y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Definir la función Z = f(X, Y)
Z = X**2 + Y**2

# Crear la figura y el gráfico 3D
fig = plt.figure()
ax = fig.gca(projection='3d')  # gca: get current axes

# Superficie 3D
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Mostrar gráfico
plt.show()
