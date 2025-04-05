"""
DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING.
USE BY CAUTION.

This file contains the UART classes and functions to use UART on the STM32F4 Discovery board.
"""


class UART:
    instances = []

    def __init__(self, name, base_addr):
        self.name = name
        self.base_addr = base_addr
        self.SR = STATUS_REGISTER(self.name)
        self.DR = DATA_REGISTER(self.name)
        self.BRR = BAUD_RATE_REGISTER(self.name)
        self.CR1 = CONTROL_REGISTER_1(self.name)
        self.CR2 = CONTROL_REGISTER_2(self.name)
        self.CR3 = CONTROL_REGISTER_3(self.name)
        UART.instances.append(self)

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

    def configure_BRR(self, BRR_values):
        self.BRR.generate_c_code_BRR(BRR_values)

    def configure_BRR_bit_field(self, field_name, value):
        self.BRR.generate_c_code_for_bit_field_BRR(field_name, value)

    def reset_BRR(self):
        self.BRR.reset_BRR()

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

    def configure_cr3(self, cr3_values):
        self.CR3.generate_c_code_cr3(cr3_values)

    def configure_cr3_bit_field(self, field_name, value):
        self.CR3.generate_c_code_for_bit_field_cr3(field_name, value)

    def reset_cr3(self):
        self.CR3.reset_cr3()


class STATUS_REGISTER:
    def __init__(self, uart_name):
        self.name = "SR"
        self.read_write = "R"
        self.uart_name = uart_name
        self.offset = 0x00
        self.reset_value = 0x000000C0
        self.bit_fields = [
            ("PE", 0, 0),
            ("FE", 1, 1),
            ("NF", 2, 2),
            ("ORE", 3, 3),
            ("IDLE", 4, 4),
            ("RXNE", 5, 5),
            ("TC", 6, 6),
            ("TXE", 7, 7),
            ("LBD", 8, 8),
            ("CTS", 9, 9),
        ]

    def reset_SR(self):
        c_code = f"{self.uart_name}->SR = {hex(self.reset_value)};"
        notification = "Make sure to reset the SR registers before using!! like this 🫠:  " + c_code
        print(notification)

    def generate_c_code_SR(self, sr_values):
        c_code = f"{self.uart_name}->SR |= "
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
        c_code = f"{self.uart_name}->SR |= ({hex(value)} << {start_bit});"
        print(c_code)


class DATA_REGISTER:
    def __init__(self, uart_name):
        self.name = "DR"
        self.read_write = "RW"
        self.uart_name = uart_name
        self.offset = 0x04
        self.reset_value = None
        self.bit_fields = [
            ("DR", 0, 18)
        ]

    def generate_c_code_DR(self, sr_values):
        c_code = f"{self.uart_name}->DR |= "
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
        c_code = f"{self.uart_name}->DR |= ({hex(value)} << {start_bit});"
        print(c_code)


class BAUD_RATE_REGISTER:
    def __init__(self, uart_name):
        self.name = "BRR"
        self.read_write = "RW"
        self.uart_name = uart_name
        self.offset = 0x08
        self.reset_value = 0x00000000
        self.bit_fields = [
            ("DIV_Fraction", 0, 3),
            ("DIV_Mantissa", 4, 15)
        ]

    def reset_BRR(self):
        c_code = f"{self.uart_name}->BRR = {hex(self.reset_value)};"
        notification = "Make sure to reset the BRR registers before using!! like this 🫠:  " + c_code
        print(notification)

    def generate_c_code_BRR(self, sr_values):
        c_code = f"{self.uart_name}->BRR |= "
        value = 0
        for field, start_bit, end_bit in self.bit_fields:
            value |= sr_values[field] << start_bit
        c_code += f"0x{value:04X};"
        print(c_code)

    def generate_c_code_for_bit_field_BRR(self, field_name, value):
        bit_field = next((f for f in self.bit_fields if f[0] == field_name), None)
        if bit_field is None:
            raise ValueError(f"Invalid field name: {field_name}")

        field, start_bit, end_bit = bit_field
        c_code = f"{self.uart_name}->BRR |= ({hex(value)} << {start_bit});"
        print(c_code)


