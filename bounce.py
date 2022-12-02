import os
import matplotlib
import matplotlib.pyplot as pyplt
import matplotlib.animation as animation
import numpy as np
import time

# - - - General utilities - - - 

def is_docker():
    path = '/proc/self/cgroup'
    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
    )

# - - - General setup and constants - - - 

figure, axes = pyplt.subplots() # figure & axes in which the animation will run
figure.suptitle('Bounce!')

# Some constants and variables
Duration =  9        # Duration of the animation in seconds
FPS      =  40       # Frames per second -- don't change me
dt       =  1.0/FPS  # The time step for the animation -- don't change me
G        = -0.67     # The gravitational constant

floor_slope = 0.20        # can be set positive or negative

ball_radius = 0.05
spotr = 0.6*ball_radius   # dist from center of ball to center of spot on ball

x0, y0 = [0.10, 0.70]     # initial position of ball
vx, vy = [0.50, 0.20]     # velocity of ball
vang = - 30 * 2*np.pi/60; # angular vel. of ball -- spinning clockwise, 30 rpm

t = 0.0                   # current time
bx, by = [x0, y0]         # current ball position
bphi = 0;                 # current ball rotation

# pyplot commands -- the ball and text (ellapsed time)

ball = pyplt.Circle([bx, by], ball_radius, color='#49D')
axes.add_patch(ball)
spot = pyplt.Circle([bx+spotr*np.cos(bphi), by+spotr*np.sin(bphi)],
                    ball_radius/8, color='#303')
axes.add_patch(spot)
txt = axes.text(0.80, 1.03, f't = {t:4.1f}')

# - - - Animation setup and the animation loop - - - 

def setup_stage():
    '''Setup the axes with the right size and draw a red bounding box.'''
    global axes, floor_slope
    axes.set_aspect('equal')
    axes.set_xlim(-0.1, 1.1)
    axes.set_ylim(min(-0.1,floor_slope-0.1), 1.1)
    axes.plot([0,1], [1,1], color='#D31', lw=4)
    axes.plot([0,0], [0,1], color='#D31', lw=4)
    axes.plot([0,1], [0,floor_slope], color= '#D31', lw=4)
    axes.plot([1,1], [floor_slope,1], color='#D31', lw=4)
    return [ball,spot,txt]  # list of animated objects

def animate(i):
   '''Called iteratively (every dt) as the main animation loop. 
      Updates the postion of the ball, etc.'''
   global bx, by, bphi, ball, spot, t, vx, vy
   t  += dt

   # - - - Put your animation logic into this block. - - -

   vy += dt*G
   bx += dt*vx
   by += dt*vy
   bphi += dt*vang;

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - 
   
   ball.set_center([bx, by])
   spot.set_center([bx+spotr*np.cos(bphi), by+spotr*np.sin(bphi)])
   txt.set_text(f't = {t:.1f}')
   return [ball,spot,txt]  # list of animated objects that were updated


ani = animation.FuncAnimation(figure, animate, np.arange(1, Duration*FPS),
                              init_func=setup_stage,
                              interval=dt*1000, blit=True, repeat=False)

# - - - Rendering of the animation, to a window or, if dockerized, an mp4 - - -

if is_docker():
    fname = 'bounce_out.mp4'
    print (f'Encoding animation to {fname}')
    ani.save('bounce_out.mp4', writer = animation.FFMpegWriter(fps=FPS) )
else:
    pyplt.show(block=False)
    pyplt.pause(Duration+2.0);
    

