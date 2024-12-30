import matplotlib.pyplot as plt

# 数据
labels = ['DDR Local', 'CXL Local','DDR Remote(NUMA)',  'Gem5 DDR Local', 'Gem5 CXL Local']
# Copy
# values_1core_1channel = [14082.7/1000, 10942.4/1000, 7758.1/1000, 6638.7/1000, 3021.2/1000, 1558.1/1000]
# Scale
# values_1core_1channel = [7302/1000, 5147.3/1000, 2841.9/1000, 1864.3/1000, 2873.1/1000, 1599.6/1000]
# Add
# values_1core_1channel=[9054/1000,6625.8/1000,3267.7/1000,2204.5/1000,3219.9/1000,1683.1/1000]
# Triad
# values_1core_1channel=[9222.4/1000,6780.9/1000,3256.7/1000,2207.8/1000,3033.9/1000,1635.9/1000]

# Copy
# values_1core_1channel = [14082.7/14082.7,  7758.1/14082.7, 10942.4/14082.7,3021.2/3021.2, 1558.1/3021.2]
# Scale
# values_1core_1channel = [7302/7302, 2841.9/7302,  5147.3/7302,2873.1/2873.1, 1599.6/2873.1]
# Add
# values_1core_1channel=[9054/9054,3267.7/9054,6625.8/9054,3219.9/3219.9,1683.1/3219.9]
# Triad
values_1core_1channel=[9222.4/9222.4,3256.7/9222.4,6780.9/9222.4,3033.9/3033.9,1635.9/3033.9]
# Random Write

# 配色
colors = ['#E8E8B9', '#BCBD46', '#A5DFE7', '#86D3DE', '#D9D9D9', '#959595']

# 创建柱状图
plt.figure(figsize=(10, 5))
plt.bar(labels, values_1core_1channel, color=colors, label=labels, zorder=2)

# 添加标题和标签
plt.title('Stream Triad Operation Bandwidth for 1 core & 1 channel')
plt.ylabel('Bandwidth Effiency')
# plt.xticks(rotation=25)

plt.grid(zorder=1)
plt.legend()
# 显示柱状图
plt.tight_layout()
# plt.show()
plt.savefig("Triad_ratio.png")