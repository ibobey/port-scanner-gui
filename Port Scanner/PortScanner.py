import socket
from threading import Thread

target = socket.gethostbyname(socket.gethostname())
print(target)

def portScanner(start,stop):
    try:
        for port in range(start,stop+1):
            S = socket.socket()
            val = S.connect_ex((target,port))
            socket.setdefaulttimeout(0.1)
            if (val == 0):
                print(f"{port} is OPEN!")
    except KeyboardInterrupt:
        print("Keyboard Interrupted!")

    except socket.timeout:
        print("Socket timeout error!")
    except:
        print("UNKNOWN ERROR!")


def threadStarter(start=1,stop=1000):
    for i in range(1,17):
        threadN = Thread(target=portScanner,args=(start,stop))
        #threadN.setDaemon(True)
        threadN.start()
        start += 1000
        stop += 1000

threadStarter()