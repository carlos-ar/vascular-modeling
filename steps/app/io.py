#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:37:08 2023

@author: carlosar
"""
import os
import re
import json, yaml
import errno
import shutil
import datetime
import subprocess
import numpy as np
import app.messages as msg

# trying to edit new file
# new natural sort without adding natsort pacakge
# https://stackoverflow.com/a/4836734
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)
def make_save_directory(directory, printflag=False):
    try:
        if printflag is True:
            print('Made directory: \n{0}'.format(directory))
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return