class CONTROL_REGISTER_1:
    def __init__(self, uart_name):
        self.name = "CR1"
        self.read_write = "RW"
        self.uart_name = uart_name
        self.offset = 0x0C
        self.reset_value = 0x00000000
        self.bit_fields = [
            ("SBK", 0, 0),
            ("RWU", 1, 1),
            ("RE", 2, 2),
            ("TE", 3, 3),
            ("IDLEIE", 4, 4),
            ("RXNEIE", 5, 5),
            ("TCIE", 6, 6),
            ("TXEIE", 7, 7),
            ("PEIE", 8, 8),
            ("PS", 9, 9),
            ("PCE", 10, 10),
            ("WAKE", 11, 11),
            ("M", 12, 12),
            ("UE", 13, 13),
            ("RESERVED", 14, 14),
            ("OVER8", 15, 15)
        ]

    def reset_cr1(self):
        c_code = f"{self.uart_name}->CR1 = {hex(self.reset_value)};"
        notification = "Make sure to reset the CR1 registers before using!! like this 🫠:  " + c_code
        print(notification)

    def generate_c_code_cr1(self, cr1_values):
        c_code = f"{self.uart_name}->CR1 |= "
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
        c_code = f"{self.uart_name}->CR1 |= ({hex(value)} << {start_bit});"
        print(c_code)


class CONTROL_REGISTER_2:
    def __init__(self, uart_name):
        self.name = "CR2"
        self.read_write = "RW"
        self.uart_name = uart_name
        self.offset = 0x10
        self.reset_value = 0x0000
        self.bit_fields = [
            ("ADD", 0, 3),
            ("RESERVED1", 4, 4),
            ("LBDL", 5, 5),
            ("LBDIE", 6, 6),
            ("RESERVED2", 7, 7),
            ("LBCL", 8, 8),
            ("CPHA", 9, 9),
            ("CPOL", 10, 10),
            ("CLKEN", 11, 11),
            ("STOP", 12, 13),
            ("LINEN", 14, 14),
            ("RESERVED3", 15, 15)
        ]

    def reset_cr2(self):
        c_code = f"{self.uart_name}->CR2 = {hex(self.reset_value)};"
        notification = "Make sure to reset the CR2 registers before using!! like this 🫠:  " + c_code
        print(notification)

    def generate_c_code_cr2(self, cr2_values):
        c_code = f"{self.uart_name}->CR2 |= "
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
        c_code = f"{self.uart_name}->CR2 |= ({hex(value)} << {start_bit});"
        print(c_code)


class CONTROL_REGISTER_3:
    def __init__(self, uart_name):
        self.name = "CR3"
        self.read_write = "RW"
        self.uart_name = uart_name
        self.offset = 0x14
        self.reset_value = 0x0000
        self.bit_fields = [
            ("EIE", 0, 0),
            ("IREN", 1, 1),
            ("IRLP", 2, 2),
            ("HDSEL", 3, 3),
            ("NACK", 4, 4),
            ("SCEN", 5, 5),
            ("DMAR", 6, 6),
            ("DMAT", 7, 7),
            ("RTSE", 8, 8),
            ("CTSE", 9, 9),
            ("CTSIE", 10, 10),
            ("ONEBIT", 11, 11),
            ("RESERVED", 12, 15),
        ]

    def reset_cr3(self):
        c_code = f"{self.uart_name}->CR3 = {hex(self.reset_value)};"
        notification = "Make sure to reset the CR3 registers before using!! like this 🫠:  " + c_code
        print(notification)

    def generate_c_code_cr3(self, cr3_values):
        c_code = f"{self.uart_name}->CR3 |= "
        value = 0
        for field, start_bit, end_bit in self.bit_fields:
            value |= cr3_values[field] << start_bit
        c_code += f"0x{value:04X};"
        print(c_code)

    def generate_c_code_for_bit_field_cr3(self, field_name, value):
        bit_field = next((f for f in self.bit_fields if f[0] == field_name), None)
        if bit_field is None:
            raise ValueError(f"Invalid field name: {field_name}")

        field, start_bit, end_bit = bit_field
        c_code = f"{self.uart_name}->CR3 |= ({hex(value)} << {start_bit});"
        print(c_code)


uart1 = UART("UART1", 0x40011000)
uart2 = UART("UART2", 0x40004400)
uart3 = UART("UART3", 0x40004800)
uart4 = UART("UART4", 0x40004c00)
uart5 = UART("UART5", 0x40005000)
uart6 = UART("UART6", 0x40011400)
uart7 = UART("UART7", 0x40007800)
uart8 = UART("UART8", 0x40007c00)
