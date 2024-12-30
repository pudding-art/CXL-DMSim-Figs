import matplotlib.pyplot as plt
import numpy as np

data = {
    "Stride": [0.00049, 0.00098, 0.00195, 0.00391, 0.00781, 0.01562, 0.03125, 0.04688, 0.09375, 0.1875, 0.375, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512,768, 1024],
    "CXL-DMSim(F)": [1.418, 1.418,1.418, 1.418,1.409, 1.406, 1.403,1.403, 5.623, 5.622, 5.621,  6.178,6.192, 7.317, 21.203,34.977, 39.763,44.431, 47.268, 48.995,49.373,49.467, 49.481,49.499, 49.496,99.100,236.342,327.165, 352.460,368.803,374.073, 377.660, 378.818 ],
    "DDR-L": [1.728, 1.728, 1.728, 1.728, 1.728, 1.728,1.728,1.729,5.529,6.181,6.747,7.874, 7.95, 8.439, 15.043, 36.633, 38.908, 40.359, 43.89, 48.194, 48.982, 51.004, 49.55, 49.665, 50.141, 59.725, 79.482,101.272,112.793,123.424,127.719,131.453,131.481],
    "DDR-R": [1.728, 1.728, 1.728, 1.728, 1.728, 1.728,1.728,1.729,5.529,6.682,7.016,7.801, 7.949, 12.212, 18.182, 35.558, 37.778, 40.366, 43.757, 47.262, 47.657, 47.785, 48.418, 50.924, 52.805, 69.784, 99.582,142.178,162.916,179.604,190.742,198.50,202.870],
    "CXL-FPGA": [1.728, 1.728, 1.728, 1.728, 1.728, 1.728,1.728, 1.729,5.528,5.528,6.569,7.808, 7.947, 7.949, 16.718, 33.676, 37.197, 38.544, 41.386, 46.658, 47.586, 47.792, 47.973, 48.163, 48.196, 75.845, 152.623,243.048,285.925,326.383 ,368.336,379.995, 382.928],
    "CXL-ASIC":[1.728, 1.728, 1.728, 1.728, 1.728, 1.728,1.728,1.729,5.527,5.527,7.22,7.882, 7.945, 7.987, 16.622, 34.522, 40.228, 40.993, 45.331, 50.047, 50.781, 50.96, 51.136, 51.211, 51.13, 66.528, 123.13, 185.858,216.799,264.898, 274.033, 278.522, 284.893],
    "CXL-DMSim(A)":[1.418, 1.418,1.418, 1.418,1.409, 1.406, 1.403, 1.404, 5.622, 5.622, 5.621,6.187, 6.195, 7.324, 21.255, 35.054, 39.613, 44.453, 47.244, 49.021, 49.385, 49.474, 49.485, 49.494, 49.504, 85.349, 184.331, 249.589, 267.873, 279.605, 283.401, 285.972, 286.831 ]
}
"""
random read pattern
remote_numa 
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.528', '5.530', '6.891', '7.948', '7.948', '9.222', '16.030', '32.677', '39.516', '40.512', '44.969', '47.605', '48.788', '48.759', '51.412', '52.824', '57.331', '81.600', '123.150', '154.635', '174.327', '191.862', '195.603', '205.608', '216.556']

local ddr
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.530', '5.529', '6.728', '7.817', '8.418', '12.616', '19.553', '32.448', '39.265', '40.857', '45.775', '47.592', '49.394', '48.068', '49.929', '51.641', '57.727', '67.711', '89.340', '114.098', '120.938', '125.775', '131.057', '132.879', '137.527']

cxl-asic                                                                                                                                                                                                                                                                    ,216.799,   264.898,   274.033,   278.522,   284.893],
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.529', '5.882', '7.117', '7.948', '7.949', '7.950', '8.123', '37.006', '38.152', '39.971', '43.852', '48.189', '48.501', '49.188', '49.275', '49.086', '50.277', '69.638', '121.049', '182.023', '213.302', '246.628', '264.098', '273.723', '283.118']
"""

# 按CXL-MemSim的标准来,要明白是要跟谁比较
cache1 = np.log2(0.046)
cache2 = np.log2(2)
cache3 = np.log2(96)


stride_log10 = [np.log10(i) for i in data["Stride"]]
# plotcolor = Hstray_2plot
stride_log2 = [np.log2(i) for i in data["Stride"]]
print(stride_log2)
plt.figure(figsize=(13, 5))


color = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#999999']

# stride_log2 = stride_log2
stride = [-11, -10, -9, -8.4, -8, -7.4, -7, -6.4, -6, -5.4, -5, -4.4, -4, -3.4, -3, -2.4, -2, -1.4, -1, -0.4, 0, 0.6, 1, 1.6, 2 , 2.6, 3, 3.6, 4, 4.6, 5, 5.6, 6, 6.6, 7, 8, 9]


plt.plot(stride_log2, data["DDR-L"], marker='p',markersize=10,markeredgecolor="black", label="DDR-L", color=color[4])
plt.plot(stride_log2, data["DDR-R"], marker='^',markersize=10, markeredgecolor="black",label="DDR-R", color=color[5])
plt.plot(stride_log2, data["CXL-ASIC"], marker='s', markersize=10, markeredgecolor="black", label="CXL-ASIC", color=color[3])
plt.plot(stride_log2, data["CXL-DMSim(A)"], marker='H', markersize=10,markeredgecolor="black",label="CXL-DMSim$_A$", color=color[0])
plt.plot(stride_log2, data["CXL-FPGA"], marker='D', markersize=10, markeredgecolor="black", label="CXL-FPGA", color=color[1])
plt.plot(stride_log2, data["CXL-DMSim(F)"], marker='o', markersize=10,markeredgecolor="black",label="CXL-DMSim$_F$", color=color[2])




plt.axvline(x=stride_log2[0], linestyle='--', color='red')
plt.axvline(x=cache1, linestyle='--', color='red')
plt.axvline(x=cache2, linestyle='--', color='red')
plt.axvline(x=cache3, linestyle='--', color='red')
plt.axvline(x=stride_log2[32], linestyle='--', color='red')


plt.text(-9, 68, 'L1 cache', fontsize=20)
plt.text(-2.8, 68, 'L2 cache', fontsize=20)
plt.text(2.7, 68, 'L3 cache', fontsize=20)
plt.text(7.3, 54, 'Memory', fontsize=20)

plt.xlabel("Array Size (log2 MB)",fontsize=24)
plt.ylabel("Latency (ns)",fontsize=24)

plt.rcParams.update({'font.size': 20})
# plt.title("Comparison of Latency for Different Memory Types")
plt.legend(loc='upper left',bbox_to_anchor=(0.03, 1), ncol=3, columnspacing=4.0,fontsize=20,frameon=False, edgecolor='black',fancybox=False,borderpad = 0.1, labelspacing = 0.2, handletextpad = 0.2) # 图例放在最下方

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
plt.xticks(np.log2(data["Stride"]), data["Stride"], fontsize=19,rotation=90)
# 等距离显式
# distance = [i for i in range(1,len(stride)+1)]
# plt.xticks(distance, data["Stride"], fontsize=15,rotation=90)

plt.yticks(fontsize=20)
plt.tight_layout()
# plt.tight_layout()
plt.savefig('lmbench.pdf', bbox_inches='tight',pad_inches=0.0)
# plt.show()