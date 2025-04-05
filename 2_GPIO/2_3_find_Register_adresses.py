"""
INPUT
"""

allRegisters = ["MODER", "OTYPER", "OSPEEDR", "PUPDR", "IDR", "ODR", "BSRR", "LCKR", "AFRL", "AFRH"]
gpio_name_to_find = "D"

"""
END INPUT
"""
gpio_name_to_find = "GPIO" + gpio_name_to_find


from GPIO_tools import GPIO

# Find the GPIO instance with the specified name
gpio_instance = next((gpio for gpio in GPIO.instances if gpio.name == gpio_name_to_find), None)

if gpio_instance:
    for register_name_to_find in allRegisters:
        register_address = gpio_instance.get_register_address(register_name_to_find)

        if register_address:
            print(f"Base Address {gpio_name_to_find:20} 0x{gpio_instance.base_addr:08X} - 0x{gpio_instance.end_boundry_adress:08X}")
            print(f"Offset {register_name_to_find:26} 0x{register_address - gpio_instance.base_addr:08X}")
            print("-" * 50)
            print(f"Register Address {(' ' * 16)} 0x{register_address:08X}")
            print("\n")  # Add a newline for better formatting between register outputs
        else:
            print(f"Register {register_name_to_find} not found")
else:
    print(f"{gpio_name_to_find} not found")

#Todo: keywords
"""
"""