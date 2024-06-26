"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    Pre-condition:Karel is on the left side of the world,facing East
    Post-condition:Karel is on the right side of the world
    """
    up()
    cross()
    down()


def cross():
    """
     Pre-condition:Karel is facing North
     Post-condition:Karel is on the upper right,facing south
    """
    turn_right()
    move()
    turn_right()

def down():
    """
    Pre-condition:Karel is on the upper right,facing South
    Post-condition:Karel is facing South
    :return:
    """
    while front_is_clear():
        move()



def up():
    """
    Pre-condition:Karel is on the left side of the world,facing East
    Post-condition:Karel is facing North
    """
    turn_left()
    # Facing North
    while not right_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
