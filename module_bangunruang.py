import math

def lingkaran(r):
    luas = math.pi*r*2
    keliling = 2*math.pi*r
    return luas, keliling

def segitiga(a, t, s):
    luas = 1/2*a*t
    keliling = s*3
    return luas, keliling
    