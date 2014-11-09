# Gray code library: Implementing algorithms dealing with Reflected Binary Gray Codes, as detailed in "Compact Hilbert Indices" - Chris Hamilton

def gc(i):
    return i ^ (i / 2)

def gci(g):
    i = 0
    while(g):
        i = i ^ g
        g /= 2

    return i
