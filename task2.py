from tkinter import Tk, filedialog, Button, Label
from PIL import Image, ImageTk
import numpy as np

def encrypt_image(image_path, key=50):
    image = Image.open(image_path)
    img_array = np.array(image)
    encrypted_array = (img_array + key) % 256  # Simple encryption by adding a key
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save("encrypted.png")
    return "encrypted.png"

def decrypt_image(image_path, key=50):
    image = Image.open(image_path)
    img_array = np.array(image)
    decrypted_array = (img_array - key) % 256  # Reverse operation for decryption
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save("decrypted.png")
    return "decrypted.png"

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        encrypted_path = encrypt_image(file_path)
        show_image(encrypted_path)

def decrypt_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        decrypted_path = decrypt_image(file_path)
        show_image(decrypted_path)

def show_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((300, 300))
    img_display = ImageTk.PhotoImage(image)
    img_label.config(image=img_display)
    img_label.image = img_display

# GUI Setup
root = Tk()
root.title("Image Encryption Tool")
root.geometry("400x450")

img_label = Label(root)
img_label.pack()

btn_encrypt = Button(root, text="Encrypt Image", command=open_file)
btn_encrypt.pack(pady=10)

btn_decrypt = Button(root, text="Decrypt Image", command=decrypt_file)
btn_decrypt.pack(pady=10)

root.mainloop()
