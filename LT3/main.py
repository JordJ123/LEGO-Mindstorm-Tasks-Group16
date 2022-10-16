#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#Variables
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.D)
line_sensor = ColorSensor(Port.S1)
gyro_sensor = GyroSensor(Port.S3)
gyro_sensor.reset_angle(0)
speed = 300
rotation = speed / 2

for i in range(0, 10, 1):

    #Moves straight for next turn
    ev3.speaker.say("Turn " + str(i + 1) + ", Gyro Value " + str(gyro_sensor.angle()))
    left_motor.run(speed)
    right_motor.run(speed)

    #Continually looks for the white sport
    run = True
    while (run):
        if (line_sensor.color() == Color.WHITE):

            #Stops when finds white spot
            left_motor.hold()
            right_motor.hold()

            #Rotates 180 degress
            left_motor.run(rotation)
            right_motor.run(0 - rotation)
            while (gyro_sensor.angle() < (180 * (i + 1))):
                continue

            #Stops rotating
            left_motor.hold()
            right_motor.hold()
            run = False
            
ev3.speaker.say("Mission Success")


