"""
INPUT
"""
clock_frequency_khz = 100

"""
END INPUT
"""


def bit_cell_duration(frequency_khz):
    frequency_hz = frequency_khz * 1000
    period_s = 1 / frequency_hz
    period_ms = period_s * 1000
    return period_ms


duration = bit_cell_duration(clock_frequency_khz)

print(f"Bit cell duration for {clock_frequency_khz} kHz clock frequency: {duration} ms")
