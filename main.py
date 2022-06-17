
#pin_L = DigitalPin.P13
#pin_R = DigitalPin.P14
speed = 220
connected = 0
bluetooth.start_uart_service()

def on_bluetooth_connected():
    global connected
    basic.show_icon(IconNames.HEART)
    connected = 1
    while connected == 1:
        uartData = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        console.log_value("data", uartData)
        if uartData == "0":
            PCAmotor.motor_run(PCAmotor.Motors.M1, 0)
            PCAmotor.motor_run(PCAmotor.Motors.M2, 0)
        if uartData == "A":
            PCAmotor.motor_run(PCAmotor.Motors.M1, speed*0.85)
            PCAmotor.motor_run(PCAmotor.Motors.M2, speed)
        if uartData == "B":
            PCAmotor.motor_run(PCAmotor.Motors.M1, -(0.85*(speed)))
            PCAmotor.motor_run(PCAmotor.Motors.M2, -(speed))
        if uartData == "C":
            PCAmotor.motor_run(PCAmotor.Motors.M1, 220)
            PCAmotor.motor_run(PCAmotor.Motors.M2, -220)
        if uartData == "D":
            PCAmotor.motor_run(PCAmotor.Motors.M1, -220)
            PCAmotor.motor_run(PCAmotor.Motors.M2, 220)
        if uartData == "E":
            PCAmotor.motor_run(PCAmotor.Motors.M1, 0)
            PCAmotor.motor_run(PCAmotor.Motors.M2, -220)
        if uartData == "F":
            PCAmotor.motor_run(PCAmotor.Motors.M1, -220)
            PCAmotor.motor_run(PCAmotor.Motors.M2, 0)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    connected = 0
    while connected == 0:
        right = pins.digital_read_pin(DigitalPin.P14)
        left = pins.digital_read_pin(DigitalPin.P13)
        pause(20)
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
        pause(80)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)