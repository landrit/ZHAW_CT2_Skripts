"""
INPUT
"""

TIM_ARR = None   # auto reload register value in hex (0xbb80 = 48000)
source = 35_000_000  # Hz only if TIM_ARR is None
prescalerTick = 70  # only if TIM_ARR is None
counter_mode = "DOWNCOUNTER"  # "UPCOUNTER" or "DOWNCOUNTER"
duty_cycle = 6. / 8.  # 6/8
pwm_mode = 1  # 1: PWM mode 1 (was anderes) , 2: PWM mode 2 (CCMR = 0x0070)
pwm_period_in_ms = 96  # in seconds (s) if you got hertz (Hz) divide 1 by the hertz value
# only if TIM_ARR is None

"""
END INPUT
"""

pwm_period_in_ms = pwm_period_in_ms / 1000

if TIM_ARR is None:
    TIM_ARR = pwm_period_in_ms / (1 / (source / prescalerTick))

TIM_CCR = TIM_ARR * duty_cycle
if pwm_mode == 2 and counter_mode == "UPCOUNTER":
    TIM_CCR = TIM_ARR * (1 - duty_cycle)

if counter_mode == "DOWNCOUNTER" and pwm_mode == 2:
    TIM_CCR = TIM_ARR * (1 - duty_cycle)


print(f"TIM_CCR (PWM mode {pwm_mode}, {counter_mode}) = {hex(round(TIM_CCR))})")
print(f"entspricht ({round(TIM_CCR + 1)} - 1) = {round(TIM_CCR + 1 - 1)}")



"""
KEYWORDS:
Gegeben ist ein universeller 16-Bit Timer mit Capture / Compare - Einheit. Er ist wie folgt konfiguriert:

• Alle Register sind 16 Bit breit.
• Die Quelle liefert ein Signal der Frequenz 35 MHz.
• Der Prescaler ist so eingestellt, dass jeder 70. Tick gezählt wird.
• Der Timer arbeitet als Downcounter.

Für das PWM-Signal gelten die folgenden Einstellungen:

• Das PWM Signal wird low gesetzt, wenn der Counter 0 erreicht.
• Das PWM Signal wird high gesetzt, wenn der Counter den Compare-Wert erreicht. 

Es soll nun ein PWM-Signal mit einer Periode von 96 ms erzeugt werden. Der Duty Cycle soll 6/8 betragen.

Bestimmen Sie den Zahlenwert (dezimal), der im Capture-Compare-Register (CCR) stehen muss.
"""
