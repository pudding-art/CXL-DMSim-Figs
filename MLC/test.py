import matplotlib.pyplot as plt
import numpy as np


cxl_read_lat = [583.88, 662.64, 962.27, 945.03, 950.9, 950.46, 950.29, 946.6, 949.77, 951.27,0]
cxl_read_bw = [0,3464.2, 16139, 18487.4, 21481.8, 21399.2, 21373.4, 21343.2, 21476.4, 21394.4, 21347.7]
cxl_write_lat = [567.46, 607.36, 628.4, 634.45, 639.5, 648.92, 650.29, 652.97, 653.1, 653.12,0]
cxl_write_bw = [0,622.5, 4332.8, 8952.8, 12083.9, 14725.2, 17252.4, 20325.7, 23003.4, 23020.2, 23003.8]




cxl_read_lat_cg =[0, 1391.38, 971.3, 797.56, 713.88, 665.22, 648.37, 628.75, 602.76, 583.18, 570.16]
cxl_write_lat_cg =[0, 1661.68, 1641.42, 1626.11, 1615.01, 1564.69, 1455.5, 1008.62, 818.91, 668.16, 609.95]


throttling_values = np.arange(100, -1, -10)  # Generate throttling values from 100% to 0% with step size of 10%
y_ticks = [0,300,600,900,1200,1500,1800]


plt.figure(figsize=(4.5, 2))

color = ['#f58231', '#4363d8', '#a9a9a9', '#469990']

# Plot read latency
plt.plot(throttling_values, cxl_read_lat[::-1], marker='^',markerfacecolor='white', markeredgewidth=2,  label='Read',color=color[0])
plt.plot(throttling_values, cxl_write_lat[::-1], marker='o', markerfacecolor='white', markeredgewidth=2, label='Write',color=color[1])


print(throttling_values)

plt.xticks(throttling_values[::-1], [str(throttling)+'%' for throttling in throttling_values])
plt.yticks(y_ticks[::1], [str(y_tick) for y_tick in y_ticks])

plt.xlabel('Index')
plt.ylabel('Execution Time(ns)')

plt.xlabel('Throttling Value (%)')
plt.legend(bbox_to_anchor=(0.73, 0.5),frameon=False)

# plt.title('Latency')
plt.tight_layout()

# plt.show()

plt.savefig('mlc_mba_time.pdf', bbox_inches='tight',pad_inches=0.0)