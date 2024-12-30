import matplotlib.pyplot as plt
import numpy as np

data = {
    "Stride": [0.00049, 0.00098, 0.00195, 0.00391, 0.00781, 0.01562, 0.03125, 0.04688, 0.09375, 0.1875, 0.375, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 256, 512],
    "gem5":  [1.614, 1.614, 1.614, 1.614, 1.614, 1.6144, 1.597, 1.597, 6.841, 6.837, 6.834,  6.834, 6.844, 9.993, 17.426, 25.279, 28.488, 31.723, 33.097, 34.38, 34.806, 64.366, 167.565, 319.095, 360.929, 368.487, 379.989, 389.722, 389.722],
    "local DDR DRAM": [2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.388, 7.635, 7.635, 9.284, 10.784, 10.988, 15.084, 20.752, 34.964, 39.361, 43.484, 47.715, 53.108, 53.615, 57.665, 68.575, 91.508, 108.14, 132.336, 141.67, 150.165, 151.265],
    "remote NUMA": [2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.388, 7.635, 7.635, 9.767, 10.936, 11.697, 14.065, 23.175, 30.357, 34.085, 39.38, 44.07, 51.142, 52.814, 68.695, 83.986, 117.998, 147.561, 178.835, 191.169, 203.371, 205.881],
    "CXL hardware prototype": [2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.388, 7.635, 7.635, 8.978, 10.905, 10.975, 11.382, 17.452, 34.226, 37.999, 40.146, 45.059, 50.233, 51.815, 62.412, 118.92, 219.727, 273.61, 325.039, 345.928, 384.831, 392.488]
}



# 按CXL-MemSim的标准来,要明白是要跟谁比较
cache1 = np.log2(0.046)
cache2 = np.log2(2)
cache3 = np.log2(30)


stride_log10 = [np.log10(i) for i in data["Stride"]]
# plotcolor = Hstray_2plot
stride_log2 = [np.log2(i) for i in data["Stride"]]
print(stride_log2)
plt.figure(figsize=(12, 5))
color = ['#f58231', '#4363d8', '#a9a9a9', '#469990']

# stride_log2 = stride_log2
stride = [-11, -10, -9, -8.4, -8, -7.4, -7, -6.4, -6, -5.4, -5, -4.4, -4, -3.4, -3, -2.4, -2, -1.4, -1, -0.4, 0, 0.6, 1, 1.6, 2 , 2.6, 3, 3.6, 4, 4.6, 5, 5.6, 6, 6.6, 7, 8, 9]


plt.plot(stride_log2, data["local DDR DRAM"], marker='s',markersize=10,markeredgecolor="black", label="DDR-L", color=color[1])
plt.plot(stride_log2, data["remote NUMA"], marker='^',markersize=10, markeredgecolor="black",label="DDR-R", color=color[2])
plt.plot(stride_log2, data["CXL hardware prototype"], marker='D', markersize=10, markeredgecolor="black", label="CXL", color=color[3])
plt.plot(stride_log2, data["gem5"], marker='o', markersize=10,markeredgecolor="black",label="CXL-MemSim", color=color[0])

plt.axvline(x=stride_log2[0], linestyle='--', color='red')
plt.axvline(x=cache1, linestyle='--', color='red')
plt.axvline(x=cache2, linestyle='--', color='red')
plt.axvline(x=cache3, linestyle='--', color='red')
plt.axvline(x=stride_log2[28], linestyle='--', color='red')


plt.text(-9, 70, 'L1 cache', fontsize=20)
plt.text(-2.8, 70, 'L2 cache', fontsize=20)
plt.text(1.7, 70, 'L3 cache', fontsize=20)
plt.text(6, 70, 'Memory', fontsize=20)

plt.xlabel("Array Size (MB)",fontsize=24)
plt.ylabel("Latency (ns)",fontsize=24)

plt.rcParams.update({'font.size': 20})
# plt.title("Comparison of Latency for Different Memory Types")
plt.legend(loc='upper left',bbox_to_anchor=(0.06, 1),frameon=False)
# plt.grid(True)

# 设置边框宽度
bwidth = 2.5
ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['bottom'].set_linewidth(bwidth)
ax.spines['left'].set_linewidth(bwidth)
ax.spines['top'].set_linewidth(bwidth)
ax.spines['right'].set_linewidth(bwidth)

# log2显式
plt.xticks(np.log2(data["Stride"]), data["Stride"], fontsize=18,rotation=90)
# 等距离显式
# distance = [i for i in range(1,len(stride)+1)]
# plt.xticks(distance, data["Stride"], fontsize=15,rotation=90)

plt.yticks(fontsize=20)
plt.tight_layout()
# plt.tight_layout()
plt.savefig('lmbench.pdf', bbox_inches='tight',pad_inches=0.0)
# plt.show()