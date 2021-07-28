import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse, Circle  
random.seed(None)     

def rand_grid():
    xdelta, ydelta = random.choice( [(1,0),(0,1),(-1,0),(0,-1)] )
    return xdelta, ydelta

def rand_angle():
    """  
    Performs unit 2D random step at random angle ( 0 to 2*PI)
    Returns (x,y) co-ordinates of unit step at random angle
     """
    rand_angle = random.uniform(0,2*np.pi)
    xdelta = np.sin(rand_angle)
    ydelta = np.cos(rand_angle)
    return xdelta, ydelta

def setup_rectangle( box_loc , width, height):
    """  
    Sets shape of rectangle. Returns upper and lower corners 
    """ 
    xloc,yloc = box_loc
    low_left  = (xloc - .5 * width, yloc -.5 * height)
    top_right = (xloc + .5 * width, yloc +.5 * height)    
    return (low_left, top_right)

def setup_ellipse( ellipse_loc , axis_one, axis_two):
    """  
    Sets shape of rectangle. Returns upper and lower corners 
    """ 
    xloc,yloc = ellipse_loc
    axis = (axis_one, axis_two)
    return (ellipse_loc, axis)

def setup_square( square_loc, side):
    xloc, yloc = square_loc
    low_left  = (xloc - .5 * side, yloc -.5 * side)
    top_right = (xloc + .5 * side, yloc +.5 * side)  
    return (low_left, top_right)

def setup_circle( circle_loc, radius):
    xloc,yloc = circle_loc
    circle_radius = radius
    return (circle_loc, circle_radius) 

def check_inside_rectangle(xvalue, yvalue, box):
    """  
    Checks if point is inside a rectangle. Returns True if inside.
    False if not      
    """ 
    xmin, ymin = box[0]
    xmax, ymax = box[1]
    if xmin < xvalue < xmax  and  ymin < yvalue < ymax:
        return True
    else:
        return False

def check_inside_ellipse(xvalue, yvalue, ellipse):
    """  
    Checks if point is inside a rectangle. Returns True if inside.
    False if not      
    """ 
    xloc, yloc = ellipse[0]
    axis_one, axis_two = ellipse[1]
    half_axis_one = axis_one/2
    half_axis_two = axis_two/2
    if ((xvalue - xloc) ** 2/half_axis_one**2 + (yvalue - yloc) ** 2/half_axis_two**2) < 1:
        return True
    else:
        return False
        
def check_inside_circle(xvalue, yvalue, circle):
    xloc, yloc = circle[0]
    radius = circle[1]
    if (np.sqrt(((xvalue-xloc)**2) + ((yvalue-yloc)**2))) < radius:
        return True
    else:
        return False
    
def draw_boundary_rectangle(start_loc,boundary, graph):
    """  
    Draw boundary on graph and set size of graph (xlim,ylim)
    """
    xmin, ymin = boundary[0]
    xmax, ymax = boundary[1]
    plt.gca().add_patch(Rectangle((xmin,ymin), xmax-xmin, ymax-ymin,  fill=False, edgecolor='b',lw=4))
    plt.xlim([-graph,graph])
    plt.ylim([-graph,graph])
    plt.axvline(start_loc[0], color='grey', lw=2)
    plt.axhline(start_loc[1], color='grey', lw=2)  
    return

def draw_boundary_ellipse(start_loc,boundary, graph):
    """  
    Draw boundary on graph and set size of graph (xlim,ylim)
    """
    xloc, yloc = boundary[0]
    axis_one, axis_two = boundary[1]
    plt.gca().add_patch(Ellipse((xloc, yloc), axis_one, axis_two,  fill=False, edgecolor='b',lw=4))
    plt.xlim([-graph,graph])
    plt.ylim([-graph,graph])
    plt.axvline(start_loc[0], color='grey', lw=2)
    plt.axhline(start_loc[1], color='grey', lw=2)  
    return

def draw_boundary_circle(start_loc, circle, graph):
    """  
    Draw circle on graph and set size of graph (xlim,ylim)
    """
    xloc, yloc = circle[0]
    radius = circle[1]
    plt.gca().add_patch(Circle((xloc,yloc), radius,  fill=False, edgecolor='b',lw=4))
    plt.xlim([-graph, graph])
    plt.ylim([-graph, graph])
    plt.axvline(start_loc[0], color='grey', lw=2)
    plt.axhline(start_loc[1], color='grey', lw=2)  
    return

def draw_target(target):
    """  
    Draw target on graph 
    """
    xmin, ymin = target[0]
    xmax, ymax = target[1]
    plt.gca().add_patch(Rectangle((xmin,ymin), xmax-xmin, ymax-ymin,  fill=True, facecolor='r'))