from termcolor import colored

"""
Input
"""

control_register_addresses = [0x4C, 0x6D, 0x4D, 0x6C]
address_lines = 8

"End Of input"


def generate_address_table(control_register_addresses, address_lines):
    combined_data_all = []

    for control_register_address in control_register_addresses:
        binary_address = bin(control_register_address)[2:].zfill(address_lines)
        conditional_data = ["A[{}]".format(i) if bit == '1' else "!A[{}]".format(i) for i, bit in
                            enumerate(reversed(binary_address))]

        combined_data = [b for b in reversed(conditional_data)]
        combined_data_all.append(combined_data)

    # Find the common bits and set "don't care" (X) for the others
    computed_lines = []
    ignored_lines = []
    for i in range(address_lines):
        if all(combined_data[i] == combined_data_all[0][i] for combined_data in combined_data_all):
            computed_lines.append(combined_data_all[0][i])
        else:
            ignored_lines.append(combined_data_all[0][i].replace("!", ""))

    # Convert number indices to strings for printing
    ignored_lines = list(map(str, ignored_lines))

    # Display the result
    print(f"Bei {address_lines} Adressleitungen für die Adressen {', '.join(map(hex, control_register_addresses))} "
            f"werden {len(ignored_lines)} Adressleitungen ignoriert.")
    print("Kodiert sind:", colored(" & ".join(computed_lines), 'red'))
    print("Nicht kodiert sind:", colored(" & ".join(ignored_lines), 'red'))

generate_address_table(control_register_addresses, address_lines)



"""
KEYWORDS:
Partielle Dekodierung
Adressdekodierung
Ignorierten Adressleitungen
NICHT dekodiert


Gegeben ist ein System mit einem 8bit-Adressbus. Sie untersuchen eine Peripherie und stellen fest, dass sie genau auf den
Adressen 0x42, 0x4A, Ox5A und 0x52 selektiert ist; offensichtlich ein Fall von partieller Adressdekodierung.
Bitte beantworten Sie die folgenden Fragen:
Wieviele der 8 Adressleitungen werden nicht dekodiert bzw. ignoriert

Geben Sie die Nummern der ignorierten Adressleitung(en) an!
Wenn es mehrere Leitungen sind, geben Sie die Nummern aufsteigend, getrennt durch Leerschläge an, z.B. 0 1 2 3 4; Leitung 0 ist wie
üblich das LSB.
"""