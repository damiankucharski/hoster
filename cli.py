import random
import socket
import sys
import time
import select

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)
random.seed()

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((ip, port))
s.setblocking(0)
print("Do Ctrl+c to exit the program !!")
tmstart=time.time()
lost=0
for i in range(1, 1000):
    #store current time
    t1=str(time.time());
    s.sendto(t1.encode('utf-8'), (ip, port))
    ready = select.select([s], [], [], 5)
    if ready[0]:
        data, address = s.recvfrom(4096)
        diff=time.time()-float(data.decode('utf-8'))
        print("Response time {:.9f}".format(diff))
    else:
        lost+=1
        print("Packet lost {:d}".format(lost))
    rnd=abs(random.gauss(0.01,0.1))
    time.sleep(rnd)
    
s.close()
#print(time.time()-tmstart)
