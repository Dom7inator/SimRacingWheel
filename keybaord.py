# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import rotaryio
from board import *

# define Physical buttons.
# buttons will be added
accelButton = digitalio.DigitalInOut(GP13)
accelButton.direction = digitalio.Direction.INPUT
accelButton.pull = digitalio.Pull.DOWN

deccelButton = digitalio.DigitalInOut(GP12)
deccelButton.direction = digitalio.Direction.INPUT
deccelButton.pull = digitalio.Pull.DOWN



enc = rotaryio.IncrementalEncoder(GP14, GP15)
last_position = None

kbd = Keyboard(usb_hid.devices)

accel = False
deccel = False
right = False
left = False


while True:
    # Accelerate
    if accelButton.value and not accel:
        kbd.press(Keycode.W)
        accel = True
    elif not accelButton.value and accel:
        kbd.release(Keycode.W)
        accel = False

    # Decelerate
    if deccelButton.value and not accel:
        kbd.press(Keycode.S)
        deccel = True
    elif not deccelButton.value and accel:
        kbd.release(Keycode.S)
        deccel = False
    
    position = enc.position
    if last_position == None or position != last_position:
        print(position)
    last_position = position

    # Turn Right
    if position >= 2 and not right:
        kbd.press(Keycode.D)
        right = True
    elif position < 2 and right:
        kbd.release(Keycode.D)
        right = False
    
    # Turn Left
    if position <= -2 and not left:
        kbd.press(Keycode.A)
        left = True
    elif position > -2 and left:
        kbd.release(Keycode.A)
        left = False