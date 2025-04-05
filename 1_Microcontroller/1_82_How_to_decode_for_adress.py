"""
Input
"""

control_register_address = 0x28
address_lines = 6

"End Of input"

from tabulate import tabulate
from termcolor import colored


def generate_address_table(control_register_address, address_lines):
    binary_address = bin(control_register_address)[2:].zfill(address_lines)
    table_data = [list(binary_address)]

    conditional_data = ["A[{}]".format(i) if bit == '1' else "!A[{}]".format(i) for i, bit in
                        enumerate(reversed(binary_address))]

    combined_data = [b for b in reversed(conditional_data)]
    table_data.append(combined_data)

    print(tabulate(table_data, tablefmt="pretty"))
    print("Result: ", colored(" & ".join(reversed(conditional_data)), 'red'))


generate_address_table(control_register_address, address_lines)

"""
KEYWORDS:
Address decoder
Address decoding
"""