import ecbhash

# The input string as bytes
input_text = b'0123456789ABCDEF0123456789abcdef'

# Compute the hash
hash_value = ecbhash.ecbhash(input_text)

# Display the hash value
print(hash_value)

# Create a modified input (just an example; more sophisticated attacks could involve bit manipulation)
second_preimage_input = b'0123456789ABCDEF0123456789abcdEE'

# Compute the hash for the second preimage candidate
second_preimage_hash = ecbhash.ecbhash(second_preimage_input)

# Display the hash value of the modified input
print(second_preimage_hash)

# Compare if the hash values match
if hash_value == second_preimage_hash:
    print("Second preimage found!")
else:
    print("Hash values do not match.")

