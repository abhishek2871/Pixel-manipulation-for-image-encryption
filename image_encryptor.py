import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class PixelImageEncryptor:
    def __init__(self, root):
        self.root = root
        self.root.title("🔒 Pixel-Based Image Encryption Tool")
        self.root.geometry("850x550")
        self.root.config(bg="#1e1e2f")

        self.image_path = None
        self.original_image = None
        self.active_image = None

        # Title
        tk.Label(root, text="🧠 Image Encryption & Decryption (Pixel Manipulation)",
                 bg="#1e1e2f", fg="#00FFFF", font=("Helvetica", 14, "bold")).pack(pady=10)

        # Controls
        frame_controls = tk.Frame(root, bg="#1e1e2f")
        frame_controls.pack(pady=10)

        tk.Button(frame_controls, text="📂 Select Image", command=self.load_image,
                  bg="#2196F3", fg="white", width=15).grid(row=0, column=0, padx=10)

        tk.Label(frame_controls, text="🔑 Key:", bg="#1e1e2f", fg="white", font=("Arial", 10)).grid(row=0, column=1, padx=5)
        self.entry_key = tk.Entry(frame_controls, width=10)
        self.entry_key.grid(row=0, column=2, padx=5)

        tk.Button(frame_controls, text="Encrypt", command=self.encrypt_image,
                  bg="#4CAF50", fg="white", width=10).grid(row=0, column=3, padx=10)

        tk.Button(frame_controls, text="Decrypt", command=self.decrypt_image,
                  bg="#F44336", fg="white", width=10).grid(row=0, column=4, padx=10)

        # Image display
        frame_images = tk.Frame(root, bg="#1e1e2f")
        frame_images.pack(pady=20)

        self.label_original = tk.Label(frame_images, text="Original / Active Image", bg="#1e1e2f", fg="white")
        self.label_original.grid(row=0, column=0)
        self.label_processed = tk.Label(frame_images, text="Processed Image", bg="#1e1e2f", fg="white")
        self.label_processed.grid(row=0, column=1)

        self.canvas_original = tk.Label(frame_images, bg="#1e1e2f")
        self.canvas_original.grid(row=1, column=0, padx=20)
        self.canvas_processed = tk.Label(frame_images, bg="#1e1e2f")
        self.canvas_processed.grid(row=1, column=1, padx=20)

        # Status bar
        self.status_label = tk.Label(root, text="💡 Select an image to begin.", bg="#1e1e2f",
                                     fg="white", font=("Arial", 10, "italic"))
        self.status_label.pack(pady=10)

    # Load image
    def load_image(self):
        filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp")]
        path = filedialog.askopenfilename(title="Select Image", filetypes=filetypes)
        if path:
            try:
                self.image_path = path
                self.original_image = Image.open(self.image_path).convert("RGB")
                self.active_image = self.original_image.copy()
                self.display_image(self.active_image, self.canvas_original)
                self.status_label.config(text=f"📂 Loaded: {os.path.basename(self.image_path)}", fg="#FFD700")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {e}")
        else:
            self.status_label.config(text="⚠️ No image selected.", fg="orange")

    # Display image on label
    def display_image(self, img, label):
        img_resized = img.copy()
        img_resized.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img_resized)
        label.config(image=photo)
        label.image = photo

    # Get key
    def get_key(self):
        key_text = self.entry_key.get()
        if not key_text.isdigit():
            messagebox.showerror("Error", "Key must be a number!")
            self.status_label.config(text="❌ Invalid key. Enter a number.", fg="red")
            return None
        return int(key_text)

    # Pixel-level encryption
    def process_image(self, mode):
        key = self.get_key()
        if key is None or self.active_image is None:
            return

        width, height = self.active_image.size
        pixels = self.active_image.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # XOR each color channel with key
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        # Save file
        base, ext = os.path.splitext(self.image_path)
        if mode == "encrypt":
            save_path = f"{base}_encrypted{ext}"
        else:
            save_path = f"{base}_decrypted{ext}"

        self.active_image.save(save_path)
        self.display_image(self.active_image, self.canvas_processed)
        self.status_label.config(
            text=f"✅ {mode.capitalize()}ion successful! Saved as {os.path.basename(save_path)}",
            fg="#4CAF50" if mode == "encrypt" else "#2196F3"
        )
        return save_path

    # Encrypt button
    def encrypt_image(self):
        if not self.active_image:
            messagebox.showerror("Error", "No image loaded.")
            return
        self.process_image("encrypt")
        # Allow re-encryption of result
        self.original_image = self.active_image.copy()

    # Decrypt button
    def decrypt_image(self):
        if not self.active_image:
            messagebox.showerror("Error", "No image loaded.")
            return
        self.process_image("decrypt")
        # Allow re-decryption of result
        self.original_image = self.active_image.copy()


def main():
    root = tk.Tk()
    app = PixelImageEncryptor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
