import matplotlib.pyplot as plt

# 数据
labels = ['Insert', 'Found', 'Update', 'Delete']
cxl_dram_hybrid_qps = [1.10779e+06, 1.65306e+06, 1.56434e+06, 885108]
dram_swap_qps = [1.58165e+06, 43271.8, 41481.6, 37318]
cxl_numa_hybrid_qps = [1.27237e+06, 2.30109e+06, 2.23605e+06, 1.16602e+06]
colors = [ '#FFF59D', '#4DD0E1','#AFB8B9']
x = range(len(labels))
patterns = ['/', '\\', 'xx', 'x', '\\\\', '//', '+', '..', '++']
plt.rcParams.update({'font.size': 18})
# 绘制柱状图
fig, ax = plt.subplots(figsize=(12, 6))  # 设置图形大小为宽10英寸，高6英寸
bar_width = 0.25
bar1 = ax.bar(x, dram_swap_qps, bar_width, label='DDR DRAM + Swap Space', color=colors[0], zorder=2,edgecolor='black',hatch=patterns[0])
bar2 = ax.bar([i + bar_width for i in x], cxl_dram_hybrid_qps, bar_width, label='Local DDR + CXL Memory', color=colors[1], zorder=2, edgecolor='black',hatch=patterns[1])
bar3 = ax.bar([i + bar_width*2 for i in x], cxl_numa_hybrid_qps, bar_width, label='Local DDR + remote DDR', color=colors[2], zorder=2,edgecolor='black',hatch=patterns[2])

# 添加标签、标题和图例
ax.set_xlabel('Operation Type')
ax.set_ylabel('QPS')
# ax.set_title('Viper QPS for different operations in different configurations')
ax.set_xticks([i + bar_width for i in x])
ax.set_xticklabels(labels)
ax.legend(loc='upper left')

# 设置图例位置
# ax.legend(loc='upper right')

# 添加数据标签
# def autolabel(bars):
#     for bar in bars:
#         height = bar.get_height()
#         ax.annotate(f'{height:.2e}', xy=(bar.get_x() + bar.get_width() / 2, height),
#                     xytext=(0, 0), textcoords="offset points", ha='center', va='bottom')

# autolabel(bar1)
# autolabel(bar2)
# autolabel(bar3)

# 显示网格线
# ax.grid(axis='y', zorder=1)

# 显示图形
plt.tight_layout()
plt.show()
# plt.savefig('viper_hybrid.pdf', bbox_inches='tight')