#      _   _        __   __
#     /_\ | |__ _ _ \ \ / /_ _ _ _ __ _ ___
#    / _ \| / _` | ' \ V / _` | '_/ _` / _ \
#   /_/ \_\_\__,_|_||_\_/\__,_|_| \__, \___/
#                                 |___/

import socket
import base64

save_path = ''
file_name = ''

C_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_sock.connect(('127.0.0.1', 4444))

file = open('file.jpg', 'rb')

try:
    while 1:
        buf = file.read(4)
        if buf == '':
            break
        print buf
        C_sock.send(buf)
except:
    print '1'

C_sock.close()