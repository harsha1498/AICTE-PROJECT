from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label="Upload Image")
    password = forms.CharField(widget=forms.PasswordInput, label="Encryption Password")
    message = forms.CharField(widget=forms.Textarea, label="Message to Hide")

class EncryptedFileUploadForm(forms.Form):
    encrypted_file = forms.FileField(label="Upload Encrypted File (.enc)")
    password = forms.CharField(widget=forms.PasswordInput, label="Decryption Password")
