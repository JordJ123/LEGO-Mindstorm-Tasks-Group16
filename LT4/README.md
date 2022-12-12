# Lab task 4 : Line-with-gaps follower

![task image](task4_img.png)

The broken line track will respect the following rules:

- Gaps will only occur on straight parts of the line

- Gaps may vary in length, but will be limited to a maximum of 30cm;

- You may again modify the hardware design, and use any sensors to solve this
  task.

## Submission

1. Document the Hardware Design (include a picture). TBD
2. Develop the Software Design (by either a timed automaton or a statechart).
   ![ta image](ta.png)
3. Develop the algorithm in pseudo-code (with clear association with elements in
   the software design).

   ```sql
   BEGIN
   	CHECK color

   	::x:: <- WHILE (color IS white)
   		GO straght
   	TURN left
   	CHECK color
   	IF (color IS white)
   		GOTO x

   	TURN 180
   	IF (color IS white)
   		GOTO x
   END
   ```

4. Implement the algorithm in MicroPython (provide a well commented code
   listing). `new.py`

   ```python
   #!/usr/bin/env pybricks-micropython
   from pybricks.hubs import EV3Brick
   from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
   								 InfraredSensor, UltrasonicSensor, GyroSensor)
   from pybricks.parameters import Port, Stop, Direction, Button, Color
   from pybricks.tools import wait, StopWatch, DataLog
   from pybricks.robotics import DriveBase
   from pybricks.media.ev3dev import SoundFile, ImageFile
   import math

   def straight():
   	deviation = line_sensor.reflection() - threshold
   	turn_rate = proportional_gain * deviation
   	robot.drive(speed, turn_rate)
   	wait(10)

   def dash():
   	left_motor.reset_angle(0)
   	robot.drive(dashSpeed, 0)
   	while(True):
   		if (left_motor.angle() > dashDistance):
   			robot.stop()
   			break

   def rotate():
   	#Turn Left
   	for i in range(0,9):
   		robot.turn(-10)
   		print(i)
   		if (line_sensor.reflection() > black):
   			robot.turn(-15)
   			return
   	robot.turn(90)

   	#Turn Right
   	for i in range(0,9):
   		robot.turn(10)
   		print(i)
   		if (line_sensor.reflection() > black):
   			robot.turn(15)
   			return
   	robot.turn(-90)

   	#Drive until white line or 30cm
   	for i in range(0,6):
   		robot.straight(50)
   		if (line_sensor.reflection() > black):
   			break
   	robot.stop()


   #Variables
   left_motor = Motor(Port.B)
   right_motor = Motor(Port.C)
   line_sensor = ColorSensor(Port.S4)
   robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
   speed = 200
   turn = speed / 2
   dashSpeed = speed / 2
   dashDistance = 63
   black = 15
   white = 76
   threshold = (black + white) / 2
   proportional_gain = 1.4

   while True:
   	while (line_sensor.reflection() > black):
   		straight()
   	if (line_sensor.reflection() <= black):
   		robot.stop()
   		dash()
   		rotate()
   ```
