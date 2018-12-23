import pyglet
from pyglet.gl import *
from pyglet.window import key
import math
import numpy as np

import model as mod
import player as ply
from MYUI import settings as sets
import window as win

class Gravity:

    def __init__(self, d,pos=(0)):
        self.pos = list(pos)
        self.d   = d

        self.colisionTop    = 0
        self.colisionBottom = 0

        self.colisionLeft   = 0
        self.colisionRight  = 0

        self.colisionFront  = 0
        self.colisionBack   = 0
        #self.npos = list((0,0,0))
                                                                                                #gravity
    def pull(self, dt):
        sens = self.d['gravity']
        s    = dt*10
        self.pos[0] -= s*sens


    def motion():
        pass

    def colision(self, map, posi):
        x,y,z = 0,0,0
        y = int(posi[0])
        z = int(posi[1])
        x = int(posi[2])
        z -= 2
        if map[y][z][x] == 1:
            self.pos[0] = 0
            self.colisionBottom = 1
        else:
            self.colisionBottom = 0

        #map als 3d matrix auslesesn
        #bewegungsrichtung betrachten
        #falls block == neachste Bewgung
            #nicht bewegen
        #falls colision nach unten == 1
            #slef.pos[0] = 0


    def update(self, dt, map, pos):
        self.pull(dt)
        self.colision(map, pos)
