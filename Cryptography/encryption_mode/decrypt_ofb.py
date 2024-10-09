from Crypto.Util import strxor

# Step 1: Read the plaintext and ciphertext of ofb1.txt and ofb1.enc
with open('ofb1.txt', 'rb') as f:
    ofb1_plaintext = f.read()

with open('ofb1.enc', 'rb') as f:
    ofb1_ciphertext = f.read()

# Step 2: Derive the keystream by XORing the plaintext and ciphertext
keystream = strxor.strxor(ofb1_plaintext, ofb1_ciphertext)

# Step 3: Read the ciphertext of ofb2.enc
with open('ofb2.enc', 'rb') as f:
    ofb2_ciphertext = f.read()

# Step 4: Decrypt ofb2.enc by XORing the ciphertext with the derived keystream
# Ensure the keystream is at least as long as the ciphertext
decrypted_ofb2 = strxor.strxor(ofb2_ciphertext, keystream[:len(ofb2_ciphertext)])

# Step 5: Write the decrypted result to a file
with open('ofb2.txt', 'wb') as f:
    f.write(decrypted_ofb2)

print("Decryption of ofb2.enc completed. Decrypted content saved to 'ofb2.txt'.")
