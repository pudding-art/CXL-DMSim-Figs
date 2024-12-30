import matplotlib.pyplot as plt
import numpy as np


# latency

ddrl_lat = [0, 36.193, 18.227, 12.206, 9.238, 7.441, 6.261, 5.432, 4.821, 4.351, 3.987, 3.697, 3.461, 3.276, 3.12, 2.997, 2.912, 2.834, 2.788, 2.726, 2.705, 2.683, 2.657, 2.651, 2.622, 2.613, 2.598, 2.584, 2.561, 2.552, 2.528,2.53, 2.504, 2.497, 2.487, 2.475, 2.456, 2.452, 2.439, 2.436, 2.423, 2.419, 2.414, 2.411, 2.417, 2.404, 2.4, 2.386, 2.381]
ddrr_lat = [0, 47.453, 23.835, 15.95, 12.073, 9.75, 9.75, 7.071, 6.252, 5.623, 5.132,
    4.735, 4.405, 4.116, 3.907, 3.708, 3.536, 3.403, 3.289, 3.188, 3.105,
    3.047, 2.988, 2.944, 2.9, 2.88, 2.857, 2.834, 2.817, 2.804, 2.792,
    2.781, 2.77, 2.757, 2.747, 2.744, 2.733, 2.722, 2.716, 2.713, 2.702,
    2.691, 2.682, 2.678, 2.671, 2.662, 2.655, 2.645, 2.64]
cxl_fpga = [0, 80.234, 40.517, 27.112, 20.51, 16.505, 13.875, 12.001, 10.597, 9.515, 8.663,
        7.955, 7.374, 6.904, 6.509, 6.177, 5.913, 5.686, 5.513, 5.378, 5.257,
        5.178, 5.106, 5.044, 4.986, 4.948, 4.907, 4.88, 4.846, 4.812, 4.797,
        4.773, 4.737, 4.714, 4.685, 4.666, 4.652, 4.632, 4.605, 4.589, 4.568,
        4.557, 4.536, 4.528, 4.512, 4.495, 4.483, 4.473, 4.455]
cxl_asic = [0, 59.179, 29.591, 19.689, 14.81, 11.911, 10.01, 8.726, 7.745, 6.983, 6.362,
        5.843, 5.415, 5.051, 4.769, 4.545, 4.381, 4.262, 4.168, 4.101, 4.058,
        4.017, 3.987, 3.958, 3.933, 3.928, 3.888, 3.876, 3.852, 3.828, 3.81,
        3.796, 3.773, 3.757, 3.742, 3.725, 3.719, 3.716, 3.71, 3.675, 3.661,
        3.649, 3.637, 3.627, 3.619, 3.608, 3.596, 3.585, 3.585]
ddr_fpga = [0, 62.533, 31.516, 21.059, 15.84, 12.672, 10.612, 9.139, 7.998, 7.153, 6.458,
        5.906, 5.433, 5.049, 4.718, 4.416, 4.158, 3.935, 3.745, 3.567, 3.412,
        3.283, 3.166, 3.055, 2.956, 2.877, 2.8, 2.731, 2.668, 2.619, 2.572,
        2.523, 2.499, 2.458, 2.444, 2.447, 2.413, 2.396, 2.403, 2.379, 2.364,
        2.342, 2.339, 2.311, 2.308, 2.297, 2.294, 2.296, 2.29]
ddr_asic = [0, 49.427, 24.766, 16.474, 12.38, 9.895, 8.263, 7.11, 6.232, 5.578, 5.069,
        4.658, 4.3, 4.008, 3.739, 3.501, 3.294, 3.104, 2.932, 2.782, 2.65,
        2.537, 2.439, 2.35, 2.278, 2.202, 2.143, 2.092, 2.049, 2.015, 1.978,
        1.954, 1.933, 1.923, 1.901, 1.886, 1.888, 1.883, 1.864, 1.862, 1.847,
        1.842, 1.839, 1.839, 1.829, 1.821, 1.82, 1.813, 1.806]
ddr_rddr = [0, 42.095, 21.078, 14.032, 10.553, 8.448, 7.063, 6.076, 5.339, 4.768, 4.3,
    3.931, 3.617, 3.354, 3.134, 2.945, 2.771, 2.626, 2.49, 2.374, 2.266,
    2.175, 2.091, 2.015, 1.943, 1.88, 1.822, 1.767, 1.72, 1.675, 1.636,
    1.597, 1.568, 1.536, 1.51, 1.485, 1.462, 1.447, 1.425, 1.412, 1.399,
    1.385, 1.377, 1.371, 1.362, 1.353, 1.348, 1.341, 1.338]





