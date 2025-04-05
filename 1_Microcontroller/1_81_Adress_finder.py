"""
Input
"""

fixed_bits = ('x', 'x', '0', '1', '1', '0')  # for eg A[5:0] = 1,1,0,0,?,?


"""
End of Input
"""

from itertools import product

def get_matching_addresses(fixed_bits):
    addresses = []

    for bits in product([0, 1], repeat=len(fixed_bits)):
        if all(bit == int(fixed_bit) if fixed_bit.isdigit() else True for bit, fixed_bit in
               zip(bits, fixed_bits)):
            address = sum(bit << (len(bits) - 1 - i) for i, bit in enumerate(bits))
            addresses.append(hex(address))

    return addresses

def get_fixed_bits(fixed_bits):
    return ''.join(fixed_bits)

addresses_c = get_matching_addresses(fixed_bits)
for addr in addresses_c:
    print(f"0x{addr[2:].zfill(2)} (0b{bin(int(addr, 16))[2:].zfill(8)})")

fixed_bits_string = get_fixed_bits(fixed_bits)

print(f"Fixierte Bits: {fixed_bits_string}. Mögliche Adressen sind {', '.join(addresses_c)}.")
