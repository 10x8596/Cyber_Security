def hex_to_ascii(hex_string):
    # Remove '0x' if present
    hex_string = hex_string.replace('0x', '')
    
    # Ensure even number of digits
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    
    # Convert to bytes and then to ASCII
    try:
        bytes_object = bytes.fromhex(hex_string)
        ascii_string = bytes_object.decode('ascii', errors='replace')
        return ascii_string
    except ValueError as e:
        return f"Error: {e}. Invalid hex string."

# Example usage:
hex_value = "41424344"  # This is 'ABCD' in hex
print(hex_to_ascii(hex_value))

# For a single large value:
large_hex = hex(0x41424344)  # '0x41424344'
print(hex_to_ascii(large_hex))

def hex_calc(a, b):
    return print(f"Addition: {a+b}\n"
                 f"Subtraction: {b-a}\n"
                 f"Multiplication: {a*b}\n"
                 f"Division: {b/a}")

a = 0xffffd56b
b = 0x5655a1a0
hex_calc(a, b)
"\n"
hex_calc(b, a)
