import zipfile
import shutil
import os

def check_pass(z,passwd):
    try:
        z.extractall(pwd=bytes(passwd.encode()))
        return True
    except Exception as e:
        #print("Error : ",str(e))
        return False

def main():
    file_name = "evil.zip"
    if zipfile.is_zipfile(file_name):
        z = zipfile.ZipFile(file_name)
        file_name = "dictionary.txt"
        '''with open(file_name,"r") as f1:
            for line in f1:
                password = line.strip("\n")
                #print(password)
                is_password = check_pass(z,password)
                if is_password:
                    print("Password found : ",password)'''
        f = open(file_name,"r")
        password_list = [line.strip("\n") for line in f]
        f = lambda x: check_pass(z,x)
        result = list(map(f,password_list))
        try:
            ix = result.index(True)
            print("Password found : ",password_list[ix])
        except:
            print("Password not found.")

        #shutil.rmtree("evil")
    else:
        print("Not a zipfile.")
        return




if __name__ == '__main__':
    main()
