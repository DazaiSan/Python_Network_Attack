#Install python-nmap not only nmap

import argparse
import nmap


def nmap_scan(h,p):
    nm_scanner = nmap.PortScanner()
    nm_scanner.scan(h,p)

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

    for p in portlist:
        nmap_scan(host,int(p))

if __name__ == "__main__":
    nmap_scan("127.0.0.1",21)