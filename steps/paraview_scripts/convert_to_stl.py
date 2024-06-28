# trace generated using paraview version 5.10.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

import os
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


cwd = os.getcwd()
input_mesh = os.path.join(cwd,'surface.vtk')
output_mesh = os.path.join(cwd, 'out.stl')

print(input_mesh, output_mesh)
# create a new 'Legacy VTK Reader'
surfacevtk = LegacyVTKReader(registrationName='surface.vtk',
	FileNames=[input_mesh])

cleantoGrid1 = CleantoGrid(registrationName='CleantoGrid1', Input=surfacevtk)

extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=cleantoGrid1)

# save data
SaveData(output_mesh, proxy=extractSurface1, ChooseArraysToWrite=0)

# testing render image
# Create a new render view
renderView = CreateView('RenderView')

# # Load a data source (replace 'data.vtk' with your actual data file)
# dataSource = OpenDataFile('data.vtk')

# Show the data in the render view
dataDisplay = Show(surfacevtk, renderView)
# Center the camera on the data
renderView.ResetCamera()
# Update the view to ensure updated data information
renderView.Update()

# # Set the camera position (optional)
# renderView.CameraPosition = [1.0, 1.0, 1.0]
# renderView.CameraFocalPoint = [0.0, 0.0, 0.0]

# Specify the output file name and format
outputFileName = 'screenshot.png'

# Take a screenshot
SaveScreenshot(outputFileName, renderView)