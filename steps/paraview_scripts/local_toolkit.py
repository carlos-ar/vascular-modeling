#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:06:42 2022

@author: carlosar
"""
import os
import pathlib
import numpy as np
# import meshio
import json
import re
# new natural sort without adding natsort pacakge
# https://stackoverflow.com/a/4836734
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

def load_json_markup(path):
    with open(path, 'r') as f:
        json_dict = json.load(f)
    return json_dict

def test():
    print('testing paraview import')
    data = load_json_markup('./input.json')
    print(data)
    return