import crypt

def test_pass(password):
    try:
        with open("dictionary.txt","r") as dictionary:
            salt = password[0:2]
            for d in dictionary.readlines():
                strip_d = d.strip("\n")
                new_d = crypt.crypt(strip_d,salt)
                if (password == new_d):
                    return new_d
    except Exception as e:
        return
    return

def main():
    try:
        with open("passwords.txt","r") as f:
            for line in f.readlines():
                user_pass_list = line.split(":")
                #print(user_pass_list)
                user = user_pass_list[0]
                password = user_pass_list[1].strip(" ")
                print("[*] Cracking password for : ",user)
                decode_pass = test_pass(password)
                if decode_pass:
                    print("[+] Password found : ",decode_pass)
                else:
                    print("[-]Password not found.")
    except Exception as e:
        print("Error : ",str(e))

        pass


if __name__ == "__main__":
    main()