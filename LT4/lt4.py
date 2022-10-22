#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro_sensor = GyroSensor(Port.S1) #Clockwise +, Anti -
line_sensor = ColorSensor(Port.S3)
gyro_sensor.reset_angle(0)
speed = 150
drift = speed - 20
time.sleep(1)

# Move
lspeed = speed
rspeed = speed
while (True):
    left_motor.run(lspeed)
    right_motor.run(rspeed)
    print(line_sensor.color())
    print(gyro_sensor.angle())

    if (line_sensor.color() != Color.BLUE):
        if (gyro_sensor.angle() < 0):
            lspeed = speed
            rspeed = drift
        elif (gyro_sensor.angle() > 0):
            lspeed = drift
            rspeed = speed
    else:
        if (gyro_sensor.angle() == 0):
            lspeed = speed
            rspeed = speed
