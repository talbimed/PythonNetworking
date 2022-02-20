
import socket 



sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "192.168.1.1"

port =53

def portscanner(port):
    
    if (sock.connect_ex((host,port))):
        print "port %d is colose" %port
    else:
        print "port %d is open" % port
        


portscanner(port)






