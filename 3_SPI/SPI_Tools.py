"""
DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING.
USE BY CAUTION.

This file contains the SPI classes and functions to use SPI on the STM32F4 Discovery board.
"""


class SPI:
    instances = []

    def __init__(self, name, base_addr):
        self.name = name
        self.base_addr = base_addr
        self.CR1 = CONTROL_REGISTER_1(self.name)
        self.CR2 = CONTROL_REGISTER_2(self.name)
        self.SR = STATUS_REGISTER(self.name)
        self.DR = DATA_REGISTER(self.name)
        SPI.instances.append(self)

    def configure_cr1(self, cr1_values):
        self.CR1.generate_c_code_cr1(cr1_values)

    def configure_cr1_bit_field(self, field_name, value):
        self.CR1.generate_c_code_for_bit_field_cr1(field_name, value)

    def reset_cr1(self):
        self.CR1.reset_cr1()

    def configure_cr2(self, cr2_values):
        self.CR2.generate_c_code_cr2(cr2_values)

    def configure_cr2_bit_field(self, field_name, value):
        self.CR2.generate_c_code_for_bit_field_cr2(field_name, value)

    def reset_cr2(self):
        self.CR2.reset_cr2()

    def configure_SR(self, SR_values):
        self.SR.generate_c_code_SR(SR_values)

    def configure_SR_bit_field(self, field_name, value):
        self.SR.generate_c_code_for_bit_field_SR(field_name, value)

    def reset_SR(self):
        self.SR.reset_SR()

    def configure_DR(self, DR_values):
        self.DR.generate_c_code_DR(DR_values)

    def configure_DR_bit_field(self, field_name, value):
        self.DR.generate_c_code_for_bit_field_DR(field_name, value)

    def reset_DR(self):
        self.DR.reset_DR()


class CONTROL_REGISTER_1:
    def __init__(self, spi_name):
        self.name = "CR1"
        self.read_write = "RW"
        self.spi_name = spi_name
        self.offset = 0x00
        self.reset_value = 0x0000
        self.bit_fields = [
            ("CPHA", 0, 0),
            ("CPOL", 1, 1),
            ("MSTR", 2, 2),
            ("BR", 3, 5),
            ("SPE", 6, 6),
            ("LSBFIRST", 7, 7),
            ("SSI", 8, 8),
            ("SSM", 9, 9),
            ("RXONLY", 10, 10),
            ("DFF", 11, 11),
            ("CRCNEXT", 12, 12),
            ("CRCEN", 13, 13),
            ("BIDIOE", 14, 14),
            ("BIDIMODE", 15, 15),
        ]

    def reset_cr1(self):
        c_code = f"{self.spi_name}->CR1 = {hex(self.reset_value)};"
        notification = "Make sure to reset the CR1 registers before using!! like this 🫠:  " + c_code
        print(notification)

    def generate_c_code_cr1(self, cr1_values):
        c_code = f"{self.spi_name}->CR1 |= "
        value = 0
        for field, start_bit, end_bit in self.bit_fields:
            value |= cr1_values[field] << start_bit
        c_code += f"0x{value:04X};"
        print(c_code)

    def generate_c_code_for_bit_field_cr1(self, field_name, value):
        bit_field = next((f for f in self.bit_fields if f[0] == field_name), None)
        if bit_field is None:
            raise ValueError(f"Invalid field name: {field_name}")

        field, start_bit, end_bit = bit_field
        c_code = f"{self.spi_name}->CR1 |= ({hex(value)} << {start_bit});"
        print(c_code)


