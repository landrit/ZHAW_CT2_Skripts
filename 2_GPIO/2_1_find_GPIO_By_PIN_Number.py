"""
INPUT
"""

pin_num_to_find = 118

"""
END INPUT
"""


from GPIO_tools import GPIO
found_port = GPIO.find_port_by_pin_num(pin_num_to_find)

if found_port:
    print(f"Found GPIO port: {found_port.name}, {found_port.pin_name}")
else:
    print(f"No GPIO port found with pin_num {pin_num_to_find}")

"""
KEYWORDS:
GPIO
GPIO port
GPIO pin
"""