# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:11:37 2020

@author: kknow

Simple example showing how to capture and process keypress events while 
code is running.

This example is based on this link:
    
    https://www.codespeedy.com/how-to-detect-which-key-is-pressed-in-python/

"""

import msvcrt

def showX():
    print ('x Key pressed')

while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        print(key_stroke) # will print which key is pressed
        if key_stroke.decode('utf-8') == 'x':
            showX()
