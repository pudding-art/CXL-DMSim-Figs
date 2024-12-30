import matplotlib.pyplot as plt

# 数据
labels = ['local DDR 100%', 'local DDR : CXL memory 50%:50%', 'CXL memory 100%', 'local DDR : remote NUMA 50%:50%']
latency = [427.825/100, 264.585/100, 1130.74/100, 739.73/100]
print(latency)
qps = []
for i in latency:
    qps.append(103597/i)
    # print(i)

print(qps)
# 绘制柱状图
fig, ax = plt.subplots(figsize=(10,6))
bars = ax.bar(labels, qps, color=['#E8E8B9', '#BCBD46', '#A5DFE7', '#86D3DE'],zorder=2, label = labels)


# 添加数据标签
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 1), textcoords="offset points", ha='center', va='bottom')

autolabel(bars)


# 显示网格线
ax.grid(axis='y', zorder=1)
# 设置图例位置

# 添加标签、标题
ax.set_xlabel('Memory Configuration')
ax.set_ylabel('QPS(Query per sec.)')
ax.set_title('MERCI QPS for Different Memory Configurations(12 cores baseline)')
ax.legend(loc='upper right')

# 显示图形
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels)
# ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
