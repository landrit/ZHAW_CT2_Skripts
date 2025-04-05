"""
DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING.
USE BY CAUTION.

This file contains the GPIO lists and functions to use GPIOs on the STM32F4 Discovery board.
"""

from tabulate import tabulate


def extract_number_from_string(s):
    return int(s[2:])


class GPIO_PORT:
    def __init__(self, name, pin_name, pin_num=None):
        self.name = name
        self.pin_name = pin_name
        self.pin_num = pin_num
        self.moder = MODER(self.pin_name, self.name)
        self.otyper = OTYPER(self.pin_name, self.name)
        self.ospeedr = OSPEEDR(self.pin_name, self.name)
        self.pupdr = PUPDR(self.pin_name, self.name)
        self.odr = ODR(self.pin_name)
        self.bssr = BSSR(self.pin_name)

    def __str__(self):
        return f"GPIO Port: {self.name}, Pin Name: {self.pin_name}, Pin Number: {self.pin_num} on LQFP144, \n{str(self.moder)} " \
               f"\n{str(self.otyper)} \n{str(self.ospeedr)} \n{str(self.pupdr)} \n{str(self.odr)} \n{str(self.bssr)}"


class GPIO:
    instances = []

    def __init__(self, name, base_addr, end_boundry_adress ,gpio_ports):
        self.name = name
        self.base_addr = base_addr
        self.end_boundry_adress = end_boundry_adress
        self.gpio_ports = gpio_ports
        self.moder_register = self.base_addr + 0x00
        self.otyper_register_addr = base_addr + 0x04
        self.ospeedr_register_addr = base_addr + 0x08
        self.pupdr_register_addr = base_addr + 0x0C
        self.idr_register_addr = base_addr + 0x10
        self.odr_register_addr = base_addr + 0x14
        self.bsrr_register_addr = base_addr + 0x18
        self.lckr_register_addr = base_addr + 0x1C
        self.afrl_register_addr = base_addr + 0x20
        self.afrh_register_addr = base_addr + 0x24
        GPIO.instances.append(self)

    @classmethod
    def find_port_by_pin_num(cls, pin_num):
        for gpio in cls.instances:
            for port in gpio.gpio_ports:
                if port.pin_num == pin_num:
                    return port
        return None

    @classmethod
    def find_port_by_pin_name(cls, pin_name):
        for gpio in cls.instances:
            for port in gpio.gpio_ports:
                if port.pin_name == pin_name:
                    return port
        return None

    @classmethod
    def find_pin_num_by_port(cls, port_name):
        for gpio in cls.instances:
            for port in gpio.gpio_ports:
                if port.pin_name == port_name:
                    return port.pin_num
        return None

    @classmethod
    def find_GPIO_by_port(cls, port_name):
        for gpio in cls.instances:
            for port in gpio.gpio_ports:
                if port.pin_name == port_name:
                    return gpio
        return None

    def get_register_address(self, register_name):
        if register_name == "OTYPER":
            return self.otyper_register_addr
        if register_name == "MODER":
            return self.moder_register
        elif register_name == "OSPEEDR":
            return self.ospeedr_register_addr
        elif register_name == "PUPDR":
            return self.pupdr_register_addr
        elif register_name == "IDR":
            return self.idr_register_addr
        elif register_name == "ODR":
            return self.odr_register_addr
        elif register_name == "BSRR":
            return self.bsrr_register_addr
        elif register_name == "LCKR":
            return self.lckr_register_addr
        elif register_name == "AFRL":
            return self.afrl_register_addr
        elif register_name == "AFRH":
            return self.afrh_register_addr
        else:
            return None


