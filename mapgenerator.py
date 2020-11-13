import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet import clock

import math
import numpy as np

import grav as grav
import player as ply
from MYUI import settings as sets

class Generator:

    def test(self, dt):
        pass

    def __init__(self, y, z, x): #''' model, player,'''
        self.map    = np.zeros((y, z, x)) #y, z, x
        self.mp     = self.map
        #self.model  = model
        #self.player = player
        self.maxdim = 0

        self.polygons = []


        #clock.schedule(self.test)

    def generate(self):
        i,k = 0,0
        while(i < 500):
            while(k < 500):
                self.mp[i][0][k] = 1
                self.mp[i][5][k] = 1
                k+=1
            i+= 1
            k = 0
        return self.mp

    def load(self, path = 'map/testmap.mp'):

        fp = open(path, 'r')

'''
TODO:
    1) load laedt in eigener clock
    2) Generator schreibt in model, nicht anders herum
        => self.model.map wird aus Generator heraus beschrieben
        => die add_block() function wird in load verwendet
    3) Generator muss ohne coordinaten (x,y,z klar kommen)
'''
