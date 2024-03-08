import socket
import random
import sys

def main():
  if len(sys.argv) < 2:
    print('not enough args')
  else:
    PORT = sys.argv[1]
    PORT = int(PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
      server_socket.bind(('', PORT))
      while True:
        message, address = server_socket.recvfrom(1024)
        server_socket.sendto(message.upper(), address)


if __name__ == '__main__':
  main()