"""
INPUT
"""

spi_name = "SPI1"

# CONFIGURE CR1 REGISTER

bidimode = 0  # 0: 2-line unidirectional data mode selected /  1: 1-line bidirectional data mode selected
bidioe = 0  # 0: Output disabled (receive-only mode) / 1: Output enabled (transmit-only mode)
crcen = 0  # 0: CRC calculation disabled / 1: CRC calculation enabled
crcnext = 0  # 0: Data phase (no CRC phase) / 1: Next transfer is CRC (CRC phase)
dff = 0  # 0: 8-bit data frame format is selected for transmission/reception  / 1: 16-bit data frame format is  selected for transmission/reception
rxonly = 0  # 0: Full duplex (Transmit and receive) / 1: Output disabled (Receive-only mode)
ssm = 1  # 0: Software slave management disabled / 1: Software slave management enabled
ssi = 1  # 0: NSS pin has to be low / 1: NSS pin has to be high
lsbfirst = 0  # 0: MSB transmitted first / 1: LSB transmitted first
spe = 0  # 0: Peripheral disabled /  1: Peripheral enabled
br = 0b111  # BINARY!!! 000: fPCLK/2
# 001: fPCLK/4
# 010: fPCLK/8
# 011: fPCLK/16
# 100: fPCLK/32
# 101: fPCLK/64
# 110: fPCLK/128
# 111: fPCLK/256
mstr = 1  # 0: Slave configuration / 1: Master configuration
cpol = 0  # 0: CK to 0 when idle / 1: CK to 1 when idle
cpha = 0  # 0: The first clock transition is the first data capture edge / 1: The second clock transition is the first data capture edge

# CONFIGURE CR2 REGISTER

txeie = 0  # 0: TXE interrupt masked / 1: TXE interrupt not masked
rxneie = 0  # 0: RXNE interrupt masked / 1: RXNE interrupt not masked
errie = 0  # 0: Error interrupt is masked / 1: Error interrupt is not masked
frf = 0  # 0: SPI Motorola mode / 1: SPI TI mode
ssoe = 0  # 0: SS output is disabled in master mode and the cell can work in multimaster configuration /
# 1: SS output is enabled in master mode and the cell cannot work in multimaster configuration
txdmaen = 0  # 0: Tx buffer DMA disabled / 1: Tx buffer DMA enabled
rxdmaen = 0  # 0: Rx buffer DMA disabled / 1: Rx buffer DMA enabled

# CONFIGURE SR REGISTER

fre = 0  # 0: No frame format error / 1: Frame format error
bsy = 0  # 0: SPI (or I2S) not busy / 1: SPI (or I2S) is busy in communication or Tx buffer is not empty
ovr = 0  # 0: No overrun occurred / 1: Overrun occurred
modf = 0  # 0: No mode fault occurred / 1: Mode fault occurred
crcerr = 0  # 0: CRC value received matches the SPI_RXCRCR value / 1: CRC value received doesn't match the SPI_RXCRCR value
udr = 0  # 0: No underrun occurred / 1: Underrun occurred
chside = 0  # 0: Channel Left has to be transmitted or has been received / 1: Channel Right has to be transmitted or has been received
txe = 0  # 0: Tx buffer not empty / 1: Tx buffer empty
rxne = 0  # 0: Rx buffer empty / 1: Rx buffer not empty

# CONFIGURE DR REGISTER

dr = 0b10  # data in binary 16 bit format (e.g. 0b10101010)

"""
END INPUT
"""

from SPI_Tools import SPI


def get_spi_instance(spi_name):
    for instance in SPI.instances:
        if instance.name == spi_name:
            return instance
    raise ValueError(f"No SPI instance found with the name: {spi_name}")


spi_instance = get_spi_instance(spi_name)

cr1_values = {
    "BIDIMODE": bidimode,
    "BIDIOE": bidioe,
    "CRCEN": crcen,
    "CRCNEXT": crcnext,
    "DFF": dff,
    "RXONLY": rxonly,
    "SSM": ssm,
    "SSI": ssi,
    "LSBFIRST": lsbfirst,
    "SPE": spe,
    "BR": br,
    "MSTR": mstr,
    "CPOL": cpol,
    "CPHA": cpha,
}

cr2_values = {
    "TXEIE": txeie,
    "RXNEIE": rxneie,
    "ERRIE": errie,
    "FRF": frf,
    "Reserved (NSSP)": 0,
    "SSOE": ssoe,
    "TXDMAEN": txdmaen,
    "RXDMAEN": rxdmaen,
}

sr_values = {
    "FRE": fre,
    "BSY": bsy,
    "OVR": ovr,
    "MODF": modf,
    "CRCERR": crcerr,
    "UDR": udr,
    "CHSIDE": chside,
    "TXE": txe,
    "RXNE": rxne,
}

dr_values = {
    "DR": dr,
}

spi_instance.reset_cr1()
spi_instance.reset_cr2()
spi_instance.reset_SR()
spi_instance.reset_DR()
spi_instance.configure_cr1(cr1_values)
spi_instance.configure_cr2(cr2_values)
spi_instance.configure_SR(sr_values)
spi_instance.configure_DR(dr_values)


# If you want to set a single bit field, you can use the following:
# spi_instance.configure_cr1_bit_field("BR", 0b111)
# spi_instance.configure_cr1_bit_field("SPE", 1)
