import matplotlib.pyplot as plt
import numpy as np

# 定义标签、操作和QPS数据
# labels = ["PMEM", "LRU CXL-SSD", "FIFO CXL-SSD"]
ops = ["Insert", "Select", "Update", "Delete"]
# pmem = [729322, 735283, 715724, 427200]
cxl_memory = [850671,914647,1264680,782527]
LRU_CXLSSD = [727704, 669959, 853188, 596502]
FIFO_CXLSSD = [727254, 670766, 881651, 523753]
CXL_SSD = [75931.6,93812.5,135770,128766]

colors = ['#FFF9C4', '#FFF59D', '#FFF176', '#B2EBF2', '#4DD0E1', '#00BCD4', '#C3CACA', '#AFB8B9', '#9BA6A8']
patterns = ['/', '..', 'xx', '+']


# 将QPS数据转换为百万分之一
cxl_memory = [i / 1000000 for i in cxl_memory]
LRU_CXLSSD = [i / 1000000 for i in LRU_CXLSSD]
FIFO_CXLSSD = [i / 1000000 for i in FIFO_CXLSSD]
CXL_SSD = [i / 1000000 for i in CXL_SSD]

# 转换数据为numpy数组，便于索引
# pmem = np.array(pmem)
cxl_memory = np.array(cxl_memory)
LRU_CXLSSD = np.array(LRU_CXLSSD)
FIFO_CXLSSD = np.array(FIFO_CXLSSD)
CXL_SSD = np.array(CXL_SSD)
# 创建图形和坐标轴
plt.figure(figsize=(13, 4))
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
plt.tick_params(axis='y',width=3)#修改刻度线线粗细width参数，修改刻度字体labelsize参数

# 刻度线长度调整
# plt.tick_params(axis='x', length=10)  # 设置x轴刻度线长度为10
plt.tick_params(axis='y', length=5)  # 设置y轴刻度线长度为10
# 设置每个柱子的宽度
bar_width = 1

# 计算每个柱子的位置
index0 = [i*5 for i in range(4)]
index1 = [i*5+1 for i in range(4)]
index2 = [i*5+2 for i in range(4)]
index3 = [i*5+3 for i in range(4)]
index_ = [i*5+1.5 for i in range(4)]
# 绘制PMEM的柱状图
# for i in range(len(ops)):
#     plt.bar(i*4, pmem[i], bar_width, label='PMEM', color=colors[0], hatch=patterns[0])
#     plt.bar(i*4+1, LRU_CXLSSD[i], bar_width, label='LRU_CXLSSD', color=colors[3], hatch=patterns[1])
#     plt.bar(i*4+2, FIFO_CXLSSD[i], bar_width, label='FIFO_CXLSSD', color=colors[6], hatch=patterns[2])
# 绘制CXL memory的柱状图
plt.bar(index0, cxl_memory, bar_width, label='CXL-DRAM', color=colors[0],linewidth=2.5, hatch=patterns[0], edgecolor='black')

# 绘制LRU CXL-SSD的柱状图，位置稍微偏移以避免重叠
plt.bar(index1, LRU_CXLSSD, bar_width, label='LRU CXL-SSD', color=colors[3], linewidth=2.5,hatch=patterns[1], edgecolor='black')

# 绘制FIFO CXL-SSD的柱状图，位置再偏移
plt.bar(index2, FIFO_CXLSSD, bar_width, label='FIFO CXL-SSD', color=colors[6], linewidth=2.5,hatch=patterns[2], edgecolor='black')

# 绘制CXL SSD的柱状图
plt.bar(index3, CXL_SSD, bar_width, label='CXL-SSD', color=colors[8], linewidth=2.5,hatch=patterns[3], edgecolor='black')



plt.xticks([])
# # 绘制LRU CXL-SSD的柱状图，位置稍微偏移以避免重叠
# plt.bar(index + bar_width, LRU_CXLSSD, bar_width, label='LRU CXL-SSD', color='#B2EBF2',hatch=patterns)
#
# # 绘制FIFO CXL-SSD的柱状图，位置再偏移
# plt.bar(index + 2 * bar_width, FIFO_CXLSSD, bar_width, label='FIFO CXL-SSD', color='#4DD0E1',hatch=patterns)

# 添加图例
plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
plt.legend(fontsize=25,ncol=4, bbox_to_anchor=(1.04, 1.25),frameon=False,edgecolor='black', columnspacing=0.5,fancybox=False,borderpad = 0.4, labelspacing = 0.4, handletextpad = 0.2)


# 设置坐标轴标签和标题
plt.xlabel('Operation Type', fontsize=30)
plt.ylabel('QPS (1e6)', fontsize=30)
# plt.title('QPS Comparison of Different Memory Pools for Operations', fontsize=20)
y_ticks = [0.0,0.2,0.4,0.6,0.8,1.0,1.2]
plt.yticks(y_ticks,[str(i) for i in y_ticks], fontsize=30)
plt.xticks(index_, ops, fontsize=30)
# 显示网格
# plt.grid(True)
bwidth=3
# 设置字体大小
ax = plt.gca()
# plt.rcParams.update({'font.size': 20})
ax.spines['bottom'].set_linewidth(bwidth)
ax.spines['left'].set_linewidth(bwidth)
ax.spines['top'].set_linewidth(bwidth)
ax.spines['right'].set_linewidth(bwidth)



# 调整子图参数，保证标签不会重叠
# plt.tight_layout()

plt.savefig('Viper_CXLSSD.pdf', bbox_inches='tight',pad_inches=0.0)
plt.show()