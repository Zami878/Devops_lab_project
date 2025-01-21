import keys
from tkinter import  messagebox
import os


def encrypt_file(file_path):
    
    if not os.path.isfile(file_path):
        messagebox.showerror("Error", f"{file_path} is not a valid file.")
        return

    key = keys.generate_key()

    key_file_path = file_path + "_key.txt"
    with open(key_file_path, 'wb') as keyfile:
        keyfile.write(key)

    try:
        with open(file_path, 'rb') as file:  
            original_file = file.read()

        encrypted_file = keys.encrypt_data(key, original_file)

        with open(file_path, 'wb') as encoded_file:  # Writing encrypted file back
            encoded_file.write(encrypted_file)

        messagebox.showinfo("Success", f"File encrypted successfully! The original file has been updated.\nKey saved as {key_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error while encrypting: {e}")
