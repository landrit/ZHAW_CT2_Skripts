"""INPUT"""

input_adressbloecher = 1024

"""END INPUT"""

import math


def berechne_adresslinien(adressbloecher):
    return int(math.log2(adressbloecher))


adresslinien = berechne_adresslinien(input_adressbloecher)

output_text = f"A[25:{25 - adresslinien + 1}]"
print(output_text)
