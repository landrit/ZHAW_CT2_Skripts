"""
FIXME: THIS IS NOT WORKING CORRECTLY BUT IT'S CLOSE

INPUT
"""

# Test with given SCLK, MOSI, and MISO sequences
sclk = [1, 1, 1, 0, 1, 0, 1, 1]
mosi = [1, 0, 1, 1, 1, 1, 0, 0]
miso = [0, 1, 0, 0, 0, 0, 1, 1]

"""
END INPUT
"""


def determine_cpol_cpha(sclk, mosi, miso):
    if not sclk or not mosi or not miso:
        raise ValueError("SCLK, MOSI, and MISO sequences must not be empty.")

    if len(sclk) != len(mosi) or len(sclk) != len(miso):
        raise ValueError("SCLK, MOSI, and MISO sequences must have the same length.")

    cpol = int(sclk[0])
    cpha = 0

    for i in range(len(sclk) - 1):
        if sclk[i] != sclk[i + 1]:
            if mosi[i] != mosi[i + 1] or miso[i] != miso[i + 1]:
                cpha = 1
                break

    return cpol, cpha




cpol, cpha = determine_cpol_cpha(sclk, mosi, miso)

print(f"CPOL: {cpol}, CPHA: {cpha}")
