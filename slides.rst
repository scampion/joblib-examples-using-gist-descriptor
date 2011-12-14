Joblib
======

Joblib is a set of tools to provide lightweight pipelining in Python. In particular, joblib offers:

- transparent disk-caching of the output values and lazy re-evaluation (memoize pattern)
- easy simple parallel computing
- logging and tracing of the execution

Philosophy
----------

- **Simple:** don't change your code 
- **Minimal:** no dependencies
- **Performant:** big data
- **Robust:** never fail

Lazy recomputation
------------------

- Take MD5 hash of function arguments 
- Store outputs to disk 

----

Install
=======

The debian way:
---------------

aptitude install python-joblib

The easy_install way : 
----------------------

.. sourcecode:: bash

 export PYTHONPATH=.
 easy_install --install-dir . joblib
 easy_install --install-dir . pyleargist


The hard way:
-------------
... later 

----

Example with one image
======================

.. sourcecode:: python

 import os, time, Image, leargist 
 import numpy as np
 from joblib import Memory, Parallel, delayed

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

Output
------

:: 

  ________________________________________________________________________________
  [Memory] Calling __main__--home-scampion-git-texmex_admin-doc-texmex_coffee_dec2011_pim_joblib-example0.gist...
  gist('pics/spatial_envelope_256x256_static_8outdoorcategories/coast_arnat59.jpg')
  _____________________________________________________________gist - 0.4s, 0.0min
  First run done in 0.442 secs
  Second run done in 0.007 secs

----

Example with a directory
========================

.. sourcecode:: python

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

----

Example with a // computing
===========================

.. sourcecode:: python

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

 Parallel(n_jobs=2)(delayed(memgist)(os.path.join(picdir, f) for f in os.listdir(picdir)

 print 'run done in %0.3f secs' % (time.time() - t0)

---------------------------------------------------

Sitography
==========

- Joblib: 
  
  http://packages.python.org/joblib/

- Python Conference (French):

  http://www.pycon.fr
  
  http://www.pycon.fr/talk/2022 

  Talk about scikit-learn and joblib (2010)


- Python for Scientific Computing Conference: 

  http://conference.scipy.org/scipy2011/slides/varoquaux_brain_mining.pdf

  http://www.archive.org/details/Thursday-203-5-PythonForBrainMiningneuroscienceWithStateOfThe
  
- PythonBrasil:

  http://sliwww.slideshare.net/marcelcaraciolo/joblib-the-pipelining