class MODER:
    def __init__(self, gpio_pin_name, gpio_name):
        self.name = "MODER"
        self.read_write = "RW"
        self.bitWidth = 2
        self.gpio_pin_name = gpio_pin_name
        self.set_moder("INPUT", gpio_name)

        parsed_number = extract_number_from_string(gpio_pin_name)
        self.register_bits = f"{2 * parsed_number + 1}..{2 * parsed_number}"
        self.clear_shift = f"~(0x03 << {(self.bitWidth * parsed_number)})"
        self.clear_hex = hex((~(0x03 << (self.bitWidth * parsed_number))) & 0xFFFFFFFF)
        self.clear_c = f"{gpio_name}" + "->" + self.name + " &= " + self.clear_shift + ";"

    def set_moder(self, moder, gpio_name):
        self.moder = moder
        if moder == "INPUT":
            self.binaryValue = 0x00
        elif moder == "OUTPUT":
            self.binaryValue = 0x01
        elif moder == "ALTERNATE":
            self.binaryValue = 0x10
        elif moder == "ANALOG":
            self.binaryValue = 0x11

        self.set_shift = f"{hex(self.binaryValue)} << {self.bitWidth * extract_number_from_string(self.gpio_pin_name)}"
        self.set_hex = hex(
            (self.binaryValue << (self.bitWidth * extract_number_from_string(self.gpio_pin_name))) & 0xFF)
        self.set_c = f"{gpio_name}" + "->" + self.name + " |= " + self.set_shift + ";"

    def __str__(self):
        headers = ["Port Register Name", "Register Bits", "Bit Werte (Binär)", "Modus", "Clear Shift",
                   "Set Shift", "Clear Hex", "Set Hex"]
        data = [
            [self.name, self.register_bits, hex(self.binaryValue), self.moder,
             self.clear_shift, self.set_shift, self.clear_hex, self.set_hex]
        ]
        table_str = tabulate(data, headers=headers)
        return "\n" + table_str + "\n" + "\n" + self.clear_c + "\n" + self.set_c


class OTYPER:
    def __init__(self, gpio_pin_name, gpio_name):
        self.name = "OTYPER"
        self.read_write = "RW"
        self.reset_value = 0x00000000
        self.bitWidth = 1
        self.gpio_pin_name = gpio_pin_name
        self.set_otyper("PUSH_PULL", gpio_name)

        parsed_number = extract_number_from_string(gpio_pin_name)
        self.register_bits = f"{parsed_number}"
        self.clear_shift = f"~(0x01 << {(self.bitWidth * parsed_number)})"
        self.clear_hex = hex((~(0x01 << (self.bitWidth * parsed_number))) & 0xFFFFFFFF)
        self.clear_c = f"{gpio_name}" + "->" + self.name + " &= " + self.clear_shift + ";"

    def set_otyper(self, otyper, gpio_name):
        self.otyper = otyper
        if otyper == "PUSH_PULL":
            self.binaryValue = 0x0
        elif otyper == "OPEN_DRAIN":
            self.binaryValue = 0x1

        self.set_shift = f"{hex(self.binaryValue)} << {self.bitWidth * extract_number_from_string(self.gpio_pin_name)}"
        self.set_hex = hex(
            (self.binaryValue << (self.bitWidth * extract_number_from_string(self.gpio_pin_name))) & 0xFF)
        self.set_c = f"{gpio_name}" + "->" + self.name + " |= " + self.set_shift + ";"

    def __str__(self):
        headers = ["Port Register Name", "Register Bits", "Bit Werte (Binär)", "Typer", "Clear Shift",
                   "Set Shift", "Clear Hex", "Set Hex"]
        data = [
            [self.name, self.register_bits, hex(self.binaryValue), self.otyper,
             self.clear_shift, self.set_shift, self.clear_hex, self.set_hex]
        ]
        table_str = tabulate(data, headers=headers)
        return "\n" + table_str + "\n" + "\n" + self.clear_c + "\n" + self.set_c


class ODR:
    def __init__(self, gpio_pin_name):
        self.name = "ODR"
        self.read_write = "RW"
        self.reset_value = 0x00000000
        self.bitWidth = 1
        self.gpio_pin_name = gpio_pin_name
        self.binaryValue = 0x1

        parsed_number = extract_number_from_string(gpio_pin_name)
        self.register_bits = f"{parsed_number}"
        self.clear_shift = f"~(0x01 << {(self.bitWidth * parsed_number)})"
        self.clear_hex = hex((~(0x01 << (self.bitWidth * parsed_number))) & 0xFFFFFFFF)
        self.set_shift = f"{hex(self.binaryValue)} << {self.bitWidth * extract_number_from_string(self.gpio_pin_name)}"
        self.set_hex = hex(
            (self.binaryValue << (self.bitWidth * extract_number_from_string(self.gpio_pin_name))) & 0xFF)

    def __str__(self):
        headers = ["Port Register Name", "Register Bits", "Bit Werte (Binär)", "Clear Shift",
                   "Set Shift", "Clear Hex", "Set Hex"]
        data = [
            [self.name, self.register_bits, hex(self.binaryValue), self.clear_shift, self.set_shift, self.clear_hex,
             self.set_hex]
        ]
        table_str = tabulate(data, headers=headers)
        return "\n" + table_str


