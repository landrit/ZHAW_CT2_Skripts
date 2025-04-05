"""INPUT"""

input_zahl = 64000
basis_adresse = 0x68000000
max_adresslinien = 26


"""END INPUT"""

import math

def berechne_adresslinien(adressbloecher):
    return int(math.log2(adressbloecher))

def berechne_adressbloecher(adresslinien):
    return 2 ** adresslinien

ergebnis = int(math.ceil(math.log2(input_zahl)))

adressbloecher = 2 ** ergebnis
adresslinien = berechne_adresslinien(adressbloecher)

print(f"Der Baustein benötigt {ergebnis} Adresspins für {adressbloecher} Adressblöcke.")
addressblock_size = ergebnis - 1
print(f"Die Adressblöcke sind A[{addressblock_size}:0].")

nicht_angeschlossene_adresslinien = max_adresslinien - adresslinien

moegliche_adressbloecher = berechne_adressbloecher(nicht_angeschlossene_adresslinien)

print(f"Auf {moegliche_adressbloecher} können {input_zahl} Adressblöcke abgebildet werden.")
print(f"Die Adressblöcke sind A[{max_adresslinien - 1}:{addressblock_size+1}].")


# Berechne den Endpunkt des Adressbereichs
end_adresse = basis_adresse + (moegliche_adressbloecher - 1) * (1 << 16)

# Gib den Adressbereich als Intervall aus
print(f"Der Adressbereich ist [{hex(basis_adresse)}, {hex(end_adresse)}].")
