import os
from tkinter import Tk, Label, Button, filedialog, messagebox, StringVar, Entry, ttk
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Dracula color scheme
BACKGROUND_COLOR = "#282a36"
TEXT_COLOR = "#f8f8f2"
BUTTON_COLOR = "#6272a4"
BUTTON_HOVER_COLOR = "#44475a"

def derive_key(password):
    salt = b'\x00' * 16  # For demo purposes; use a random salt in production
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return kdf.derive(password.encode())

def encrypt_file(input_file, output_file, password):
    key = derive_key(password)
    iv = os.urandom(16)
    
    with open(input_file, 'rb') as f:
        data = f.read()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = iv + encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(input_file, output_file, password):
    key = derive_key(password)

    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    iv = encrypted_data[:16]
    cipher_text = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(cipher_text) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    with open(output_file, 'wb') as f:
        f.write(data)

def encrypt():
    input_file = filedialog.askopenfilename(title="Select a file to encrypt", filetypes=[("Text files", "*.txt")])
    if not input_file:
        return
    password = password_var.get()
    output_file = filedialog.asksaveasfilename(title="Save encrypted file as", defaultextension=".enc", filetypes=[("Encrypted files", "*.enc")])
    if not output_file:
        return
    encrypt_file(input_file, output_file, password)
    messagebox.showinfo("Success", "File encrypted successfully!")

def decrypt():
    input_file = filedialog.askopenfilename(title="Select a file to decrypt", filetypes=[("Encrypted files", "*.enc")])
    if not input_file:
        return
    password = password_var.get()
    output_file = filedialog.asksaveasfilename(title="Save decrypted file as", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not output_file:
        return
    decrypt_file(input_file, output_file, password)
    messagebox.showinfo("Success", "File decrypted successfully!")

# Create the GUI
root = Tk()
root.title("AES-256 File Encryption/Decryption")
root.geometry("400x300")  # Fixed window size
root.configure(bg=BACKGROUND_COLOR)

# Style configuration
style = ttk.Style()
style.configure('TButton', background=BUTTON_COLOR, foreground=TEXT_COLOR, padding=10)
style.map('TButton', background=[('active', BUTTON_HOVER_COLOR)])
style.configure('TLabel', background=BACKGROUND_COLOR, foreground=TEXT_COLOR)
style.configure('TEntry', fieldbackground="#44475a", foreground=TEXT_COLOR)

password_var = StringVar()

# Centered layout
Label(root, text="Enter Password:", font=("Helvetica", 12)).pack(pady=(20, 5))
password_entry = Entry(root, textvariable=password_var, show='*', width=30)
password_entry.pack(pady=(0, 15))

Button(root, text="Encrypt File", command=encrypt, width=15).pack(pady=5)
Button(root, text="Decrypt File", command=decrypt, width=15).pack(pady=5)

root.mainloop()
