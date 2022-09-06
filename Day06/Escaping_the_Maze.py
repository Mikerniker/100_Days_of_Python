
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def stay_right():
    while wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move() 

while not at_goal():
    if front_is_clear():
        move()
        if front_is_clear() and right_is_clear():
            turn_right()
    elif wall_in_front() and right_is_clear():
        turn_right()
    elif wall_in_front() and wall_on_right():
        turn_left()      
    elif front_is_clear() and wall_on_right():
        stay_right() 
