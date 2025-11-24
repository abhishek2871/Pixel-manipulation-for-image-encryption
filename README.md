# Pixel-manipulation-for-image-encryption
A Python GUI tool built with Tkinter and Pillow for encrypting and decrypting images using pixel-level XOR manipulation. Users can apply a custom numeric key to secure or restore images, making it a simple yet powerful demonstration of visual cryptography.

---

## 🧭 Overview

The Pixel-Based Image Encryption Tool provides a practical demonstration of cryptography and image processing.
It allows users to load an image, apply a numeric key for encryption or decryption, and visualize the results side by side — all through an intuitive Tkinter interface.

This project helps beginners understand how XOR-based encryption works and how pixel values can be transformed to secure visual data.

---

## **⚙️ How the Encryption Works**

The tool uses the XOR (exclusive OR) operation on each pixel’s RGB values with a user-provided numeric key.

Encryption Logic:

Encrypted Pixel = Original Pixel ⊕ Key


Decryption Logic:

Decrypted Pixel = Encrypted Pixel ⊕ Key


Since XOR is a reversible operation, applying the same key again restores the original image — ensuring a perfect one-to-one decryption.

---

## **✨ Key Features**

  🖼️ Load and display images (JPG, PNG, BMP, JPEG formats)
  
  🔑 Custom key-based encryption and decryption
  
  ⚡ Pixel-level XOR encryption algorithm
  
  💾 Automatic saving of encrypted/decrypted images
  
  🧠 User-friendly interface built with Tkinter
  
  📊 Side-by-side comparison of original and processed images
  
  🚫 Error handling for invalid inputs or missing images

---

## 💡** Usage Example**
  Encrypting an Image
  
  Click “Select Image” and choose your file (e.g., photo.jpg).
  
  Enter a numeric key (e.g., 25).
  
  Click “Encrypt” — the tool processes the image and saves it as photo_encrypted.jpg.
  
  Decrypting an Image
  
  Load the encrypted image.
  
  Enter the same key used during encryption.
  
  Click “Decrypt” — your original image will be restored and saved as photo_decrypted.jpg.

---

## **🧰 Implementation Details**

  Language: Python
  
  Libraries Used:
  
  tkinter → GUI design
  
  PIL (Pillow) → Image handling and pixel operations
  
  os → File handling and saving
  
  Encryption Logic: XOR operation applied to each RGB pixel
  
  UI Design: Minimal dark theme with clear status messages and dual-image preview

---

## **🚀 How to Run the Tool**

  1️⃣ Clone the Repository
  
    git clone https://github.com/abhishek2871/Pixel-manipulation-for-image-encryption.git
  
    cd Pixel-Image-Encryption-Tool
  
  2️⃣ Install Required Libraries
  
    pip install pillow
  
  3️⃣ Run the Program
  
    python image_encryptor.py

---

## **🏁 Conclusion**

  The Pixel-Based Image Encryption Tool demonstrates how basic cryptographic principles can be applied to multimedia files.
  It’s a simple yet powerful project to understand XOR encryption, image processing, and GUI development using Python.
