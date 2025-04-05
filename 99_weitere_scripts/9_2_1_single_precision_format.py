"""
INPUT:
"""

number = -4.75

"""
END OF INPUT
"""

import struct


def float_to_bin(number):
    # Convert the float to a binary string
    binary_str = format(struct.unpack('!I', struct.pack('!f', number))[0], '032b')

    return binary_str


# Convert the number to binary
binary = float_to_bin(number)

# Extract the sign, exponent, and mantissa from the binary string
sign = binary[0]
exponent = binary[1:9]
mantissa = binary[9:]

# Convert the exponent to decimal
exponent_decimal = int(exponent, 2) - 127

print(f"Dezimal -> Binär: {number}d = {binary}b")
print(f"Normalisieren: {binary}b = 1.{mantissa} * 2^{exponent_decimal}")
print(f"Mantisse: {mantissa}")
print(f"Exponent: E = {exponent_decimal}d + 127d = {int(exponent, 2)}d = {exponent}b")
print(f"Sign: {number}<0 -> V = {sign}")
print(f"Packen: {binary}")
print(f"Hex: 0x{hex(int(binary, 2))[2:].zfill(8).upper()}")

"""
Keywords:
Geben Sie an, wie -4.75d im Single Precision-Format nach IEEE Standard 754/ 854 abgelegt wird.
Ihr Lösungsweg muss nachvollziehbar sein.
"""
