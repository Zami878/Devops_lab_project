from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def encrypt_data(key, data):
    f = Fernet(key)
    return f.encrypt(data)

def decrypt_data(key, data):
    f = Fernet(key)
    return f.decrypt(data)

def load_key(file_path):
    key_file_path = file_path + "_key.txt"
    with open(key_file_path, 'rb') as keyfile:
        return keyfile.read()
