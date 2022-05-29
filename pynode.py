#!/usr/bin/python3
# -*- coding: utf-8 -*-
## ~/.local/bin/removestar -i pynode.py
#
## pip install python-xlib
#
# PyNoDE is written by o6n <https://github.com/o6n/PyNoDE>
#
# This software is in the public domain
# and is provided AS IS, with NO WARRANTY.

from Xlib.display import Display
from Xlib import X, XK
import os
import subprocess

dsp = Display()

dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("F1")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
'''
dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("F2")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("F3")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("F4")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("F10")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("F11")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
'''
dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("F12")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
#dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("Tab")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
#dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("Up")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
#dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("Down")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
#dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("Left")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
#dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("Right")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("Return")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("Menu")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
#dsp.screen().root.grab_key(dsp.keysym_to_keycode(XK.string_to_keysym("Delete")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)

dsp.screen().root.grab_button(1, X.Mod4Mask, 1, X.ButtonPressMask|X.ButtonReleaseMask|X.PointerMotionMask, X.GrabModeAsync, X.GrabModeAsync, X.NONE, X.NONE)
dsp.screen().root.grab_button(3, X.Mod4Mask, 1, X.ButtonPressMask|X.ButtonReleaseMask|X.PointerMotionMask, X.GrabModeAsync, X.GrabModeAsync, X.NONE, X.NONE)

start = None
while 1:
	ev = dsp.next_event()

	if ev.type == X.KeyPress:
		if ev.detail == dsp.keysym_to_keycode(XK.string_to_keysym("Return")):
			#os.system("xterm &")
			#subprocess.Popen("xterm").wait()
			subprocess.call(['xterm'], shell=True)
		elif ev.detail == dsp.keysym_to_keycode(XK.string_to_keysym("Menu")):
			#os.system("rofi -show drun &")
			#subprocess.Popen("rofi -show drun").wait()
			subprocess.call(['rofi -show drun'], shell=True)
		elif ev.detail == dsp.keysym_to_keycode(XK.string_to_keysym("Tab")):
			#os.system("rofi -show window &")
			#subprocess.Popen("rofi -show window").wait()
			subprocess.call(['rofi -show window'], shell=True)
		elif ev.detail == dsp.keysym_to_keycode(XK.string_to_keysym("F12")):
			raise SystemExit
			#sys.exit(-1)

	if ev.type == X.KeyPress and ev.child != X.NONE:
		ev.child.configure(stack_mode = X.Above)
	elif ev.type == X.ButtonPress and ev.child != X.NONE:
		attr = ev.child.get_geometry()
		start = ev
	elif ev.type == X.MotionNotify and start:
		xdiff = ev.root_x - start.root_x
		ydiff = ev.root_y - start.root_y
		start.child.configure(
			x = attr.x + (start.detail == 1 and xdiff or 0),
			y = attr.y + (start.detail == 1 and ydiff or 0),
			width = max(1, attr.width + (start.detail == 3 and xdiff or 0)),
			height = max(1, attr.height + (start.detail == 3 and ydiff or 0)))
	elif ev.type == X.ButtonRelease:
		start = None
