import numpy as np
import meshprocessing as mp
import re

def load(path = 'maps/testmap.mp'):

    fp = open(path, 'r')

    #find char in file so that i can reshape properly

    a = np.loadtxt(path, dtype = float).reshape(5,3,3)
    print(a)


def save(ary, path = 'maps/testmap.mp'):

    a = np.zeros([5,3,3])

    with open(path,'w') as outfile:
        outfile.write('#Array shape: \n#{0}\n'.format(a.shape))
        for data_slice in a:
            np.savetxt(outfile, data_slice, fmt='%-7.2f')
            outfile.write('#new slice\n')

def indextest():
    l = [1,2,3,4,5]
    print(3 + (not(3 in l[:2])))
    print(3 + True)

#print("Hallo")
#save(1)
#load()
#indextest()



l = ["Hobel", "Holunder", "Holz", "Holzschuppen"]
l.sort()
print(l)

#mesher = mp.Meshloader()
#mesher.openmesh()
