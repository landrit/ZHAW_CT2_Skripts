"""
INPUT
"""

bit_register = 16
counter_mode = "DOWNCOUNTER"  # "UPCOUNTER" or "DOWNCOUNTER"
isAutoReload = True # True or False
prescalerTick = 7
ccr = 22
cnt = 39

"""
END INPUT
"""
print(f"dif = {prescalerTick * abs(cnt - ccr)}")

"""
KEYWORDS:
prescaler Tick

Timer/Counter

Gegeben ist ein 16 Bit Counter mit folgender Konfiguration:
• Downcounter mir autoreload
• Prescaler zählt jeden 4. Puls (Clock Zyklus).
• Capture-Compare-Register enthält den Dezimalwert 25
"""