import optparse
import socket
import argparse
from threading import *


screen_lock = Semaphore(value=1)

def conn_scan(h,p):

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect((h,p))
        string = "HI i AM Amina Khatun \r\n"
        sock.send(string.encode())
        results = sock.recv(100).decode()
        screen_lock.acquire()
        print("Scanning port : ",p)
        print("[+] %d tcp open"%p)
        print("[+] ",results)
    except Exception as e:
        screen_lock.acquire()
        print("[-] %d tcp closed"%p)
    finally:
        screen_lock.release()
        sock.close()

def port_scan(h,plist):
    try:
        ip = socket.gethostbyname(h)
    except Exception as e:
        print("[-] Cannot resolve ",h," : Unknown host")
        return
    try:
        name = socket.gethostbyaddr(ip)
        print("[+] Scan result for : ",name[0])
    except Exception as e:
        print("[-] Scan result for : ",ip)
    socket.setdefaulttimeout(1)
    for p in plist:
        t = Thread(target=conn_scan,args=(h,int(p)))
        t.start()

    return

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--H', dest = "host",type=str,help = "specify target host")
    parser.add_argument('--p', dest = "ports",nargs = '+' ,type=str,help = "specify ports separated by space")
    args = parser.parse_args()
    host = args.host
    portlist = args.ports


    if (host == None) or (portlist == None):
        print(parser.print_help())
        exit(0)

    port_scan(host,portlist)


if __name__ == '__main__':
    #port_scan("127.0.0.1","21,22,80,50000")
    main()

