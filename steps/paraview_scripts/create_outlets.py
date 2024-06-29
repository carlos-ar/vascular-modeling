#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:24:18 2022

@author: carlosar

"""
import os, sys
from paraview.simple import *
import numpy as np

def calculate_angle(point):
    x = point[0]
    y = point[1]
    z = point[2]

    r = np.sqrt(x**2+y**2+z**2)
    theta = np.arccos(z/r)
    phi = np.arcsin(y/r/np.sin(theta))
    alpha = np.pi/2 - phi #np.arccos(x/r/np.sin(theta))

    # theta = np.arctan2(y,x)*(180/np.pi)
    # phi = 90-theta
    # alpha = np.arctan2(z,y)*(180/np.pi)

    alpha *= 180/np.pi
    phi *= 180/np.pi
    theta *= 180/np.pi
    return [phi, alpha, theta]

def clip_func(clip_in, x, n, r, clip_num):
    clip_name = "Clip{}".format(clip_num)
    # create a new 'Clip'
    clip = Clip(registrationName=clip_name, Input=clip_in)
    clip.ClipType = 'Plane'
    clip.HyperTreeGridClipper = 'Plane'
    clip.Scalars = [None, '']

    # init the 'Plane' selected for 'ClipType'
    clip.ClipType.Origin = [75.495041847229, 144.30945205688477, 81.56141185760498]

    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip.HyperTreeGridClipper.Origin = [75.495041847229, 144.30945205688477, 81.56141185760498]


    # Properties modified on clip1
    clip.ClipType = 'Box'
    clip.Scalars = ['POINTS', '']
    clip.Invert = 0
    clip.Crinkleclip = 0
    clip.Exact = 1

    # Properties modified on clip1.ClipType
    clip.ClipType.UseReferenceBounds = 1
    clip.ClipType.Bounds = [-0.5, 0.5, -0.5, 0.5, -0.5, 0.5]
    clip.ClipType.Position = x.tolist()

    if r < 0.1:
        clip.ClipType.Length = [.25, .25, .25]
    else:
        d = 3*r
        clip.ClipType.Length = [d, d, d]
    angle =  calculate_angle(n)
    clip.ClipType.Rotation = angle
    print('point:')
    print(x)
    print("angle:")
    print(angle)
    UpdatePipeline(time=0.0, proxy=clip)

    return clip

def create_box_cuts(input_mesh, points, normals, radii):
    #### import the simple module from the paraview
    
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    import_model = STLReader(registrationName=input_mesh,
        FileNames=[input_mesh])

    renderView1 = GetActiveViewOrCreate('RenderView')
    # alternatively, if you want to write images, you can use SaveScreenshot(...).
    renderView1.Update()
    UpdatePipeline(time=0.0, proxy=import_model)
    clip_in = GetActiveSource()
    
    # begin adding cylinders
    create_cylinder_cuts = True
    if create_cylinder_cuts == True:
        # endpoint cylinders
        num_points, _ = np.shape(points)
        for n in range(0, num_points):
        # for n in range(37, 38):
            print('clipping number: ', n)
            # if n == 0:
            #     cut_obj = entities
                
            # add a cyclinder
            point = points[n,:]
            normal = normals[n,:]
            radius = radii[n]
            c = clip_func(clip_in, point, normal, radius, n)

            clip_in = GetActiveSource()
    return renderView1

points = np.load('endpoints.npy')
normals = np.load('normals.npy')
radii = np.load('radii.npy')
input_mesh = 'surface_curated.stl'
renderView1 = create_box_cuts(input_mesh, points, normals, radii)

#--------------------------------------------
# uncomment the following to render all views
RenderAllViews()

# Specify the output file name and format
outputFileName = 'screenshot.png'

# Take a screenshot
SaveScreenshot(outputFileName, renderView1)

SaveState('paraview_state.pvsm')
