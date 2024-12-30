import matplotlib.pyplot as plt

# 数据
labels = ['Insert', 'Found', 'Update', 'Delete']
cxl_qps = [1.12803e+06, 1.75288e+06, 1.90508e+06, 986125]
local_qps = [2.18444e+06, 4.06014e+06, 4.35761e+06, 2.22703e+06]

x = range(len(labels))

# 绘制柱状图
fig, ax = plt.subplots()
bar_width = 0.35
bar1 = ax.bar(x, local_qps, bar_width, label='Local Memory')
bar2 = ax.bar([i + bar_width for i in x], cxl_qps, bar_width, label='CXL Memory')

# 添加标签、标题和图例
ax.set_xlabel('Operations')
ax.set_ylabel('QPS')
ax.set_title('QPS for Different Operations in Local Memory and CXL Memory')
ax.set_xticks([i + bar_width/2 for i in x])
ax.set_xticklabels(labels)
ax.legend()

# 显示图形
plt.show()
