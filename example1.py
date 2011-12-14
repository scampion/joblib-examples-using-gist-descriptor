import os, time, Image, leargist 
import numpy as np
from joblib import Memory, Parallel, delayed


def gist(path):
    im = Image.open(path)
    return leargist.color_gist(im)

mem = Memory(cachedir='tmp')
memgist = mem.cache(gist)

picdir = "pics/spatial_envelope_256x256_static_8outdoorcategories/"

t0 = time.time() 
for f in os.listdir(picdir):
    memgist(os.path.join(picdir, f))
print 'run done in %0.3f secs' % (time.time() - t0)