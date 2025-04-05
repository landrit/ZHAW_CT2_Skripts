"""
INPUT
"""

dataBits = 7 # siehe ACHTUNG!
maxDeviation = 0.5

"""
END OF INPUT
"""

print(f"{100 * maxDeviation / (dataBits + maxDeviation)}%")

"""
ACHTUNG:
Es gibt Schaltungen die prüfen das Stopp Bit und Schaltungen die tuen das nicht
Berechnung der relativen Taktabweichung bei 1.5 Stopp Bits lautet die Gleichung:
50/stopp-bits + data-bits = Erlaubte Taktabweichung %

JE NACH AUFGABENSTELLUNG dataBits anpassen! z.B. 7 Datenbits + 1.5 Stoppbits => databits = 8.5
"""
