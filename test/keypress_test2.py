# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:11:37 2020

@author: kknow

Another keypress example showing how to capture and process keypress events while 
code is running.

This example is based on the keyboard package found here:
    
    https://pypi.org/project/keyboard/

To install the keyboard package:
    
    pip install keyboard

"""

import keyboard

# keyboard.press_and_release('shift+s, space')

# keyboard.write('The quick brown fox jumps over the lazy dog.')

# keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# # Press PAGE UP then PAGE DOWN to type "foobar".
# keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Blocks until you press esc.
keyboard.wait('esc')
print('You pressed [Esc]')

# Wait until "p" is pressed
while True:
    if keyboard.read_key() == "p":
        print("Part 1: You pressed p")
        break

# Wait until "x" is pressed
while True:
    if keyboard.is_pressed("x"):
        print("Part 2: You pressed x")
        break

# # Type @@ then press space to replace with abbreviation.
# keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# # Block forever, like `while True`.
# keyboard.wait()

# To unhook all keyboard events    
keyboard.unhook_all()