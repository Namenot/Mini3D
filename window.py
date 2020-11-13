from pyglet.gl import *
from pyglet.window import key
from pyglet import clock

import model  as mod
import entities

class Window(pyglet.window.Window):

    def cam(self, pos, rot):
        glPushMatrix()
        glRotatef(-rot[0], 1, 0, 0)
        glRotatef(-rot[1], 0, 1, 0)
        glTranslatef(-pos[0], -pos[1], -pos[2])

    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    def set2d(self): self.Projection(); gluOrtho2D(0, self.width, 0, self.height); self.Model()
    def set3d(self): self.Projection(); gluPerspective(self.d['fov'], self.width / self.height, 0.05,
                                                       self.d['maxrenderdist']); self.Model()

    def __init__(self, settings, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #load the games config
        self.settings = settings
        self.d = self.settings.d

        #init the entity section
        #entity and camera properties
        self.pentity = entities.PlayerEntity(self.d, (10, 10, 10), (0, 0))

                #check the key state
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
                #cam rotation and position
        self.camrot = self.pentity.rot
        self.campos = self.pentity.pos

        #init forces that act on entities

        #init collisions

        #init lightning

        #init sounds


        self.spin = 0 #turns the camera (temp)

        #game tick clock
        clock.schedule_interval(self.update, 1 / self.d['tickrate'])
        self.model = mod.Model()

    def on_mouse_motion(self, x, y, dx, dy):
        sens = self.d['sensitivity'] / 20  # mouse sens
        self.pentity.mouse_motion(dx * sens, dy * sens)

    def on_key_press(self, KEY, mod):
        pass

    def update(self, dt): #ist fps unabhaengig
        self.pentity.entupdate(dt, self.keys)


    def on_draw(self):

        self.spin += 1

        self.clear()

        self.set3d()
        glEnable(GL_DEPTH_TEST)

        #self.cam((0,0,0),(self.spin,self.spin)) #draws the camera
        self.cam(self.campos, self.camrot)
        self.model.draw() #draws the world !!!!TODO rewrite completly for optimisation purposes

        self.set2d()
        glDisable(GL_DEPTH_TEST)

        glPopMatrix()