# index
index_rddr = [0, 1, 2, 4, 8, 16, 32, 47]
index_fpga = [0, 1, 2, 4, 8, 16, 32, 47]
index_asic = [0, 1, 2, 4, 8, 16, 32, 47]

index_rddr = [i+1 for i in range(48)]

index = [i for i in range(8)]
patterns = ['++', 'xx', 'o',  '+', '..', '/', 'x','\\']
# labels
memory_config_rddr = [ 'DDR-L', 'DDR-L+DDR-R','DDR-R']
memory_config_fpga = [ 'DDR-L','DDR-L+CXL-FPGA','CXL-FPGA']
memory_config_asic = ['DDR-L', 'DDR-L+CXL-ASIC','CXL-ASIC']


colors = ['#FFF9C4', '#FFF59D', '#9DC3E7', '#5F97D2', '#C4A5DE','#8983BF']

# Plotting
plt.figure(figsize=(15, 8))
# Latency Line Plot
index = range(len(index_rddr))
bar_width = 0.3



plt.subplot(3,1,1)
for i in index_rddr:
    print(ddrr_lat[i])
    print(ddr_rddr[i])
    print(ddrl_lat[i])
    print("-----")


    plt.bar(i + bar_width, ddrl_lat[i], bar_width, color=colors[0],label='DDR-L',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[0])
    plt.bar(i + bar_width * 2, ddr_rddr[i], bar_width,color=colors[1], label='DDR-L+DDR-R',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[1])
    plt.bar(i + bar_width * 3, ddrr_lat[i], bar_width, color=colors[2], label='DDR-R',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[2])



plt.xticks([i + bar_width * 2 for i in index_rddr], [str(i) for i in index_rddr],fontsize=15)
y_ticks = [0,10,20,30,40,50,60,70,80]
plt.yticks(y_ticks,[str(i) for i in y_ticks],fontsize=15)
plt.xlabel('CPU Cores Number',fontsize=15)
plt.ylabel('Execution Time (s)',fontsize=15)
# plt.title('Latency Comparison')
# plt.title('Latency Comparison')
plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
legend = plt.legend(memory_config_rddr, bbox_to_anchor=(0.975, 1),columnspacing=0.1,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3,frameon=False,fontsize=15)  # 图例放在最下方
plt.axvline(x=15.2, linestyle='--', color='red')



plt.subplot(3,1,2)
for i in index_rddr:

    plt.bar(i + bar_width, ddrl_lat[i], bar_width, color=colors[0],label='DDR-L',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[0])
    plt.bar(i + bar_width * 2, ddr_fpga[i], bar_width,color=colors[3], label='DDR-L+CXL-FPGA',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[3])
    plt.bar(i + bar_width * 3, cxl_fpga[i], bar_width, color=colors[4], label='CXL-FPGA',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[4])


plt.xticks([i + bar_width * 2 for i in index_rddr], [str(i) for i in index_rddr],fontsize=15)
y_ticks = [0,10,20,30,40,50,60,70,80]
plt.yticks(y_ticks,[str(i) for i in y_ticks],fontsize=15)
plt.xlabel('CPU Cores Number',fontsize=15)
plt.ylabel('Execution Time (s)',fontsize=15)
# plt.title('Latency Comparison')

plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
legend = plt.legend(memory_config_fpga,frameon=False, bbox_to_anchor=(1, 1),columnspacing=0.1,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3 ,fontsize=15)  # 图例放在最下方
plt.axvline(x=26.2, linestyle='--', color='red')

plt.subplot(3,1,3)
for i in index_rddr:

    plt.bar(i + bar_width, ddrl_lat[i], bar_width, color=colors[0],label='DDR-L',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[0])
    plt.bar(i + bar_width * 2, ddr_asic[i], bar_width,color=colors[4], label='DDR-L+CXL-ASIC',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[4])
    plt.bar(i + bar_width * 3, cxl_asic[i], bar_width, color=colors[5], label='CXL-ASIC',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[5])



plt.xticks([i + bar_width * 2 for i in index_rddr], [str(i) for i in index_rddr],fontsize=15)
y_ticks = [0,10,20,30,40,50,60,70,80]
plt.yticks(y_ticks,[str(i) for i in y_ticks],fontsize=15)
plt.xlabel('CPU Cores Number',fontsize=15)
plt.ylabel('Execution Time (s)',fontsize=15)
# plt.title('Latency Comparison')
plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
legend = plt.legend(memory_config_asic, bbox_to_anchor=(1, 1),columnspacing=0.1,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3,frameon=False,fontsize=15)  # 图例放在最下方
plt.axvline(x=19.2, linestyle='--', color='red')

plt.tight_layout()
# plt.show()
plt.savefig('xsbench_lat_0817.pdf', bbox_inches='tight',pad_inches=0.0)