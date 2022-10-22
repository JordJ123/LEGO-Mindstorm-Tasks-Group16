# CSC368/CSCM68 Embedded System Design – Lab Task 3

**Task 1: Justification of sensor choice**  
One sensor we used is the colour sensor. The purpose of the sensor is to detect
when the colour changes from the current floor colour to white so it knows that
it has reached the white spot and needs to change directions.

Another sensor we used is the gyro sensor. The purpose of this sensor is to know
when the driving base has turned exactly 180 degrees before moving again because
once it reaches the white spot, it needs to go in the reverse direction.

**Task 2: Picture of setup**  
![image](./task_3.jpeg)

**Task 3: Idea behind the setup**  
The algorithmic idea is that the driving base is intended to go straight and
while it is going straight it should continually check if the colour sensor has
picked up the white spot. Once it reaches the white spot, the driving base needs
to stop and continually rotate until the gyro sensor picks up the next
occurrence of 180 degrees from the gyro sensor so it is able to go in the
reverse of the direction it was originally going. It needs to complete all of
these steps 10 times.

**Task 4: Pseudocode**

```pseudocode
ev3 = new EV3Brick()
leftMotor = new Motor(Port.B)
rightMotor = new Motor(Port.B)
lineSensor = new ColorSensor(Port.S1)
gyroSender = new GyroSensor(Port.S3)
speed = 300 rotatation = speed / 2

for i=0 to 9
    leftMotor.run(speed)
    rightMotor.run(speed)

    while true
        if lineSensor.color == Color.WHITE then
            leftMotor.hold()
            rightMotor.hold()
            leftMotor.run(rotation)
            rightMoto.run(0 – rotation)
            while gyroSensor.angle() < (180 * (i + 1))
                continue
            endwhile
			leftMotor.hold()
            rightMotor.hold()
            BREAK
		endif
	endwhile
next i

```

**Task 5: Well commented code**

```python
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
```
