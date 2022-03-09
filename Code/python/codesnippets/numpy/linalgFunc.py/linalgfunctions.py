

import numpy as np

import scipy.linalg as sl

# VANDERMONDE MATRIX

V = np.vander(Xi, increasing=True)
V = np.vander(X, N+1, increasing=True) # Here N+1 is the degree of the polynomial


# USE LINALG.SOLVE TO FIND COEFFICIENTS OF POLYNOMIAL
a = np.linalg.solve(V, yi)

# USE POLY1D - FOR CREATING THE POLYNOMIAL FROM COEFFICIENTS
# Use numpy.flip to reverse the coefficients as poly1d assume decreasing rather than
p2 = np.poly1d(np.flip(a, 0))


# TRANSPOSE 
A = V.T @ V  # same as A = np.transpose(V) @ V

# INVERSE
invA = sl.inv(A)

# POLYFIT _ COEFFCIENTS FIT A POLYNOMIAL
poly_coeffs = np.polyfit(X, y, N)


# EIGEN VALS
sl.eigvals(a, b)
# OUTPUT : array([ 1.+0.j, -1.+0.j])

sl.eigvals(a) == sl.eig(a)[0]

# The function scipy.linalg.eigh returns two arrays, 
# the first containing the eigenvalues, and the second the
# eigenvectors. For matrix A we use the following code to print the eigenvalues only
print ( sl . eigh ([[ 2 , 1 ], [ 1 , 2 ]])[ 0 ])


# UPPER AND OWER TRIANGULAR MATRIX
# tril(A) returns D+L
# tril(A, -1) returns L only
np.tril(m, k=0)
np.triu
