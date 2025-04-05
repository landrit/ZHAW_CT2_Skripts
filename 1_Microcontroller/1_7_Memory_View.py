"""
Input
"""
address = 0xC8887744 # z.b.A[31:0] the starting adress usally on the left side of the diagram
datalines = 0xBB44CC33 # z.b. D[31:0] the starting adress usally on the left side of the diagram

withNBL = False  # Set false if all NBL lines are high
nbl = [0, 0, 1, 0]  # and it goes NBL[0, 1, 2, 3] => 1 if you want to show them

"""
End of Input
"""

b = bytearray(datalines.to_bytes(4, byteorder='big'))
mv = memoryview(b)

if not withNBL:
    print("without NBL")
    print("===THIS IS LITTLE ENDIAN!===")
    print(f"{'Memory':^12} | {'Value':^6} | {'Datalines':^10}")
    print('-' * 37)
    for i in range(len(mv)):
        mem = f"0x{address + i:08X}"
        val = f"0x{mv[len(mv) - i - 1]:02X}"
        d = f"D[{i * 8 + 7}:{i * 8}]"
        print(f"{mem:>12} | {val:>6} | {d:>10}")

    def print_binary_values(value, end):
        binary_value = bin(value)[2:].zfill(8)
        bitVal = ''
        for i, bit in enumerate(binary_value):
            bitVal += bit
            print(f"D[{end - i}] = {bit}")
        print(bitVal)

    for i in range(len(mv)):
        val = mv[len(mv) - i - 1]
        start = i * 8
        end = start + 7
        print(f"\nDataline D[{end}:{start}] contains 0x{val:02X}")
        print_binary_values(val, end)

if withNBL:
    print("with NBL")

    def save_values_with_nbl(address, datalines, nbl):
        saved_values = []
        for i, active in enumerate(nbl):
            if active:
                mem = address + i
                val = datalines[len(datalines) - i - 1]
                d = f"D[{i * 8 + 7}:{i * 8}]"
                saved_values.append((mem, val, d))
        return saved_values

    saved_values = save_values_with_nbl(address, mv, nbl)
    print("Saved values with active NBLs:")
    print(f"{'Memory':^12} | {'Value':^6} | {'Datalines':^10}")
    print('-' * 37)
    for mem, val, d in saved_values:
        print(f"0x{mem:08X} | 0x{val:02X} | {d:>10}")




"""
KEYWORDS
Buszugriff
Gegeben ist das folgende Diagramm eines Buszugriffs

Tragen Sie alle Bytes des Read-Zugriffs in die untenstehende Tabelle ein. Geben Sie für jedes Byte die Adresse und den gelesenen Wert an;
der Prozessor ist little endian
Adresse (aufsteigend) Daten-Bvte
0x70001235
0X/0001236
UX70001237 0x01
Verwenden Sie für Adressen die folgende Form: Ox..... (achtstellige Hexzahl, Zeichen 0 bis F,
Verwenden Sie für Daten die folgende Form: Ox.. (zweistellige Hexzahl, Zeichen 0 bis F)

Gegeben sind die folgenden Buszugriffe
Welcher Zugriff führt welche Operation aus?
Zeichnen Sie die Memory Map nach dem Schreibtugriff.

Gegeben sind die folgenden Buszugriffe mit 32-bit breiten Daten.
Tragen Sie alle Bytes, welche durch den oben gezeigten 'write access' verändert wer- den in der folgenden Tabelle ein. Geben Sie für jedes Byte die Adresse und den ge- schriebenen Wert an. Der Prozessor ist little endian.
"""