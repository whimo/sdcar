import socket

HOST = '0.0.0.0'
PORT = 3509


class DriverServer(object):
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))

        self.connection = None

    def accept_connection(self):
        self.sock.listen(1)
        conn, addr = self.sock.accept()

        print('Client connected on %s, waiting for confirmation' % str(addr))

        resp = ''
        while 'ping' not in resp:
            resp, addr = conn.recvfrom(1024)

        conn.sendto(bytes('pong', 'utf-8'), addr)
        print('Client confirmed on %s, ready to drive' % str(addr))

        self.connection = conn


def main():
    driver = DriverServer(HOST, PORT)
    driver.accept_connection()

if __name__ == '__main__':
    main()
