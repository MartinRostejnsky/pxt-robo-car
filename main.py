
# #speedFactor = 80
# #pin_L = DigitalPin.P13
# #pin_R = DigitalPin.P14
# #pin_Trig = DigitalPin.P8
# #pin_Echo = DigitalPin.P15
# line_tracking = 0
# speed = 220
# connected = 0
# bluetooth.start_uart_service()

# def picovinanefukncni():
#     global line_tracking
#     while line_tracking == 1:
#         print(line_tracking)
#         left = pins.digital_read_pin(DigitalPin.P13)
#         right = pins.digital_read_pin(DigitalPin.P14)
#         pause(400)
#         if left == right:
#             PCAmotor.motor_run(PCAmotor.Motors.M1, 140)
#             PCAmotor.motor_run(PCAmotor.Motors.M2, 140)
#         elif left == 1:
#             PCAmotor.motor_run(PCAmotor.Motors.M1, 140)
#             PCAmotor.motor_run(PCAmotor.Motors.M2, 0)
#         elif right == 1:
#             PCAmotor.motor_run(PCAmotor.Motors.M2, 140)
#             PCAmotor.motor_run(PCAmotor.Motors.M1, 0)


# def on_bluetooth_connected():
#     global connected, line_tracking
#     basic.show_icon(IconNames.HEART)
#     connected = 1
#     while connected == 1 and line_tracking == 0:
#         uartData = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
#         console.log_value("data", uartData)
#         if uartData == "0":
#             PCAmotor.motor_run(PCAmotor.Motors.M1, 0)
#             PCAmotor.motor_run(PCAmotor.Motors.M2, 0)
#         if uartData == "S":
#             line_tracking = 1
#             picovinanefukncni()
#         if uartData == "A":
#             PCAmotor.motor_run(PCAmotor.Motors.M1, speed*0.85)
#             PCAmotor.motor_run(PCAmotor.Motors.M2, speed)
#         if uartData == "B":
#             PCAmotor.motor_run(PCAmotor.Motors.M1, -(0.85*(speed)))
#             PCAmotor.motor_run(PCAmotor.Motors.M2, -(speed))
#         if uartData == "C":
#             PCAmotor.motor_run(PCAmotor.Motors.M1, 220)
#             PCAmotor.motor_run(PCAmotor.Motors.M2, 0)
#         if uartData == "D":
#             PCAmotor.motor_run(PCAmotor.Motors.M1, 0)
#             PCAmotor.motor_run(PCAmotor.Motors.M2, 220)
#         if uartData == "E":
#             PCAmotor.motor_run(PCAmotor.Motors.M1, 0)
#             PCAmotor.motor_run(PCAmotor.Motors.M2, -220)
#         if uartData == "F":
#             PCAmotor.motor_run(PCAmotor.Motors.M1, -220)
#             PCAmotor.motor_run(PCAmotor.Motors.M2, 0)
# bluetooth.on_bluetooth_connected(on_bluetooth_connected)

# def on_bluetooth_disconnected():
#     global connected
#     basic.show_icon(IconNames.SAD)
#     connected = 0
# bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

# # def on_forever():
# #     obstacle_distance = sonar.ping(pin_Trig, pin_Echo, PingUnit.CENTIMETERS, 100)

# #     l = False if (whiteline ^ pins.digital_read_pin(pin_L)) == 0 else True
# #     r = False if (whiteline ^ pins.digital_read_pin(pin_R)) == 0 else True

# #     # TO DO ...

# #     basic.pause(50) #reakční frekvence 20 Hz
# # basic.forever(on_forever)

def on_forever():
    right = pins.digital_read_pin(DigitalPin.P14)
    left = pins.digital_read_pin(DigitalPin.P13)
    pause(10)
    if left == 0 and right == 0:
        PCAmotor.motor_run(PCAmotor.Motors.M1, -200)
        PCAmotor.motor_run(PCAmotor.Motors.M4, 200)
    elif right == 1:
        PCAmotor.motor_run(PCAmotor.Motors.M1, 0)
        PCAmotor.motor_run(PCAmotor.Motors.M4, 200)
    elif left == 1:
        PCAmotor.motor_run(PCAmotor.Motors.M1, -200)
        PCAmotor.motor_run(PCAmotor.Motors.M4, 0)
    if left == 1 and right == 1:
        PCAmotor.motor_run(PCAmotor.Motors.M1, 0)
        PCAmotor.motor_run(PCAmotor.Motors.M4, 0)

    pause(100)
    PCAmotor.motor_run(PCAmotor.Motors.M1, 0)
    PCAmotor.motor_run(PCAmotor.Motors.M4, 0)
    pause(10)
basic.forever(on_forever)


