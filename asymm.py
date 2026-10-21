from time import sleep
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import os
from pyfiglet import figlet_format as ff
import getpass
from cryptography.hazmat.primitives import serialization
import argparse



def enc(folder_path):
    private_key = rsa.generate_private_key(65537, 2048)
    public_key = private_key.public_key()
    with open(folder_name + ".prv_key", "wb") as f:
        f.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.BestAvailableEncryption(password)))
    for root, dirs, files in os.walk(folder_path):
        for file in files: 
            if not file.endswith(".asm"):
                path = os.path.join(root, file)
                with open(path, "rb") as f:
                    data = f.read()
                enc_data = public_key.encrypt(data, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

                with open(path + ".asm", "wb") as f:
                    f.write(enc_data)
                print(f"\033[37m[\033[33mEncrypted: \033[4:34m{path}.asm\033[0m]")

                os.remove(path)
            else:
                print(f"\033[1:34mFiles already encrypted in this folder \033[4m{folder_path}")
                os._exit(0)


def dec(folder_path):
    try:
        with open(folder_name + ".prv_key", "rb") as f:
            prv_key = serialization.load_pem_private_key(f.read(), password=password)

    
        
    
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".asm"):
                    path = os.path.join(root, file)
                    with open(path, "rb") as f:
                        enc_data = f.read()
                    dec_data = prv_key.decrypt(enc_data, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
                    new_name = path.replace(".asm", "")
                    with open(new_name, "wb") as f:
                        f.write(dec_data)
                    os.remove(path)
                    print(f"\033[37m[\033[33mDecrypted: \033[4:34m{path}\033[0m]")

                else:
                    
                    print(f"\033[1:34mFiles already decrypted in this folder \033[4m{folder_path}")
                    os._exit(0)
    except ValueError:
        print("\033[31mPassoword is not correct!")



if __name__ == "__main__":
    sleep(1)
    logo = ff("RSA ENC")
    for i in logo:
        print(f"\033[36m{i}", end="")
    inp = input("\033[1:35m1. Encrypt\n2. Decrypt\n3. Exit \n \033[1:37m/?>> ")
    if inp == "1":
        try:
        
            folder_name = input("Enter the folder path: ")
            password = getpass.getpass("Enter your password : ").encode()

            
            enc(folder_name)
        
        except Exception as e:
            print("\033[34mError: ", e)
    elif inp == "2":
        folder_name = input("Enter the folder path: ")
        password = getpass.getpass("Enter your password : ").encode()
        dec(folder_path=folder_name)
    elif inp == "3":
        print("\033[32mThanks of using our program!")
        exit(0)
    else:
        print("\033[34mInvalid option!")
