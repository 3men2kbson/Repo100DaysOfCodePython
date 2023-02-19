#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
def turn_around():
    turn_left()
    turn_left()
    turn_left()

def advance():
    turn_left()
    while wall_on_right():
        move()
    
    turn_around()
    move()
    turn_around()
    
    while front_is_clear():
        move()
        
    turn_left()

while not at_goal():
    if front_is_clear():
        move()

    if wall_in_front():
        advance()
