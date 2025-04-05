"""
INPUT
"""

uart_name = "UART1"

# CONFIGURE SR REGISTER

cts = 0  # 0: No change occurred on the CTS status line / 1: A change occurred on the CTS status line
lbd = 0  # 0: O: LIN Break not detected / 1: LIN break detected
txe = 0  # 0: Data is not transferred to the shift register / 1: Data is transferred to the shift register)
tc = 0  # 0: Transmission is not complete / 1: Transmission is complete
rxne = 0  # 0: Data is not received / 1: Received data is ready to be read.
idle = 0  # 0: No idle line detected / 1: Idle line detected
ore = 0  # 0: No Overrun error / 1: Overrun error is detected
nf = 0  # 0: No noise is detected / 1: Noise is detected
fe = 0  # 0: No Framing error is detected / 1: Framing error or break character is detected
pe = 0  # O: No parity error / 1: Parity error is detected

# CONFIGURE DR REGISTER

dr = 0b10  # data 9 bit in binary format (e.g. 0b10101010)

# CONFIGURE BRR REGISTER

div_fraction = 0b0000  # 4 bit binary value
div_mantissa = 0b100000000000  # 12 bit binary value

# CONFIGURE CR1 REGISTER

over8 = 0  # 0: oversampling by 16 / 1: oversampling by 8
ue = 1  # 0: USART prescaler and outputs disabled / 1: USART enabled
m = 0  # 0: 1 Start bit, 8 Data bits, n Stop bit / 1: 1 Start bit, 9 Data bits, n Stop bit
wake = 0  # 0: Idle Line / 1: Address Mark
pce = 0  # 0: Parity control disabled / 1: Parity control enabled
ps = 0  # 0: Even parity / 1: Odd parity
peie = 0  # O: Interrupt is inhibited / 1: An USART interrupt is generated whenever PE=1 in the USART_SR register
txeie = 0  # O: Interrupt is inhibited / 1: An USART interrupt is generated whenever TXE=1 in the USART_ SR register
tcie = 0  # 0: Interrupt is inhibited / 1: An USART interrupt is generated whenever TC=1 in the USART_ SR register
rxneie = 0  # O: Interrupt is inhibited / 1: An USART interrupt is generated whenever ORE=1 or RXNE=1 in the USART_SR
idleie = 0  # O: Interrupt is inhibited / 1: An USART interrupt is generated whenever IDLE=1 in the USART SR register
te = 0  # 0: Transmitter is disabled / 1: Transmitter is enabled
re = 0  # 0: Receiver is disabled / 1: Receiver is enabled and begins searching for a start bit
rwu = 0  # 0: Receiver in active mode / 1: Receiver in mute mode
sbk = 0  # 0: No break character is transmitted / 1: Break character will be transmitted

# CONFIGURE CR2 REGISTER

linien = 0  # O: LIN mode disabled / 1: LIN mode enabled
stop = 0b00  # 00: 1 Stop bit / 01: 0.5 Stop bit / 10: 2 Stop bits / 11: 1.5 Stop bit
clken = 0  # 0: CK pin disabled / 1: CK pin enabled
cpol = 0  # 0: Steady low value on CK pin outside transmission window. / 1: Steady high value on CK pin outside transmission window.
cpha = 0  # 0: The first clock transition is the first data capture edge / 1: The second clock transition is the first data capture edge
lbcl = 0  # 0: The clock pulse of the last data bit is not output to the CK pin / 1: The clock pulse of the last data bit is output to the CK pin
lbdie = 0  # 0: Interrupt is inhibited / 1: An interrupt is generated whenever LBD=1 in the USART SR register
lbdl = 0  # 0: 10-bit break detection / 1: 11-bit break detection
add = 0b000  # 3 bit binary value

# CONFIGURE CR3 REGISTER

