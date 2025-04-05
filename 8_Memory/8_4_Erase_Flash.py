"""INPUT"""
oldValue = "0xC3"
newValue = "0xF2"

"""END INPUT"""

# mit erase wird alles auf 1 gesetzt
valAsBinary = format(int(newValue, 16), 'b').zfill(8)
print(f"Mit Erase:")
print(f"{newValue} -> {valAsBinary}")

# ohne erase wird nur 1 -> 0 gesetzt
valAsBinary = format(int(newValue, 16), 'b').zfill(8)
oldValAsBinary = format(int(oldValue, 16), 'b').zfill(8)

result = ""
for i in range(len(valAsBinary)):
    if valAsBinary[i] == "1" and oldValAsBinary[i] == "0":
        result += "0"
    else:
        result += valAsBinary[i]

print(f"Ohne Erase:")
print(f"oldValue:  0b{format(int(oldValue, 16), 'b').zfill(8)} ({oldValue})")
print(f"newValue:  0b{format(int(newValue, 16), 'b').zfill(8)} ({newValue})")
print(f"result:    0b{result} ({hex(int(result, 2))})")
