import pyglet
from pyglet.gl import *
from pyglet.window import key

import math
import numpy as np
import threading

import grav as grav
import player as ply
from MYUI import settings as sets
import window as win
import mapgenerator as gen

class Model():

    def get_tex(self, file):
        tex = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def add_block(self, x,y,z):

        tex_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))

        X,Y,Z = x+1, y+1, z+1 #Breite, hoehe, tiefe

        self.batch.add(4, GL_QUADS, self.side,   ('v3f', (X, y, z,  x, y, z,  x, Y, z,  X, Y, z)), tex_coords) # back
        self.batch.add(4, GL_QUADS, self.side,   ('v3f', (x, y, Z,  X, y, Z,  X, Y, Z,  x, Y, Z)), tex_coords) # front

        self.batch.add(4, GL_QUADS, self.side,   ('v3f', (x, y, z,  x, y, Z,  x, Y, Z,  x, Y, z)), tex_coords)  # left
        self.batch.add(4, GL_QUADS, self.side,   ('v3f', (X, y, Z,  X, y, z,  X, Y, z,  X, Y, Z)), tex_coords)  # right

        self.batch.add(4, GL_QUADS, self.bottom, ('v3f', (x, y, z,  X, y, z,  X, y, Z,  x, y, Z)), tex_coords)  # bottom
        self.batch.add(4, GL_QUADS, self.top,    ('v3f', (x, Y, Z,  X, Y, Z,  X, Y, z,  x, Y, z)), tex_coords)  # top

    def __init__(self):

        self.top = self.get_tex('res/tex/top.png')
        self.side = self.get_tex('res/tex/side.png')
        self.bottom = self.get_tex('res/tex/bottom.png')

        self.map = None
        self.generator = gen.Generator(1000, 1000, 1000) #the maps dimensions

        self.batch = pyglet.graphics.Batch()

        self.map = self.generator.generate()

        self.add_block(1,1,1)

        self.run()

    def run(self):
        pass

        x,y,z = 0,0,0
        while(x < 100):
            while(y < 100):
                while(z < 100):
                    if self.map[x][y][z] == 1:
                        self.add_block(x, y, z) #links/rechts, oben/unten, forne/hinten
                        #print(x,y,z, " == 1")
                    z+=1
                y+=1
                z= 0
            x+=1
            y= 0



    def draw(self):
        self.batch.draw()
