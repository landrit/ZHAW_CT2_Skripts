
""""""""""TO FIX THIS AIN'T WORKING"""""""""""

import matplotlib.pyplot as plt
import numpy as np

ne = [0, 1, 1, 1, 0, 1, 1]
nwe = [0, 1, 1, 0, 0, 1, 1]
noe = [0, 1, 1, 0, 0, 1, 1]
address = ['unknown', 'invalid', 'invalid', 'valid', 'invalid', 'invalid', 'invalid']
data = ['unknown', 'invalid', 'invalid', 'invalid', 'valid', 'valid', 'invalid']

data_plot = [1 if x == 'valid' else 0 if x == 'z' else np.nan for x in data]

t = range(0, len(address))

fig, axs = plt.subplots(4, 1, figsize=(8, 6))
fig.suptitle('SRAM Write Cycle')

address_final = address + [address[-1]]

axs[0].step(range(len(address_final)), address_final, 'b')
axs[0].set_yticks(['valid', 'invalid'])
axs[0].set_ylabel('Address')

for i in range(len(address)):
    if address[i] == 'valid':
        axs[0].axvspan(i, i + 1, alpha=0.2, color='green')

axs[1].step(t, ne, 'r')
axs[1].set_yticks([0, 1])
axs[1].set_yticklabels(['0', '1'])
axs[1].set_ylabel('NE')

axs[2].step(t, nwe, 'g')
axs[2].set_yticks([0, 1])
axs[2].set_yticklabels(['0', '1'])
axs[2].set_ylabel('NWE')

data_plot_final = data_plot + [data_plot[-1]]
axs[3].step(range(len(data_plot_final)), data_plot_final, 'm', where='post')
axs[3].set_yticks([0, 1])
axs[3].set_yticklabels(['z', 'valid'])
axs[3].set_ylabel('Data')

for i in range(len(data)):
    if data[i] == 'valid':
        axs[3].axvspan(i, i + 1, alpha=0.2, color='green')

axs[-1].set_xlabel('Time (ns)')

plt.show()
