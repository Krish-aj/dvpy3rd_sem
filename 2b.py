def binary_to_decimal(binary):
    return int(binary, 2)

def octal_to_hexadecimal(octal):
    return hex(int(octal, 8))[2:].upper()

# Main program
binary = input("Enter a binary number: ")
print(f"Decimal: {binary_to_decimal(binary)}")

octal = input("Enter an octal number: ")
print(f"Hexadecimal: {octal_to_hexadecimal(octal)}")
