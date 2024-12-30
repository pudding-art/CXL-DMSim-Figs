import matplotlib.pyplot as plt
import numpy as np

data = {
    "Stride": [0.00049, 0.00098, 0.00195, 0.00293, 0.00391, 0.00586, 0.00781, 0.01172, 0.01562, 0.02344, 0.03125, 0.04688, 0.0625, 0.09375, 0.125, 0.1875, 0.25, 0.375, 0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 256, 512],
    "gem5":  [1.614, 1.614, 1.614, 1.614, 1.614, 1.614, 1.614, 1.614, 1.614, 1.614, 1.597, 1.597, 5.209, 6.841, 6.838, 6.837, 6.836, 6.834, 6.834, 6.834, 6.844, 9.993, 17.426, 25.279, 28.488, 31.723, 33.097, 34.38, 34.806, 64.366, 167.565, 319.095, 360.929, 368.487, 379.989, 389.722, 389.722],
    "local DDR DRAM": [2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.388, 7.635, 7.635, 7.635, 7.635, 8.105, 9.284, 10.031, 10.784, 10.988, 15.084, 20.752, 34.964, 39.361, 43.484, 47.715, 53.108, 53.615, 57.665, 68.575, 91.508, 108.14, 132.336, 141.67, 150.165, 151.265],
    "remote NUMA": [2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.388, 7.635, 7.635, 7.635, 7.635, 8.054, 9.767, 10.081, 10.936, 11.697, 14.065, 23.175, 30.357, 34.085, 39.38, 44.07, 51.142, 52.814, 68.695, 83.986, 117.998, 147.561, 178.835, 191.169, 203.371, 205.881],
    "CXL hardware prototype": [2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.386, 2.388, 7.635, 7.635, 7.635, 7.635, 8.307, 8.978, 9.879, 10.905, 10.975, 11.382, 17.452, 34.226, 37.999, 40.146, 45.059, 50.233, 51.815, 62.412, 118.92, 219.727, 273.61, 325.039, 345.928, 384.831, 392.488]
}


stride_log10 = [np.log10(i) for i in data["Stride"]]
# plotcolor = Hstray_2plot
stride_log2 = [np.log2(i) for i in data["Stride"]]
print(stride_log2)
plt.figure(figsize=(12, 5))
color = ['#f58231', '#4363d8', '#a9a9a9', '#469990']

# stride_log2 = stride_log2
stride = [-11, -10, -9, -8.4, -8, -7.4, -7, -6.4, -6, -5.4, -5, -4.4, -4, -3.4, -3, -2.4, -2, -1.4, -1, -0.4, 0, 0.6, 1, 1.6, 2 , 2.6, 3, 3.6, 4, 4.6, 5, 5.6, 6, 6.6, 7, 8, 9]

# plt.plot(stride_log2, data["gem5"], marker='o', markeredgecolor="black",label="gem5 CXL HDM", color=color[0])
# plt.plot(stride_log2, data["local DDR DRAM"], marker='s',markeredgecolor="black", label="local DDR DRAM", color=color[1])
# plt.plot(stride_log2, data["remote NUMA"], marker='^', markeredgecolor="black",label="remote NUMA", color=color[2])
# plt.plot(stride_log2, data["CXL hardware prototype"], marker='D', markeredgecolor="black", label="CXL hardware prototype", color=color[3])




plt.xlabel("Array Size",fontsize=18)
plt.ylabel("Latency (ns)",fontsize=18)

plt.rcParams.update({'font.size': 18})
# plt.title("Comparison of Latency for Different Memory Types")

# plt.grid(True)

# log2显式
# plt.xticks(np.log2(data["Stride"]), data["Stride"], fontsize=15,rotation=90)
# 等距离显式
distance = [i for i in range(1,len(stride)+1)]
plt.xticks(distance, data["Stride"], fontsize=15,rotation=90)



plt.plot(distance, data["gem5"], marker='o', markeredgecolor="black",label="gem5 CXL HDM", color=color[0])
plt.plot(distance, data["local DDR DRAM"], marker='s',markeredgecolor="black", label="local DDR DRAM", color=color[1])
plt.plot(distance, data["remote NUMA"], marker='^', markeredgecolor="black",label="remote NUMA", color=color[2])
plt.plot(distance, data["CXL hardware prototype"], marker='D', markeredgecolor="black", label="CXL hardware prototype", color=color[3])

plt.axvline(x=distance[0], linestyle='--', color='red')
plt.axvline(x=distance[10], linestyle='--', color='red')
plt.axvline(x=distance[22], linestyle='--', color='red')
plt.axvline(x=distance[29], linestyle='--', color='red')
plt.axvline(x=distance[36], linestyle='--', color='red')

plt.text(4, 52, 'L1 cache', fontsize=18)
plt.text(14, 52, 'L2 cache', fontsize=18)
plt.text(22.5, 52, 'L3 cache', fontsize=18)
plt.text(31.5, 51, 'Memory', fontsize=18)

plt.yticks(fontsize=18)

plt.legend(loc="upper left")
plt.tight_layout()
# plt.tight_layout()
plt.savefig('lmbench_equal.pdf', bbox_inches='tight')
# plt.show()