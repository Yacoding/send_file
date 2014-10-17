#      _   _        __   __
#     /_\ | |__ _ _ \ \ / /_ _ _ _ __ _ ___
#    / _ \| / _` | ' \ V / _` | '_/ _` / _ \
#   /_/ \_\_\__,_|_||_\_/\__,_|_| \__, \___/
#                                 |___/

import socket
import thread
import base64
import string

save_path = ''
file_name = ''

S_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S_sock.bind(('127.0.0.1', 4444))
S_sock.listen(1)

conn, addr = S_sock.accept()
file = open('file_cp.jpg', 'wb')

try :
    while 1:
        buf = conn.recv(48)
        if buf == '':
            break
        print buf
        file.write(buf)
except:
    print '1'

conn.close()