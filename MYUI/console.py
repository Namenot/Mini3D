import pyglet
from pyglet.gl import *
from pyglet.window import key

from MYUI import settings as set

class Console:

    def __init__(self, settings):
        self.settings = settings
        self.d        = self.settings.d

        self.keys       = 0
        self.key        = 0
        self.currentcmd = ''

        self.toggle   = -1
        self.apply    = -1
        self.command  = ''

        self.cmd_lable   = pyglet.text.Label('')
        self.fps_lable   = pyglet.text.Label('')
        self.pic         = pyglet.graphics.Batch()
        self.ui()

        self.cmdlist = []

    def inp(self, key):
        self.key = key

        if self.toggle == 1:
            self.currentcmd += chr(self.key)
            if self.key == 65288: #delete
                if len(self.currentcmd) >= 2: #last val + del key
                    self.currentcmd = self.currentcmd[:-2]
                if len(self.currentcmd) <  2 and len(self.currentcmd) > 0:
                    self.currentcmd = self.currentcmd[:-1]

            if self.key == 65505: #LSHIFT
                    self.currentcmd = self.currentcmd[:-1]


    def update(self, keys):
        self.keys = keys

        if self.keys[key.L]:
            self.toggle = 1
        if self.keys[key.ESCAPE]:
            self.toggle = -1
        if self.keys[key.ENTER]:
            self.apply = 1


        if self.toggle == 1:
            self.c.colors = [0,0,0,155]*4
        else:
            self.c.colors = [0,0,0,0]*4
            self.currentcmd = ''
        if self.apply == 1 and self.toggle ==1:
            self.execute(self.currentcmd[:-1])
            self.currentcmd= ''
            self.apply = -1
        self.FPS()

        self.settings.d['console'] = self.toggle

        self.cmd_lable   = pyglet.text.Label(self.currentcmd, font_size=16, color=(255, 255, 255, 255),x=520, y=35,dpi=96, anchor_x='left', anchor_y='top')

    def get_tex(self, file):
        tex = pyglet.image.load(file).get_texture()
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)


    def ui(self, path = 'res/tex/cmd.png'):
        ocp = int(155)
        self.pic_png = self.get_tex(path)
        self.c = self.pic.add(4, GL_QUADS, self.pic_png, ('v2f', [500,1080, 500,0, 1920,0, 1920,1080] ),
                                                ('c4B/dynamic', [0,0,0, ocp]*4))



    def execute(self, inp):
        if inp != "":
            self.cmdlist.append(inp)

        list  = inp.split()
        num   = 0

        if inp == 'quit':
            self.settings.d['kill'] = 1
        else:

            if len(list) == 2:
                try:
                    num = float(list[1])
                    self.settings.d[list[0]] = num
                except ValueError:
                    pass
            else:
                pass



    def chat(self):
        if self.command.split()[0] == "showfps":
            self.FPS()

    def FPS(self):

        #pyglet.clock.showfps = True

        if self.d['showfps'] == 1:
            self.fps_lable = pyglet.text.Label('{:.0f} fps'.format(int(pyglet.clock.get_fps())), font_size=9, color=(180, 255, 0, 255),x=10, y=1070, anchor_x='left', anchor_y='top')

        else:
            self.fps_lable = pyglet.text.Label('')
