import socket
import sys
import os


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
    print("Banner :",banner)
    f = open(file_name, 'r')
    fout = open("output.txt","w")
    for line in f.readlines():
        if line.strip('\n') in banner:
            #print( '[+] Server is vulnerable: ' +banner.strip('\n'))
            fout.write('[+] Server is vulnerable: ' +banner.strip('\n'))
    f.close()
    fout.close()

    '''
    try:
        with open(file_name,"r") as f:
            for line in f.readlines():
                new_line = line.strip("\n")
                print(new_line)
                if new_line in banner:
                    print("[+] Server is vulnearble.....")
                    break
    except Exception as e:
        print("Error : ",str(e))
        return

    return'''


def main(file_name):
    ip_ext = ".0.0.1"
    port_list = [21,22,25,80,110,443]
    #file_name = "vuln_banners.txt"


    for i in range(120,130,1):
        host = str(i) + ip_ext
        for port in port_list:
            print("[+] Checking ",host," : ",port)
            banner = ret_banner(host,port)
            if (banner):
                print(banner)
                check_vul(banner,file_name)
#check_vul("220 FreeFloat Ftp Server (Version 1.00)","vuln_banners.txt")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        if not os.path.isfile(file_name):
            print(file_name," does not exist...")
            exit(0)
        elif not os.access(file_name,os.R_OK):
            print("Permission denied.")
        else :
            main(file_name)
    else:
        print("[-] Usage :",str(sys.argv[0]," <vuln filename"))



