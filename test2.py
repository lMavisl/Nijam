import pyvista as pv
from pyvista import examples

# Volume rendering is not supported with Panel yet
pv.rcParams["use_panel"] = False

# Download a volumetric dataset
vol = pv.read("PipeScanInterpolation (1).vtk")

vol2 = pv.UniformGrid(x, y, z)
cpos = [(-381.74, -46.02, 216.54), (74.8305, 89.2905, 100.0), (0.23, 0.072, 0.97)]

vol2.plot(volume=True, cmap="bone", cpos=cpos)