class BSSR:
    def __init__(self, gpio_pin_name):
        self.name = "BSSR"
        self.read_write = "W"
        self.reset_value = 0x00000000
        self.bitWidth = 1
        self.gpio_pin_name = gpio_pin_name

        parsed_number = extract_number_from_string(gpio_pin_name)
        self.register_bits = f"{parsed_number}"
        self.clear_bit = f"0x1 << {(16 + self.bitWidth * parsed_number)}"
        self.clear_bit_hex = hex((~(0x1 << (16 + self.bitWidth * parsed_number))) & 0xFFFFFFFF)
        self.set_bit = f"{hex(0x1)} << {self.bitWidth * extract_number_from_string(self.gpio_pin_name)}"
        self.set_bit_hex = hex((0x1 << (self.bitWidth * extract_number_from_string(self.gpio_pin_name))) & 0xFF)

    def __str__(self):
        headers = ["Port Register Name", "Register Bits", "Clear Bit", "Clear Bit Hex", "Set Bit", "Set Bit Hex"]
        data = [
            [self.name, self.register_bits, self.clear_bit, self.clear_bit_hex, self.set_bit, self.set_bit_hex]
        ]
        table_str = tabulate(data, headers=headers)
        return "\n" + table_str


class OSPEEDR:
    def __init__(self, gpio_pin_name, gpio_name):
        self.name = "OSPEEDR"
        self.read_write = "RW"
        self.bitWidth = 2
        self.gpio_pin_name = gpio_pin_name
        self.set_ospeedr("LOW_SPEED", gpio_name)

        parsed_number = extract_number_from_string(gpio_pin_name)
        self.register_bits = f"{2 * parsed_number + 1}..{2 * parsed_number}"
        self.clear_shift = f"~(0x03 << {(self.bitWidth * parsed_number)})"
        self.clear_hex = hex((~(0x03 << (self.bitWidth * parsed_number))) & 0xFFFFFFFF)
        self.clear_c = f"{gpio_name}" + "->" + self.name + " &= " + self.clear_shift + ";"

    def set_ospeedr(self, ospeedr, gpio_name):
        self.ospeedr = ospeedr
        if ospeedr == "LOW_SPEED":
            self.binaryValue = 0x00
        elif ospeedr == "MEDIUM_SPEED":
            self.binaryValue = 0x01
        elif ospeedr == "HIGH_SPEED":
            self.binaryValue = 0x10
        elif ospeedr == "VERY_HIGH_SPEED":
            self.binaryValue = 0x11

        self.set_shift = f"{hex(self.binaryValue)} << {self.bitWidth * extract_number_from_string(self.gpio_pin_name)}"
        self.set_hex = hex(
            (self.binaryValue << (self.bitWidth * extract_number_from_string(self.gpio_pin_name))) & 0xFF)
        self.set_c = f"{gpio_name}" + "->" + self.name + " |= " + self.set_shift + ";"

    def __str__(self):
        headers = ["Port Register Name", "Register Bits", "Bit Werte (Binär)", "Ospeedr", "Clear Shift",
                   "Set Shift", "Clear Hex", "Set Hex"]
        data = [
            [self.name, self.register_bits, hex(self.binaryValue), self.ospeedr,
             self.clear_shift, self.set_shift, self.clear_hex, self.set_hex]
        ]
        table_str = tabulate(data, headers=headers)
        return "\n" + table_str + "\n" + "\n" + self.clear_c + "\n" + self.set_c


