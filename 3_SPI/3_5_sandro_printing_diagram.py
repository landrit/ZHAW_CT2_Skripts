import numpy as np
import matplotlib.pyplot as plt


def hex_to_binary_array(hex_string):
    decimal_value = int(hex_string, 16)  # Convert hex string to decimal
    binary_string = format(decimal_value, '08b')  # Convert decimal to binary string
    binary_array = [int(bit) for bit in binary_string]  # Convert binary string to binary array
    return binary_array


''' INPUT'''

cpol = 1
cpha = 1
input_hex = "0x3D"
msbfirst = 1

input_b = hex_to_binary_array(input_hex)
input_b = input_b.reverse() if msbfirst == 0 else input_b

clk = [i % 2 for i in range(1,17)]

if cpol == 0:
    clk.insert(0, cpol)
    clk = clk[:16]
clk.insert(0, cpol)
clk.insert(0, cpol)
clk.append(cpol)
clk.append(cpol)

duplicated_array = [bit for bit in input_b for _ in range(2)]  # Duplicate each element

print(duplicated_array)
data = np.zeros(len(clk))
data[2:18] = duplicated_array[0:]
print(duplicated_array)
duplicated_array = data.tolist()
# duplicated_array.insert(0, 0)
# duplicated_array.insert(0, 0)
# duplicated_array.append(0)
# duplicated_array.append(0)

if cpha == 1:
    duplicated_array.pop()
    # duplicated_array.pop()
    # duplicated_array.insert(0, 0)
    duplicated_array.insert(0, 0)
    # duplicated_array.append(0)
# else:
    # duplicated_array.pop(0)
    # duplicated_array.insert(0, 0)
    # duplicated_array.append(0)




x = np.arange(0, len(clk) / 2, 0.5)
fig, axs = plt.subplots(2)
plt.ylim(-0.1, 1.1)

axs[0].set_xticks(x)
axs[1].set_xticks(x)
axs[0].set_yticks([0, 1])
axs[1].set_yticks([0, 1])
axs[1].axes.xaxis.set_ticklabels([])
axs[1].axes.yaxis.set_ticklabels([])
axs[0].axes.xaxis.set_ticklabels([])
axs[0].axes.yaxis.set_ticklabels([])

axs[0].step(x, clk)
axs[1].step(x, duplicated_array)
axs[1].grid()
axs[0].grid()
plt.title(f'CPOL: {cpol}, CPHA: {cpha}, MSB First: {msbfirst}')
plt.show()
