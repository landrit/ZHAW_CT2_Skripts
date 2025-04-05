"""Input"""

clock_rate = 1_000_000 # Prozessor clock rate in Hz
data_rate = 16_000 # Datenrate in bit/s
data_buffer_size = 32 # Größe des Datenpuffers in bits
ISR_cycles = 100 # Anzahl der Clockzyklen, die die ISR benötigt
compute_time = 1 # Rechenzeit in Sekunden
desired_cpu_load = 100 # Gewünschte CPU-Belastung in Prozent

"""End Input"""

# Berechnungen
interrupt_frequency = data_rate / data_buffer_size # Interruptfrequenz in Hz
ISR_time = ISR_cycles / clock_rate # Zeit für die ISR in Sekunden
impact = interrupt_frequency * ISR_time * 100 # Einfluss des Interrupts auf das System in Prozent
print("=========================================")
print(f"Interrupt frequency: {interrupt_frequency} Hz")
print(f"Interrupt Service Time (ISR): {ISR_time} s")
print(f"Interrupt impact: {impact} %")

print("=========================================")
# Berechnung der Datenrate, bei der der Prozessor die gewünschte CPU-Belastung erreichen würde
max_data_rate = (compute_time / ISR_time) * data_buffer_size * desired_cpu_load / 100
print(f"Maximal data rate for {desired_cpu_load}% CPU load: {max_data_rate} bit/s ({max_data_rate/1000} kbit/s)")


"""
Keywords:
Ein Prozessorsystem, welches mit 1 MHz getaktet ist, empfängt über ein Peripheriegerät auf
einer Schnittstelle Daten mit einer Rate von 16 kbit/s. Das Peripheriegerät kann 32 bit
zwischenspeichern und zeigt dem Prozessor über eine Interrupt Leitung an, dass die
nächsten 32 bit abholbereit sind. Werden die Daten bis zum nächsten Interrupt nicht
abgeholt, gehen die Daten verloren.
Die Interrupt Service Routine (ISR) benötigt inklusive Aufruf und Rücksprung im Schnitt 100
Clockzyklen. Das System verwendet keine Weiteren Interrupts.

a) Quantifizieren Sie den Einfluss des Interrupts auf das System. D.h. welchen Anteil in
Prozent der Gesamtrechenzeit verbringt das System mit der Behandlung der Interrupts?

b) Bei welcher Datenrate der Schnittstelle würde der Prozessor 100% der Rechenzeit mit
der Behandlung von Interrupts verbringen?
"""
