import os
import Image
import numpy as np
from joblib import Memory, Parallel, delayed
import leargist
import time

def gist(path):
    im = Image.open(path)
    return leargist.color_gist(im)

mem = Memory(cachedir='tmp')
memgist = mem.cache(gist)

im = "pics/spatial_envelope_256x256_static_8outdoorcategories/coast_arnat59.jpg"

t0 = time.time()
memgist(im)
print 'First run done in %0.3f secs' % (time.time() - t0)

t1 = time.time()
memgist(im)
print 'Second run done in %0.3f secs' % (time.time() - t1)