"""
Python 3.8.2

Pygame 2.0.0.dev6

@author: Isaak Choi
"""


import pygame as py


def scale_display(displayRatio=(16/9), scale=0.8):
    ## DOCSTRING
    '''
Returns the largest possible width and height of display with given 'displayRatio', then scales based on the given 'scale'
    -> Maximum screen size is the largest possible display resolution without the display being off-screen

Ex: py.display.set_mode(scale_display(16/9, 0.8))
---------------------------------------------------------------------------------------------------------------------------

displayRatio 
    -> The resulting screen ratio expressed as width/height
    -> Can input as either a single float or an expression of (width/height)
        -> This allows you to simply input the width and height you used in testing and it will scale for any monitor size;
            e.g. displayRatio = (1000/600)

    -> Resulting display dimentions are based off the monitor's resolution;
        -> Calling this function after calling py.display.set_mode() will result in the wrong values being output

scale
    -> After the largest display size is found, the display is then scaled by multiplying the display size by the 'scale'
        -> scale=1 results in largest display size
        -> scale<=0 results in the program crashing
        -> scale>1 results in parts of the display being off-screen
    '''

    ## ENSURE PYGAME IS INITIALISED
    py.init()

    ## RETRIEVE MONITOR RESOLUTION
    monitorWidth = py.display.Info().current_w
    monitorHeight = py.display.Info().current_h

    ## CHECK SCALED SCREEN AGAINST MONITOR BORDERS & FIND MAX DIMENSIONS
    if int(monitorHeight*displayRatio) <= monitorWidth:
        outputWidth = monitorHeight*displayRatio
        outputHeight = outputWidth/displayRatio
    elif int(monitorWidth/displayRatio) <= monitorHeight:
        outputHeight = monitorWidth/displayRatio
        outputWidth = outputHeight * displayRatio

    ## DETECT INVALID SCALE
    if scale <= 0:
        scale = 1
        print('Invalid scale input; scale must be greater than 0. Set scale to 1 to prevent game crash.')

    ## SCALE RESULTING DISPLAY WINDOW TO SPECIFICATIONS
        #-> Float to int conversion because pygame.display.set_mode() requires intager input
    outputWidth = int(outputWidth * scale)
    outputHeight = int(outputHeight * scale)

    ## PREVENT CRASH FROM DISPLAY SIZE 
    if outputWidth < 1:
        print('\nResulting width was less than 1, set value of width to 1 to prevent game crash.')
    if outputHeight < 1:
        outputHeight = 1
        print('\nResulting height was less than 1, set value of height to 1 to prevent game crash.')

    ## RETURN DISPLAY DIMENSIONS
    return (outputWidth, outputHeight)








