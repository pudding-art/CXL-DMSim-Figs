
#
# 带有K4 Phase
# No_Limit = [155.79, 260.76, 185.11, 10.52]
# CPU30 = [1195.7, 2040.21, 1395.19, 59.9]
# MBA30 = [191.95, 315.15, 231.69, 13.48]
# CPU50 = [303.38, 526, 371.71, 21.03]
# MBA50 = [239.1, 382.7, 284.22, 14.37]

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

bar_width = 0.15

No_Limit = [155.79, 260.76, 185.11]
CPU30 = [1195.7, 2040.21, 1395.19]
MBA30 = [191.95, 315.15, 231.69]
CPU50 = [303.38, 526, 371.71]
MBA50 = [239.1, 382.7, 284.22]

labels = ['No Limit', '30% CPU', '30% MBA', '50% CPU', '20% MBA']
x_label = ['K1 Phase', 'K2 Phase', 'K3 Phase']

colors = ['#9BA6A8', '#9467bd', '#c5b0d5', '#FFF176','#FFF9C4']
patterns = ['o', '\\', '/', 'xx', 'x']

x = np.arange(len(x_label))

plt.figure(figsize=(5, 2))

for i, data in enumerate([No_Limit, CPU30, MBA30, CPU50, MBA50]):
    plt.bar(x + i*bar_width, data, label=labels[i], color=colors[i], hatch=patterns[i], width=bar_width, edgecolor='black')

plt.xlabel('PageRank Phase')
plt.ylabel('Execution Time (ns)')
plt.xticks(x + bar_width*2, x_label)

# 设置y轴为科学记数法
formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-3,3))  # 设置科学记数法的阈值
ax = plt.gca()
ax.yaxis.set_major_formatter(formatter)

plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
legend = plt.legend(labels, bbox_to_anchor=(1.0, 1.1), columnspacing=0.2, borderpad=0.2, labelspacing=0.5, handletextpad=0.3, frameon=False)

plt.tight_layout()
plt.savefig('pagerank_time20241005.pdf', bbox_inches='tight',pad_inches=0.0)
# plt.show()