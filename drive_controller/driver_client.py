import socket
import serial

SERVER_HOST = '192.168.0.100'
SERVER_PORT = 3509


class DriverClient():
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.serial_port = serial.Serial('/dev/tty.usbserial', 9600)

        self.message = 0x0

        while 'pong' not in str(self.message):
            self.sock.send(bytes('ping', 'utf-8'))
            self.message = self.sock.recv(1024)

        print('Connected to server %s on port %s' % (host, str(port)))
        self.message = 0x0

    def update(self):
        self.message = self.sock.recv(1024)
        self.serial_port.write(self.message)

    def drive(self):
        while 'quit' not in str(self.message):
            self.update()

        self.serial_port.write(0x0)
        print('Connection closed')


def main():
    driver = DriverClient(SERVER_HOST, SERVER_PORT)
    driver.drive()


if __name__ == '__main__':
    main()
