import math
from pyglet.window import key

class PlayerEntity:

    def __init__(self, d, pos = (0,0,0), rot = (0,0)):
        self.d   = d
        self.pos = list(pos)
        self.rot = list(rot)


    def mouse_motion(self, dx, dy):
        dx / 8
        dy / 8
        self.rot[0] += dy
        self.rot[1] -= dx

        if self.rot[0] > 90:
            self.rot[0] = 90
        elif self.rot[0] < -90:
            self.rot[0] = -90

    def controlablevectors(self, k):

        self.sens = self.d['walking']
        binds = [[1,-1], [-1,1], [-1,-1], [1,1]]

        vec = [0,0]
        if k[key.W]:
            vec[0] +=  1 * self.dx
            vec[1] += -1 * self.dz
        if k[key.S]:
            vec[0] += -1*self.dx
            vec[1] +=  1* self.dz
        if k[key.A]:
            vec[0] += -1* self.dz
            vec[1] += -1*self.dx
        if k[key.D]:
            vec[0] += 1* self.dz
            vec[1] += 1*self.dx

        self.pos[0] += (vec[0] *self.sens)
        self.pos[2] += (vec[1] *self.sens)

        #todo
        # DONE 1. read binds from a config
        # 2. dont change the self.pos values for they should only be changed in the mementumvectors calculations
        # 3. addjumping
        # 4. fix speed : currently speed is higher when using 2 directions at the same time (walking with W/A is faster than walking with only W)



    def momentumvectors(self):
        pass
        #todo
        # 1. gather all the movement vectors that aply to the given entity
        # 2. add them all together to find out how fast it moves in what direction
        # 3. aply the directions

    def entupdate(self, dt, keys):

        self.s = dt * 10

        rotY = -self.rot[1] / 180 * math.pi
        self.dx = self.s * math.sin(rotY)
        self.dz = self.s * math.cos(rotY)
        self.controlablevectors(keys)