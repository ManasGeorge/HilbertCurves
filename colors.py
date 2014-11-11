import matplotlib.pyplot as plt
import profile
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

def makeRGBImageHilbert():
    dim = 2
    order = 12

    img = Image.new('RGB', (2**order, 2**order), "white")
    pixels = img.load()

    color = RGBTrav()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            hin = hilbertIndex(dim,order,[i,j])
            pixels[i,j] = (color[hin][0], color[hin][1], color[hin][2])

    img.save("hilbertRGB.png")

def makeRGBImageVanilla():
    dim = 2
    order = 12

    img = Image.new('RGB', (2**order, 2**order), "white")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            index = i*(2**order) + j
            b = (index) % 256
            g = ((index)/256) % 256
            r = ((index)/256/256) % 256
            pixels[i,j] = (b,g,r)

    img.save("vanillaRGB.png")

def makeRGBHilbertImage2DVanilla():
    dim = 2
    order = 12

    img = Image.new('RGB', (2**order, 2**order), "white")
    pixels = img.load()

    for index in range(2 ** (order+order)):
        b = (index) % 256
        g = ((index)/256) % 256
        r = ((index)/256/256) % 256
        coords = hilbertIndexInverse(dim,order,index)
        pixels[coords[0], coords[1]] = (b,g,r)

    img.save("vanillaRGBhilbert.png")

# makeRGBImageHilbert()
# makeRGBImageVanilla()
makeRGBHilbertImage2DVanilla()
