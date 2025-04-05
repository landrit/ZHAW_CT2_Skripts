'''Input'''

write_world_length = 32

# if you have no idea, just leave it like this:
minRange = 1
maxRange = 10

'''End Input'''

data_lines_lengths = [2 ** i for i in range(minRange, maxRange + 2)]

print("Write OR Read")
for i in range(minRange, maxRange + 1):
    split: float = write_world_length / data_lines_lengths[i]
    split = 1 if split < 1 else split
    print(f"Für {data_lines_lengths[i]} Datenleitungen wird der Wert in {split:.0f} Teile aufgeteilt.")

"""
Keywords
In wie viel Teile muss der Wert aufgeteilt werden, wenn er über 32 Datenleitungen geschrieben/gelesen werden soll?

"""