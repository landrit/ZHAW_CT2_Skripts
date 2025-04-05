"""INPUT"""

vref = 3.0
offset_error_lsb = 2
adc_id = 1 # 1 = ADC1, 2 = ADC2, 3 = ADC3
adc_bits = 10
rundung_volate_offset = 1 # Wie viel Stellen genau?

data_register_offset = 0x4C # Refer reference manual (bro wenn ka hesch denn lahn eif so und seg Bismillah wenns laufe lahsch amin)
"""INPUT"""

if adc_id == 1:
    adc_base_address = 0x40012000
elif adc_id == 2:
    adc_base_address = 0x40012100
elif adc_id == 3:
    adc_base_address = 0x40012200
else:
    raise ValueError("Ungültige ADC-ID")

# Berechnung der absoluten Adresse des ADC-Datenregisters
absolute_address = hex(adc_base_address + data_register_offset)

# Berechnung der Spannung pro Stufe
voltage_per_step = vref / (2 ** adc_bits)

# Berechnung der Spannung des Offsetfehlers
offset_voltage = offset_error_lsb * voltage_per_step * 1000
offset_voltage_roundet = round(offset_voltage, rundung_volate_offset)  # Ergebnis in Millivolt

print(f"Absolute Adresse des ADC-Datenregisters: {absolute_address}")
print(f"Spannung des Offsetfehlers: {offset_voltage} mV")
print(f"Gerundet: {offset_voltage_roundet} mV")


