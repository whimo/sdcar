import socket
import time

HOST = '0.0.0.0'
PORT = 3509


class DriverServer(object):
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))

        self.connection = None
        self.conn_address = None

    def accept_connection(self):
        self.sock.listen(1)
        conn, addr = self.sock.accept()

        print('Client connected on %s, waiting for confirmation' % str(addr))

        resp = ''

        while 'ping' not in resp:
            resp, temp = conn.recvfrom(1024)

        print addr

        conn.sendto('pong', addr)
        print('Client confirmed on %s, ready to drive' % str(addr))

        self.connection = conn
        self.conn_address = addr

    def turn(self, direction):
        self.connection.sendto(str(direction), self.conn_address)

    def stop(self):
        self.connection.sendto('quit', self.conn_address)

    def close_conn(self):
        self.connection.close()


def main():
    driver = DriverServer(HOST, PORT)
    driver.accept_connection()

    while True:
        direction = int(input())

        if direction == 8:
            driver.stop()
            time.sleep(2)
            driver.close_conn()
            break

        driver.turn(direction)


if __name__ == '__main__':
    main()