class CONTROL_REGISTER_2:
    def __init__(self, spi_name):
        self.name = "CR2"
        self.read_write = "RW"
        self.spi_name = spi_name
        self.offset = 0x04
        self.reset_value = 0x0000
        self.bit_fields = [
            ("RXDMAEN", 0, 0),
            ("TXDMAEN", 1, 1),
            ("SSOE", 2, 2),
            ("Reserved (NSSP)", 3, 3),
            ("FRF", 4, 4),
            ("ERRIE", 5, 5),
            ("RXNEIE", 6, 6),
            ("TXEIE", 7, 7),
        ]

    def reset_cr2(self):
        c_code = f"{self.spi_name}->CR2 = {hex(self.reset_value)};"
        notification = "Make sure to reset the CR2 registers before using!! like this 🫠:  " + c_code
        print(notification)

    def generate_c_code_cr2(self, cr2_values):
        c_code = f"{self.spi_name}->CR2 |= "
        value = 0
        for field, start_bit, end_bit in self.bit_fields:
            value |= cr2_values[field] << start_bit
        c_code += f"0x{value:04X};"
        print(c_code)

    def generate_c_code_for_bit_field_cr2(self, field_name, value):
        bit_field = next((f for f in self.bit_fields if f[0] == field_name), None)
        if bit_field is None:
            raise ValueError(f"Invalid field name: {field_name}")

        field, start_bit, end_bit = bit_field
        c_code = f"{self.spi_name}->CR2 |= ({hex(value)} << {start_bit});"
        print(c_code)


class STATUS_REGISTER:
    def __init__(self, spi_name):
        self.name = "SR"
        self.read_write = "R"
        self.spi_name = spi_name
        self.offset = 0x08
        self.reset_value = 0x0002
        self.bit_fields = [
            ("RXNE", 0, 0),
            ("TXE", 1, 1),
            ("CHSIDE", 2, 2),
            ("UDR", 3, 3),
            ("CRCERR", 4, 4),
            ("MODF", 5, 5),
            ("OVR", 6, 6),
            ("BSY", 7, 7),
            ("FRE", 8, 8)
        ]

    def reset_SR(self):
        c_code = f"{self.spi_name}->SR = {hex(self.reset_value)};"
        notification = "Make sure to reset the SR registers before using!! like this 🫠:  " + c_code
        print(notification)

    def generate_c_code_SR(self, sr_values):
        c_code = f"{self.spi_name}->SR |= "
        value = 0
        for field, start_bit, end_bit in self.bit_fields:
            value |= sr_values[field] << start_bit
        c_code += f"0x{value:04X};"
        print(c_code)

    def generate_c_code_for_bit_field_SR(self, field_name, value):
        bit_field = next((f for f in self.bit_fields if f[0] == field_name), None)
        if bit_field is None:
            raise ValueError(f"Invalid field name: {field_name}")

        field, start_bit, end_bit = bit_field
        c_code = f"{self.spi_name}->SR |= ({hex(value)} << {start_bit});"
        print(c_code)


class DATA_REGISTER:
    def __init__(self, spi_name):
        self.name = "DR"
        self.read_write = "RW"
        self.spi_name = spi_name
        self.offset = 0x0C
        self.reset_value = 0x0000
        self.bit_fields = [
            ("DR", 0, 15)
        ]

    def reset_DR(self):
        c_code = f"{self.spi_name}->DR = {hex(self.reset_value)};"
        notification = "Make sure to reset the DR registers before using!! like this 🫠:  " + c_code
        print(notification)

    def generate_c_code_DR(self, sr_values):
        c_code = f"{self.spi_name}->DR |= "
        value = 0
        for field, start_bit, end_bit in self.bit_fields:
            value |= sr_values[field] << start_bit
        c_code += f"0x{value:04X};"
        print(c_code)

    def generate_c_code_for_bit_field_DR(self, field_name, value):
        bit_field = next((f for f in self.bit_fields if f[0] == field_name), None)
        if bit_field is None:
            raise ValueError(f"Invalid field name: {field_name}")

        field, start_bit, end_bit = bit_field
        c_code = f"{self.spi_name}->DR |= ({hex(value)} << {start_bit});"
        print(c_code)


spi1 = SPI("SPI1", 0x40013000)
spi2 = SPI("SPI2", 0x40003800)
spi3 = SPI("SPI3", 0x40003C00)
spi4 = SPI("SPI4", 0x40013400)
spi5 = SPI("SPI5", 0x40015000)
spi6 = SPI("SPI6", 0x40015400)
