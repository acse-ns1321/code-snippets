import numpy as np
import matplotlib.pyplot as plt
from mpltools import annotation

# X- Axis
n = [ 100 , 400 , 1600 , 6400 , 14400 ]

# Y axis
t_cg= [ 0.004562782007269561 , 0.02994208800373599 , 1.8747289170278236 , 150.62071980402106 , 1944.6007807209971 ]
t_solve= [ 0.00038385100197046995 , 0.0037327419850043952 , 0.14031925599556416 , 6.2320067409891635 , 76.656829766]

# Setup figure
plt.figure ( figsize= ( 12 , 6 ))

# Add log-log plot
plt.loglog ( n , t_solve , '.-' , label= 'direct solve (LU)' ) # THIS IS THE CONVERGENCE PLOT
plt.loglog ( n , t_cg , '.-' , label= 'full CG iteration' ) # THIS IS THE CONVERGENCE PLOT

# Add Annotation Slope Marker
annotation.slope_marker (( 4e3 , 2e2 ), ( 3 , 1 ), invert=True ,
size_frac= .2 , pad_frac=0.05 , text_kwargs = dict ( fontsize = 14 ))

# Add Axis lable and legends
plt . xlabel ( 'Problem size $n$' )
plt . ylabel ( 'Time (s)' )
plt . legend ()