class PUPDR:
    def __init__(self, gpio_pin_name, gpio_name):
        self.name = "PUPDR"
        self.read_write = "RW"
        self.bitWidth = 2
        self.gpio_pin_name = gpio_pin_name
        self.set_pupdr("NO_PULL_UP_DOWN", gpio_name)

        parsed_number = extract_number_from_string(gpio_pin_name)
        self.register_bits = f"{2 * parsed_number + 1}..{2 * parsed_number}"
        self.clear_shift = f"~(0x03 << {(self.bitWidth * parsed_number)})"
        self.clear_hex = hex((~(0x03 << (self.bitWidth * parsed_number))) & 0xFFFFFFFF)
        self.clear_c = f"{gpio_name}" + "->" + self.name + " &= " + self.clear_shift + ";"

    def set_pupdr(self, pupdr, gpio_name):
        self.pupdr = pupdr
        if pupdr == "NO_PULL_UP_DOWN":
            self.binaryValue = 0x00
        elif pupdr == "PULL_UP":
            self.binaryValue = 0x01
        elif pupdr == "PULL_DOWN":
            self.binaryValue = 0x10
        elif pupdr == "RESERVED":
            self.binaryValue = 0x11

        self.set_shift = f"{hex(self.binaryValue)} << {self.bitWidth * extract_number_from_string(self.gpio_pin_name)}"
        self.set_hex = hex(
            (self.binaryValue << (self.bitWidth * extract_number_from_string(self.gpio_pin_name))) & 0xFF)
        self.set_c = f"{gpio_name}" + "->" + self.name + " |= " + self.set_shift + ";"

    def __str__(self):
        headers = ["Port Register Name", "Register Bits", "Bit Werte (Binär)", "PUPDR", "Clear Shift",
                   "Set Shift", "Clear Hex", "Set Hex"]
        data = [
            [self.name, self.register_bits, hex(self.binaryValue), self.pupdr,
             self.clear_shift, self.set_shift, self.clear_hex, self.set_hex]
        ]
        table_str = tabulate(data, headers=headers)
        return "\n" + table_str + "\n" + "\n" + self.clear_c + "\n" + self.set_c


gpios_A = [GPIO_PORT("GPIOA", "PA0", 34),
           GPIO_PORT("GPIOA", "PA1", 35),
           GPIO_PORT("GPIOA", "PA2", 36),
           GPIO_PORT("GPIOA", "PA3", 37),
           GPIO_PORT("GPIOA", "PA4", 40),
           GPIO_PORT("GPIOA", "PA5", 41),
           GPIO_PORT("GPIOA", "PA6", 42),
           GPIO_PORT("GPIOA", "PA7", 43),
           GPIO_PORT("GPIOA", "PA8", 100),
           GPIO_PORT("GPIOA", "PA9", 101),
           GPIO_PORT("GPIOA", "PA10", 102),
           GPIO_PORT("GPIOA", "PA11", 103),
           GPIO_PORT("GPIOA", "PA12", 104),
           GPIO_PORT("GPIOA", "PA13", 105),
           GPIO_PORT("GPIOA", "PA14", 109),
           GPIO_PORT("GPIOA", "PA15", 110)]

gpios_B = [GPIO_PORT("GPIOB", "PB0", 46),
           GPIO_PORT("GPIOB", "PB1", 47),
           GPIO_PORT("GPIOB", "PB2", 48),
           GPIO_PORT("GPIOB", "PB3", 133),
           GPIO_PORT("GPIOB", "PB4", 134),
           GPIO_PORT("GPIOB", "PB5", 135),
           GPIO_PORT("GPIOB", "PB6", 136),
           GPIO_PORT("GPIOB", "PB7", 137),
           GPIO_PORT("GPIOB", "PB8", 139),
           GPIO_PORT("GPIOB", "PB9", 140),
           GPIO_PORT("GPIOB", "PB10", 69),
           GPIO_PORT("GPIOB", "PB11", 70),
           GPIO_PORT("GPIOB", "PB12", 73),
           GPIO_PORT("GPIOB", "PB13", 74),
           GPIO_PORT("GPIOB", "PB14", 75),
           GPIO_PORT("GPIOB", "PB15", 76)]

gpios_C = [GPIO_PORT("GPIOC", "PC0", 26),
           GPIO_PORT("GPIOC", "PC1", 27),
           GPIO_PORT("GPIOC", "PC2", 28),
           GPIO_PORT("GPIOC", "PC3", 29),
           GPIO_PORT("GPIOC", "PC4", 44),
           GPIO_PORT("GPIOC", "PC5", 45),
           GPIO_PORT("GPIOC", "PC6", 96),
           GPIO_PORT("GPIOC", "PC7", 97),
           GPIO_PORT("GPIOC", "PC8", 98),
           GPIO_PORT("GPIOC", "PC9", 99),
           GPIO_PORT("GPIOC", "PC10", 111),
           GPIO_PORT("GPIOC", "PC11", 112),
           GPIO_PORT("GPIOC", "PC12", 113),
           GPIO_PORT("GPIOC", "PC13", 7),
           GPIO_PORT("GPIOC", "PC14", 8),
           GPIO_PORT("GPIOC", "PC15", 9)]

