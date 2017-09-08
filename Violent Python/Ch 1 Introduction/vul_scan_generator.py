'''This code was written using generator
to show how generator could be used.'''

import socket
import sys


def ret_banner(host,port):

    try:
        #code
        socket.setdefaulttimeout(2)
        sock = socket.socket()
        sock.connect((host,port))
        banner = sock.recv(1024).decode()
        sock.close()

        return banner

    except Exception as e:
        return

    return

def vul_ban_list_generator(file_name):
    try:
        with open("vuln_banners.txt","r") as f:
            for line in f.readlines():
                n_line = line.strip('\n')
                yield n_line
    except:
        return None
    return


def check_vul(banner,file_name):

    vul_ban_list = vul_ban_list_generator(file_name)

    for v in vul_ban_list:
        if v in banner:
            print("[+]Server is vulnerable......")
    return


def main(file_name = "vuln_banners.txt"):
    ip_ext = ".0.0.1"
    port_list = [21,22,25,80,110,443]
    #file_name = "vuln_banners.txt"


    for i in range(120,130,1):
        host = str(i) + ip_ext
        for port in port_list:
            #print("[+] Checking "+host+" : "+str(port)+"\n")
            banner = ret_banner(host,port)
            if (banner):
                print("[+] Checking "+host+" : "+str(port)+"\n")
                print("Found : " ,banner)
                check_vul(banner,file_name)


if __name__ == "__main__":
    main()
    '''if len(sys.argv) == 2:

        main(sys.argv[1])
    else:
        print("[-] Usage :",str(sys.argv[0]," <vuln filename"))'''



