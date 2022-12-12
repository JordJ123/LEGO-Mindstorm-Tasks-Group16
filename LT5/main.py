#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#Straight Method
def straight():
    # ang_vel = (abs(gyro.speed())) + 1
    # print(ang_vel)
    deviation = line_sensor.reflection() - threshold 
    newSpeed = speed
    turn_rate = proportional_gain * deviation    
    # if (ang_vel > 200):
    #     newSpeed = speed / ang_vel
    #     turn_rate = turn_rate * (ang_vel/10)
    robot.drive(newSpeed, turn_rate)
    wait(10)

# Variables
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
line_sensor = ColorSensor(Port.S4)
gyro = GyroSensor(Port.S1)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
speed = 200

# caliberate before each session
black = 5
white = 55
threshold = (black + white) / 2
# threshold = 20
# turn_increase = 2

# Controls turn radius (value↓️ radius )
proportional_gain = 1.2

# Main
while True:
    straight()