from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput)
    message = forms.CharField(widget=forms.Textarea, required=False)
