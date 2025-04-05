"""
INPUT
"""

deviceToFind = "Device4"
datenBusGroesse = 16  # Datenbus Größe in Bit (Extern)

anzahlAdressleitungen = 15  # Anzahl Adressleitungen
anzahlMemories = 2  # Anzahl Memories

# Calculate the number of different addresses that can be addressed
# FMC address range for Device 4: 2^26 Bytes (internal addresses A25 to AO)
# Size of the two memories together: 2 * 2^15 = 2^16
# = 2^26 / 2^16 = 2^10 = 1024 different addresses

# Total address range of FMC for each device (bruder wenn nöd weisch was du machsch, denn lahn so und seg bismillah, amin)
total_address_range = 2 ** 26

"""
END OF INPUT
"""

initMemories = {
    "Device1": {
        "start": 0x60000000,
        "end": 0x63FFFFFF
    },
    "Device2": {
        "start": 0x64000000,
        "end": 0x67FFFFFF
    },
    "Device3": {
        "start": 0x68000000,
        "end": 0x6BFFFFFF
    },
    "Device4": {
        "start": 0x6C000000,
        "end": 0x6FFFFFFF,
    }
}


# Calculate end address for different external data bus sizes
def calculate_end_address(start, datenBusGroesse):
    # Convert bus size from bits to bytes (1 byte = 8 bits)
    bitsToSubtract = 0
    if datenBusGroesse == 8:
        # All 32 bits are used
        bitsToSubtract = 1
    elif datenBusGroesse == 16:
        # Only the first 31 bits are used, the last bit is always 0
        bitsToSubtract = 2
    elif datenBusGroesse == 32:
        # Only the first 30 bits are used, the last 2 bits are always 0
        bitsToSubtract = 3
    return start + (anzahlMemories * 2 ** anzahlAdressleitungen) - bitsToSubtract


# Find the start address of the device
start = initMemories[deviceToFind]["start"]

# Calculate end address
end = calculate_end_address(start, datenBusGroesse)

print(f"RAM_BASE_ADDRESS for {deviceToFind} is {hex(start)}")
print(f"RAM_END_ADDRESS for {deviceToFind} given the data bus size is {hex(end)}")


# Calculate the number of different addresses that can be addressed in software
def calculate_different_addresses(total_address_range):
    groesseDerMemories = anzahlMemories * 2 ** anzahlAdressleitungen
    total_address_range = total_address_range // groesseDerMemories
    print(f"Total address range of FMC for each device: {total_address_range} unterschiedliche Adressen")


calculate_different_addresses(total_address_range)

"""
Keywords:
#define RAM BASE ADDRESS XXXX
#define RAM END ADDRESS УУУУ


void mem init (void){
    volatile uint16_t *mem ptr;
    mem_ptr = RAM_BASE_ADDRESS;
    while (mem ptr <= RAM END ADDRESS) {
        *mem ptr = 0;
        mem_ptr++;
    }
}

Welche Werte müssen für die Platzhalter xxxx und yyyy eingesetzt werden?

Keine Speicherstelle soll mehrfach beschrieben werden.

d) Unter wie vielen unterschiedlichen Adressen können Sie ein einzelnes 16-bit half-word
in den Memories in Software ansprechen?

Zwei dieser SRAMs sollen gemeinsam an den SRAM Bereich des 'Flexible Memory Controllers' des STM32F429 angeschlossen werden. Dabei sollen sie zusammen ein Memory mit 16-Bit breitem Datenbus bilden. Das Memory soll unter 'Device 3' (NE3) gemäss untenstehender Darstellung angeschlossen werden. Die obersten 6 Bit der internen Adressen werden wie folgt kodiert:
Das Memory wird mit der folgenden C-Sequenz vollständig initialisiert.
Welche Werte müssen für die Platzhalter xxxx und yyyy eingesetzt werden?
Keine Speicherstelle soll mehrfach beschrieben werden.

Die Memories werden mit der Funktion mem_init() vollständig initialisiert.
Welche Werte müssen für die Platzhalter xxxx und yyyy eingesetzt werden?
Keine Speicherstelle soll mehrfach beschrieben werden.
Gegeben ist der folgende 'asynchronous SRAM' Baustein.

"""
