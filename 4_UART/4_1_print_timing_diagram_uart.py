"""
INPUT
"""

data_bits = 7
hex_value = "0x52"

idleBit = 1
startBit = 0
stopBit = 1

parityBitType = "odd" # even, odd, none

"""
END INPUT
"""

parityBit = None

from tabulate import tabulate
from matplotlib import pyplot as plt


def hex_to_ascii(hex_value):
    return chr(int(hex_value, 16))


def uart_transmission(data_bits, start_bit, stop_bit, hex_value):
    output = []

    character = hex_to_ascii(hex_value)
    binary_char = format(ord(character), 'b').zfill(data_bits)[::-1]
    if parityBitType == "even":
        parityBit = sum([int(bit) for bit in binary_char]) % 2
    elif parityBitType == "odd":
        parityBit = (sum([int(bit) for bit in binary_char]) + 1) % 2

    transmission = [start_bit] + [f'{bit}' for bit in binary_char] + [parityBit] + [stop_bit]
    output.extend(transmission)

    return output


def plot_uart_transmission(data_bits, start_bit, stop_bit, parity_bit, hex_value):
    idleOccurence = 3
    plt.rcParams["figure.figsize"] = (7, 3)
    plt.title(f"UART Transmission: {hex_value}")

    transmission_sequence = [idleBit] * idleOccurence \
                            + [int(bit) for bit in uart_transmission(data_bits, start_bit, stop_bit, hex_value)] \
                            + [idleBit] * idleOccurence

    my_xticks = ['Idle'] * idleOccurence \
                + ['Start'] \
                + [f'D{i}' for i in range(data_bits)] \
                + ['Parity'] \
                + ['Stop'] \
                + ['Idle'] * idleOccurence

    fig, xlabel_bottom = plt.subplots()
    xlabel_bottom.step(range(len(transmission_sequence)), transmission_sequence, color='black', linewidth=3)

    # Set the bottom x-axis labels with right alignment and additional padding
    xlabel_bottom.set_xticks(range(len(transmission_sequence)))
    xlabel_bottom.set_xticklabels(my_xticks, ha='right', rotation=45, x=-0.1)

    # Set the top x-axis labels representing time starting from 0
    xlabelTop = xlabel_bottom.twiny()
    xlabelTop.set_xlim(xlabel_bottom.get_xlim())
    xlabelTop.set_xticks(xlabel_bottom.get_xticks())
    xlabelTop.set_xticklabels(range(len(transmission_sequence)))

    plt.grid()
    plt.show()


transmission_sequence = uart_transmission(data_bits, startBit, stopBit, hex_value)

# Create headers and values lists
headers = ['S'] + [f'D{i}' for i in range(data_bits)] + ['P'] + ['E']
values = transmission_sequence

# Print the table with headers and values
print(tabulate([values], headers=headers, tablefmt="grid"))
plot_uart_transmission(data_bits, startBit, stopBit, parityBit, hex_value)
