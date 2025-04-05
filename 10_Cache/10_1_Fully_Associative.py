"""Input"""

cache_size_in_bytes = 64
block_size = 64  # 64-byte blocks
memory_address = "0x1234" # Example memory address in hexadecimal format

"""End Input"""

cache_size = 2 ** cache_size_in_bytes


def fully_associative_cache_addressing(cache_size, block_size, memory_address):
    # Determine the input base (binary, hex, or decimal)
    if memory_address.startswith("0b"):
        memory_address = int(memory_address, 2)
    elif memory_address.startswith("0x"):
        memory_address = int(memory_address, 16)
    else:
        memory_address = int(memory_address)

    # Convert memory address to binary
    memory_address_bin = bin(memory_address)[2:]

    # Calculate the number of blocks in the cache
    num_blocks = cache_size // block_size

    # Calculate the block number
    block_number = int(memory_address_bin, 2) // block_size

    # Calculate the offset within the block
    offset = int(memory_address_bin, 2) % block_size

    # Convert block number and offset to binary
    block_number_bin = bin(block_number)[2:]
    offset_bin = bin(offset)[2:]

    # Calculate the tag
    tag = block_number

    return block_number_bin, tag, offset_bin

block_number_bin, tag, offset_bin = fully_associative_cache_addressing(cache_size_in_bytes, block_size, memory_address)

print("Block Number (binary):", block_number_bin)
print("Tag (decimal):", tag)
print("Offset (binary):", offset_bin)
