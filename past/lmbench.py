import matplotlib.pyplot as plt

# 数据
labels = ['DDR Local', 'DDR Remote', 'CXL Local', 'CXL Remote', 'Gem5 DDR Local', 'Gem5 CXL Local']

# rd
# values_1core_1channel = [8209.64/1000, 5635.54/1000, 2816.03/1000, 1896.93/1000, 4255.89/1000, 2340.55/1000]
# # frd
# values_1core_1channel = [2539.94/1000, 1707.97/1000, 850.36/1000, 557.95/1000, 2146.93/1000, 1319.26/1000]
# # wr
# values_1core_1channel = [4537.13/1000, 3493.91/1000, 1930.33/1000, 1138.02/1000, 3955.99/1000, 2197.95/1000]
# # fwr
# values_1core_1channel = [5135.42/1000, 3814.67/1000, 2254.06/1000, 1352.77/1000, 1793.52/1000, 1258.36/1000]


# # rd ratio
# values_1core_1channel = [8209.64/8209.64, 5635.54/8209.64, 2816.03/8209.64, 1896.93/8209.64, 4255.89/4255.89, 2340.55/4255.89]
# # frd ratio
# values_1core_1channel = [2539.94/2539.94, 1707.97/2539.94, 850.36/2539.94, 557.95/2539.94, 2146.93/2146.93, 1319.26/2146.93]
# # wr ratio
# values_1core_1channel = [4537.13/4537.13, 3493.91/4537.13, 1930.33/4537.13, 1138.02/4537.13, 3955.99/3955.99, 2197.95/3955.99]
# # fwr ratio
values_1core_1channel = [5135.42/5135.42, 3814.67/5135.42, 2254.06/5135.42, 1352.77/5135.42, 1793.52/1793.52, 1258.36/1793.52]

# 配色
colors = ['#E8E8B9', '#BCBD46', '#A5DFE7', '#86D3DE', '#D9D9D9', '#959595']

# 创建柱状图
plt.figure(figsize=(10, 5))
plt.bar(labels, values_1core_1channel, color=colors, label=labels, zorder=2)

# 添加标题和标签
plt.title('Lmbench fwr opertaion Bandwidth Efficiency for 1 core & 1 channel')
# plt.ylabel('Bandwidth (GB/s)')
plt.ylabel("Bandwidth Efficiency")
plt.xticks(rotation=25)

plt.grid(zorder=1)
plt.legend()
# 显示柱状图
plt.tight_layout()
# plt.show()
plt.savefig("lmbench_fwr_ratio.png")