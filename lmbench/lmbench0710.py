import matplotlib.pyplot as plt
import numpy as np

data = {
    "Stride": [0.00049, 0.00098, 0.00195, 0.00293, 0.00391, 0.00586, 0.00781, 0.01172, 0.01562, 0.02344, 0.03125, 0.04688, 0.0625, 0.09375, 0.125, 0.1875, 0.25, 0.375, 0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 256, 512, 640,  832,  1024],
    "gem5 FPGA":  [1.614, 1.614, 1.614, 1.614, 1.614, 1.6144, 1.597, 1.597, 6.841, 6.837, 6.834,  6.834, 6.844, 9.993, 17.426, 25.279, 28.488, 31.723, 33.097, 34.38, 34.806, 64.366, 167.565, 319.095, 360.929, 368.487, 379.989, 389.722, 389.722,  319.095,  368.487,389.722],
    "local DDR DRAM":[1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.729, 5.53, 5.529, 5.529, 6.181, 6.039, 6.747, 7.271, 7.874, 7.95, 8.439, 15.043, 36.633, 38.908, 40.359, 43.89, 48.194, 48.982, 51.004, 49.55, 49.665, 50.141, 59.725, 79.482, 112.793, 127.719, 131.630, 138.076,  131.481],
    "remote NUMA": [1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.729, 5.529, 5.529, 5.529, 6.682, 5.832, 7.016, 7.375, 7.801, 7.949, 12.212, 18.182, 35.558, 37.778, 40.366, 43.757, 47.262, 47.657, 47.785, 48.418, 50.924, 52.805, 69.784, 99.582, 162.916, 190.742, 194.427,  199.078,  202.870],
    "CXL FPGA":[1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.729, 5.528, 5.528, 5.528, 5.528, 6.369, 6.569, 7.137, 7.808, 7.947, 7.949, 16.718, 33.676, 37.197, 38.544, 41.386, 46.658, 47.586, 47.792, 47.973, 48.163, 48.196, 75.845, 152.623, 285.925, 346.191,372.970, 374.158,  379.995] ,
    "CXL ASIC":[1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.728, 1.729, 5.527, 5.527, 5.527, 5.527, 5.829, 7.22, 7.512, 7.882, 7.945, 7.987, 16.622, 34.522, 40.228, 40.993, 45.331, 50.047, 50.781, 50.96, 51.136, 51.211, 51.13, 66.528, 123.13, 216.417, 260.699, 269.411,  278.676, 284.893]

}



# 按CXL-MemSim的标准来,要明白是要跟谁比较
cache1 = np.log2(0.046)
cache2 = np.log2(2)
cache3 = np.log2(96)


stride_log10 = [np.log10(i) for i in data["Stride"]]
# plotcolor = Hstray_2plot
stride_log2 = [np.log2(i) for i in data["Stride"]]
print(stride_log2)
plt.figure(figsize=(16, 5))
color = ['#f58231', '#4363d8', '#a9a9a9', '#469990', '#b39ddb']

# stride_log2 = stride_log2
stride = [-11, -10, -9, -8.4, -8, -7.4, -7, -6.4, -6, -5.4, -5, -4.4, -4, -3.4, -3, -2.4, -2, -1.4, -1, -0.4, 0, 0.6, 1, 1.6, 2 , 2.6, 3, 3.6, 4, 4.6, 5, 5.6, 6, 6.6, 7, 8, 9]

print(len(stride_log2))
print(len(data["local DDR DRAM"]))

plt.plot(stride_log2, data["DDR-L"], marker='s',markersize=10,markeredgecolor="black", label="DDR-L", color=color[1])
plt.plot(stride_log2, data["DDR-R"], marker='^',markersize=10, markeredgecolor="black",label="DDR-R", color=color[2])
# plt.plot(stride_log2, data["CXL FPGA"], marker='D', markersize=10, markeredgecolor="black", label="CXL FPGA", color=color[3])
# plt.plot(stride_log2, data["gem5 FPGA"], marker='o', markersize=10,markeredgecolor="black",label="CXL-MemSim FPGA", color=color[0])
plt.plot(stride_log2, data["CXL-ASIC"], marker='o', markersize=10,markeredgecolor="black",label="CXL-ASIC", color=color[0])
plt.plot(stride_log2, data["CXL-FPGA"], marker='o', markersize=10,markeredgecolor="black",label="CXL-FPGA", color=color[3])





plt.axvline(x=stride_log2[0], linestyle='--', color='red')
plt.axvline(x=cache1, linestyle='--', color='red')
plt.axvline(x=cache2, linestyle='--', color='red')
plt.axvline(x=cache3, linestyle='--', color='red')
plt.axvline(x=stride_log2[39], linestyle='--', color='red')


plt.text(-9, 70, 'L1 cache', fontsize=20)
plt.text(-2.8, 70, 'L2 cache', fontsize=20)
plt.text(3, 70, 'L3 cache', fontsize=20)
plt.text(7.6, 70, 'Memory', fontsize=20)

plt.xlabel("Array Size (log2 MB)",fontsize=24)
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
plt.savefig('lmbench_new.pdf', bbox_inches='tight',pad_inches=0.0)
# plt.show()