gpios_D = [GPIO_PORT("GPIOD", "PD0", 114),
           GPIO_PORT("GPIOD", "PD1", 115),
           GPIO_PORT("GPIOD", "PD2", 116),
           GPIO_PORT("GPIOD", "PD3", 117),
           GPIO_PORT("GPIOD", "PD4", 118),
           GPIO_PORT("GPIOD", "PD5", 119),
           GPIO_PORT("GPIOD", "PD6", 122),
           GPIO_PORT("GPIOD", "PD7", 123),
           GPIO_PORT("GPIOD", "PD8", 77),
           GPIO_PORT("GPIOD", "PD9", 78),
           GPIO_PORT("GPIOD", "PD10", 79),
           GPIO_PORT("GPIOD", "PD11", 80),
           GPIO_PORT("GPIOD", "PD12", 81),
           GPIO_PORT("GPIOD", "PD13", 82),
           GPIO_PORT("GPIOD", "PD14", 85),
           GPIO_PORT("GPIOD", "PD15", 86)]

gpios_E = [GPIO_PORT("GPIOE", "PE0", 141),
           GPIO_PORT("GPIOE", "PE1", 142),
           GPIO_PORT("GPIOE", "PE2", 1),
           GPIO_PORT("GPIOE", "PE3", 2),
           GPIO_PORT("GPIOE", "PE4", 3),
           GPIO_PORT("GPIOE", "PE5", 4),
           GPIO_PORT("GPIOE", "PE6", 5),
           GPIO_PORT("GPIOE", "PE7", 58),
           GPIO_PORT("GPIOE", "PE8", 59),
           GPIO_PORT("GPIOE", "PE9", 60),
           GPIO_PORT("GPIOE", "PE10", 63),
           GPIO_PORT("GPIOE", "PE11", 64),
           GPIO_PORT("GPIOE", "PE12", 65),
           GPIO_PORT("GPIOE", "PE13", 66),
           GPIO_PORT("GPIOE", "PE14", 67),
           GPIO_PORT("GPIOE", "PE15", 68)]

gpios_F = [
    GPIO_PORT("GPIOF", "PF0", 10),
    GPIO_PORT("GPIOF", "PF1", 11),
    GPIO_PORT("GPIOF", "PF2", 12),
    GPIO_PORT("GPIOF", "PF3", 13),
    GPIO_PORT("GPIOF", "PF4", 14),
    GPIO_PORT("GPIOF", "PF5", 15),
    GPIO_PORT("GPIOF", "PF6", 18),
    GPIO_PORT("GPIOF", "PF7", 19),
    GPIO_PORT("GPIOF", "PF8", 20),
    GPIO_PORT("GPIOF", "PF9", 21),
    GPIO_PORT("GPIOF", "PF10", 22),
    GPIO_PORT("GPIOF", "PF11", 49),
    GPIO_PORT("GPIOF", "PF12", 50),
    GPIO_PORT("GPIOF", "PF13", 53),
    GPIO_PORT("GPIOF", "PF14", 54),
    GPIO_PORT("GPIOF", "PF15", 55)
]

gpios_G = [
    GPIO_PORT("GPIOG", "PG0", ),
    GPIO_PORT("GPIOG", "PG1", ),
    GPIO_PORT("GPIOG", "PG2", 87),
    GPIO_PORT("GPIOG", "PG3", 88),
    GPIO_PORT("GPIOG", "PG4", 89),
    GPIO_PORT("GPIOG", "PG5", 90),
    GPIO_PORT("GPIOG", "PG6", 91),
    GPIO_PORT("GPIOG", "PG7", 92),
    GPIO_PORT("GPIOG", "PG8", 93),
    GPIO_PORT("GPIOG", "PG9", 124),
    GPIO_PORT("GPIOG", "PG10", 125),
    GPIO_PORT("GPIOG", "PG11", 126),
    GPIO_PORT("GPIOG", "PG12", 127),
    GPIO_PORT("GPIOG", "PG13", 128),
    GPIO_PORT("GPIOG", "PG14", 129),
    GPIO_PORT("GPIOG", "PG15", 132)
]

gpios_H = [
    GPIO_PORT("GPIOH", "PH0", 23),
    GPIO_PORT("GPIOH", "PH1", 24),
    GPIO_PORT("GPIOH", "PH2", ),
    GPIO_PORT("GPIOH", "PH3", ),
    GPIO_PORT("GPIOH", "PH4", ),
    GPIO_PORT("GPIOH", "PH5", ),
    GPIO_PORT("GPIOH", "PH6", ),
    GPIO_PORT("GPIOH", "PH7", ),
    GPIO_PORT("GPIOH", "PH8", ),
    GPIO_PORT("GPIOH", "PH9", ),
    GPIO_PORT("GPIOH", "PH10", ),
    GPIO_PORT("GPIOH", "PH11", ),
    GPIO_PORT("GPIOH", "PH12", ),
    GPIO_PORT("GPIOH", "PH13", ),
    GPIO_PORT("GPIOH", "PH14", ),
    GPIO_PORT("GPIOH", "PH15", )
]

