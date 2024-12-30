import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 横轴和纵轴标签
labels = ['CXL Seq Read', 'CXL Rand Read', 'CXL Seq Write', 'CXL Rand Write']

# Alone列的数据，单位为GB/s
alone_data = [21.81, 21.67, 16.24, 16.24]

# 百分比数据，已经是相对于Alone的值
percentage_data = [
    [63.39, 63.55, 43.48, 40.03],
    [27.03, 63.70, 32.71, 43.85],
    [41.23, 41.22, 72.62, 72.55],
    [45.71, 50.73, 33.69, 72.31]
]

# 将Alone数据和百分比数据合并，形成热力图数据
# 将Alone数据作为第一列
heatmap_data = np.vstack(np.array(percentage_data))
# heatmap_data = np.vstack([np.array(alone_data), np.array(percentage_data)])

# 创建一个热力图
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="YlGnBu",
            xticklabels=labels, yticklabels=labels, cbar_kws={'label': 'Percentage(%)'})

# 调整y轴的标签，使其不显示"Alone"
# plt.yticks(ticks=np.arange(.5, len(labels), 1), labels=labels[1:])
# 将横坐标放在上面的横线上
# plt.xlabel('Operation Type', labelpad=10)  # 调整labelpad的值可以改变标签与横线的距离
# 设置标题
plt.title('Performance Relative to Alone')

# 显示图表
# plt.show()

plt.savefig('read_write_contention.pdf', bbox_inches='tight',pad_inches=0.0)