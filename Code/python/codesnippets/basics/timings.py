from timeit import default_timer as timer

# do some timings to compare with dense matrix-vector multiplication
t_matvec_dense = []
t_matvec_diag = []
n = []
for nx in 20 , 40 , 60 , 80 , 100 , 120 , 140 , 160 , 180 , 200 : # expand this list to recreate the timings in the cel
A , b = Poisson_2D_Dirichlet_FD ( nx , nx , RHS_f , DBC )
n . append ( A . shape [ 0 ])
Adiag = DiagonalMatrix( A , [ - nx , - 1 , 0 , 1 , nx ])
time1 = timer ()
A @ b
time2 = timer ()
Adiag @ b
time3 = timer ()
t_matvec_dense . append ( time2 - time1 )
t_matvec_diag . append ( time3 - time2 )
print ( n )
print ( t_matvec_dense )
print ( t_matvec_diag )