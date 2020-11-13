# how the infos are build:

# edges:
#e1 | v1, v2 | t1, t2
#e2 | v3, v4 | t3, t4

#triangles:
#t1 | e1, e2, e3

#verticies
#v1 | x, y, z

class Meshloader:

    def __init__(self):
        self.meshpath = 'res/mesh/default.mesh' #the mesh file
        self.MemCache = [] #cache for alle the triangles that need to be loaded
        self.Vertices = [] #list of vertices that make up the triangle
        self.Edges = []    #list of items that describe the relation between vertices and triangles
        self.Triangles =[] #alle the edges that make up each triagnle

    def getTriangle(self, triangle):

        #get the triangle
        current = self.Triangles[triangle]

        #extract its edges
        e1 = current[0]
        e2 = current[1]
        e3 = current[2]

        #load the next batch of triangles into memory
        #tbh this looks kinda awful but eh
        self.MemCache.append(self.Edges[e1][2 + (not(triangle == self.Edges[e1][2]))])
        self.MemCache.append(self.Edges[e2][2 + (not(triangle == self.Edges[e2][2]))])
        self.MemCache.append(self.Edges[e3][2 + (not(triangle == self.Edges[e3][2]))])

        #extract it's vertices from its edges
        coords = []

        coords.append(self.Edges[e1][0])
        coords.append(self.Edges[e1][1])
        coords.append(self.Edges[e2][not(self.Edges[e2][0] in self.Edges[e1][:2])])

        return coords

    def openmesh(self):
        with open(self.meshpath, 'r') as file:
            data = file.read().split('\n')

        print(data)



