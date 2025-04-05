"""
INPUT
"""

address_bits = 32 # Anzahl der Adressleitungen
decoded_address_bits = 26 # Anzahl der Adressleitungen, die dekodiert werden

"""
END OF INPUT
"""

adressedOn = 2 ** (address_bits - decoded_address_bits)

if address_bits == decoded_address_bits:
    print(f"Bei {address_bits} Adressleitungen und {decoded_address_bits} dekodierten Adressleitungen, können alle Adressen genau einmal adressiert werden.")
else:
    print(f"Bei {address_bits} Adressleitungen und {decoded_address_bits} dekodierten Adressleitungen, können alle Adressen auf je {adressedOn} Adressen adressiert werden.")


"""
KEYWORDS:
Partielle Dekodierung
Adressdekodierung
Adressleitungen

Für den Zugriff auf ein bestimmtes 8-bit breites 'Control Register' dekodiert ein 'Address De- coder' eines Systembusses die höherwertigen Adressleitungen A[31:6]. Die tieferwertigen Adressleitungen A[5:0] werden nicht dekodiert.
Unter wie vielen unterschiedlichen (Byte-) Adressen kann dieses 'Control Register' angesprochen werden?

Für den Zugriff auf ein bestimmtes 8-bit breites 'Control Register' dekodiert ein 'Address De- coder' die höherwertigen Adressleitungen A[31:6] eines Systembusses. Die tieferwertigen Adressleitungen A[5:0] werden nicht dekodiert.
Unter wie vielen unterschiedlichen (Byte-) Adressen kann dieses 'Control Register' an- gesprochen werden?
"""