"""
INPUT
"""

port_name_to_find = "GPD4"

"""
END INPUT
"""

port_name_to_find = port_name_to_find.replace("G", "").upper()

from GPIO_tools import GPIO

found_pin_num = GPIO.find_pin_num_by_port(port_name_to_find)

if found_pin_num:
    print(f"Found pin number for GPIO port {port_name_to_find}: {found_pin_num}")
else:
    print(f"No pin number found for GPIO port {port_name_to_find}")

"""
KEYWORDS:
GPIO
GPIO port
GPIO pin
"""