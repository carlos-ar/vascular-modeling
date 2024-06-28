#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 09:09:01 2022

@author: carlosar
"""

def notification(text, padding=80):
    out ='\n{:-^{p}}\n'.format('', p=padding)
    out+='{}'.format(text)
    out+='\n{:-^{p}}\n'.format('', p=padding)
    print(out)
    return 0

def padprint(text, padding=10):
    out='\n{:-^{p}}'.format('', p=padding)
    out+='  {}  '.format(text)
    out+='{:-^{p}}'.format('', p=padding)
    print(out)
    return

def warning(text, padding=10):
    out ='\n{:!^{p}}'.format('', p=2)
    out+='{:-^{p}}'.format('', p=padding)
    out+='  {}  '.format(text)
    out+='{:-^{p}}'.format('', p=padding)
    out+='{:!^{p}}\n'.format('', p=2)
    print(out)
    return