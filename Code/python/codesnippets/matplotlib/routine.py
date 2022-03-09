import matplotlib.pyplot as plt
import numpy as np
#-----------------------------------------------------
# INITIALIZATION OF FIGURE AND AXES
#-----------------------------------------------------
# Initialize figure with size
fig = plt.figure(figsize=(5, 2))
# Iniialize figure and axes
fig, axes = plt.subplots(5, 2, figsize=(5, 5)) # fig and 5 x 2 nparray of axes
# Organize Axes
fig, ax = plt.subplots(1,1) # Single figure with an axes
fig,(ax1,ax2)=plt.subplots((2,1))  # TWO ROWS AND ONE COLUMN
fig,(ax1,ax2)=plt.subplots((1,2))  # Two cols one row
# Create and add subplots
ax = fig.add_subplot(3, 2, 2)     # add second subplot in a 3 x 2 grid

# Other customizations
ax = plt.subplot2grid((2, 2), (0, 0), colspan=2)  # multi column/row axis
ax = fig.add_axes([left, bottom, width, height])  # add custom axis

#-----------------------------------------------------
# PREPARATION OF DATA
#-----------------------------------------------------
X=np.linspace(0,4*np.pi,1000)
Y=np.sin(X)

#-----------------------------------------------------
# SET TITLE, LABELS, GRID, LEGENDS ETC
#-----------------------------------------------------
# Big and Subplot Titles
fig.suptitle('title')            # big figure title
ax.set_title('blabla')           # sets the axis title

# X and Y Lables
ax.set_xlabel('xbla')            # set xlabel
ax.set_ylabel('ybla')            # set ylabel
# X and Y Limits
ax.set_xlim(1, 2)                # sets x limits
ax.set_ylim(3, 4)                # sets y limits

ax.set(xlabel='bla')             # set multiple parameters at once

# Annotations
ax.annotate("”A”",(X[250],Y[250]),(X[250],-1),
    ha="center",va="center",arrowprops = {"arrowstyle":"->","color":"C1"})
# Other Customizations : colors, markers, linewidth and styles,ticks and ticks labels, titles, etc.
ax.plt(X,Y,color="black") # line colour
ax.plot(X,Y,linestyle="--") # Linestyle
ax.plot(X,Y,marker="o") # line-markers

# Grid and Legend
ax.legend(loc='upper center')    # activate legend
ax.grid(True, which='both')      # activate grid

# Adjust Layouts
fig.subplots_adjust(bottom=0.1, right=0.8, top=0.9, wspace=0.2,
                    hspace=0.5)  # adjust subplot positions
fig.tight_layout(pad=0.1, h_pad=0.5, w_pad=0.5,
                 rect=None)      # adjust subplots to fit into fig


# Save Image
fig.savefig('out.png')            # save png image
fig.savefig("my-first-figure.png",dpi=300)
fig.savefig("”my-first-figure.pdf”")  # Save as svg
# Show Image
plt.show()