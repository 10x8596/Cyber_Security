from Crypto.Util.number import *
from Crypto.Util.strxor import *
from sympy import symbols, Eq, solve

# read the encrypted document to bytes ct
with open('doc.enc', 'rb') as f:
    ciphertext = f.read()

# known plaintext. 
known_pt = b'<html>'

# TODO: use the known plaintext to find S1, S2 and S3

S1, S2, S3, m = 3505, 451, 51178, 64283

# XOR known plaintext first 6 part of ciphertext
keystream_part = strxor(ciphertext[:6], known_pt)
print("first few part of keystream:", keystream_part.hex())

# TODO: calculate the key (S0, A, B) using S1, S2 and S3

# Brute force search for A and B
for A in range(m):
    # Calculate B from the first equation
    B = (S2 - A * S1) % m
    
    # Check if this B satisfies the second equation
    if (S3 - A * S2) % m == B:
        print(f"A: {A}, B: {B}")
        break  # Stop after finding the first valid (A, B)
else:
    print("No valid (A, B) pair found.")

A, B = 678, 2532

# so we have S1 = A*S0 + B mod m | 3505 = 678 * S0 + 2532 mod 64283 
# therefore S0 = inverse(678, 64283) * (2532 - 3505) mod 64283
S0 = (S1 - B) * pow(A, -1, m) % m

print("The key is (S0 = %d, A = %d, B = %d)" % (S0, A, B))

# S0 = 1234
print(S1 == (A * S0 + B) % m)

# Now you can use the key to decrypt doc.enc using the provided lcgcipher.py.

