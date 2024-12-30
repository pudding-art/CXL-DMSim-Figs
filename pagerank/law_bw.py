import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

bar_width = 0.15

No_Limit = [430762.79, 257362.36, 362534.4]  # , 127564788.6]
CPU30 = [56125.08, 32893.18, 48100.09]  # , 22406067.96]
MBA30 = [349613.45, 212942.61, 289644.56]  # , 99604720.64]
CPU50 = [221200.9, 127582.59, 180541.7]  # , 63835234.84]
MBA50 = [280675.07, 175354.63, 236116.2]  # , 93419267.54]

labels = ['No Limit', '30% CPU', '30% MBA', '50% CPU', '20% MBA']
x_labels = ['K1 Phase', 'K2 Phase', 'K3 Phase']  # , 'K4 Phase'

colors = ['#9BA6A8', '#9467bd', '#c5b0d5', '#FFF176', '#FFF9C4']
patterns = ['o', '\\', '/', 'xx', 'x']


x = np.arange(len(x_labels))

plt.figure(figsize=(5, 2))

for i, data in enumerate([No_Limit, CPU30, MBA30, CPU50, MBA50]):
    plt.bar(x + i * bar_width, data, label=labels[i], color=colors[i], hatch=patterns[i], width=bar_width, edgecolor='black')

plt.xlabel('PageRank Phase')
plt.ylabel('Edges/sec')
# plt.title('Execution Bandwidth')
plt.xticks(x + bar_width * 2, x_labels)

# 设置y轴为科学记数法
formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
ax = plt.gca()
ax.yaxis.set_major_formatter(formatter)

# 调整图例
plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
legend = plt.legend(labels, bbox_to_anchor=(1.0, 1.05), columnspacing=0.2, borderpad=0.2, labelspacing=0.5, handletextpad=0.3, frameon=False)

plt.tight_layout()
# plt.show()

plt.savefig('pagerank_bw20241005.pdf', bbox_inches='tight',pad_inches=0.0)