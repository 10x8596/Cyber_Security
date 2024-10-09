from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# Function to read PPM file and extract pixel data
def extract_pixel_data(ppm_file):
    with open(ppm_file, 'rb') as f:
        # Read header
        header = b""
        while True:
            line = f.readline()
            if line.startswith(b"P6"):
                header += line
            elif line.startswith(b"#"):  # Comment lines
                continue
            else:
                header += line
                if len(header.split()) == 4:  # Format, width, height, max color value
                    break
        
        # Read the remaining part (pixel data)
        pixel_data = f.read()
    return header, pixel_data

# Function to encrypt pixel data using AES-128 ECB mode
def encrypt_pixel_data(pixel_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    # Padding the pixel data to make it a multiple of 16 bytes
    padded_data = pad(pixel_data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# Main execution
ppm_file = "Tux.ppm"
header, pixel_data = extract_pixel_data(ppm_file)

# Generate a random 128-bit key (16 bytes)
key = os.urandom(16)

# Encrypt the pixel data
encrypted_pixel_data = encrypt_pixel_data(pixel_data, key)

# Optionally, save the encrypted data back to a file (for example as encrypted.ppm)
with open("ecb_encrypted_Tux.ppm", "wb") as f:
    f.write(header)  # Write the header
    f.write(encrypted_pixel_data)  # Write the encrypted pixel data

print("Encryption completed. Encrypted image saved as 'encrypted_Tux.ppm'.")

