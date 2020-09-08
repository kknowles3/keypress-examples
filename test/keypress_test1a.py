# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:11:37 2020

@author: kknow

Simple example showing how to capture and process keypress events while 
code is running.  

The original simple example is based on this link:
    
    https://www.codespeedy.com/how-to-detect-which-key-is-pressed-in-python/

This version adds a dictionary of keys and corresponding functions to call on 
each keypress event.  The dictionary includes a mix of inline lambda functions,
plus a call to an encapsulated function to illustrate a few ways this dictionary 
approach can be used.

Note this example is intended to be run from an external command prompt or terminal.
It may not work properly when run from the python console within the development
environment.

"""

# https://www.codespeedy.com/how-to-detect-which-key-is-pressed-in-python/

import sys
import msvcrt

def you_pressed(x):
    print('You pressed {}'.format(x))
    return None

# Dictionary of keys and functions to process for each key
# Simple example using a mix of inline "lambda" functions and calls to a separate function
key_dict = {
    'esc': lambda: print('You pressed [Esc]'),
    'x': lambda: print('You pressed "x"'),
    'p': lambda: you_pressed('p'),
    'q': lambda: sys.exit(),
    }

print('Press any key ("q" to quit)')

# Wait until user presses a key in the dictionary's list of keys
while True:
    # TODO make this more concise
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch().decode('utf-8')  # Get the key pressed and convert to unicode character
        print(key_stroke)
        
        # Get the function for the key pressed by the user
        key_func = key_dict.get(key_stroke, None)
        if key_func is not None:
            key_func()
        else:
            print("No key event hander for key: {}".format(key_stroke))
            # break

