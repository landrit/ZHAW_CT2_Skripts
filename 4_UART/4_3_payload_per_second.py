"""
INPUT
"""

baud_rate = 19200  # in bits per second
start_bit = 1  # Anzahl Start-Bits
data_bits = 7  # Anzahl Daten-Bits
stop_bit = 1  # Anzahl Stop-Bits
parity_bit = 1  # Anzahl Parity-Bits

"""
END INPUT
"""


def calculate_payload_per_second(baud_rate, start_bit, data_bits, stop_bit, parity_bit):
    payload_per_bit = start_bit + data_bits + stop_bit + parity_bit
    payload_per_second = baud_rate / payload_per_bit
    return payload_per_second


print(
    f"The payload per second is {calculate_payload_per_second(baud_rate, start_bit, data_bits, stop_bit, parity_bit):.2f} bytes / s")

"""
KEYWORDS:
UART
asynchronous
serial
transmission
baud rate
bit period
start bit
payload
"""