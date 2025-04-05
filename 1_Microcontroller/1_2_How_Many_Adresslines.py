import math

"""
input
"""
neededGigaAdresses = 4.0

"""
end of input
"""

x = math.log2(neededGigaAdresses * 1_000_000_000)

print(f"Für {neededGigaAdresses} Giga-Adressen werden {math.ceil(x)} Adressleitungen benötigt.")

"""
KEYWORDS: 
Adressleitungen 
"""