import pyvista as pv

mesh = pv.read('testtest.vti')    # read data

plotter = pv.Plotter()    # instantiate the plotter
plotter.add_volume(mesh, cmap='jet')    # add volume

#plotter.add_mesh_threshold(mesh)  # add mesh threshold

#Untick below statement to save file from vtk to vti
#mesh.save('sarimage.vti', binary=False)
cpos = plotter.show()     # show the rendering window
