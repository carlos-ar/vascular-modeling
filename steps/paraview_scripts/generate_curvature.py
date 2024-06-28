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
input_mesh = os.path.join(cwd,'convert_to_stl.stl')
output_mesh = os.path.join(cwd, 'out.stl')

print(input_mesh, output_mesh)

# create a new 'STL Reader'
surface_prepstl = STLReader(registrationName='convert_to_stl.stl', FileNames=[input_mesh])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
surface_prepstlDisplay = Show(surface_prepstl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
surface_prepstlDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Curvature'
curvature1 = Curvature(registrationName='Curvature1', Input=surface_prepstl)

# show data in view
curvature1Display = Show(curvature1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
curvature1Display.Representation = 'Surface'

# hide data in view
Hide(surface_prepstl, renderView1)

# show color bar/color legend
curvature1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Gauss_Curvature'
gauss_CurvatureLUT = GetColorTransferFunction('Gauss_Curvature')

# get opacity transfer function/opacity map for 'Gauss_Curvature'
gauss_CurvaturePWF = GetOpacityTransferFunction('Gauss_Curvature')

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=curvature1)

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'

# hide data in view
Hide(curvature1, renderView1)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(curvature1)

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=curvature1)

# show data in view
threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'

# hide data in view
Hide(curvature1, renderView1)

# show color bar/color legend
threshold2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(curvature1)

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Histogram View'
histogramView1 = CreateView('XYHistogramChartView')

# assign view to a particular cell in the layout
AssignViewToLayout(view=histogramView1, layout=layout1, hint=2)

# set active source
SetActiveSource(curvature1)

# show data in view
curvature1Display_1 = Show(curvature1, histogramView1, 'HistogramChartRepresentation')

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# split cell
layout1.SplitHorizontal(6, 0.5)

# Create a new 'Histogram View'
histogramView2 = CreateView('XYHistogramChartView')

# assign view to a particular cell in the layout
AssignViewToLayout(view=histogramView2, layout=layout1, hint=13)

# set active source
SetActiveSource(threshold1)

# set active source
SetActiveSource(threshold1)

# show data in view
threshold1Display_1 = Show(threshold1, histogramView2, 'HistogramChartRepresentation')

# set active view
SetActiveView(None)

# Create a new 'Histogram View'
histogramView3 = CreateView('XYHistogramChartView')

# assign view to a particular cell in the layout
AssignViewToLayout(view=histogramView3, layout=layout1, hint=14)

# set active source
SetActiveSource(threshold2)

# set active source
SetActiveSource(threshold2)

# show data in view
threshold2Display_1 = Show(threshold2, histogramView3, 'HistogramChartRepresentation')

# set active source
SetActiveSource(curvature1)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(threshold1)

# set active source
SetActiveSource(curvature1)

# show data in view
curvature1Display = Show(curvature1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
curvature1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(threshold1)

# Properties modified on threshold1
threshold1.UpperThreshold = -1.0

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
histogramView2.Update()

# change representation type
threshold1Display.SetRepresentationType('Points')

# turn off scalar coloring
ColorBy(threshold1Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(gauss_CurvatureLUT, renderView1)

# change solid color
threshold1Display.AmbientColor = [0.17254901960784313, 0.6274509803921569, 0.17254901960784313]
threshold1Display.DiffuseColor = [0.17254901960784313, 0.6274509803921569, 0.17254901960784313]

# Properties modified on threshold1Display
threshold1Display.PointSize = 25.0

# set active source
SetActiveSource(threshold2)

# Properties modified on threshold2
threshold2.LowerThreshold = 10.0

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
histogramView3.Update()

# change representation type
threshold2Display.SetRepresentationType('Points')

# turn off scalar coloring
ColorBy(threshold2Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(gauss_CurvatureLUT, renderView1)

# change solid color
threshold2Display.AmbientColor = [0.8392156862745098, 0.15294117647058825, 0.1568627450980392]
threshold2Display.DiffuseColor = [0.8392156862745098, 0.15294117647058825, 0.1568627450980392]

# Properties modified on threshold2Display
threshold2Display.PointSize = 25.0

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1457, 565)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [75.42138385772705, 144.39734649658203, 446.6710001479498]
renderView1.CameraFocalPoint = [75.42138385772705, 144.39734649658203, 81.51547622680664]
renderView1.CameraParallelScale = 94.50920401518096

#--------------------------------------------
# uncomment the following to render all views
RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
renderView1.Update()

# # Set the camera position (optional)
# renderView.CameraPosition = [1.0, 1.0, 1.0]
# renderView.CameraFocalPoint = [0.0, 0.0, 0.0]

# Specify the output file name and format
outputFileName = 'screenshot.png'

# Take a screenshot
SaveScreenshot(outputFileName, renderView1)


SaveState('paraview_state.pvsm')