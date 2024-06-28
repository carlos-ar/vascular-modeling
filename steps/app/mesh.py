#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:21:33 2023

@author: carlosar

Refactor meshing steps
"""
import os, sys
import subprocess
import app.messages as msg
import app.io as io
import gmsh
import numpy as np

def recreate_mesh(input_mesh):
    gmsh.initialize()
    gmsh.option.setNumber("General.Verbosity", 0)

    gmsh.merge(input_mesh)

    gmsh.option.setNumber("Mesh.MeshSizeMax", .5)    
    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.model.geo.synchronize()


    surfaces = gmsh.model.getEntities(2)
    bnd_ent = gmsh.model.getBoundary(surfaces)
    if '-nopopup' not in sys.argv:
        gmsh.fltk.run()
    
    gmsh.finalize()

    msg.warning("Number of boundary entities: {}".format(len(bnd_ent)))

    return




if __name__ == '__main__':
    print('main run')