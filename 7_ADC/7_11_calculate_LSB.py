"""Input"""

referenzspannung = 9  # Referenzspannung in Volt
gewuenschte_millivolt = 5  # Gewünschte LSB-Spannung in milli Volt

"""End of Input"""

gewuenschte_millivolt = gewuenschte_millivolt / 1000  # Umrechnung in mV

import math
min_steps = referenzspannung / gewuenschte_millivolt
print(f"Die beste ADC-Auflösung ist {math.ceil(math.log2(min_steps))}-Bit.")


"""
Keywords
ADC

Für einen ADC HW Block soll die Resolution so konfiguriert werden, dass für die gegebene Referenzspannung von 3V ein LSB möglichst
nahe bei 12mv liegt.
Ein externes analoges Signal soll digital abgetastet werden.
a) Bei einer maximalen Referenzspannung von 4.5V soll eine Abtast-Auflösung von mindestens 5mV erreicht werden. Wie viele Bits werden mindestens für die Analog- Digital Wandlung benötigt?
b) Nun wird die maximale Eingangsspannung auf 9V verdoppelt. Wie viele Bits werden nun für die gleiche Abtast-Auflösung (5mV) benötigt?
"""
