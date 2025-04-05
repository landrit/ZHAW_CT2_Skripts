"""INPUT"""
import math

possible_presacler_values = [i for i in range(20)] # from 2^0 to 2^19
# possible_presacler_values = [2,4,6,8,12,14,16,18]


source = 10_000_000  # Hz
bitsOfTimer = 16

outputInMS = 62  # None
outputFreq = None # None

"""END OF INPUT"""

value_to_use = 0
if outputInMS is not None:
    value_to_use = 1 / (outputInMS / 1000)  # Convert to seconds
elif outputFreq is not None:
    value_to_use = outputFreq
else:
    raise ValueError("Only one value can be set Sie lellek.")


bitsNeeded = source / (2**bitsOfTimer * value_to_use)
# get the next higher integer possible_presacler_values based on the bitsNeeded
next_higher_value = min([value for value in possible_presacler_values if value > bitsNeeded])
print(f"{next_higher_value} is the next higher value to use for the prescaler")



"""

Dieses Skript berechnet den genauen Bit Wert für den Prescaler.
Dieser Wert kann in 6_1_prescaler_timer_autoreload.py benutzt werden!!!





KEYWORDS:
Prescaler herausfinden
Timer/Counter

Gegeben sei ein 16-bit Counter, der mit einem 40 MHz Clock-Signal verbunden ist. Mit Hilfe dieses Counters soll nun alle 10 ms ein Interrupt
ausgelöst werden. Durch welchen Wert aus der Auswahlliste muss der Prescaler die Clock-Frequenz teilen, damit der Wertebereich des Auto-Reload-Registers (ARR) möglichst gut ausgeschöpft wird?

Die Frequenz fin des selektierten Eingangssignals beträgt 10 MHz. Wie müssen die Register 
initialisiert werden, damit periodisch alle 62 ms ein Interrupt über UIF ausgelöst wird. 
Hinweise: 
- Herleitung muss zwingend ersichtlich sein. 
- Es ist kein Code verlangt. Registernamen gemäss Blockdiagramm und Werte genügen. 
- Werte können als Dezimalzahlen angegeben werden.
"""