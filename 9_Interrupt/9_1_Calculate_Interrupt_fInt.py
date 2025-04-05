"""
INPUT
"""

baudrate = None  # in hz
interruptOneveryXBit = 8
interruptServiceTime = 6  # in us (microseconds) (Tisr)
fInt = 20  # Interrupts per second (fInt) SET IF BAUDRATE IS NOT SET

"""
END INPUT
"""


def calculate_fInt(baudrate, interruptOneveryXBit):
    return baudrate / interruptOneveryXBit


if baudrate is not None:
    fInt = calculate_fInt(baudrate, interruptOneveryXBit)

impact = (interruptServiceTime / 10 ** 6) * fInt * 100

output_text = f"fInt = Interrupts per second: {fInt}"
output_text += f"\nTisr = Interrupt Service Time: {interruptServiceTime} us"
print(output_text)
print(f"impact = {impact} %")
