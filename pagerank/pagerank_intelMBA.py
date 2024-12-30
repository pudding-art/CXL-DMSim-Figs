import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


percentage = [i for i in range(0,101,10)]

cxl_latency = [ [1059.25, 1676.93, 1322.26, 50.12], [239.10, 382.70, 284.22, 14.37], [191.95, 315.15, 231.69, 13.48], [161.92, 276.60, 202.26, 13.12], [158.24, 271.52, 198.43, 13.10], [153.9, 260.39, 185.59, 10.28], [153.51, 259.85, 185.22, 10.26], [153.33, 261.11, 186.31, 10.38], [155.59, 269.32, 196.95, 13.00], [155.79, 260.76, 185.11, 10.52] ]
cxl_bandwidth =[ [63355.32, 40018.67, 50753.01, 26777883.88], [280675.07, 175354.63, 236116.20, 93419267.54], [349613.45, 212942.61, 289644.56, 99604720.64], [414453.31, 242618.32, 331794.84, 102307657.16], [424094.89, 247164.21, 338204.46, 102456357.21], [435832.22, 257725.37, 361607.03, 130531589.15], [437146.50, 258255.67, 362322.57, 130762912.56], [437688.81, 257016.70, 360200.10, 129343606.81], [431321.56, 249175.81, 340744.43, 103274672.80], [430762.79, 257362.36, 362534.40, 127564788.61] ]


dram_latency =[ [623.37, 1084.24, 819.54, 40.39], [164.53, 269.37, 189.07, 7.72], [133.90, 219.63, 151.63, 5.60], [117.02, 191.53, 130.44, 5.51], [110.41, 182.88, 124.10, 5.49], [107.23, 178.87, 122.30, 5.49], [108.20, 179.52, 116.85, 4.76], [106.05, 178.18, 119.63, 5.20], [107.20, 179.80, 120.63, 5.46], [104.82, 176.20, 116.75, 5.12] ]
dram_bandwidth = [ [107655.25, 61894.86, 81885.82, 33230135.56], [407879.24, 249129.50, 354929.25, 173880294.99], [501190.75, 305549.05, 442566.91, 239627180.94], [573461.42, 350385.43, 514474.75, 243752825.73], [607788.10, 366948.75, 540768.11, 244317943.11], [625845.85, 375193.04, 548709.51, 244400078.53], [620222.57, 373808.64, 574315.44, 281531779.94], [632809.30, 376638.92, 560969.79, 257974354.16], [626029.55, 373240.45, 556313.22, 245726313.63], [640214.06, 380855.49, 574802.77, 262077373.79] ]

colors = ['#9BA6A8','#9467bd', '#c5b0d5', '#c49c94']

# latency
plt.figure(figsize=(12, 1))
barWidth = 0.2
x = np.arange(10)

for i in range(4):
    plt.bar(x + i * barWidth, [cxl_latency[j][i] for j in range(10)], color=colors[i], width=barWidth, label=f'K{i} time')

plt.xlabel('Percentage')
plt.ylabel('Time')
plt.title('Time for K0, K1, K2, K3 at Different Percentages in Intel MBA(CXL)')
plt.xticks(x + barWidth * 1.5, ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])
labels_legend=['K0 Phase','K1 Phase', 'K2 Phase','K3 Phase']
legend = plt.legend(labels_legend, bbox_to_anchor=(0.8, -0.5), ncol=4)  # 图例放在最下方
# plt.show()

plt.savefig('pagerank_intelMBA_cxl.pdf', bbox_inches='tight',pad_inches=0.0)


# bandwidth
# plt.figure(figsize=(12, 1))
# barWidth = 0.2
# x = np.arange(10)
#
# for i in range(4):
#     plt.bar(x + i * barWidth, [np.log2(cxl_bandwidth[j][i]) for j in range(10)], color=colors[i], width=barWidth, label=f'K{i} Edges/Sec')
#
#
# labels_legend=['K0 Phase','K1 Phase', 'K2 Phase','K3 Phase']
# plt.xlabel('Percentage')
# plt.ylabel('Edges/Sec')
# plt.title('Edges/Sec for K0, K1, K2, K3 at Different Percentages in Intel MBA(CXL)')
# plt.xticks(x + barWidth * 1.5, ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])
# legend = plt.legend(labels_legend, bbox_to_anchor=(0.8, -0.5), ncol=4)  # 图例放在最下方
# # plt.show()
#
#
# plt.savefig('pagerank_intelMBA_CXL_bw.pdf', bbox_inches='tight',pad_inches=0.0)