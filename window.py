import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet import clock

import math
import numpy as np

import grav  as grav
import model  as mod
import player  as ply
import mapgenerator as gen
from MYUI import settings as sets
from MYUI import console as cmd


class Window(pyglet.window.Window):

    def push(self, pos, rot):
        glPushMatrix()
        glRotatef(-rot[0], 1, 0, 0)
        glRotatef(-rot[1], 0, 1, 0)
        glTranslatef(-pos[0], -pos[1], -pos[2])

    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    def set2d(self): self.Projection(); gluOrtho2D(0, self.width, 0, self.height); self.Model()
    def set3d(self): self.Projection(); gluPerspective(self.d['fov'], self.width/self.height, 0.05, self.d['maxrenderdist']); self.Model()

    #103=fov;0.05/1000=min/max-render-dist;

    lock = False

    def setLock(self, state): self.lock = state, self.set_exclusive_mouse(state)


    mouse_lock = property(lambda self:self.lock, setLock)

    def __init__(self, settings, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.settings = settings
        self.d = self.settings.d #Settings

        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        clock.schedule_interval(self.update, 1/self.d['max_fps'])

        self.grav      = grav.Gravity(self.d,(0,0,0))
        self.model     = mod.Model()
        self.player    = ply.Player(self.d, self.grav, (10, 10, 10), (0, 0))                                      #spawn
        self.console   = cmd.Console(self.settings)
        #self.generator = gen.Generator(self.model, self.player, 0,0,0)

    def on_mouse_motion(self, x, y, dx, dy):
        sens = self.d['sensitivity'] / 20                                                                     #mouse sens
        if self.mouse_lock: self.player.mouse_motion(dx*sens, dy*sens)

    def kill(self):
        if self.d['kill'] == 1:
            self.close()

    def on_mouse_release(self, x, y, button, mod):
        if button == pyglet.window.mouse.LEFT: self.mouse_lock = not self.mouse_lock

    def on_key_press(self, KEY, mod):
        if KEY == 65307:  return pyglet.event.EVENT_HANDLED                     #ESCAPE
        else:
            self.console.inp(KEY)

        #print(KEY," : ",chr(KEY))

    def update(self, dt): #ist fps unabhaengig
        self.grav.update(dt, self.model.map, self.player.pos)
        self.player.update(dt, self.keys)
        self.console.update(self.keys)
        self.kill()

    def on_draw(self):
        self.clear()

        self.set3d()
        glEnable(GL_DEPTH_TEST)
        self.push(self.player.pos + self.grav.pos, self.player.rot)  #hier kommt gravity ins spiel (hier scheint die player pos "angewand zu werden")
        self.model.draw()

        self.set2d()
        glDisable(GL_DEPTH_TEST)
        self.console.fps_lable.draw()
        self.console.cmd_lable.draw()
        self.console.fps_lable.draw()
        self.console.pic.draw()

        glPopMatrix()
