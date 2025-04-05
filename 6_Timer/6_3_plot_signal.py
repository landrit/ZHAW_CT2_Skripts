"""
INPUT
"""

TIM_PSC = 499  # dec or hex or !!None!! => PRE
TIM_ARR = 29999  # dec or hex => ARR
TIM_CCR1 = 10000  # dec or hex => CCR
frequency_in_hz = 500_000  # Timer clock frequency (50 MHz)

PWMMODE = 2  # 1: PWM mode 1 (was anderes), 2: PWM mode 2 (CCMR = 0x0070) find out based on CCMR register
counter_mode = "UPCOUNTER"  # "UPCOUNTER" or "DOWNCOUNTER"

"""
END INPUT
"""

TIM_PSC = TIM_PSC if TIM_PSC is not None else 0

TIM_PSC = int(TIM_PSC)
TIM_ARR = int(TIM_ARR)
TIM_CCR1 = int(TIM_CCR1)

import matplotlib.pyplot as plt
import numpy as np

prescaler = TIM_PSC + 1
timer_frequency = frequency_in_hz / prescaler
pwm_period = (TIM_ARR + 1) / timer_frequency

# Calculate PWM high and low duration based on mode
if PWMMODE == 1:
    pwm_high_duration = TIM_CCR1 / timer_frequency
    pwm_low_duration = pwm_period - pwm_high_duration
elif PWMMODE == 2:
    pwm_low_duration = TIM_CCR1 / timer_frequency
    pwm_high_duration = pwm_period - pwm_low_duration

print(f"PWM Frequency: {timer_frequency} Hz")
print(f"PWM Period: {pwm_period} s (is {pwm_period * 1000} ms)")
print(f"PWM High Duration (Duty Cycle): {pwm_high_duration} s")
print(f"PWM Low Duration (Duty Cycle): {pwm_low_duration} s")
print(f"Duty Cycle in percent: {round((pwm_high_duration / pwm_period) * 100, 2)} %")

# Number of periods to plot
num_periods = 1

# Create time samples
t = np.linspace(0, pwm_period * num_periods, 1000 * num_periods, endpoint=False)

# Generate PWM signal
if counter_mode == "UPCOUNTER":
    if PWMMODE == 1:
        OCxREF = [(1 if (i % pwm_period) < pwm_high_duration else 0) for i in t]
    elif PWMMODE == 2:
        OCxREF = [(0 if (i % pwm_period) < pwm_low_duration else 1) for i in t]
elif counter_mode == "DOWNCOUNTER":
    if PWMMODE == 1:
        OCxREF = [(0 if (i % pwm_period) < (pwm_period - pwm_high_duration) else 1) for i in t]
    elif PWMMODE == 2:
        OCxREF = [(1 if (i % pwm_period) < (pwm_period - pwm_low_duration) else 0) for i in t]

# Plot the OCxREF signal
plt.plot(t, OCxREF)
plt.ylim([-0.1, 1.1])  # to make the plot more readable
plt.xlabel("Time (s)")
plt.ylabel("OCxREF")
plt.title(f"OCxREF Signal ({counter_mode} with PWM mode {PWMMODE})")
plt.grid(True)
plt.show()

"""
KEYWORDS:
PWM - Periode und Duty Cycle

Gegeben ist der folgende Counter. Dieser ist als Up-counter konfiguriert
Die Quelle liefert eine Frequenz von 50 MHz. Die relevanten Register sind wie folgt konfiguriert:
PRE = 100-1
ARR = 15000-1
CCR = 4500
Welche Eigenschaften hat das Signal am Ausgang OCxREF

Gegeben ist der folgende Upcounter
Reload = 10'000d   1d CCR = 3000d
Skizzieren Sie den zeitlichen Verlauf des Signals OC_REF. Tragen Sie Werte für Periode und Duty Cycle in Ihrer Skizze ein. Berechnung muss ersichtlich sein.
"""
