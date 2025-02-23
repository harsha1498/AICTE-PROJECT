import os
import cv2
import base64
import numpy as np

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from cryptography.fernet import Fernet
from django import forms


# Forms
class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput)
    message = forms.CharField(widget=forms.Textarea, required=False)

class EncryptedFileUploadForm(forms.Form):
    encrypted_file = forms.FileField()
    password = forms.CharField(widget=forms.PasswordInput)


# Generate encryption key
def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32).encode()[:32])


# Encrypt & decrypt messages
def encrypt_message(msg, password):
    key = generate_key(password)
    cipher = Fernet(key)
    return cipher.encrypt(msg.encode()).decode()

def decrypt_message(encrypted_msg, password):
    try:
        key = generate_key(password)
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_msg.encode()).decode()
    except:
        return "ERROR: Incorrect password or corrupted data!"


# Hide message in image using LSB
def encode_message(img, msg):
    msg += "####"  # End delimiter
    binary_msg = ''.join(format(ord(char), '08b') for char in msg)

    if len(binary_msg) > img.size * 3:
        return None  # Message too large

    data_index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                if data_index < len(binary_msg):
                    img[i, j, k] = (img[i, j, k] & 254) | int(binary_msg[data_index])
                    data_index += 1
                else:
                    return img
    return img


# Extract message from image
def decode_message(img):
    binary_data = ""
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                binary_data += str(img[i, j, k] & 1)  # Extract LSB

    extracted_text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        extracted_text += chr(int(byte, 2))
        if extracted_text[-4:] == "####":
            return extracted_text[:-4]
    return "ERROR: No hidden message found!"


# Encrypt Image View
def encrypt_image_view(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            password = form.cleaned_data['password']
            message = form.cleaned_data.get('message', 'No message provided')

            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_path = os.path.join(fs.location, filename)

            img = cv2.imread(image_path)
            if img is None:
                return HttpResponse("ERROR: Invalid image!", status=400)

            encrypted_msg = encrypt_message(message, password)
            encoded_img = encode_message(img, encrypted_msg)

            if encoded_img is not None:
                encrypted_filename = filename.split('.')[0] + ".enc.png"
                cv2.imwrite(encrypted_filename, encoded_img)

                with open(encrypted_filename, "rb") as f:
                    response = HttpResponse(f.read(), content_type="image/png")
                    response["Content-Disposition"] = f"attachment; filename={encrypted_filename}"
                    return response

    else:
        form = ImageUploadForm()

    return render(request, 'encrypt.html', {'form': form})


# Decrypt Image View
def decrypt_image_view(request):
    decrypted_message = None
    decrypted_image_url = None
    error = None

    if request.method == "POST":
        form = EncryptedFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            encrypted_file = form.cleaned_data["encrypted_file"]
            password = form.cleaned_data["password"]

            fs = FileSystemStorage()
            filename = fs.save(encrypted_file.name, encrypted_file)
            file_path = os.path.join(fs.location, filename)

            img = cv2.imread(file_path)
            if img is None:
                error = "Invalid file format! Please upload a valid encrypted image."
            else:
                extracted_msg = decode_message(img)
                decrypted_message = decrypt_message(extracted_msg, password)

                if "ERROR" in decrypted_message:
                    error = decrypted_message
                    decrypted_message = None
                else:
                    # Save decrypted image for download
                    decrypted_filename = "decrypted_" + filename.replace(".enc", ".png")
                    decrypted_image_path = os.path.join(fs.location, decrypted_filename)
                    cv2.imwrite(decrypted_image_path, img)

                    # Generate download URL
                    decrypted_image_url = fs.url(decrypted_filename)

    else:
        form = EncryptedFileUploadForm()

    return render(request, "decrypt.html", {
        "form": form,
        "decrypted_message": decrypted_message,
        "decrypted_image_url": decrypted_image_url,
        "error": error
    })



# Home Page
def home_view(request):
    return render(request, "base.html")
