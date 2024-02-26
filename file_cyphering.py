from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import secrets
from datetime import datetime
import json



def encrypt_data_selected():
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(key, file_path)
            os.remove(file_path)


def generate_token():
    return secrets.token_bytes(16)

def get_current_date():
    date_time = datetime.now()
    data_time_formated_timestamp = date_time.strftime("%d:%m:%Y-%H:%M")
    return data_time_formated_timestamp

def store_token(name: str, date: str, key: str):
    
    data_to_store = {"Item name":name, "Date of encoding":date, "Encoding key":key }

    with open('logs.json', 'a') as file:
        json.dump(data_to_store, file)

    return True
    

def generate_key(name: str):
    key = generate_token()
    date = get_current_date()
    
    if store_token(name=name, date=date, key=str(key)):
        return key


def encrypt_file(key, filename):
    chunk_size = 64*1024
    output_file = filename + '.enc'
    
    iv = get_random_bytes(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    
    with open(filename, 'rb') as infile, open(output_file, 'wb') as outfile:
        outfile.write(iv)
        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += b' ' * (16 - len(chunk) % 16)
            outfile.write(encryptor.encrypt(chunk))


def decryption_selected():
    print("provide encryption key: ")
    key = input()

    decrypt_file(key=key, filename=folder_path)

def decrypt_file(key, filename):
    chunk_size = 64*1024
    output_file = filename[:-4]
    
    with open(filename, 'rb') as infile, open(output_file, 'wb') as outfile:
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            outfile.write(decryptor.decrypt(chunk))

# Example usage
key = generate_key(name='test')
folder_path = 'E:/projects/File-Ciphering/test-folder'

print("Please choose action type you like to perform")

action = input("If you wana to encrypt data type 'e' otherwise type 'd'")
if action == 'e':
    encrypt_data_selected()
elif action == 'd':
    decryption_selected()




# To decrypt the files, use the decrypt_file function