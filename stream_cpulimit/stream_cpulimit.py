import matplotlib.pyplot as plt
import numpy as np


## big test


## asic
copy_asic = [0, 3069.3, 6701.4, 8024.8, 14463.8, 17782.7, 18299.3, 18389, 25178.3, 25170.5, 25183.6]
scale_asic =[0, 2264.7, 4191, 5706.7, 7634, 8226.6, 11116.6, 13392.8, 13635.2, 13645.7, 16647.6]
add_asic =[0, 2295.2, 4292.9, 5963.1, 8234.8, 9390.5, 10829.6, 13529.5, 15820.6, 15817.7, 18396.5]
triad_asic =[0,2296, 4295.7, 5968.5, 8246.2, 9408.5, 10849.3, 13560.3, 12495.4, 15848.4, 18449.6]

## fpga

copy_fpga = [0, 1807.07, 2911.2, 4076, 6808.5, 7231.9, 7554.5, 9499.3, 11238.5, 11160.7, 13130.1]
scale_fpga = [0, 1293, 2159.3, 3264.8, 4033.3, 4686.5, 5658.7, 6098.7, 6835.8, 7547.7, 8279.7]
add_fpga = [0, 1373, 2561.1, 3538.1, 4823.1, 5685.9, 6641.6, 7598.9, 8383.5, 9007.4, 9753]
triad_fpga = [0, 1372.9, 2561.1, 3541.2, 4841.1, 5363.7, 6675.3, 7620.9, 8400.1, 9038.2, 9780.6]

standard = 1000




color = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#999999']

throttling_values = np.arange(100, -1, -10)  # Generate throttling values from 100% to 0% with step size of 10%


plt.figure(figsize=(12, 4))


plt.plot(throttling_values, copy_asic, marker='D', markersize=10, markeredgecolor="black", label="copy", color=color[1],linewidth=2.5)
plt.plot(throttling_values, scale_asic, marker='o', markersize=10,markeredgecolor="black",label="scale", color=color[2],linewidth=2.5)
plt.plot(throttling_values, add_asic, marker='^', markersize=10, markeredgecolor="black", label="add", color=color[3],linewidth=2.5)
plt.plot(throttling_values, triad_asic, marker='p', markersize=10,markeredgecolor="black",label="triad", color=color[4],linewidth=2.5)


# plt.plot(throttling_values, copy_fpga, marker='D', markersize=10, markeredgecolor="black", label="copy", color=color[1],linewidth=2.5)
# plt.plot(throttling_values, scale_fpga, marker='o', markersize=10,markeredgecolor="black",label="scale", color=color[2],linewidth=2.5)
# plt.plot(throttling_values, add_fpga, marker='^', markersize=10, markeredgecolor="black", label="add", color=color[3],linewidth=2.5)
# plt.plot(throttling_values, triad_fpga, marker='p', markersize=10,markeredgecolor="black",label="triad", color=color[4],linewidth=2.5)
#

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