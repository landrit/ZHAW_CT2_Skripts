"""
INPUT
"""

hasDatabits = 8
baudRate = 9600
# if you don't know what this is, then don't change it
hasStartbit = True
hasStopbit1 = True
hasStopbit2 = True
hasPritybit = True
"""
END OF INPUT
"""

print(f"{baudRate / (hasDatabits + hasStartbit + hasStopbit1 + hasStopbit2 + hasPritybit)} Bytes/s")
