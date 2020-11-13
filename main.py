import pyglet
from pyglet.gl import *
from pyglet.window import key
import math
import numpy as np

import grav as grav
import model as mod
import player as ply
from MYUI import settings as sets
import window as win


if __name__ == '__main__':

    settings = sets.Settings("res/cfg/settings.txt")

    window = win.Window(settings, int(settings.d['reswidth']), int(settings.d['resheight']), caption='Cube Test',
                                        resizable = False, fullscreen=True)
    window.set_exclusive_mouse()
    glClearColor(0.5, 0.7, 1, 1)

    #---------------------3D-------------------------
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    #------------------------------------------------

    #----------------------2D------------------------
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    #------------------------------------------------

    pyglet.app.run()
