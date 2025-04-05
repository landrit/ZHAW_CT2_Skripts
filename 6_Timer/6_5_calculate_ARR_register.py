"""Input"""

fcount = 100_000 # Hz
PWM_Period = 0.4 # s
Duty_Cycle = 0.3 # %

"""End Input"""

takt_periode = 1 / fcount
print(f"takt_periode = 1 / {fcount} Hz = {takt_periode} s")
print()

anzahl_ticks = PWM_Period / takt_periode
print(f"Anzahl der Ticks = PWM_Period / Taktperiode")
print(f"Anzahl der Ticks = {PWM_Period} s / {takt_periode} = {anzahl_ticks} Ticks")
print(f"Der ARR-Registerwert muss auf {int(anzahl_ticks)} gesetzt werden.")
print()

print(f"Um ein Duty-Cycle von {Duty_Cycle * 100}% zu erreichen:")
print(f"CCR-Wert = Anzahl der Ticks * Duty-Cycle")
CCR_Wert = anzahl_ticks * Duty_Cycle
print(f"CCR-Wert = {anzahl_ticks} * {Duty_Cycle} = {CCR_Wert}")

"""
KEYWORDS:
PWM - Periode und Duty Cycle
Gegeben ist der folgende Counter. Dieser ist als Up-counter konfiguriert und inkrementiert mit einer Frequenz fcount = 100 kHz. Alle Register sind 16-bit breit.

Mit welchen Werten müssen das ARR Register und die drei CCR Register programmiert werden, um die untenstehenden PWM Signale mit den angegebenen Duty Cycles zu generieren? 
Geben Sie die Werte als Dezimalzahlen an. Die Herleitung muss ersichtlich sein. 
"""
