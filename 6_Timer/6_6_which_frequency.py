"""
INPUT
"""

INT_CLK = 100_000  # in hz
ARR = 39999
PRE = 0

"""
END OF INPUT
"""


# Funktion, die die Interrupt-Frequenz berechnet
def calculate_interrupt_frequency(INT_CLK, ARR, PRE):
    return INT_CLK / (PRE + 1) / (ARR + 1)


# Berechnung der aktuellen Interrupt-Frequenz
interrupt_frequency = calculate_interrupt_frequency(INT_CLK, ARR, PRE)
print(f"\nCurrent Interrupt Frequency: {interrupt_frequency} Interrupts/s")

print("=========================================")

# Änderung der Clockfrequenz
new_INT_CLK = 2 * INT_CLK
new_interrupt_frequency = calculate_interrupt_frequency(new_INT_CLK, ARR, PRE)
print(f"New Interrupt Frequency after doubling the clock frequency: {new_interrupt_frequency} Interrupts/s")

# Änderung von PRE
new_PRE = 1
new_interrupt_frequency = calculate_interrupt_frequency(INT_CLK, ARR, new_PRE)
print(f"New Interrupt Frequency after changing PRE to 1: {new_interrupt_frequency} Interrupts/s")

# Konfigurierung eines Timers mit einer Interrupt-Frequenz von 5 Hz
target_frequency = 5
new_ARR = INT_CLK / (PRE + 1) / target_frequency - 1
print(f"New ARR to achieve an interrupt frequency of 5 Hz: {new_ARR}")

# Demonstration der Auswirkung von ARR und PRE auf die Interrupt-Frequenz
print("\nDemonstration of the impact of changing ARR and PRE values on Interrupt Frequency:")
for new_ARR in range(10000, 50001, 10000):
    for new_PRE in range(5):
        new_interrupt_frequency = calculate_interrupt_frequency(INT_CLK, new_ARR, new_PRE)
        print(f"ARR: {new_ARR}, PRE: {new_PRE}, Interrupt Frequency: {new_interrupt_frequency} Interrupts/s")

"""
Keywords:
Ein Timer mit INT_CLK = 100 kHz ist mit folgenden Werten konfiguriert:
ARR = 39'999
PRE = 0

Welche Frequenz hat der erzeugte Interrupt?

100 khz = 100'000 = 100'000
100'000/1/40000 = 2.5 Interrupts pro sekunde

(clock in Hz)(PSC+1)/(ARR+1) = (Interrupts/s)

"""
