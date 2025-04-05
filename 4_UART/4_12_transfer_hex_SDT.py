"""INPUT"""

start_bit = 1 # 0 oder 1
data_bits = 8
parity_bit = None # None (in Prüfung steht: Ein kein parity bit) 0 oder 1
stop_bits = 1
hex_value = "0x5A"

"""END OF INPUT"""

from tabulate import tabulate

# convert hex to binary but keep the leading zeros
hex_value_as_binary = format(int(hex_value, 16), 'b').zfill(data_bits)
print(f"hex_value_as_binary: {hex_value_as_binary}")
reversed_hex_value_as_binary = hex_value_as_binary[::-1]
print(f"reversed_hex_value_as_binary: {reversed_hex_value_as_binary}")

# Create headers and values lists
headers = ['Start'] + [f'D{i}' for i in range(data_bits)] + ['Parity'] + ['Stop']
values = [start_bit] + [f'{bit}' for bit in reversed_hex_value_as_binary] + [parity_bit] + ['1'] * stop_bits

# Print the table with headers and values
print(tabulate([values], headers=headers, tablefmt="grid"))

"""
Keywords

Serieller Daten Transfer

Uber eine UART Verbindung soll der Hex Wert Ox6C transferiert werden.

Die UART Konfiguration:
- 1 Startbit
- 8 Datenbits
- 1 Kein Parity Bit
- 1 Stopbit

Geben Sie die Sequenz der transferierten Bits an (inklusive Start- und Stopbits). Das erste transferierte Bit steht links, das letzte rechts
z.B. 0110110101 ohne Spaces oder anderen Zeichen zwischen den Bit Werten).
"""