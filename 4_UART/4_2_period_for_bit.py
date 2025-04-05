"""
INPUT

Für Aufgaben der Art:

Auf einer seriellen asynchronen Übertragungsleitung
(UART) mit 19‘200 Bit/s,
7 Daten-Bits, und einem Stop-Bit (ohne Parity Bit)
soll die Zeichenfolge ”AC” übertragen werden.
ASCII('A') = 0x41 = 100 0001b ASCII('C') = 0x43 = 100 0011b
a) Wie lange dauert die Übertragung eines Bits (Periode T)?
"""
baud_rate = 19_200  # in bits per second
bit_period = 1 / baud_rate  # in seconds

"""
END INPUT
"""

print(f"The duration of a bit period is {bit_period * 1000000:.2f} microseconds")
