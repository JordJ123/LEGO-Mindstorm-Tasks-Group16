#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Turn
def check():

    #Left
    robot.turn(first_turn)
    robot.turn(first_turn)
    robot.turn(first_turn)
    print(ultrasonic.distance())
    if (ultrasonic.distance() > wall):
        print("LEFT")
        print(" ")
        return

    #Forward
    robot.turn(second_turn)
    robot.turn(second_turn)
    robot.turn(second_turn)
    print(ultrasonic.distance())
    if (ultrasonic.distance() > wall):
        print("FORWARD")
        print(" ")
        return

    #Right
    robot.turn(second_turn)
    robot.turn(second_turn)
    robot.turn(second_turn)
    print(ultrasonic.distance())
    if (ultrasonic.distance() > wall):
        print("RIGHT")
        print(" ")
        return

    #Back
    robot.turn(second_turn)
    robot.turn(second_turn)
    robot.turn(second_turn)
    print(ultrasonic.distance())
    if (ultrasonic.distance() > wall):
        print("BACK")
        print(" ")
        return
    
    print("ERROR!!!")
    print(" ")

# Components
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
ultrasonic = UltrasonicSensor(Port.S2)
line_sensor = ColorSensor(Port.S1)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=142)

# Values
speed = 200
white = 20
middle = 28
wall = 250
right = 30
left = - right
first_turn = 0
second_turn = 0

# while True:
#     robot.turn(left)
#     robot.turn(left)
#     robot.turn(left)
#     robot.turn(right)
#     robot.turn(right)
#     robot.turn(right)

# Hardcode
robot.drive(speed, 0)
while True:
    if (line_sensor.reflection() > white):
        robot.straight(middle)
        print(ultrasonic.distance())
        if (ultrasonic.distance() < wall):
            robot.turn(left)
            robot.turn(left)
            robot.turn(left)
            first_turn = left
            second_turn = right
        else:
            first_turn = right
            second_turn = left        
        break

# Main
while True:
    robot.drive(speed, 0)
    if (line_sensor.reflection() > white):
        robot.straight(middle)
        check()


