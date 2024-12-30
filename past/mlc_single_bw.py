import matplotlib.pyplot as plt

# 数据
labels = ['DDR Local', 'DDR Remote', 'CXL Local', 'CXL Remote', 'Gem5 DDR Local', 'Gem5 CXL Local']
# Sequential Read
# values_1core_1channel = [16255.9/1000, 12886.3/1000, 7205/1000, 5091.4/1000, 2942.7/1000, 1497.5/1000]
# Sequential Write
# values_1core_1channel = [24028.3/1000, 23225.1/1000, 24590.3/1000, 22469.6/1000, 1000.5/1000, 290.3/1000]
# Random Read
# values_1core_1channel = [16858.1/1000, 12892.3/1000, 7199.1/1000, 5088.3/1000, 2942.7/1000, 1497.5/1000]
# Random Write
# values_1core_1channel = [23052/1000, 23218.3/1000, 24585.4/1000, 22462.9/1000, 1000.5/1000, 290.3/1000]

# Random Read Ratio
# values_1core_1channel = [16858.1/16858.1, 12892.3/16858.1, 7199.1/16858.1, 5088.3/16858.1, 2942.7/2942.7, 1497.5/2942.7]
# Random Write Ratio
values_1core_1channel = [23052/23052, 23218.3/23052, 24585.4/23052, 22462.9/23052, 1000.5/1000.5, 290.3/1000.5]
# 配色
colors = ['#E8E8B9', '#BCBD46', '#A5DFE7', '#86D3DE', '#D9D9D9', '#959595']

# 创建柱状图
plt.figure(figsize=(10, 5))
plt.bar(labels, values_1core_1channel, color=colors, label=labels, zorder=2)

# 添加标题和标签
plt.title('Random Write Bandwidth Effiency for 1 core & 1 channel')
# plt.ylabel('Bandwidth (GB/s)')
plt.ylabel("Bandwidth Effiency")
plt.xticks(rotation=25)

plt.grid(zorder=1)
plt.legend()
# 显示柱状图
plt.tight_layout()
plt.show()
# plt.savefig("mlc_random_write_ratio.png")