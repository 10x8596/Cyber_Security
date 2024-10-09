#!/usr/bin/env python3 

# ECB-Hash: A flawed cryptographic hash function
# (c) Alwen Tiu, 2020

from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.strxor import strxor

key=b'ECB-HASH-1234567'

# compute the XOR of all blocks in the input
def xorblocks(data):
    if len(data) % AES.block_size != 0:
        raise ValueError("data length must be a multiple of block size")

    bs=AES.block_size
    n = len(data)//bs
    d=data[:bs]
    data=data[bs:]

    for i in range(n-1):
        d=strxor(d,data[:bs])
        data=data[bs:]
    return d

def ecbhash(data):
    if (len(data) % AES.block_size) != 0:
        raise ValueError("Input length must be a multiple of 16 bytes")
    
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(data)
    digest=xorblocks(ct)
    return digest.hex()

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " file ")
        quit()

    with open(sys.argv[1], "rb") as f:
        data=f.read()
    digest = ecbhash(data)
    print(digest)

if __name__ == "__main__":
    main()
   
