import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


percentage = [i for i in range(0,101,10)]

cxl_latency = [ [1960.79, 2662.60, 1881.90, 108.40], [1268.64, 1393.10, 974.79, 54.10], [1195.70, 2040.21, 1395.19, 59.90], [485.95, 670.68, 470.79, 26.10], [303.38, 526.00, 371.71, 21.03], [286.74, 437.09, 315.18, 17.33], [212.92, 382.04, 279.99, 18.55], [191.21, 335.57, 245.33, 16.12], [170.11, 291.15, 207.00, 11.33], [152.68, 259.08, 184.57, 10.15] ]
cxl_bandwidth = [ [34225.35, 25204.25, 35660.12, 12382164.34], [52898.25, 48172.39, 68844.08, 24810191.63], [56125.08, 32893.18, 48100.09, 22406067.96], [38098.11, 100060.36, 142543.05, 51428045.04], [221200.90, 127582.59, 180541.76, 63835234.84], [234040.78, 153535.30, 212920.56, 77440454.43], [315176.45, 175657.55, 239680.84, 72348852.83], [350967.84, 199987.49, 273547.51, 83275295.00], [394505.53, 230494.26, 324190.60, 118500816.62], [439539.88, 259029.32, 363602.99, 132269388.78] ]

dram_latency = [ [1283.20, 1812.29, 1208.80, 52.49], [936.92, 920.68, 625.09, 28.51], [359.06, 646.29, 424.41, 18.29], [389.42, 448.97, 303.91, 13.00], [412.08, 351.91, 233.91, 9.69], [171.35, 289.89, 193.69, 7.82], [146.33, 252.32, 169.21, 6.86], [127.58, 218.14, 145.84, 6.15], [113.56, 192.52, 128.60, 5.14], [103.65, 173.76, 115.92, 4.70] ]
dram_bandwidth =[ [52298.00, 37029.80, 55516.88, 25567883.26], [71627.08, 72890.20, 107357.57, 47080472.96], [186903.65, 103836.61, 158122.49, 73408571.49], [172332.38, 149472.48, 220815.85, 103214782.76], [162853.21, 190699.45, 286894.88, 138514214.44], [391643.39, 231500.05, 346467.09, 171649234.91], [458614.13, 265965.68, 396610.07, 195588939.59], [526022.45, 307630.44, 460153.76, 218271333.44], [590965.85, 348571.84, 521828.50, 260911981.32], [647485.55, 386206.93, 578925.48, 285704428.36] ]




colors = ['#9BA6A8','#9467bd', '#c5b0d5', '#c49c94']

# latency 改成条件编译
# plt.figure(figsize=(12, 1))
# barWidth = 0.2
# x = np.arange(10)
#
# for i in range(4):
#     plt.bar(x + i * barWidth, [cxl_latency[j][i] for j in range(10)], color=colors[i], width=barWidth, label=f'K{i} time')
#
# plt.xlabel('Percentage')
# plt.ylabel('Time')
# plt.title('Time for K0, K1, K2, K3 at Different Percentages in cgroup(CXL)')
# plt.xticks(x + barWidth * 1.5, ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])
# labels_legend=['K0 Phase','K1 Phase', 'K2 Phase','K3 Phase']
# legend = plt.legend(labels_legend, bbox_to_anchor=(0.8, -0.5), ncol=4)  # 图例放在最下方
# # plt.show()
#
# plt.savefig('pagerank_cgroup_cxl_lat.pdf', bbox_inches='tight',pad_inches=0.0)


# bandwidth
plt.figure(figsize=(12, 1))
barWidth = 0.2
x = np.arange(10)

for i in range(4):
    plt.bar(x + i * barWidth, [np.log2(dram_bandwidth[j][i]) for j in range(10)], color=colors[i], width=barWidth, label=f'K{i} Edges/Sec')

plt.xlabel('Percentage')
plt.ylabel('Edges/Sec')
plt.title('log2(Edges/Sec) for K0, K1, K2, K3 at Different Percentages in cgroup(DRAM)')
plt.xticks(x + barWidth * 1.5, ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])
labels_legend=['K0 Phase','K1 Phase', 'K2 Phase','K3 Phase']
legend = plt.legend(labels_legend, bbox_to_anchor=(0.8, -0.5), ncol=4)  # 图例放在最下方
# plt.show()

plt.savefig('pagerank_cgroup_DRAM_bw.pdf', bbox_inches='tight',pad_inches=0.0)