from gray import gc
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import log, ceil
from PIL import Image

def xy2d(n,x,y):
    s = n
    d = 0
    # Iterate over each level of the curve, starting with the outermost,
    # peeling off most significant bits of the coordinates as you go along
    while(n > 0):
        s = s/2
        # rx is one if the lg(s)'th bit of x is set, and similarly for ry,rz
        rx = (int)(s & x > 0)
        ry = (int)(s & y > 0)
        # (rx,ry) determine which quadrant of the curve (x,y) is in
        # Treating this tuple as the Gray code representation of the quadrant,
        # (3*ry)*rx gives the decimal value of the quadrant (x,y)
        # belongs to. The total distance at this level is then just the 
        # quadrant number multiplied by s**2
        d += s*s*(((3*ry)^rx))
        # Rotate - flip, etc. as needed so that the orientation of the subcube
        # is correct
        x,y = rot(x,y,rx,ry,s)

    return d

# Returns a list of coordinate in RGB space, ordered as a Hilbert
# curver traversal of the space
def rgb_trav():
    # First subcube
    gcs = []
    trav = []
    for i in range(8):
        a = gc(i);
        x = (int)((a & 4) > 0)
        y = (int)((a & 2) > 0)
        z = (int)((a & 1) > 0)
        gcs.append((x,y,z))
        trav.append((x,y,z))

    # For each gray number, split the gray number into digits g -> (rx,ry,rz)
    # For each point in the traversal (x,y,z), prepend
    for i in range(1,6):
        for (rx,ry,rz) in gcs[1:]:
            for (x,y,z) in trav[:8**i]:
                # print rx,ry,rz,"=>",
                # print x,y,z,"=>",
                lx = rx << i
                ly = ry << i
                lz = rz << i
                # print lx,ly,lz
                trav.append((x+lx,y+ly,z+lz))
        fig = plt.figure()
        fig.canvas.set_window_title('Floating')
        ax = fig.add_subplot(111, projection='3d')
        ax.plot([t[0] for t in trav], [t[1] for t in trav], [t[2] for t in trav])
        print len(trav)

    plt.show()

    return trav

def rot(x,y,rx,ry,s):
    if(ry == 0):
        if(rx == 1):
            x = s-1 - x
            y = s-1  -y

        x,y = y,x

    return x,y

def main():
    size = (2048,2048)
    im = Image.new("RGB", size) 
    colors = rgb_trav()
    # pixels = im.load()
    # for x in range(size[0]):
        # for y in range(size[1]):
            # pixels[x,y] = colors[xy2d(2048,x,y)]
    # im.show()

main()
