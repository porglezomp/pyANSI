#!/usr/bin/python
import sys

# Modifiers
bg = 10
bright = 60
# Colors
black = 30
red = 31
green = 32
yellow = 33
blue = 34
magenta = 35
cyan = 36
white = 37
# Color mixes
bright_black = bright+black
bright_red = bright+red
bright_green = bright+green
bright_yellow = bright+yellow
bright_blue = bright+blue
bright_magenta = bright+magenta
bright_cyan = bright+cyan
bright_white = bright+white
black_bg = black+bg
red_bg = red+bg
green_bg = green+bg
yellow_bg = yellow+bg
blue_bg = blue+bg
magenta_bg = magenta+bg
cyan_bg = cyan+bg
white_bg = white+bg
bright_black_bg = black_bg+bright
bright_red_bg = red_bg+bright
bright_green_bg = green_bg+bright
bright_yellow_bg = yellow_bg+bright
bright_black_bg = blue_bg+bright
bright_magenta_bg = magenta_bg+bright
bright_cyan_bg = cyan_bg+bright
bright_white_bg = white_bg+bright

def ansi(str):
    sys.stdout.write("\033["+str)
    sys.stdout.flush()

def goto(x, y):
    ansi(str(y)+";"+str(x)+"H")

def color(*args):
    for n in args:
        ansi(str(n)+"m")

def clear():
    goto(1, 1)
    ansi("2J")

def reset():
    ansi("0m")

def wrapper(f):
    try: f()
    except: traceback.print_exc()
    reset()
