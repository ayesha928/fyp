from lib.protocol import encode_command, decode_command
import serial
import time

ser = serial.Serial(
    port='//dev/ttyS0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)


def send_command():
     
    byte = encode_command()
    ser.open()
    txData = byte;
    ser.write(txData);
    
    time.sleep(10)

    rxData = ser.read(byte);
    rxData.decode_command()

    ser.close()

    print(rxData);



