

# three data point example
import numpy as np


Xi = [0.3, 0.5, 0.8]
yi = [0.2, 0.8, 0.6]
#----------------------------------------------------------------------------------------------------
# VANDERMONDE MATRIX
# use a function to construct the matrix above
# note than numpy already has a function to do this
V = np.vander(Xi, increasing=True)
# V = np.vander(X, N+1, increasing=True) # Here N+1 is the degree of the polynomial

print('V = \n{}'.format(V))
#----------------------------------------------------------------------------------------------------

# USE LINALG.SOLVE TO FIND COEFFICIENTS OF POLYNOMIAL
# use a numpy linear algebra solver to solve the system
# uses an LU algorithm - we'll come back to how this is done
a = np.linalg.solve(V, yi)

# USE POLY1D - FOR CREATING THE POLYNOMIAL FOM COEFFICIENTS
# Set up a polynomial from the coefficients using numpy rather than writing out.
# Use numpy.flip to reverse the coefficients as poly1d assume decreasing rather than
# increasing powers - look at documentation
p2 = np.poly1d(np.flip(a, 0))
print('\nWhich agrees with us as long as we reverse the order of our coefficients:')
print('np.flip(a, 0) = \n{}'.format(np.flip(a, 0)))

# the p2 here is a function so evaluate it at our x locations
y = p2(X)

#----------------------------------------------------------------------------------------------------

# MATRIX DIAGNOLIZATION

lam, vecs = sl.eig(A)

print('sl.eig returns for eigenvalues: ',lam)
# ah we forgot that eig returns complex numbers even when real, so instead let's check
print('The diagonal Lambda matrix we constructed is the same matrix you get via np.diag(np.real(lam)):', 
      np.allclose(Lambda , np.diag(np.real(lam))))
# and therefore now
print('A =  vecs@np.diag(np.real(lam))@sl.inv(vecs)) :', np.allclose(A, vecs@np.diag(np.real(lam))@sl.inv(vecs)))
#----------------------------------------------------------------------------------------------------

# SVD
# This is the scipy solution

A = np.array([
    [3, 1, 9, 4],
    [2, 1, 7, 3],
    [5, 2, 16,7]])


UU, SS, VVT = sl.svd(A)
SSS = np.zeros_like(A,dtype='float')
# the following just places the SS vector on singular vectors into the 
# right locations of the matrix SSS
SSS[:min(A.shape[0],A.shape[1]),:min(A.shape[0],A.shape[1])] = np.diag(SS)

print('\nSS')
pprint(SS)

print('\nUU')
pprint(UU)

print('\nVV')
pprint(VVT.T)

print('\nSSS')
pprint(SSS)

print('\nres')
pprint(UU @ SSS @ VVT)