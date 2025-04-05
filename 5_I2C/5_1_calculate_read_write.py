"""
INPUT
"""
bits = 8
hex_value = None # None
bit_value = 0b00100110  # None (nur alle 7 Datenbits ohne Start Bit + R/W Bit)
msbFirst = True

"""
END OF INPUT
"""


def i2c_interpretation(bits, hex_value, bit_value, msbFirst):
    if bits != 8:
        raise ValueError("Only 8-bit values are supported.")
    value = 0;
    if hex_value is None:
        value = bit_value
    elif bit_value is None:
        value = hex_value
    else:
        raise ValueError("Only one value can be set Sie lellek.")

    if not msbFirst:
        # Reverse the bit order
        value = int('{:08b}'.format(value)[::-1], 2)

    shifted_value = value >> 1
    slave_address = shifted_value & 0x7F  # Masking the 7 most significant bits after the shift

    read_write = "write" if (value & 0x01) == 0 else "read"

    return slave_address, read_write


slave_address, read_write = i2c_interpretation(bits, hex_value, bit_value, msbFirst)

print(f"Slave address: 0x{slave_address:02X} ({slave_address} in decimal)")
print(f"Operation: {read_write}")


"""
KEYWORDS:

I2C Adressierung

Der Master sendet zur Initialisierung der Kommunikation mit einem Slave die folgenden 8 Bit: 0110'0100 (MSB first)
Geben Sie die Slave Adresse in Hexadezimal an. z.B. Ox45 und ob es sich um einen Read oder Write handelt
"""