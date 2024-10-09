# ANU COMP2700 Cyber Security Foundations
# A simple (and flawed) stream cipher using linear congruence generator
# Alwen Tiu, 2019 

import sys
from Crypto.Util.number import *
from Crypto.Util.strxor import *

# Each block is 2 bytes
BLOCK_SIZE=2
# Fixed the modulus; must be representable as a 2-byte integer. 
MODULUS=64283


# All key material S0, A, B and p are 16-bit integers (2 bytes)
def lcg(S0, A, B, n):
  S = S0
  keystream = bytearray()

  # generate a 2-byte pseudo-random number at a time.  
  for i in range(n):
    S = (S*A + B) % MODULUS
    R = bytearray(long_to_bytes(S,BLOCK_SIZE))
    keystream.extend(R)
  return bytes(keystream)

# NOTE: since this is a streamcipher, encryption and decryption are the same function. 
def encfile(S0, A, B, infile, outfile):
  with open(infile, 'rb') as f: 
    inbytes = f.read()

  sz = len(inbytes)

  # generate keystream
  # n = how many random numbers need to be generated. 
  # Each number is BLOCK_SIZE byte long. 
  n  = sz//BLOCK_SIZE + 1
  keystream = lcg(S0,A,B,n)

  # byte-wise XOR plaintext with keystream
  outbytes = strxor(inbytes, keystream[0:sz])

  with open(outfile, 'wb') as g:
    g.write(outbytes)

def main(): 
  if len(sys.argv) < 6:
     print("Usage: python3 " + sys.argv[0] + " S0 A B infile outfile ")
     quit()
  S0 = int(sys.argv[1]) % MODULUS
  A  = int(sys.argv[2]) % MODULUS
  B  = int(sys.argv[3]) % MODULUS
  encfile(S0,A,B,sys.argv[4],sys.argv[5])

if __name__ == "__main__":
  main()
   
