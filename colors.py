import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from gray import *

# Index to color
def RGBTrav():
    color = {}
    dim = 3
    order = 8
    for i in range(2 ** (dim * order)):
        color[i] = hilbertIndexInverse(dim,order,i)
    return color

def makeRGBImage():
    dim = 2
    order = 12

    img = Image.new('RGB', (2**order, 2**order), "white")
    pixels = img.load()

    color = RGBTrav()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            hin = hilbertIndex(dim,order,[i,j])
            pixels[i,j] = (color[hin][0], color[hin][1], color[hin][2])
            print hin,pixels[i,j]

    img.save("hilbertRGB.png")

makeRGBImage()
