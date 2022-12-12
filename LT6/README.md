## Submission

1. Document the Hardware Design (include a picture).<br />
   Hardware used: Ultrasonic sensor, Color sensor<br />
   In this task we have used the “Ultrasonic sensor” to detect the distance from each block while the EV3 is moving towards it. A “Color sensor” is used because on the ground there is a white tape for each rectangle. Therefore, we are using the light sensor to as soon as it catches a white line to move 2-3 cm more forward and then try to scan the area by turning left, right or forwards to scan the place to see which distance is the greatest in order to continue its journey. This will make the robot move to the greatest distance not to hit the blocks.

 
2. Develop the Software Design (by either a timed automaton or a statechart).
   ![sc image](sc.png)
   
3. Develop the algorithm in pseudo-code (with clear association with elements in
   the software design).
   ```sql
   ```

4. Implement the algorithm in MicroPython (provide a well commented code
   listing). `lt6.py`

   ```python
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
   ```
