"""
INPUT
"""

pin_name_to_configure = "PE1" # Pin Port Number -> PD4
moder = "INPUT"  # Set the mode to INPUT(0x00), OUTPUT(0x01), ALTERNATE(0x10) or ANALOG(0x11)
# DEFAULT moder = "INPUT"
# IF PA15, PA14, PA13, PB4, PB3 -> ALTERNATE (DEFAULT)

otyper = "PUSH_PULL"  # Set the mode to PUSH_PULL(0x0), OPEN_DRAIN(0x1),
# DEFAULT otyper = "PUSH_PULL"

ospeedr = "LOW_SPEED" # Set the mode to LOW_SPEED(0x00), MEDIUM_SPEED(0x01), HIGH_SPEED(0x10) or VERY_HIGH_SPEED(#0x11)
# DEFAULT ospeedr = "LOW_SPEED"
# IF PA11, PB3 -> VERY_HIGH_SPEED (DEFAULT)

pupdr = "NO_PULL_UP_DOWN"  # Set the mode to NO_PULL_UP_DOWN(0x00), PULL_UP(0x01), PULL_DOWN(0x10) or RESERVED(0x11)
# DEFAULT ospeedr = "NO_PULL_UP_DOWN"
# IF PA13, PA11, PB4 -> PULL_UP (DEFAULT)
# IF PB12 -> PULL_DOWN (DEFAULT)

"""
END INPUT
"""

if not pin_name_to_configure[0] == "P":
    pin_name_to_configure = "P" + pin_name_to_configure
pin_name_to_configure = pin_name_to_configure.replace(".", "").upper()

from GPIO_tools import GPIO

found_port = GPIO.find_port_by_pin_name(pin_name_to_configure)

if found_port:
    found_port.moder.set_moder(moder, GPIO.find_GPIO_by_port(pin_name_to_configure).name)
    found_port.otyper.set_otyper(otyper, GPIO.find_GPIO_by_port(pin_name_to_configure).name)
    found_port.ospeedr.set_ospeedr(ospeedr, GPIO.find_GPIO_by_port(pin_name_to_configure).name)
    found_port.pupdr.set_pupdr(pupdr, GPIO.find_GPIO_by_port(pin_name_to_configure).name)
    print(f"{found_port}")

else:
    print(f"No GPIO port found with pin_num {pin_name_to_configure}")

"""
Sie schliessen eine LED direkt an einen GPIO-Pin, den Sie zuvor als Open-drain konfiguriert haben. Auf der anderen Seite liegt die LED auf GND.
GPIO Pin 5 an Port D soll wie folgt konfiguriert werden. - Output
- Push-Pull
- High Speed
- No Pullup/No Pulldown
Vervollständigen Sie in der untenstehenden Tabelle die dafür zu konfigurierenden Bits.

Gegeben ist der folgende Rahmen einer C-Funktion. Die Funktion konfiguriert den GPIO Pin 
E.1 als «input» mit «pull-up». Dabei sollen die Konfigurationen aller anderen Pins unverändert 
bleiben. 
a) Setzen Sie beim markierten Macro die korrekte Adresse für GPIOE ein. 
b) Implementieren Sie die Funktion configure_PE1_input_pullup()


GPIO Konfiguration
Verwenden sie für folgende Aufgaben die Daten in der Beilage. GPIO Pin 14 an Port B soll wie folgt konfiguriert werden.
General Purpose Output Push-Pull
High Speed
No pull-up, pull-down
An welchen Bits in den angegebenen Registern müssen welche Bit Werte geschrieben werden um diese Konfiguration umzusetzen?

"""