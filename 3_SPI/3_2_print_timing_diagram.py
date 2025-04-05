"""
INPUT
"""

# Configuration
mosi = 0x3D  # master out slave in
miso = 0x3D  # master in slave out
msb_first = True
cpol = 1
cpha = 1

# The max number of clock cycles to show on the diagram (if you have no idea what this should be, leave it at 20)
max_clock_cycles = 20

"""
END INPUT
"""

import matplotlib.pyplot as plt
from matplotlib import gridspec


def addLinesToDiagram(dias):
    for dia in dias:
        for i in range(1, max_clock_cycles, 2):
            dia.axvline(i, color='black', linewidth=1.2)  # Toggling edge
            dia.axvline(i+1, color='red', linewidth=1.2)  # Sampling edge

def draw_spi_timing_diagram(mosi, miso, msb_first, cpol, cpha):
    mosi_bits = format(mosi, '08b')  # Convert to 8-bit binary string
    miso_bits = format(miso, '08b')

    if not msb_first:
        mosi_bits = mosi_bits[::-1]  # Reverse the bit order
        miso_bits = miso_bits[::-1]

    sclk = [cpol] * 20  # Add an initial cpol value
    ss = [1] + [0] * 17 + [1,1]
    mosi_signal = []
    miso_signal = []

    first_clk_cycle = False
    MOSI_done = False
    MISO_done = False

    for i in range(max_clock_cycles):
        ss_current = ss[i]

        # write SCLK signal one by one
        if ss[i - 1] == 0 and ss_current == 0:
            if sclk[i - 1] == cpol:
                sclk[i] = 0 if sclk[i] == 1 else 1
                if cpha == 1:
                    first_clk_cycle = True

        # if ss is 0, set first_clk_cycle = True
        if cpha == 0 and ss_current == 0:
            first_clk_cycle = True

        # write all MOSI signal
        if first_clk_cycle == True and MOSI_done is False:
            for x in mosi_bits:
                mosi_signal.extend([int(x)] * 2)
            MOSI_done = True
        else:
            if len(mosi_signal) < 20:
                mosi_signal.extend([0])

        # write all MISO signal
        if first_clk_cycle == True and MISO_done is False:
            for x in miso_bits:
                miso_signal.extend([int(x)] * 2)
            MISO_done = True
        else:
            if len(miso_signal) < 20:
                miso_signal.extend([0])

    fig, ax = plt.subplots(4, 1, figsize=(12, 8), sharex=False, sharey=False)

    addLinesToDiagram(ax)

    plt.rcParams['lines.linewidth'] = 4

    ax[0].step(range(max_clock_cycles), sclk, where='post')
    ax[0].set_ylim(-0.5, 1.5)
    ax[0].set_title('SCLK:')
    ax[0].grid(True)

    ax[1].step(range(max_clock_cycles), ss, where='post')
    ax[1].set_ylim(-0.5, 1.5)
    ax[1].set_title('SS:')
    ax[1].grid(True)

    ax[2].step(range(max_clock_cycles), mosi_signal, where='post')
    ax[2].set_ylim(-0.5, 1.5)
    ax[2].set_title('MOSI:')
    ax[2].grid(True)

    ax[3].step(range(max_clock_cycles), miso_signal, where='post')
    ax[3].set_ylim(-0.5, 1.5)
    ax[3].set_title('MISO:')
    ax[3].grid(True)

    plt.setp(ax, xticks=range(0, max_clock_cycles + 1), xticklabels=range(0, max_clock_cycles + 1),
             yticks=[0, 1], yticklabels=['0', '1'], ylabel='Logic Level')

    plt.subplots_adjust(hspace=10)

    fig.suptitle('SPI Timing Diagram\nBlack: Toggling Edge, Red: Sampling Edge')
    fig.tight_layout()
    plt.show()


# Draw the timing diagram
draw_spi_timing_diagram(mosi, miso, msb_first, cpol, cpha)


"""
Keywords

SPI Timing Diagramm

Eine SPI Schnittstelle ist wie folat konfiguiert: CPOL=1. CPHA=0. MSB first
Der Master sendet das Bvte 0x59. Bildet eines der untenstehenden Diagramme den Verlauf korrekt ab. und wenn ia, welches?


Ein Prozessor sendet über SPI das Byte 0x8D. Die Schnittstelle ist wie folgt konfiguriert: Mode 1, d.h. CPOL = 0 und CPHA = 1
LSB first
Zeichnen Sie den zeitlichen Verlauf des Clock Signales und des Datensignales ein. Beschrif- ten Sie diese mit den üblicherweise verwendeten Signalnamen.

Ein Prozessor (SPI Master) sendet über SPI das Byte 0x3D. Die Schnittstelle ist wie folgt konfiguriert: 
- Mode 3, d.h. CPOL = 1 und CPHA = 1 
- MSB first 
Zeichnen Sie den zeitlichen Verlauf des Clock Signales und des Datensignales ein. Beschriften Sie diese mit den üblicherweise verwendeten Signalnamen. 
Siehe Beilage SPI.
"""