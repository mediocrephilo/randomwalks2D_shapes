import matplotlib.pyplot as plt
import numpy as np
from rectangle import random_walk_target_rectangle
from ellipse import random_walk_target_ellipse
from square import random_walk_target_square
from circle import random_walk_target_circle
from randwalk2d_module import setup_rectangle, setup_ellipse, setup_square, setup_circle, draw_boundary_rectangle, draw_boundary_ellipse, draw_boundary_circle, draw_target

def rectangle_stats(num_walks):
  max_steps = 50000
  rectangle = setup_rectangle((0.0, 0.0), 50, 32)
  target = setup_rectangle((10.0, 10.0), 4, 4)    
  start_loc = ( 0.0, 0.0)
  plt.clf
  walk_list = []
  for i in range(num_walks):      
      xwalk1,ywalk1,steps_taken,target_reached = random_walk_target_rectangle(max_steps, start_loc, rectangle, target )
      if target_reached :
          walk_list.append(steps_taken)
  walk_list = np.array(walk_list)
  ave_steps = int(np.mean(walk_list))
  std_dev_steps = int(np.std(walk_list))
  plt.hist(walk_list, bins=50, color='red')      
  plt.title(f'rectangle 2D walks with target (steps: mean= {ave_steps}, std_dev = {std_dev_steps}')
  plt.xlabel(' Number of steps')
  plt.ylabel(' Frequency')
  # plt.savefig("rw2d_target_stats.png")
  plt.grid(True)
  plt.show()

def ellipse_stats(num_walks):
  max_steps = 50000
  ellipse = setup_ellipse((0.0, 0.0), (2*(1600/(20*np.pi))), 40)
  target = setup_rectangle((10.0, 10.0), 4, 4)    
  start_loc = ( 0.0, 0.0)
  plt.clf
  walk_list = []
  for i in range(num_walks):      
      xwalk1,ywalk1,steps_taken,target_reached = random_walk_target_ellipse(max_steps, start_loc, ellipse, target )
      if target_reached :
          walk_list.append(steps_taken)
  walk_list = np.array(walk_list)
  ave_steps = int(np.mean(walk_list))
  std_dev_steps = int(np.std(walk_list))
  plt.hist(walk_list, bins=50, color='red')      
  plt.title(f'ellipse 2D walks with target (steps: mean= {ave_steps}, std_dev = {std_dev_steps}')
  plt.xlabel(' Number of steps')
  plt.ylabel(' Frequency')
  # plt.savefig("rw2d_target_stats.png")
  plt.grid(True)
  plt.show()

def square_stats(num_walks):
  max_steps = 50000
  square = setup_square((0.0, 0.0), 40)
  target = setup_rectangle((10.0, 10.0), 4, 4)    
  start_loc = ( 0.0, 0.0)
  plt.clf
  walk_list = []
  for i in range(num_walks):      
      xwalk1,ywalk1,steps_taken,target_reached = random_walk_target_square(max_steps, start_loc, square, target )
      if target_reached :
          walk_list.append(steps_taken)
  walk_list = np.array(walk_list)
  ave_steps = int(np.mean(walk_list))
  std_dev_steps = int(np.std(walk_list))
  plt.hist(walk_list, bins=50, color='red')      
  plt.title(f'square 2D walks with target (steps: mean= {ave_steps}, std_dev = {std_dev_steps}')
  plt.xlabel(' Number of steps')
  plt.ylabel(' Frequency')
  # plt.savefig("rw2d_target_stats.png")
  plt.grid(True)
  plt.show()

def circle_stats(num_walks):
  max_steps = 50000
  circle = setup_circle((0.0, 0.0), np.sqrt(1600/(np.pi)))
  target = setup_rectangle((10.0, 10.0), 4, 4) 
  start_loc   = (0.0, 0.0)
  plt.clf
  walk_list = []
  for i in range(num_walks):      
      xwalk1,ywalk1,steps_taken,target_reached = random_walk_target_circle(max_steps, start_loc, circle, target )
      if target_reached :
          walk_list.append(steps_taken)
  walk_list = np.array(walk_list)
  ave_steps = int(np.mean(walk_list))
  std_dev_steps = int(np.std(walk_list))
  plt.hist(walk_list, bins=50, color='red')      
  plt.title(f'circle 2D walks with target (steps: mean= {ave_steps}, std_dev = {std_dev_steps}')
  plt.xlabel(' Number of steps')
  plt.ylabel(' Frequency')
  # plt.savefig("rw2d_target_stats.png")
  plt.grid(True)
  plt.show()