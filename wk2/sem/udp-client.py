import socket
import random
import sys

def main():
  if len(sys.argv) < 4:
    print('not enough args')
  else:
    (HOST, PORT) = sys.argv[2:4]
    PORT = int(PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
      while True:
        data = input("Please enter the message:\n")
        client_socket.sendto(data.encode('utf-8'), (HOST, PORT))
        message, address = client_socket.recvfrom(1024)
        print(message)


if __name__ == '__main__':
  main()