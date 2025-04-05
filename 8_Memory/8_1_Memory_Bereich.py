"""Input"""
address_lines = 15
block_size = 1
factor = "kilo" # bytes, kilo, mega, giga, tera, peta, exa, zetta, yotta, bronto

"""End of Input"""


# Einheitenfaktoren
unit_factors = {
    "bytes": 0,
    "kilo": 1,
    "mega": 2,
    "giga": 3,
    "tera": 4,
    "peta": 5,
    "exa": 6,
    "zetta": 7,
    "yotta": 8,
    "bronto": 9
}

import math

# Berechnung der Grösse des Speicherbereichs
memory_size = math.pow(2, address_lines) * block_size
print(f"Die Grösse des Speichers beträgt {memory_size} Byte.")
unit_factor = unit_factors.get(factor, None)

if unit_factor is None:
    raise "Falsche Einheit!"
else:
    memory_size = memory_size / math.pow(1024, unit_factor)
    print(f"Die Grösse des Speichers beträgt {memory_size:.0f} {factor}Byte.")


"""
Keywords:
Wie gross ist der Speicherbereich in kBytes, der mit 20 Adressleitungen maximal angesprochen werden kann, wenn jede Adresse ein
individuelles Byte identifiziert?

Gegeben ist der folgende 'asynchronous SRAM' Baustein.
Was ist die Grösse y des Bausteines in KBytes ( y K x 8bit) ?

Gegeben ist der folgende 'asynchronous SRAM' Baustein.
Was ist die Grösse y des Bausteines in KBytes ( y K x 8bit) ?
"""