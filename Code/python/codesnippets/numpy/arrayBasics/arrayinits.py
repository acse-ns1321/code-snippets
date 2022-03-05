import numpy as np

np.array([2, 3, 4])             # direct initialization
np.empty(20, dtype=np.float32)  # single precision array of size 20
np.zeros(200)                   # initialize 200 zeros
np.ones((3,3), dtype=np.int32)  # 3 x 3 integer matrix with ones
np.eye(200)                     # ones on the diagonal
np.zeros_like(a)                # array with zeros and the shape of a
np.linspace(0., 10., 100)       # 100 points from 0 to 10
np.arange(0, 100, 2)            # points from 0 to <100 with step 2
np.logspace(-5, 2, 100)         # 100 log-spaced from 1e-5 -> 1e2
np.copy(a)                      # copy array to new memory