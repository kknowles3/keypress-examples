# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:11:37 2020

@author: kknow

Another keypress example showing how to capture and process keypress events while 
code is running.  This example implements a longer list of keys to process

This example is based on the keyboard package found here:
    
 dfdf   https://pypi.org/project/keyboard/

To install the keyboard package:
    
    pip install keyboard

"""

import sys
import keyboard

# Release any previously registered keyboard hooks
keyboard.unhook_all()

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

# Blocks until you press esc
# print('Press [Esc] to continue')
# keyboard.wait('esc')
# print('You pressed [Esc]')

print('Press any key ("q" to quit)')
# Wait until user presses a key in the dictionary's list of keys
while True:
    # TODO make this more concise
    key_pressed = keyboard.read_key()
    key_func = key_dict.get(key_pressed, None)
    if key_func is not None:
        key_func()
    else:
        print("No key event hander for key: {}".format(key_pressed))
        keyboard.unhook_all()
        # break

# # Type @@ then press space to replace with abbreviation.
# keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# # Block forever, like `while True`.
# keyboard.wait()

# To unhook all keyboard events    
# keyboard.unhook_all()

keyboard.on_release_key(key, callback)
