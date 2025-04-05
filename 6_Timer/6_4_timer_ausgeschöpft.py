"""
INPUT
"""

source = 40_000_000  # Hz
bitsOfTimer = 8

output = 0.01  # in seconds (s) if you got hertz (Hz) divide 1 by the hertz value
# it can also be the pwm period


"""
END OF INPUT
"""

hertz = 1 / output
hertz2 = hertz * 2 ** bitsOfTimer
prescaler = source / hertz2
arr = output * prescaler  # formula for auto reload register max 65'535 when using 16 bit timer

print(f"TIM_PSC={hex(round(prescaler - 1))}   // {round(prescaler)} -1")
print(f"TIM_ARR={hex(round(arr - 1))}   // {round(arr)} -1")

"""
Keywords:
Gegeben sei ein 16-bit Counter, der mit einem 40 MHz Clock-Signal verbunden ist. Mit Hilfe dieses Counters soll nun alle 10 ms ein Interrupt ausgelöst werden.
Durch welchen Wert aus der Auswahlliste muss der Prescaler die Clock-Frequenz teilen, damit der Wertebereich des Auto-Reload-Registers (ARR) möglichst gut
ausgeschöpft wird?

"""
