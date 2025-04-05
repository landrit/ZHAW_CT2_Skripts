"""
INPUT
"""

isLittleEndian = False  # True: Little Endian, False: Big Endian
hexValue = 0x11223344
registerStartAddress = 0x6100ABC8  # 0x6100

"""
END OF INPUT
"""

for i in range(4):
    if isLittleEndian:
        print("0x{:08X}".format(registerStartAddress + i), "0x{:02X}".format(hexValue & 0xFF))
    else:
        print("0x{:08X}".format(registerStartAddress + 3 - i), "0x{:02X}".format(hexValue & 0xFF))
    hexValue = hexValue >> 8
