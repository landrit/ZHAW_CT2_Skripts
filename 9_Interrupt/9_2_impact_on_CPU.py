"""
INPUT
"""

abtastFrequenz = 44100  # in Hz (fint)
tisr = 1.5e-5  # in sekunden z.B. Berechnung Equalizer (wenn us angegeben dann e-5)

"""
END OF INPUT
"""

print(f"impact = {abtastFrequenz * tisr * 100} %")

"""
Keywords:
Ein A/D Wandler liefert mit CD Abtastfrequenz (44.1 kHz) Signale, die in der
ISR mit einem Equalizer bearbeitet und dann gespeichert werden. Die
Berechnung des Equalizers dauert 15 us. Berechnen Sie den CPU Impact
des Interrupts

fINT = 44.1kHz = 44100 Hz
tisR = 15 us = 15s*10^-6

Impact = f_INT *+_ISR *100% = 66.15%
"""
