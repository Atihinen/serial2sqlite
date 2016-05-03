__author__ = 'jjauhiainen'
import serial
import time
import traceback
class SerialDataAdapter(object):
    port = None
    baudrate = None
    serial_connection = None

    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate

    def open_connection(self, retry_times=3, timeout=1):
        if self.check_connection_status():
            return False
        else:
            for i in range(retry_times):
                try:
                    self.serial_connection = serial.Serial(self.port, self.baudrate)
                    return True
                except serial.SerialException:
                    time.sleep(timeout)
            msg = "Could not open connection to {} with baudrate {} after trying {} times. Check debug level message."
            raise serial.SerialException(msg.format(self.port, self.baudrate, retry_times))

    def check_connection_status(self):
        try:
            return self.serial_connection.isOpen()
        except (AttributeError, serial.SerialException) as e:
            return False

    def read_int(self):
        value = self.serial_connection.readline()
        try:
            return int(value)
        except:
            raise ValueError("Could not read integer value")

    def disconnect(self):
        try:
            if self.serial_connection.isOpen():
                self.serial_connection.close()
                self.serial_connection = None
        except:
            pass
