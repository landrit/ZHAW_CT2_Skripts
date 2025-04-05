"""
INPUT
"""

bitsOfADC = 3
Vref = 2 # in volts (V)
offsetError = 1.5  # LSB (the absolute value of the offset error e.g. -1.5 is 1.5)

"""
END INPUT
"""

LSB = Vref / 2 ** bitsOfADC
offsetErrorInVolt = LSB * offsetError
offsetErrorInMillivolt = offsetErrorInVolt * 1000
print(f"1 LSB = {LSB}")
print(f"VFSR = {Vref - LSB} Volt")
print(f"Offset Error = {offsetErrorInVolt} Volt")
print(f"Offset Error = {offsetErrorInMillivolt} Millivolt")
print(f"Offset Error in % of FSR = {(offsetErrorInVolt * 100) / (Vref - LSB)} %")

"""Keywords

Gegeben ist ein 3-Bit ADC mit folgenden Merkmalen:
• 16 Volt Referenzspannung VREF
• -2 LSB Offsetfehler (Der Digitalwert ist zu tief)
a) Welche drei Fehler Arten gibt es bei der ADC Konversion?
b) Berechnen Sie den Wert eines LSB in Volt.
e) Berechnen Sie den FSR (Full Scale Range).
f) Zeichnen Sie im nachfolgenden Diagramm die mit dem Offsetfehler behaftete Übertra- gungsfunktion (Transfer Function) des Wandlers auf.

"""