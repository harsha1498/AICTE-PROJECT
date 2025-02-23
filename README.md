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
![Home Page]
(https://github.com/user-attachments/assets/c037186f-e420-49bf-83a3-09317a1360c0)


### Encryption Page
![Encryption Page]
(https://github.com/user-attachments/assets/1b0412c9-c686-4b8d-a512-c1b3814ce4de)

### Decryption Page
![Decryption Page]
(https://github.com/user-attachments/assets/daa38a56-f0b6-407e-8dc4-9e0e860f6cf7)





## Contributing  

Contributions are welcome! Feel free to open issues or submit pull requests.  


## Contact  

For any queries, reach out at jampaniharsha6105@gmail.com.  

