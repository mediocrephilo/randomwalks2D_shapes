from randwalk2d_module import rand_angle, check_inside_circle, check_inside_rectangle

def random_walk_target_circle(max_steps, start_loc, circle, target):
    """ Function conducts 2D random walk inside a box """
#    Start point for walk
    xpos = start_loc[0]
    ypos = start_loc[1]
    xwalk = [xpos]
    ywalk = [ypos]
    steps_taken = 0 
    was_target_hit = False
    while steps_taken < max_steps :
        # Create trial move
        xdelta, ydelta = rand_angle()
        xtrial = xpos + xdelta
        ytrial = ypos + ydelta
        if check_inside_rectangle(xtrial, ytrial, target):
            xpos = xtrial
            ypos = ytrial
            xwalk.append(xpos)
            ywalk.append(ypos)
            steps_taken += 1 
            was_target_hit = True
            break
        # Check if trial move is inside boundary. If so, accept it
        if check_inside_circle(xtrial, ytrial, circle) :
            xpos = xtrial
            ypos = ytrial
            xwalk.append(xpos)
            ywalk.append(ypos)
            steps_taken += 1  
    return xwalk,ywalk,steps_taken, was_target_hit