"""Input: """

adresslines = 32

""" End of Input """


"""Output: """
num_addresses = 2 ** adresslines
unit = 'Bytes'

while num_addresses > 1000:
    num_addresses /= 1024
    if unit == 'Bytes':
        unit = 'Kilobytes'
    elif unit == 'Kilobytes':
        unit = 'Megabytes'
    elif unit == 'Megabytes':
        unit = 'Gigabytes'
    elif unit == 'Gigabytes':
        unit = 'Terabytes'
    elif unit == 'Terabytes':
        unit = 'Petabytes'

start_address = 0
end_address = (2 ** adresslines) - 1

print(f"Bei {adresslines} Adressleitungen können von 0x{start_address:08X} bis 0x{end_address:08X} {num_addresses:.2f} {unit} adressiert werden.")



"""
KEYWORDS:
Partielle Dekodierung
Adressdekodierung
Adressleitungen 
"""