from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import secrets
from datetime import datetime
import json
import base64



class EncryptFiles():

    def encrypt_data_selected(self):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.encrypt_file(key, file_path)
                os.remove(file_path)


    def generate_token(self):
        return secrets.token_bytes(16)

    def get_current_date(self):
        date_time = datetime.now()
        data_time_formated_timestamp = date_time.strftime("%d:%m:%Y-%H:%M")
        return data_time_formated_timestamp

    def store_token(self, name: str, date: str, key: str):
        key_str = base64.b64encode(key).decode('utf-8')
        
        data_to_store = {"Item name":name, "Date of encoding":date, "Encoding key":key_str },

        with open('logs.json', 'r') as file:
            archied_data = json.load(file)

        if type(archied_data) != list :
            archied_data = [archied_data]

        archied_data.append(data_to_store)

        with open('logs.json', 'w') as file:
            json.dump(archied_data, file)

        return True
        

    def generate_key(self, name: str):
        key = self.generate_token()
        date = self.get_current_date()
        
        if self.store_token(name=name, date=date, key=key):
            return key


    def encrypt_file( self, key, filename):
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


    def decryption_selected(self):
        print("provide encryption key: ")
        key = input()
        
        key = base64.b64decode(key.encode('utf-8'))
        print(key)
        
        
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.decrypt_file(key=key, filename=file_path)
                os.remove(file_path)

        

    def decrypt_file(self, key, filename):
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

folder_path = 'E:/projects/File-Ciphering/test-folder'
encryption = EncryptFiles()

print("Please choose action type you like to perform")

action = input("If you wana to encrypt data type 'e' otherwise type 'd': ")
if action == 'e':
    print("encrypt")
    key = encryption.generate_key(name='test')
    encryption.encrypt_data_selected()
elif action == 'd':
    print("decrypt")
    encryption.decryption_selected()




# To decrypt the files, use the decrypt_file function