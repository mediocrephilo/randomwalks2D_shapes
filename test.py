import matplotlib.pyplot as plt
import numpy as np
from rectangle import random_walk_target_rectangle
from ellipse import random_walk_target_ellipse
from square import random_walk_target_square
from circle import random_walk_target_circle
from randwalk2d_module import setup_rectangle, setup_ellipse, setup_square, setup_circle, draw_boundary_rectangle, draw_boundary_ellipse, draw_boundary_circle, draw_target

max_steps = 30000

area = 1600

plot_size = 40

def rectangle_test(num_walks):
  boundary    = setup_rectangle((0.0, 0.0), 50, 32)
  target      = setup_rectangle((10.0, 10.0), 4, 4)    
  start_loc   = ( 0.0, 0.0)
  line_type = ['r-','c-','k-','g-','m-'] 
  for i in range(num_walks):      
    xwalk1,ywalk1,steps_taken,target_reached = random_walk_target_rectangle(max_steps, \
    start_loc, boundary, target )
    plt.plot(xwalk1, ywalk1, line_type[i],label= f'wk{i+1}, {steps_taken}  steps') 
    plt.plot(xwalk1[-1],ywalk1[-1], 'b*', ms=8)  
  draw_boundary_rectangle(start_loc, boundary, plot_size)
  draw_target(target)
  plt.title(f'2D walks inside rectangle w/ target ({num_walks})' )
  plt.legend(loc="upper left")
  plt.grid(True)
  plt.savefig("rw2d_target1.png")
  plt.show() 

def ellipse_test(num_walks):
  boundary    = setup_ellipse((0.0, 0.0), (2*(1600/(20*np.pi))), 40)
  target      = setup_rectangle((10.0, 10.0), 4, 4)    
  start_loc   = (0.0, 0.0)
  line_type = ['r-','c-','k-','g-','m-'] 
  for i in range(num_walks):      
    xwalk1,ywalk1,steps_taken,target_reached = random_walk_target_ellipse(max_steps, \
            start_loc, boundary, target )
    plt.plot(xwalk1, ywalk1, line_type[i],label= f'wk{i+1}, {steps_taken} steps') 
    plt.plot(xwalk1[-1],ywalk1[-1], 'b*', ms=8) 
  draw_boundary_ellipse(start_loc, boundary, plot_size)
  draw_target(target)
  plt.title(f'2D walks inside ellipse w/ target ({num_walks})' )
  plt.legend(loc="upper left")
  plt.grid(True)
  plt.savefig("rw2d_target1.png")
  plt.show() 

def square_test(num_walks):
  boundary    = setup_square((0.0, 0.0), 40)
  target      = setup_rectangle((10.0, 10.0), 4, 4)    
  start_loc   = ( 0.0, 0.0)
  line_type = ['r-','c-','k-','g-','m-'] 
  for i in range(num_walks):      
    xwalk1,ywalk1,steps_taken,target_reached = random_walk_target_square(max_steps, \
    start_loc, boundary, target )
    plt.plot(xwalk1, ywalk1, line_type[i],label= f'wk{i+1}, {steps_taken}  steps') 
    plt.plot(xwalk1[-1],ywalk1[-1], 'b*', ms=8)  
  draw_boundary_rectangle(start_loc, boundary, plot_size)
  draw_target(target)
  plt.axis('square')
  plt.title(f'2D walks inside box w/ target ({num_walks})' )
  plt.legend(loc="upper left")
  plt.grid(True)
  plt.savefig("rw2d_target1.png")
  plt.show() 

def circle_test(num_walks):
  circle = setup_circle((0.0, 0.0), np.sqrt(1600/(np.pi)))
  target = setup_rectangle((10.0, 10.0), 4, 4) 
  start_loc   = (0.0, 0.0)
  line_type = ['r-','c-','k-','g-','m-']
  plt.clf
  for i in range(num_walks):      
    xwalk1,ywalk1,steps_taken,target_reached = random_walk_target_circle(max_steps, start_loc, circle, target )
    plt.plot(xwalk1, ywalk1, line_type[i],label= f'wk{i+1}, {steps_taken} steps') 
    plt.plot(xwalk1[-1],ywalk1[-1], 'k*', ms=16)
  draw_boundary_circle(start_loc, circle, plot_size)
  draw_target(target)
  plt.axis('square')
  plt.title(f'2D walks inside circle w/ target ({num_walks})' )
  plt.legend(loc="upper left")
  plt.grid(True)
  plt.savefig("rw2d_box1.png")
  plt.show() 