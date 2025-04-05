"""
INPUT
"""

source = 10_000_000  # Hz
prescalers = [10,11,12,17,20]  # Hz max 65'535 when 16 bits timer

output = 0.062  # in seconds (s) if you got hertz (Hz) divide 1 by the hertz value
# it can also be the pwm period


"""
END OF INPUT
"""


for prescaler in prescalers:
    print(f"Für prescaler {prescaler}:")

    scaled_value = source / prescaler # scaled value is the output after the prescaler

    arr = output * scaled_value  # formula for auto reload register max 65'535 when using 16 bit timer


    print(f"TIM_PSC={hex(round(prescaler - 1))}   // {round(prescaler)} -1")
    print(f"TIM_ARR (if you want to use it for caputre register!) = {hex(round(arr))}   // {round(arr)}")
    print(f"TIM_ARR={hex(round(arr - 1))}   // {round(arr)} -1 = {round(arr) -1}")
    print(f"Fout = {round(scaled_value / arr)} Hz")
    print("============================================")

"""
Keywords

1) Die Eingangsfrequenz fin beträgt 10 MHz. Wie müssen die Register initialisiert werden, damit
periodisch alle 38 ms ein Interrupt ausgelöst wird.

Gegeben ist der folgende Down-counter
Die Eingangsfrequenz fin beträgt 10 MHz. Wie müssen die Register initialisiert werden, damit periodisch alle 38 ms ein Interrupt ausgelöst wird.
Hinweise:
Herleitung muss zwingend ersichtlich sein.
Es ist kein Code verlangt. Registername und Wert genügt. Werte können als Dezimalzahlen angegeben werden.

Die Frequenz fin des selektierten Eingangssignals beträgt 10 MHz. Wie müssen die Register 
initialisiert werden, damit periodisch alle 62 ms ein Interrupt über UIF ausgelöst wird. 
Hinweise: 
- Herleitung muss zwingend ersichtlich sein. 
- Es ist kein Code verlangt. Registernamen gemäss Blockdiagramm und Werte genügen. 
- Werte können als Dezimalzahlen angegeben werden.
"""