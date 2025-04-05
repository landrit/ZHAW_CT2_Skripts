"""Input"""

input_in_CMOS = 1

""" End of Input"""


class CMOSInverter:
    def __init__(self):
        self.p_type = 1
        self.n_type = 0

    def simulate(self, input_value):
        if input_value == 0:
            self.p_type = 1
            self.n_type = 0
        elif input_value == 1:
            self.p_type = 0
            self.n_type = 1
        else:
            raise ValueError("Input value must be 0 or 1.")


inverter = CMOSInverter()
inverter.simulate(input_in_CMOS)

print(f"Bei CMOS Inverter Input {input_in_CMOS}, sind p-Typ {inverter.p_type} und n-Typ {inverter.n_type}.")


"""
KEYWORDS:
CMOS Inverter
Transistor
p-type
n-type
"""