import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Provided known point locations (longitude, latitude) and values
lon_known = np.array([121.39, 126.19, 130.27, 127.42, 126.14, 125.96, 123.15, 130.5, 129.08, 122.74])
lat_known = np.array([13.51, 12.02, 13.11, 10.09, 15.33, 14.0, 10.88, 11.18, 15.78, 15.82])
values_known = np.array([1.494, 1.934, 2.148, 9.155, 2.221, 8.1, 2.039, 1.916, 3.729, 7.137])

# Combine lon_known and lat_known into a list of coordinate points
points = np.column_stack((lon_known, lat_known))

# Define structured grid (50 rows and 70 columns)
lon_range = np.linspace(121.0, 131.0, 70)
lat_range = np.linspace(10.0, 16.0, 50)
lon_grid, lat_grid = np.meshgrid(lon_range, lat_range)

# Interpolate values to the grid using 'linear' method
interpolated_values = griddata(points, values_known, (lon_grid, lat_grid), method='linear')


# Plot the 2D grid
plt.figure(figsize=(10, 6))
plt.scatter(lon_grid, lat_grid, c='red', s=10, label='Grid Points', alpha=0.5)

# Overlay the known points
plt.scatter(lon_known, lat_known, c='blue', s=50, label='Known Points', edgecolors='black')

# Label the axes
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Interpolated Grid of Longitude and Latitude')

# Add grid lines for clarity
plt.grid(True)
plt.legend()
plt.show()
