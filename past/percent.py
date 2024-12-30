import matplotlib.pyplot as plt

# 定义块大小和P99延迟值
block_sizes = ['4k', '8k', '16k', '32k', '64k', '128k', '256k', '512k']
p99_latency_ddr = [233, 359, 627, 1172, 2245, 4228, 8717, 19006]
p99_latency_cxl = [285, 474, 832, 1582, 3032, 5932, 12125, 30016]

# 计算P99 Percent Increase
percent_increase = [(cxl - ddr) / ddr * 100 for cxl, ddr in zip(p99_latency_cxl, p99_latency_ddr)]

# 创建柱状图
fig, ax1 = plt.subplots(figsize=(12, 5))

bar_width = 0.35
index = range(len(block_sizes))

bars1 = ax1.bar(index, p99_latency_ddr, bar_width, color=(1, 0.7, 0, 0.7), label='DDR Local')
bars2 = ax1.bar([i + bar_width for i in index], p99_latency_cxl, bar_width,color=(0, 0, 0.7, 0.7), label='CXL Local')

ax1.set_xlabel('Block Size (Bytes)')
ax1.set_ylabel('P99 Latency (us)')
ax1.set_xticks([i + bar_width/2 for i in index])
ax1.set_xticklabels(block_sizes)  # 设置x轴标签为块大小
ax1.set_yscale('log')
ax1.set_yticks([1, 10, 100, 1000, 10000])

# 计算折线图中每个点的x轴坐标
line_index = [i + bar_width/2 for i in index]

# 添加P99 Percent Increase的折线图
ax2 = ax1.twinx()
line = ax2.plot(line_index, percent_increase, marker='o', markerfacecolor='white', markeredgecolor='red', linestyle='-', color='red', label='P99 Percent Increase')
ax2.set_ylabel('P99 Percent Increase (%)')

ax2.set_yticks([0, 20, 40, 60, 80, 100])

# 将图例放在一起，横向排列在图像的上方
handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles + handles2, labels + labels2, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3)

plt.suptitle('P99 Latency values of FIO for various block sizes', y=0.92)  # 整体标题
# plt.title('P99 Latency values of DDR Local and CXL Local, and P99 Percent Increase', pad=20)  # 子标题

# plt.show()
plt.savefig("fio.png")