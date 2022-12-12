#!/usr/bin/env pybricks-micropython

# Import the necessary libraries
from pybricks.parameters import *
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Create the sensors and motors objects
ev3 = EV3Brick()

motorA = Motor(Port.A)
motorB = Motor(Port.B)
left_motor = motorA
right_motor = motorB

color_sensor_in1 = ColorSensor(Port.S1)


def move_tank_dc(left, right):
    left_motor.dc(left)
    right_motor.dc(right)


def move_tank(left, right):
    left_motor.run(left)
    right_motor.run(right)


def move_steer(speed, steer):
    # init l_speed and r_speed to same values
    l_speed = speed
    r_speed = speed

    gain = (threshold - abs(float(steer))) / threshold

    if steer >= 0:
        r_speed *= gain
    else:
        l_speed *= gain

    if abs(steer) < 2.0:
        # full speed
        move_tank_dc(70.0, 70.0)
    else:
        move_tank_dc(l_speed, r_speed)


# Here is where your code starts
# color values for line detection. caliberate these for ever sensor.
BLACK = 3
WHITE = 60
threshold = (BLACK + WHITE) / 2.0

# drive speed and proportional gain for turning rate
DRIVE_SPEED = 160.0
PROPORTIONAL_GAIN = 1.60


# ==================== MAIN LOOP ====================
while True:
    # Calculate the deviation from the threshold.
    deviation = threshold - color_sensor_in1.reflection()

    # Calculate the turn rate. e.g. 2.5 * 10 = 25 deg/s
    turn_rate = PROPORTIONAL_GAIN * deviation
    speed = DRIVE_SPEED

    move_steer(speed, turn_rate)

    # wait(10)
