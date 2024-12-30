import matplotlib.pyplot as plt
import numpy as np


## big test


## asic
copy_asic = [0, 9558, 25012.8, 25095.9, 25145.5, 25127.1, 25164.9, 25162.9, 25093.2, 25166.2, 25145.4]
scale_asic = [0, 3751.7, 16471.2, 16618.5, 16634.5, 16657.6, 16657.6, 16650.8, 16641.4, 16655.8, 16652]
add_asic =[0, 4339.7, 18307.2, 18198.6, 18330.1, 18352.5, 18379.6, 18356.1, 18365.8, 18374.4, 18377.4]
triad_asic =[0, 4347, 18327.8, 18235.7, 18376, 18396.1, 18420.8, 18406.9, 18410.6, 18426.4, 18429.2]

## fpga

copy_fpga =[0, 8852.7, 13426.3, 13294.3, 13249.7, 13303.2, 13234.7, 13176.9, 13189.6, 13451.2, 13331.1]
scale_fpga =[0, 3729.1, 9358.1, 9240.3, 9432.4, 9381.4, 9222.3, 9385.2, 9321.9, 9180.3, 9527.3]
add_fpga =[0, 4278, 10674.2, 10479.3, 10722.8, 10681.2, 10583.8, 10729, 10699, 10539.7, 10852.1]
triad_fpga =[0, 4283.9, 10700.5, 10509.9, 10802.8, 10730.5, 10581.4, 10723.3, 10704.6, 10530.8, 10881.6]


standard = 1000




color = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#999999']

throttling_values = np.arange(100, -1, -10)  # Generate throttling values from 100% to 0% with step size of 10%


plt.figure(figsize=(12, 4))

#
# plt.plot(throttling_values, copy_asic, marker='D', markersize=10, markeredgecolor="black", label="copy", color=color[1],linewidth=2.5)
# plt.plot(throttling_values, scale_asic, marker='o', markersize=10,markeredgecolor="black",label="scale", color=color[2],linewidth=2.5)
# plt.plot(throttling_values, add_asic, marker='^', markersize=10, markeredgecolor="black", label="add", color=color[3],linewidth=2.5)
# plt.plot(throttling_values, triad_asic, marker='p', markersize=10,markeredgecolor="black",label="triad", color=color[4],linewidth=2.5)


plt.plot(throttling_values, copy_fpga, marker='D', markersize=10, markeredgecolor="black", label="copy", color=color[1],linewidth=2.5)
plt.plot(throttling_values, scale_fpga, marker='o', markersize=10,markeredgecolor="black",label="scale", color=color[2],linewidth=2.5)
plt.plot(throttling_values, add_fpga, marker='^', markersize=10, markeredgecolor="black", label="add", color=color[3],linewidth=2.5)
plt.plot(throttling_values, triad_fpga, marker='p', markersize=10,markeredgecolor="black",label="triad", color=color[4],linewidth=2.5)


# 设置边框宽度
bwidth = 2.5
ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['bottom'].set_linewidth(bwidth)
ax.spines['left'].set_linewidth(bwidth)
ax.spines['top'].set_linewidth(bwidth)
ax.spines['right'].set_linewidth(bwidth)

plt.xticks(throttling_values[::-1], [str(throttling)+'%' for throttling in throttling_values],fontsize=24)
plt.yticks(fontsize=24)
# plt.xlabel('Index')
plt.ylabel('Bandwidth (MB/s)',fontsize=24)
plt.xlabel('Throttling Value (%)',fontsize=24)
plt.legend(fontsize=24,frameon=False,edgecolor='black',fancybox=False,borderpad = 0.1, labelspacing = 0.2, handletextpad = 0.2)

plt.tight_layout()
# plt.title('Bandwidth')
plt.show()


# plt.savefig('stream_asic_cpulimit.pdf', bbox_inches='tight',pad_inches=0.0)