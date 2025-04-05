"""
INPUT
"""

# I2C Adresse
adresse = 0x56

# Read/Write Bit (1 für Lesen, 0 für Schreiben)
rw_bit = 1

"""
END OF INPUT
"""


import matplotlib.pyplot as plt
import numpy as np

# Timing Konstanten
t_periode = 1
t_halb_periode = t_periode / 2

# Konvertiert eine Zahl zu einer Liste von Bits
def zahl_zu_bits(zahl, bit_anzahl):
    return [(zahl >> i) & 1 for i in range(bit_anzahl)][::-1]  # reversed, da das höchste Bit zuerst gesendet wird


# Erzeugt ein I2C Signal
def erzeuge_i2c_signal(adresse_bits, read_write_bit, sda_start=1, scl_start=1):
    # Start des Signals (SCL: 1 -> 1, SDA: 1 -> 0)
    sda = [sda_start, 0]
    scl = [scl_start, scl_start]

    # Daten Bits (Adresse + R/W)
    for bit in adresse_bits + [read_write_bit]:
        sda += [bit, bit]
        scl += [1, 0]

    # ACK-Bit (SCL: 0 -> 1 -> 0, SDA: 0)
    sda += [0, 0]
    scl += [1, 0]

    # Stop des Signals (SCL: 0 -> 1, SDA: 0 -> 1)
    sda += [0, sda_start]
    scl += [1, scl_start]

    return sda, scl


# Erzeuge das I2C Signal
sda, scl = erzeuge_i2c_signal(zahl_zu_bits(adresse, 7), rw_bit)

# Erzeuge den Zeitvektor
t = np.linspace(0, len(sda) * t_halb_periode, len(sda))

# Erstelle die Figure
plt.figure(figsize=(15, 10))

# Plotte das SDA Signal
plt.subplot(2, 1, 1)  # 2 Reihen, 1 Spalte, aktueller Plot ist der erste
plt.step(t, sda, label='SDA', where='post', linewidth=4)
plt.ylim(-0.5, 1.5)
plt.xlim(-1, len(sda) * t_halb_periode + 1)
plt.grid(True)
plt.legend()
plt.title("SDA-Signal")

for i in range(2, len(t), 2):  # Vertikale Linien für die Abtastzeitpunkte
    plt.axvline(x=t[i], color='r')

# Beschriftungen für die Bits
plt.text((t[0]+t[1])/2, 0.8, "Start", fontsize=12, ha='center',
         bbox=dict(facecolor='red', alpha=0.5))

for i in range(2, 18, 2):  # Daten Bits
    plt.text((t[i]+t[i+1])/2, 0.8, str(sda[i]), fontsize=12, ha='center',
             bbox=dict(facecolor='red', alpha=0.5))

# Text für Read/Write
rw_text = "Read" if rw_bit else "Write"
plt.text((t[16]+t[17])/2, 0.8, rw_text, fontsize=12, ha='center',
         bbox=dict(facecolor='red', alpha=0.5))

# Beschriftung für das ACK-Bit
plt.text((t[18]+t[19])/2, 0.8, "ACK", fontsize=12, ha='center',
         bbox=dict(facecolor='red', alpha=0.5))

# Plotte das SCL Signal
plt.subplot(2, 1, 2)  # 2 Reihen, 1 Spalte, aktueller Plot ist der zweite
plt.step(t, scl, label='SCL', linestyle='--', where='post', linewidth=2)
plt.ylim(-0.5, 1.5)
plt.xlim(-1, len(sda) * t_halb_periode + 1)
plt.grid(True)
plt.legend()
plt.title("SCL-Signal")

plt.tight_layout()
plt.show()


"""
KEYWORDS:
Mittels I2C soll ein Baustein zum Lesen adressiert werden. Die 7-Bit Adresse lautet 0×56.
Zeichnen Sie die übertragenen Signale vom Start bis zum Acknowledge auf.
"""