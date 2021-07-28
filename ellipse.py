from randwalk2d_module import rand_angle, check_inside_ellipse, check_inside_rectangle

def random_walk_target_ellipse(max_steps,start_loc, boundary,target):
    """  Performs a random walk inside a boundary with target """
    #  Start point for walk
    xpos, ypos = start_loc
    xwalk = [xpos]
    ywalk = [ypos]
    steps_taken = 0
    was_target_hit = False 

    while steps_taken < max_steps :

        xdelta, ydelta = rand_angle()
        xtrial = xpos + xdelta
        ytrial = ypos + ydelta

        if check_inside_rectangle(xtrial, ytrial, target) is True:
            xpos = xtrial
            ypos = ytrial
            xwalk.append(xpos)
            ywalk.append(ypos)
            steps_taken += 1
            was_target_hit = True
            break

        if check_inside_ellipse(xtrial, ytrial,boundary) is True:
            xpos = xtrial
            ypos = ytrial
            xwalk.append(xpos)
            ywalk.append(ypos)
            steps_taken += 1 
    return xwalk,ywalk,steps_taken, was_target_hit