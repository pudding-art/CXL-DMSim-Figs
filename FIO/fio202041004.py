import matplotlib.pyplot as plt
import numpy as np

# Block sizes
block_sizes = ['4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K']

# P99 Latency for DDR Local and CXL Local
p99_ddr = [786.7311289379799, 851.9612198415737, 926.6752967972102, 1020.4378892628946, 1117.3618104125935, 1201.600145123254, 1304.8769274182168, 1408.1335738616892]
p99_cxl = [811.6190413802833, 892.6759115554389, 967.4302602140567, 1064.34411343801, 1151.7639126841752, 1248.6979017596193, 1348.803287444823, 1477.4411746921166]

# P99 Latency Increase Percentage
p99_increase = [22.95584415584415, 32.599999999999994, 33.420779220779224, 35.67792207792208, 35.26753246753247, 40.807792207792204, 39.78181818181819, 58.24935064935065]

# Define colors and patterns for bars
colors = ['#FFF9C4', '#FFF59D', '#FFF176', '#B2EBF2', '#4DD0E1',  '#9BA6A8', '#F6CAE5',
          '#C4A5DE', '#A1A9D0', '#CFEAF1', '#96CCCB', '#8ECFC9']
patterns = ['o', 'x', '*', '//', '||', '\\\\', '.', 'xo','--']

# Create figure and axes
fig, ax1 = plt.subplots(figsize=(10, 4))
plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125

# Plotting P99 Latency as bars
bar_width = 0.35
index = np.arange(len(block_sizes))

bars1 = ax1.bar(index, p99_ddr, bar_width, label='DDR Local', linewidth=2, color=colors[0], edgecolor='black', hatch=patterns[0])
bars2 = ax1.bar(index + bar_width, p99_cxl, bar_width, label='CXL Local', linewidth=2, color=colors[3], edgecolor='black', hatch=patterns[2])

ax1.set_xlabel('Block Size', fontsize=20)
ax1.set_ylabel('P99 Latency (us)', fontsize=20)
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(block_sizes, fontsize=20)
ax1.legend(bbox_to_anchor=(0.28, 1.03), fontsize=20, frameon=False, edgecolor='black', fancybox=False, borderpad=0.2, labelspacing=0.2, handletextpad=0.2, columnspacing=0.2)
ax1.set_ylim(0, 1500)
ax1.set_yticks(np.arange(0, 1501, 250))
ax1.tick_params(axis='y', labelsize=20)

# Instantiate a second y-axis
ax2 = ax1.twinx()

# Calculate the center of each bar for the line plot
line_x = index + bar_width / 2

# Plotting P99 Latency Increase Percentage as line
line1 = ax2.plot(line_x, p99_increase, 'r-o', label='P99 Percentage', markerfacecolor='white', markeredgewidth=2, markeredgecolor='red', linewidth=2, markersize=10)


ax2.set_ylim(0, 100)
ax2.set_yticks(np.arange(0, 101, 10))
ax2.set_ylabel('P99 Percentage Increase (%)', fontsize=20)
ax2.legend(bbox_to_anchor=(0.65, 1.03), fontsize=20, columnspacing=0.2, borderpad=0.2, labelspacing=0.2, handletextpad=0.2, frameon=False)

ax1.tick_params(axis='y', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)

# Show the plot
# plt.show()
plt.savefig('fio1004.pdf', pad_inches=0.0)