from tkinter import filedialog, messagebox
from tkinter.simpledialog import askstring
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import ttk
from tkinter import filedialog, messagebox


def on_drop(event):
    file_path = event.data
    print(f"File dropped: {file_path}")
    encrypt_file(file_path)


def open_and_decrypt():
    file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    if file_path:
        decrypt_file(file_path)


root = TkinterDnD.Tk()  


root.title("File Encryptor")
root.geometry("500x300")


style = ttk.Style()
style.theme_use("clam")

label = ttk.Label(root, text="Drag a file here to Encrypt", width=50, anchor="center", relief="solid", padding=10)
label.pack(padx=10, pady=10)


root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)


decrypt_button = ttk.Button(root, text="Open and Decrypt File", command=open_and_decrypt)
decrypt_button.pack(pady=20)


root.mainloop()