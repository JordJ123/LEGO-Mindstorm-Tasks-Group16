#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Wall
def wallMove():
    deviation = wall - ultrasonic.distance()
    # if (deviation > devMax):
    #     deviation = devMax
    # elif (deviation < 0 - devMax):
    #     deviation = 0 - devMax
    turn_rate = proportional_gain * deviation
    if (turn_rate > devMax):
        turn_rate = devMax
    elif (turn_rate < 0 - devMax):
        turn_rate = 0 - devMax
    robot.drive(speed * abs(devMax - turn_rate) /10, turn_rate)
    print(turn_rate)

# Components
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
ultrasonic = UltrasonicSensor(Port.S2)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=121)

# Values
speed = 50
wall = 125
proportional_gain = 0.1
devMax = 100

# Main
while True:
    wallMove()


