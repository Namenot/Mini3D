import pyglet
from pyglet.gl import *
from pyglet.window import key
import math
import numpy as np

import grav as grav
import model as mod
from MYUI import settings as sets
import window as win

class Player:

    def __init__(self, d, grav, pos=(0,0,0), rot = (0,0)):
        self.grav     = grav
        self.d        = d
        self.pos      = list(pos)
        self.rot      = list(rot)
        self.jumping  = 0

    def mouse_motion(self, dx, dy):
        dx/8; dy/8; self.rot[0] += dy; self.rot[1] -=dx
        if self.rot[0] > 90: self.rot[0] = 90
        elif self.rot[0] < -90: self.rot[0] = -90

    def jump(self):

        self.jumpenable = -1
        self.speed      = 0

        if self.jumping:
            self.speed = 1
            if self.grav.colisionBottom:
                self.jumpenable *= -1
        else:
            self.speed = 0

        if self.grav.colisionBottom:
            self.jumpenable *= -1
            self.jumping = 0

        if self.jumpenable:
            self.pos[1] += self.s*self.sens * self.speed

    def update(self, dt, keys):
        self.sens = self.d['walking']                                                                                #movement speed
        self.s = dt*10
        rotY = -self.rot[1]/180*math.pi
        dx = self.s*math.sin(rotY)
        dz = self.s*math.cos(rotY)
        self.jump()

        if self.d['console'] != 1:
            if keys[key.W]:
                self.pos[0] += dx*self.sens
                self.pos[2] -= dz*self.sens
            if keys[key.S]:
                self.pos[0] -= dx*self.sens
                self.pos[2] += dz*self.sens
            if keys[key.A]:
                self.pos[0] -= dz*self.sens
                self.pos[2] -= dx*self.sens
            if keys[key.D]:
                self.pos[0] += dz*self.sens
                self.pos[2] += dx*self.sens
            if keys[key.SPACE]:
                self.jumping = 1                                                              #jump (on keypress && !colision)
            if keys[key.LSHIFT]:
                self.pos[1] -= self.s*self.sens

        self.pos[1] += self.grav.pos[0] #pull from gravity
