"""Input"""

input_in_CMOS = 1
enable = 0

""" End of Input"""


class TriStateCMOSInverter:
    def __init__(self):
        self.enable = 0
        self.in_value = 0
        self.out_value = 'Z'

    def set_input(self, value):
        self.in_value = value
        self.update_output()

    def set_enable(self, value):
        self.enable = value
        self.update_output()

    def update_output(self):
        if self.enable == 1:
            self.out_value = int(not self.in_value)
        else:
            self.out_value = 'Z'

    def get_output(self):
        return self.out_value


inverter = TriStateCMOSInverter()
inverter.set_input(input_in_CMOS)
inverter.set_enable(enable)

print("Input: {}, Enable: {}, Out: {}".format(input_in_CMOS, enable, inverter.get_output()))

if enable == 0:
    print("Output is high impedance (hochohmig) and the driver is disconnected")

"""
KEYWORDS:
TriState CMOS Inverter
Transistor
p-type
n-type
"""