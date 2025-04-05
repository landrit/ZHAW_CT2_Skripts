"""Input"""

bits_per_second = 2_000_000  # 2 Mbit/s = 2_000_000 bit/s
bits_per_byte = 8  # SPI verwendet 8 Daten Bits
telegram_length = 50  # Länge eines Telegramms in Bytes
t_ISR_SPI = 1.5 * 10 ** -6  # Bearbeitungszeit der ISR für SPI inklusive Context-Switching Overhead in Sekunden

# Additional input for AD converter
ad_readings_per_second = 4  # Anzahl der AD-Einlesevorgänge pro Sekunde
t_ISR_AD = 6 * 10 ** -6  # Bearbeitungszeit der ISR für AD inklusive Context-Switching Overhead in Sekunden

"""End Input"""

# Berechnungen für SPI
f_INT_per_byte = bits_per_second / bits_per_byte  # Interruptfrequenz pro Byte
f_INT_per_telegram = f_INT_per_byte * telegram_length  # Interruptfrequenz pro Telegramm
impact_per_byte = f_INT_per_byte * t_ISR_SPI * 100  # CPU Last pro Byte
impact_per_telegram = f_INT_per_telegram * t_ISR_SPI * 100  # CPU Last pro Telegramm

print(f"SPI Interrupt frequency per byte: {f_INT_per_byte} Hz")
print(f"SPI Interrupt frequency per telegram: {f_INT_per_telegram} Hz")
print(f"SPI CPU load per byte (Impact): {impact_per_byte}%")
print(f"SPI CPU load per telegram: {impact_per_telegram}%")

# Annahmen für die sekundäre Berechnung
telegram_per_second = 1  # Anzahl der Telegramme pro Sekunde

# Sekundäre Berechnungen für SPI
f_INT_per_second_SPI = telegram_per_second * telegram_length  # Interruptfrequenz pro Sekunde
impact_per_second_SPI = f_INT_per_second_SPI * t_ISR_SPI * 100  # CPU Last pro Sekunde

print(f"SPI Interrupt frequency per second: {f_INT_per_second_SPI} Hz")
print(f"SPI CPU load per second: {impact_per_second_SPI}%")

# Berechnungen für AD converter
f_INT_per_second_AD = ad_readings_per_second  # Interruptfrequenz pro Sekunde
impact_per_second_AD = f_INT_per_second_AD * t_ISR_AD * 100  # CPU Last pro Sekunde

print(f"AD Converter Interrupt frequency per second: {f_INT_per_second_AD} Hz")
print(f"AD Converter CPU load per second: {impact_per_second_AD}%")

# Berechnungen für beide Interrupts
impact_per_second = impact_per_second_SPI + impact_per_second_AD  # CPU Last pro Sekunde
print(f"CPU load per second: {impact_per_second}%")

"""
Keyword

Ein Microcontroller ist über SPI (8 Daten Bits) mit einem Peripheriebaustein verbunden. Einmal pro Sekunde wird ein Telegramm von 50 Bytes Länge mit 2 Mbps an diesen übertragen. Die Implementierung verwendet den Interrupt TXE (TX buffer empty).

a) Berechnen Sie die Interruptfrequenz und die durch die ISR generierte CPU Last (Impact). Annahme: Die Bearbeitung der ISR dauert inklusive Context-Switching Overhead t ISR= 1.5 us

b) Derselbe Microcontroller liest von einem AD Wandler Daten ein, verarbeitet diese und legt die verarbeiteten Daten in einem File ab. Die Verarbeitung der Daten dauert 6 Mikrosekunden, der AD-Wandler wird pro Sekunde 4 Mal eingelesen. Berechnen Sie die CPU Last für diesen Fall.


c) Berechnen Sie die mittlere CPU Belastung durch die beiden Interrupts.
Sehe Sie mögliche Probleme mit ihrem System?


"""
