import pyglet
from pyglet.gl import *
from pyglet.window import key
import math
import numpy as np

class Settings:

    def __init__(self):
        self.d = {}
        self.s = "res/cfg/settings.txt"
        self.loadSettings()
        self.d['kill'] = 0


    def loadSettings(self):
        with open(self.s) as file:
            for line in file:
                if len(line.split()) == 2:
                   (key, val) = line.split()
                   self.d[key] = float(val)


    def save(self):

        result = list(self.d.items())

        file = open(self.s, 'w')
        print("len: ", len(self.d))
        for i in range(0, len(self.d)):
            file.write(result[i][0])
            file.write(" ")
            file.write(str(result[i][1]))
            file.write("\n")

        ##changeable:
        ##-------------------------------
        ## mouse sens
        ## resolution
        ## sound volume
        ## render distance
        ## FOV
        ## key binds (w,a,s,d,i,e,m,c,esc,space,mouse1,mouse2)
        ## skins
        ##-------------------------------

        ##set:
        ##-------------------------------
        ## walking speed
        ## Gravity
        ##-------------------------------

        ##map :
        ##-------------------------------
        ## spawn
        ## size (dims (x,y,z))
        ## various mapGen values //needs yet to be defined
        ## texture location
        ##-------------------------------
