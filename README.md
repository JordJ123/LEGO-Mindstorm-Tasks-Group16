# Task 1: Analysing Sensors

1. **Document values with the different**

_Light sensor on blue carpet_

| Distance (mm) | Value 1 | Value 2 | Value 3 | Value 4 | Value 5 | Value 6 | Value 7 | Mean     | Std. Deviation |
| ------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- | -------------- |
| 5             | 100     | 100     | 100     | 100     | 100     | 100     | 100     | 100      | 0              |
| 25            | 32      | 27      | 26      | 27      | 25      | 29      | 26      | 27.42857 | 2.194613       |
| 50            | 5       | 8       | 7       | 7       | 7       | 7       | 6       | 6.714286 | 0.880631       |
| 100           | 1       | 2       | 1       | 2       | 2       | 1       | 1       | 1.428571 | 0.494872       |

_Light sensor on white line_

| Distance (mm) | Value 1 | Value 2 | Value 3 | Value 4 | Value 5 | Value 6 | Value 7 | Mean     | Std. Deviation |
| ------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- | -------------- |
| 5             | 14      | 16      | 15      | 16      | 13      | 12      | 14      | 14.28571 | 1.385051       |
| 25            | 4       | 4       | 4       | 4       | 4       | 4       | 4       | 4        | 0              |
| 50            | 0       | 1       | 0       | 1       | 0       | 1       | 0       | 0.428571 | 0.494872       |
| 100           | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0        | 0              |

_Ultrasonic sensor_

| Distance (mm) | Value 1 | Value 2 | Value 3 | Value 4 | Value 5 | Value 6 | Value 7 | Mean     | Std. Deviation |
| ------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- | -------------- |
| 5             | 2550    | 2550    | 2550    | 2550    | 2550    | 2550    | 2550    | 2550     | 0              |
| 25            | 32      | 32      | 32      | 32      | 32      | 32      | 32      | 32       | 0              |
| 50            | 55      | 51      | 50      | 50      | 50      | 51      | 51      | 51.14286 | 1.641304       |
| 100           | 101     | 107     | 103     | 103     | 103     | 101     | 107     | 103.5714 | 2.321154       |
| 250           | 250     | 251     | 251     | 251     | 251     | 251     | 251     | 250.8571 | 0.349927       |
| infinity      | 2550    | 2550    | 2550    | 2550    | 2550    | 2550    | 2550    | 2550     | 0              |

_Gyroscopic sensor_

| Angle (degrees) | Value 1 | Value 2 | Value 3 | Value 4 | Value 5 | Value 6 | Value 7 | Mean     | Std. Deviation |
| --------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- | -------------- |
| 90              | 90      | 89      | 95      | 91      | 90      | 83      | 90      | 89.71429 | 3.282607       |
| 180             | 187     | 185     | 183     | 169     | 184     | 184     | 183     | 182.1429 | 5.51436        |
| 270             | 274     | 270     | 272     | 264     | 264     | 251     | 261     | 265.1429 | 7.259055       |
| 360             | 333     | 334     | 345     | 347     | 345     | 353     | 365     | 346      | 10.18402       |
| 720             | 710     | 717     | 713     | 693     | 697     | 716     | 706     | 707.4286 | 8.633111       |
| 1080            | 1045    | 1060    | 1068    | 1044    | 1043    | 1029    | 1044    | 1047.571 | 11.7699        |

2. **Discuss the reliability of the sensors based on your findings.**

All sensors appear to work as intended. Most of these sensors appear to be
consistent with their recorded values and close to the intended value. Only
exception is the gyroscopic sensor, which had varying readings from one sensor
to another. This makes the gyroscopic sensor not suitable for most of the tasks
in lab due to it's inconsistency.

Another notably issue is that the ultrasonic sensor doesn't seem to pick up
objects where they are incredibly close. Anywhere between 5mm and 24mm this
thresehold is found. This is evident when it produces the value of the distance
between and the object in front at the max distance value it can measure, though
this drops back to a more excepted value at 25mm.

The colour sensor doesn't also seem to be perfect at short distances. Though its
measurements seem to be fine on the white line, likely due to its reflectivey,
the colour sensor doesn't seem to pick up the carpet very well, showing a max
value for 5mm, but dropping back to something more expected at 25mm.

# Task 2: Testing Motors

1.**Document values from the experiments.** (4 in total):

Repeat each experiment 7 times. Record values in a spreadsheet and compute mean
and standard deviation of the recorded values.

_Straight line_

| Speed        | Value 1(cm) | Value 2(cm) | Value 3(cm) | Value 4(cm) | Value 5(cm) | value 6(cm) | Value 7(cm) | Mean     | Std. Deviation |
| ------------ | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | -------- | -------------- |
| slow (60)    | 135         | 82          | 293         | 74          | 164         | 34          | 128         | 130      | 77.83683       |
| medium (120) | 34          | 125         | 114         | 140         | 37          | 73          | 215         | 105.4286 | 59.15321       |
| fast (240)   | 50          | 60          | 162         | 30          | 60          | 56          | 41          | 65.57143 | 40.6443        |

2. **Discuss the reliability of the motors based on your findings.**

# Task 3: Spot Finding

1. **Document selection of sensors) with justification.**

2. **Provide a picture of the driving base with the selected sensor(s).**
   ![image of the driving base with selected sensor](images/task3.jpeg)

3. **Document the algorithmic idea.**

4. **Document the algorithm in pseudo-code.**

5. **Provide well-commented MicroPython source code of the implementation.**
