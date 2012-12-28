from protocol import encode_command, decode_command
import serial
import time


def send_command(command_type, status, section_number, device_number):
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=2400)
    byte = encode_command(command_type, status, section_number, device_number)
    #ser.open()
    ser.write(byte)
    time.sleep(1)
    rb = ser.read()
    result = decode_command(rb)
    ser.close()

    return result
