"""INPUT"""

blocksizeBytes = 64  # Cache with a block size of x Bytes.
sizeAddressesBits = 24  # The address space comprises x Bit
sizeDataBits = 8 # CPU reads data in x-bit units
zeilen = 32  # The cache has x lines

"""END INPUT"""

import math

def calculate_memory_size(sizeAddressesBits, sizeDataBits):
    numAddresses = 2 ** sizeAddressesBits
    memorySizeBytes = numAddresses * (sizeDataBits / 8)
    return memorySizeBytes

def calculate_num_blocks(memorySizeBytes, blocksizeBytes):
    return memorySizeBytes / blocksizeBytes

def calculate_offsetBits(blocksizeBytes):
    return math.log(blocksizeBytes, 2)

def calculate_addressBitsPerBlock(numBlocks):
    return int(math.log(numBlocks, 2))

def calculate_indexBits(zeilen):
    return math.log(zeilen, 2)

memorySizeBytes = calculate_memory_size(sizeAddressesBits, sizeDataBits)
print(f"Memory Size: {memorySizeBytes} (2^{math.log(memorySizeBytes, 2)}) Bytes")

numBlocks = calculate_num_blocks(memorySizeBytes, blocksizeBytes)
offsetBits = calculate_offsetBits(blocksizeBytes)
print(f"Block Size: {blocksizeBytes} (2^{offsetBits}) Bytes")

addressBitsPerBlock = calculate_addressBitsPerBlock(numBlocks)
print(f"Number of address bits needed to uniquely identify a block: {addressBitsPerBlock} (2^{addressBitsPerBlock})")

print("=========================================================================================================")
print("\nDirect Mapped Cache")

indexBits = calculate_indexBits(zeilen)
tagBits = sizeAddressesBits - indexBits - offsetBits
offsetBits = int(sizeAddressesBits-1-tagBits-indexBits)
print(f"Tag Bits: {tagBits} (2^{tagBits})")
print(f"Index Bits: {indexBits} (2^{indexBits})")
print(f"Cache Size: {zeilen * blocksizeBytes} (2^{math.log(zeilen * blocksizeBytes, 2)}) Bytes")
print(f"Offset Size: {offsetBits + 1}")
print(f"Address [{sizeAddressesBits-1}:0] = Tag [{sizeAddressesBits-1}:{int(sizeAddressesBits-1-tagBits+1)}] + Index [{int(sizeAddressesBits-1-tagBits)}:{int(sizeAddressesBits-1-tagBits-indexBits+1)}] + Offset [{offsetBits}:0]")

print("=========================================================================================================")
print("\nFully Associative Cache")

offsetBits = calculate_offsetBits(blocksizeBytes)  # Offset is determined by the block size
tagBits = sizeAddressesBits - offsetBits  # Tag is whatever remains of the address after offset
print(f"Tag Bits: {tagBits} (2^{tagBits})")
print(f"Offset Bits: {offsetBits} (2^{offsetBits})")
print(f"Cache Size: {numBlocks * blocksizeBytes} (2^{math.log(numBlocks * blocksizeBytes, 2)}) Bytes")
print(f"Address [{sizeAddressesBits-1}:0] = Tag [{sizeAddressesBits-1}:{int(sizeAddressesBits-1-offsetBits+1)}] + Offset [{int(sizeAddressesBits-1-offsetBits)}:0]")

print("=========================================================================================================")
print("\nN-Way Set Associative Cache")

numSets = zeilen / 2
indexBits = calculate_indexBits(numSets)
tagBits = sizeAddressesBits - offsetBits - indexBits
print(f"Number of sets: {numSets}")
print(f"Tag Bits: {tagBits} (2^{tagBits})")
print(f"Index Bits: {indexBits} (2^{indexBits})")
print(f"Cache Size: {numBlocks * blocksizeBytes} (2^{math.log(numBlocks * blocksizeBytes, 2)}) Bytes")
print(f"Offset Bits: {offsetBits} (2^{offsetBits})")
print(f"Address [{sizeAddressesBits-1}:0] = Tag [{sizeAddressesBits-1}:{int(sizeAddressesBits-1-tagBits+1)}] + Index [{int(sizeAddressesBits-1-tagBits)}:{int(sizeAddressesBits-1-tagBits-indexBits+1)}] + Offset [{int(sizeAddressesBits-1-tagBits-indexBits)}:0]")


"""
Keyword

Gegeben sei ein Cache mit einer Blockgrösse von 64 Bytes.

Der Adressraum umfasst 24 Bit, die CPU liest Daten in 8-Bit Einheiten.

a) Wie viele Adressbits werden benötigt, um einen Block eindeutig zu identifizieren?

b) Der Cache umfasst 32 Zeilen. Wie teilen sich in einem «direct mapped» Cache die oben bestimmten Bits zwischen Tag und Index auf? Welche Grösse hat der Cache?

c) Wie sieht die Aufteilung in einem «fully associative» Cache aus?

"""