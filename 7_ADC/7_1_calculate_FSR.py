"""
INPUT
"""
bitsOfADC = 3
Vref = 8  # in volts (V)
actual_voltage_at_max_output = 5.5  # in volts basierend auf der realen Übertragungsfunktion (Aufgabenstellung gegeben) (wo die Kurve 111 trifft)
ideal_voltage_at_max_output = 6.5  # in volts basierend auf der idealen Übertragungsfunktion (wo die Kurve 111 trifft)
offset_v = None  # in volts (V)
offset_LSB = -1  # in LSB (the absolute value of the offset error e.g. -1.5 is 1.5)
"""
END OF INPUT
"""

import matplotlib.pyplot as plt
import numpy as np

LSB = Vref / 2 ** bitsOfADC
vFSR = Vref - LSB

print(f"1 LSB = {LSB} V (this equals {LSB * 1000} mV)")
print(f"VFSR = {vFSR} V (this equals {vFSR * 1000} mV)")
print(f"Quantisierungsfehler = +- {LSB / 2} V (this equals +- {LSB / 2 * 1000} mV)")

# Create a range of input voltages
input_voltages = np.linspace(0, Vref, 1000)

# Quantize the input voltages to the nearest LSB
quantized_values = np.round(input_voltages / LSB)

# Convert the quantized values to binary format
binary_values = [format(int(i), f'0{bitsOfADC}b') for i in quantized_values]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(input_voltages, quantized_values, drawstyle='steps-post')
plt.plot(input_voltages, input_voltages / LSB, drawstyle='steps-post')
plt.grid(True)
plt.title('ADC Transfer Function')
plt.xlabel('Input Voltage (V)')
plt.ylabel('Output Code')

# Change the y-axis labels to binary format
plt.yticks(range(2 ** bitsOfADC), binary_values[::int(len(binary_values) / 2 ** bitsOfADC)])

plt.show()

# Calculate the gain error
if offset_v is not None:
    gain_error = ideal_voltage_at_max_output - (actual_voltage_at_max_output + offset_v)
elif offset_LSB is not None:
    gain_error = ideal_voltage_at_max_output - (actual_voltage_at_max_output + offset_LSB)
else:
    gain_error = ideal_voltage_at_max_output - actual_voltage_at_max_output

gain_error_in_LSB = gain_error / LSB  # in LSB

print(f"Gain error = {gain_error} V (this equals {gain_error_in_LSB} LSB)")

if offset_v is not None:
    print(f"Offset error = {offset_v} V")
    print(f"Full Scale Error = {offset_v + gain_error} V")
elif offset_LSB is not None:
    print(f"Offset error = {offset_LSB} LSB")
    print(f"Full Scale Error = {offset_LSB + gain_error_in_LSB} LSB")
else:
    print(f"Offset error = 0")
    print(f"Full Scale Error = {gain_error_in_LSB} LSB")

print("Negative offset in the graphic to the right, positive offset in the graphic to the left, just copy the staircase shifted to the left or right")
"""
Keywords:

ADC Auflösung / Full Scale Range
Gegeben ist ein 7-bit ADC mit einer Referenzspannung Vref = 4096 mV.
Wieviel beträgt die Auflösung eines LSBs (Least Significant Bits) in mV?

Wie hoch ist der Full Scale Range (FSR) in mV?
"""

"""
Keywords:
Gegeben ist ein 3-bit ADC. Die Referenzspannung VREF ist auf 8V festgelegt.
a) Zeichnen Sie die Übertragungsfunktion!
b) In welchem Spannungsbereich (in V) bewegt sich der Quantisierungsfehler?
c) Gegeben ist ein realer 3-bit ADC. Er hat keinen Offsetfehler (offset error = 0 LSB). Ab
einer Spannung von 5V gibt der ADC den digitalen Wert von „111" aus. Wie gross ist
der Verstärkungsfehler (Gain error)? Der Lösungsweg muss nachvollziehbar sein.
"""
