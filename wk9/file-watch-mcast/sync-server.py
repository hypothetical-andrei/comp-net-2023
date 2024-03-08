import socketserver
import inotify.adapters
import threading
import socket

SOURCE_DIRECTORY = './temp'

def file_watch(directory):
    i = inotify.adapters.Inotify()
    i.add_watch(directory)
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        # print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(path, filename, type_names))
        if (len(filename) == 1 and len(type_names) == 1 and type_names[0] == 'IN_CLOSE_WRITE'):
            send_multicast(filename[0])

def send_multicast(filename):
    MCAST_GROUP = '224.0.0.1'
    MCAST_PORT = 5001
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    sock.sendto(filename.encode('utf-8'), (MCAST_GROUP, MCAST_PORT))

class SyncTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print('sending ', self.data.decode())
        with open('./temp/' + self.data.decode(), 'rb') as f:
            self.request.sendall(f.read())

def _main():
    HOST, PORT = "localhost", 12345
    watch_thread = threading.Thread(target=file_watch, args=(SOURCE_DIRECTORY,))
    watch_thread.start()
    # watch_thread.join()
    with socketserver.TCPServer((HOST, PORT), SyncTCPHandler) as server:
        server.serve_forever()

if __name__ == '__main__':
    _main()