gpios_I = [
    GPIO_PORT("GPIOI", "PI0", ),
    GPIO_PORT("GPIOI", "PI1", ),
    GPIO_PORT("GPIOI", "PI2", ),
    GPIO_PORT("GPIOI", "PI3", ),
    GPIO_PORT("GPIOI", "PI4", ),
    GPIO_PORT("GPIOI", "PI5", ),
    GPIO_PORT("GPIOI", "PI6", ),
    GPIO_PORT("GPIOI", "PI7", ),
    GPIO_PORT("GPIOI", "PI8", ),
    GPIO_PORT("GPIOI", "PI9", ),
    GPIO_PORT("GPIOI", "PI10", ),
    GPIO_PORT("GPIOI", "PI11", ),
    GPIO_PORT("GPIOI", "PI12", ),
    GPIO_PORT("GPIOI", "PI13", ),
    GPIO_PORT("GPIOI", "PI14", ),
    GPIO_PORT("GPIOI", "PI15", )
]

gpios_J = [
    GPIO_PORT("GPIOJ", "PJ0", ),
    GPIO_PORT("GPIOJ", "PJ1", ),
    GPIO_PORT("GPIOJ", "PJ2", ),
    GPIO_PORT("GPIOJ", "PJ3", ),
    GPIO_PORT("GPIOJ", "PJ4", ),
    GPIO_PORT("GPIOJ", "PJ5", ),
    GPIO_PORT("GPIOJ", "PJ6", ),
    GPIO_PORT("GPIOJ", "PJ7", ),
    GPIO_PORT("GPIOJ", "PJ8", ),
    GPIO_PORT("GPIOJ", "PJ9", ),
    GPIO_PORT("GPIOJ", "PJ10", ),
    GPIO_PORT("GPIOJ", "PJ11", ),
    GPIO_PORT("GPIOJ", "PJ12", ),
    GPIO_PORT("GPIOJ", "PJ13", ),
    GPIO_PORT("GPIOJ", "PJ14", ),
    GPIO_PORT("GPIOJ", "PJ15", )
]

gpios_K = [
    GPIO_PORT("GPIOK", "PK0", ),
    GPIO_PORT("GPIOK", "PK1", ),
    GPIO_PORT("GPIOK", "PK2", ),
    GPIO_PORT("GPIOK", "PK3", ),
    GPIO_PORT("GPIOK", "PK4", ),
    GPIO_PORT("GPIOK", "PK5", ),
    GPIO_PORT("GPIOK", "PK6", ),
    GPIO_PORT("GPIOK", "PK7", ),
    GPIO_PORT("GPIOK", "PK8", ),
    GPIO_PORT("GPIOK", "PK9", ),
    GPIO_PORT("GPIOK", "PK10", ),
    GPIO_PORT("GPIOK", "PK11", ),
    GPIO_PORT("GPIOK", "PK12", ),
    GPIO_PORT("GPIOK", "PK13", ),
    GPIO_PORT("GPIOK", "PK14", ),
    GPIO_PORT("GPIOK", "PK15", )
]

gpio_A = GPIO("GPIOA", 0x40020000, 0x400203FF, gpios_A)
gpio_B = GPIO("GPIOB", 0x40020400, 0x400207FF, gpios_B)
gpio_C = GPIO("GPIOC", 0x40020800, 0x40020BFF, gpios_C)
gpio_D = GPIO("GPIOD", 0x40020C00, 0x40020FFF, gpios_D)
gpio_E = GPIO("GPIOE", 0x40021000, 0x400213FF, gpios_E)
gpio_F = GPIO("GPIOF", 0x40021400, 0x400217FF, gpios_F)
gpio_G = GPIO("GPIOG", 0x40021800, 0x40021BFF, gpios_G)
gpio_H = GPIO("GPIOH", 0x40021C00, 0x40021FFF, gpios_H)
gpio_I = GPIO("GPIOI", 0x40022000, 0x400223FF, gpios_I)
gpio_J = GPIO("GPIOJ", 0x40022400, 0x400227FF, gpios_J)
gpio_K = GPIO("GPIOK", 0x40022800, 0x40022BFF, gpios_K)
