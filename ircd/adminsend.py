import socket, sys
if not hasattr(socket,'AF_UNIX'):
    print ('lol windows')
else:
    s = socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM)
    s.sendto(' '.join(sys.argv[1:]), 'admin.sock')
