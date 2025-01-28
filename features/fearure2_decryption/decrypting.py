import keys
from tkinter import  messagebox



def decrypt_file(file_path):
    key = keys.load_key(file_path)
    if key is None:
        return
    
    with open(file_path, 'rb') as encoded_file:
        encrypted_data = encoded_file.read()

    try:
        decrypted_data = keys.decrypt_data(key, encrypted_data)

        with open(file_path, 'wb') as decoded_file:
            decoded_file.write(decrypted_data)

        messagebox.showinfo("Success", f"File decrypted successfully! The file has been updated.")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")
