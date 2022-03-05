import numpy as np

np.loadtxt(fname, skiprows=2, delimiter=',')   # ascii data from file
np.savetxt(fname, array, fmt='%.5f')           # write ascii data
np.fromfile(fname, dtype=np.float32, count=5)  # binary data from file
np.tofile(fname)                               # write (C) binary data
np.save(fname, array)                          # save as numpy binary (.npy)
np.load(fname, mmap_mode='c')                  # load .npy file (memory mapped)