one_bit = 0  # O: Three sample bit method / 1: One sample bit method
ctsie = 0  # 0: Interrupt is inhibited / 1: An interrupt is generated whenever CTS=1 in the USART_SR register
ctse = 0  # 0: CTS hardware flow control disabled / 1: CTS mode enabled, data is only transmitted when the CTS input is asserted (tied to 0).
rtse = 0  # 0: RTS hardware flow control disabled / 1: RTS interrupt enabled, data is only requested when there is space in the receive buffer
dmat = 0  # 1: DMA mode is enabled for transmission. / 0: DMA mode is disabled for transmission.
dmar = 0  # 1: DMA mode is enabled for reception / O: DMA mode is disabled for reception
scen = 0  # O: Smartcard Mode disabled / 1: Smartcard Mode enabled
nack = 0  # O: NACK transmission in case of parity error is disabled / 1: NACK transmission during parity error is enabled
hdsel = 0  # 0: Half duplex mode is not selected / 1: Half duplex mode is selected
irlp = 0  # 0: Normal mode / 1: Low-power mode
iren = 0  # 0: IrDA disabled / 1: IrDA enabled
eie = 0  # O: Interrupt is inhibited / 1: An interrupt is generated whenever DMAR=1 in the USART CR3 register and FE=1 or ORE=1 or NF=1 in the USART SR register.

"""
END INPUT
"""

from UART_Tools import UART


def get_uart_instance(uart_name):
    for instance in UART.instances:
        if instance.name == uart_name:
            return instance
    raise ValueError(f"No UART instance found with the name: {uart_name}")


uart_instance = get_uart_instance(uart_name)

sr_values = {
    "CTS": cts,
    "LBD": lbd,
    "TXE": txe,
    "TC": tc,
    "RXNE": rxne,
    "IDLE": idle,
    "ORE": ore,
    "NF": nf,
    "FE": fe,
    "PE": pe,
}

dr_values = {
    "DR": dr,
}

brr_values = {
    "DIV_Fraction": div_fraction,
    "DIV_Mantissa": div_mantissa,
}

cr1_values = {
    "OVER8": over8,
    "RESERVED": 0,
    "UE": ue,
    "M": m,
    "WAKE": wake,
    "PCE": pce,
    "PS": ps,
    "PEIE": peie,
    "TXEIE": txeie,
    "TCIE": tcie,
    "RXNEIE": rxneie,
    "IDLEIE": idleie,
    "TE": te,
    "RE": re,
    "RWU": rwu,
    "SBK": sbk,
}

cr2_values = {
    "RESERVED3": 0,
    "LINEN": linien,
    "STOP": stop,
    "CLKEN": clken,
    "CPOL": cpol,
    "CPHA": cpha,
    "LBCL": lbcl,
    "RESERVED2": 0,
    "LBDIE": lbdie,
    "LBDL": lbdl,
    "RESERVED1": 0,
    "ADD": add,
}

cr3_values = {
    "RESERVED": 0b000,
    "ONEBIT": one_bit,
    "CTSIE": ctsie,
    "CTSE": ctse,
    "RTSE": rtse,
    "DMAT": dmat,
    "DMAR": dmar,
    "SCEN": scen,
    "NACK": nack,
    "HDSEL": hdsel,
    "IRLP": irlp,
    "IREN": iren,
    "EIE": eie,
}

uart_instance.reset_SR()
uart_instance.reset_BRR()
uart_instance.reset_cr1()
uart_instance.reset_cr2()
uart_instance.reset_cr3()
uart_instance.configure_SR(sr_values)
uart_instance.configure_DR(dr_values)
uart_instance.configure_BRR(brr_values)
uart_instance.configure_cr1(cr1_values)
uart_instance.configure_cr2(cr2_values)
uart_instance.configure_cr3(cr3_values)

# If you want to set a single bit field, you can use the following:
# spi_instance.configure_cr1_bit_field("BR", 0b111)
# spi_instance.configure_cr1_bit_field("SPE", 1)
