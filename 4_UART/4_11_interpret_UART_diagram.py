"""
INPUT

ACHTUNG DIESES SCRIPT NUR FÜR AUFGABEN, BEI WELCHEN DAS DIAGRAM VORGEGEBEN WIRD!!!
"""

graphic = [1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1,1,1,1]


amount_of_data_bits = 7
parity_bit = 1  # 0 = even, 1 = odd, None = no parity bit
start_bit = True
stop_bit = True

MSB_first = False  # Set to False for LSB first
# UART is always LSB first

baudrate = 19200  # Baudrate in characters per second

"""
END INPUT
"""

from tabulate import tabulate
from matplotlib import pyplot as plt

def plot_input():
    """
    Print the input to verify it is correct
    """



def print_bits():
    start_bit_index = graphic.index(0)
    if parity_bit is not None:
        parity_bit_index = start_bit_index + amount_of_data_bits + 1
        stop_bit_index = parity_bit_index + 1
        data_bits = graphic[start_bit_index + 1:parity_bit_index]
    else:
        stop_bit_index = start_bit_index + amount_of_data_bits + 1
        data_bits = graphic[start_bit_index + 1:stop_bit_index]

    data_bits_hex = hex(int(''.join(map(str, data_bits if MSB_first else data_bits[::-1])), 2))
    print(f"Transferred data: {data_bits_hex}")
    print(f"Maximum transfer rate without overhead: {baudrate / (start_bit + len(data_bits) + stop_bit + (parity_bit is not None))} Bytes/s")

    ####################################

    # Create a new figure
    plt.figure(figsize=(10, 3))

    # Plot the data
    x = list(range(len(graphic)))
    plt.step(x, graphic, where='post')
    plt.xticks(range(len(graphic)), x)
    plt.yticks([0, 1], ['0', '1'])

    # region plot text
    plt.text(start_bit_index + 0.5, 0.5, 'start', fontsize=10, verticalalignment='center', horizontalalignment='center')
    plt.text(stop_bit_index + 0.5, 0.5, 'stop', fontsize=10, verticalalignment='center', horizontalalignment='center')
    if parity_bit is not None: plt.text(parity_bit_index + 0.5, 0.5, 'parity', fontsize=10, verticalalignment='center', horizontalalignment='center')
    [plt.text(start_bit_index + 1.5 + i, 0.5, data_bits[i], fontsize=10, verticalalignment='center', horizontalalignment='center') for i in range(len(data_bits))]
    # endregion

    # Add labels (optional)
    plt.xlabel('Time')
    plt.ylabel('Value')

    plt.grid()
    plt.show()


def main():
    print_bits()


main()




"""
KEYWORDS:
Auf einer seriellen Datenleitung (UART) messen Sie den folgenden zeitlichen Verlauf. Die Übertragung verwendet ein Startbit, ein Stoppbit, 7 Datenbits mit Parity-bit bei 19'200 baud. Es wird Odd Parity verwendet.
a) Notieren Sie die Bedeutung der einzelnen Bits im obenstehenden Zeitverlauf und geben Sie die übertragenen Daten als Hexwert an.
b) Wie viele Daten-Bytes (ohne Overhead) kann man pro Sekunde maximal übertragen?

Auf einer seriellen Datenleitung (UART) messen Sie den folgenden zeitlichen Verlauf. Die Übertragung verwendet bei 9'600 bits/s
- ein Startbit
- ein Stoppbit
- 7 Nutzdatenbits - Even-Parity-Bit
a) Notieren Sie im obigen Diagramm die Bedeutung der Bits im Zeitverlauf und geben Sie die übertragenen Daten als Hexwert an.
Bemerkung: der UART sendet LSB-first.
b) Wie viele Pakete zu 7 Nutzdatenbits (ohne Synchronisations-Overhead) kann man bei dieser Konfiguration pro Sekunde maximal übertragen?

"""