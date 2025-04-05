"""INPUT"""

inputBits = "1011001000" # Input muss mindestens 10 Stellen haben (einfach mit 0 auffüllen)

"""END INPUT"""

# todo: komplette SDA angeben inkl. start von SCL
# todo: plot erzeugen

addressBits = inputBits[0:7]
isRead = "write" if inputBits[7] == "0" else "read"
dataBits = inputBits[9:]
ackBit = True if inputBits[-1] == "0" else False


# print read or write
print("Read/Write: " + isRead)

print("Daten vom Slave korrekt empfangen? " + str(ackBit))

# print adressBits as bit, hex, and decimal
print(f"""Address:
    Bits: {addressBits}
    Hex: {hex(int(addressBits, 2))}
    Decimal: {int(addressBits, 2)}""")


# print dataBits as bit, hex, and decimal
print(f"")
print(f"""Data:
    Bits: {dataBits}
    Hex: {hex(int(dataBits, 2))}
    Decimal: {int(dataBits, 2)}""")

# print out everything in binary
print(f"")
print(f"""Full input:
    Bits: {inputBits}
    Hex: {hex(int(inputBits, 2))}
    Decimal: {int(inputBits, 2)}""")