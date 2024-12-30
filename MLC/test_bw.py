import matplotlib.pyplot as plt
import numpy as np


cxl_read_lat = [0,583.88, 662.64, 962.27, 945.03, 950.9, 950.46, 950.29, 946.6, 949.77, 951.27]
cxl_read_bw = [0,3464.2, 16139, 18487.4, 21481.8, 21399.2, 21373.4, 21343.2, 21476.4, 21394.4, 21347.7]
cxl_write_lat = [0,567.46, 607.36, 628.4, 634.45, 639.5, 648.92, 650.29, 652.97, 653.1, 653.12]
cxl_write_bw = [0,622.5, 4332.8, 8952.8, 12083.9, 14725.2, 17252.4, 20325.7, 23003.4, 23020.2, 23003.8]


# 需要重新测试
cxl_read_bw_cg = [0,2471.5, 5320.3, 8235.6, 10739.8, 13621.2, 16137.3, 18407.5, 20016, 21113, 20510.8]
cxl_write_bw_cg = [0, 4323.8, 8776.5, 12525.8, 14923.8, 15946.9, 16353.2, 15631.5, 15434.5, 15212.4, 15065.5]






throttling_values = np.arange(100, -1, -10)  # Generate throttling values from 100% to 0% with step size of 10%
y_ticks = [0,5000,10000,15000,20000]

plt.figure(figsize=(4.5, 2))

color = ['#f58231', '#4363d8', '#a9a9a9', '#469990']

# Plot read latency
plt.plot(throttling_values, cxl_read_bw, marker='^',markerfacecolor='white', markeredgewidth=2, label='Read',color=color[0])
plt.plot(throttling_values, cxl_write_bw, marker='o',markerfacecolor='white', markeredgewidth=2, label='Write',color=color[1])


print(throttling_values)

plt.xticks(throttling_values[::-1], [str(throttling)+'%' for throttling in throttling_values])
plt.yticks(y_ticks[::1], (str(y_tick) for y_tick in y_ticks))

plt.xlabel('Index')
plt.ylabel('Bandwidth(MB/s)')

plt.xlabel('Throttling Value (%)')
plt.legend(frameon=False)

#plt.title('Bandwidth')

plt.tight_layout()
# plt.show()

plt.savefig('mlc_mba_bw_real.pdf', bbox_inches='tight',pad_inches=0.0)