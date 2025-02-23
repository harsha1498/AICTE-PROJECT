# AICTE Steganography Project  

This project was developed as part of the **AICTE Internship Program**. It is a Django-based web application that enables **image steganography**—the process of hiding and retrieving encrypted messages within images using **Least Significant Bit (LSB) encoding**.

## Features  
- **Encrypt Messages in Images**: Hide a secret message inside an image securely.  
- **Decrypt Messages from Images**: Extract and decrypt messages from encrypted images.  
- **Password-Protected Encryption**: Ensures data security by using encryption before embedding messages.  
- **Django Web Interface**: Simple UI for uploading and processing images.  

## Installation  

1. **Clone the Repository**  
   ```sh
   git clone https://github.com/harsha1498/AICTE-PROJECT.git
   cd AICTE-PROJECT
   ```

2. **Set Up a Virtual Environment**  
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Migrations**  
   ```sh
   python manage.py migrate
   ```

5. **Start the Django Server**  
   ```sh
   python manage.py runserver
   ```

## Usage  

1. Open `http://127.0.0.1:8000/` in your browser.  
2. Use the **Encrypt** page to upload an image, enter a message, and encrypt it.  
3. Download the encrypted image.  
4. Use the **Decrypt** page to upload the encrypted image and enter the password to retrieve the hidden message.  

## Project Structure  

- `admin.py`: Registers models with Django Admin.  
- `apps.py`: Defines the Django application configuration.  
- `forms.py`: Contains forms for image upload and password input.  
- `models.py`: Defines the image-related models.  
- `urls.py`: Maps views to URLs.  
- `views.py`: Implements encryption, decryption, and image processing logic.  
- `tests.py`: Placeholder for unit tests.  

## Technologies Used  

- **Django** – Backend framework  
- **OpenCV** – Image processing  
- **Cryptography (Fernet)** – Message encryption  
- **HTML/CSS** – Frontend templates ## Screenshots

### Home Page
![HOME](https://github.com/user-attachments/assets/db3b6eef-2a24-4704-8770-6732ce27a36a)


### Encryption Page
![encrypt](https://github.com/user-attachments/assets/85e8f252-4956-4b77-b128-1249464f9e7a)


### Decryption Page
![decrypt](https://github.com/user-attachments/assets/4f6386ed-e294-4d19-8409-1c750ec8ec91)






## Contributing  

Contributions are welcome! Feel free to open issues or submit pull requests.  


## Contact  

For any queries, reach out at jampaniharsha6105@gmail.com.  

