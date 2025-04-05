"""
INPUT
"""

# Formula: ttotal = tsample + tconversion

clock = 48_000_000  # Hz
prescaler = 2
cycle_sampling_time = 3  # cycles sample timing
bits_of_adc = 12  # resolution of adc

"""
END OF INPUT
"""

adc_clk = clock / prescaler
n_total = cycle_sampling_time + bits_of_adc
t_total = n_total * (1 / adc_clk)
sampling_rate = 1 / t_total

# Calculate sampling time (tsample)
tsample = cycle_sampling_time * (1 / adc_clk)  # tsample = Nsample * (1 / fadc)

# Calculate conversion time (tconversion)
tconversion = bits_of_adc * (1 / adc_clk)  # Nconversion * (1 / fadc)

print(f"ADC_CLK: {adc_clk} Hz")
print(f"Sampling time (Tsample, Sampling Zeit): {tsample:.10f} s is equal to {tsample * 1000} ms")
print(f"Conversion time (Tconversion, Messzeit): {tconversion:.10f} s is equal to {tconversion * 1000} ms")
print(f"Total time (Ttotal): {t_total:.10f} s is equal to {t_total * 1000} ms")
print(f"Sampling rate: <= {sampling_rate / 1_000_000} Msps")
