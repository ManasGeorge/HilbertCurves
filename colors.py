from multiprocessing import Pool,Manager
from functools import partial
from PIL import Image
from hilbert import *

# Index to color
def fillColor(color,dim,order,i):
    color[i] = hilbertIndexInverse(dim,order,i)

def RGBTrav():
    manager = Manager()
    color = manager.dict()
    dim = 3
    order = 8
    p = Pool(8)
    p.map(partial(fillColor,color,dim,order), range(2** (dim*order)))
    return color

def makeRGBImageHilbert():
    dim = 2
    order = 12

    img = Image.new('RGB', (2**order, 2**order), "white")
    pixels = img.load()

    color = RGBTrav()

    count = 0
    for i in range(2 ** (order * dim)):
        coords = hilbertIndexInverse(dim,order,i)
        if i % (2 ** (order * dim - 5)) == 0:
            img.save("hilbertRGB" + str(count) + ".png")
            count = count+1
        pixels[coords[0],coords[1]] = (color[i][0], color[i][1], color[i][2])

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

makeRGBImageHilbert()
# makeRGBImageVanilla()
# makeRGBHilbertImage2DVanilla()
