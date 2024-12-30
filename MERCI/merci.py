import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 创建一个 FontProperties 对象并设置 weight 属性为 'bold'
font = FontProperties()
# font.set_weight('bold') # 设置所有的字体均为加粗


# 原始延迟数据（毫秒）
# 顺序 DDR-R CXL CXL-MemSim
# FPGA Data: 30.2934, 25.3612, 64.1165,72.9889, 91.986, 181.972,
# delays_ms = [ 97.2902, 49.7066, 97.4834, 97.2902,90.6086, 198.179, 86.9868, 77.9881, 146.978]
delays_ms_96 = [30.2934, 15.372, 30.0796,  30.2934, 23.6173, 54.8686, 72.9889, 59.9909, 117.982]  # -3，-6 三个数据为旧gem5的结果数据



delays_ms_12 = [35.9181, 32.8975, 45.41, 35.9181,46.2586, 71.5609, 72.9889, 59.9909, 117.982]
delays_ms_24 = [35.6533, 25.0249, 39.0689, 35.6533,30.1243, 45.3497, 72.9889, 59.9909, 117.982]

delays_ms_36 = [33.4911, 20.8325, 37.5185, 33.4911,24.4222, 34.8731, 72.9889, 59.9909, 117.982]

delays_ms_48 = [40.826, 35.1592, 40.1844,40.826, 35.3696, 35.8453, 72.9889, 59.9909, 117.982]


# woc 数据放置位置可能也不一样，可能是相同配置组放在一起？？？？
# 72.9889, 59.9909, 117.982
# 72.9889, 91.986, 181.972
# Queries总数
total_queries = 103591

# 将延迟从毫秒转换为秒
delays_s = [delay / 1000 for delay in delays_ms_12]
# 计算QPS（每秒查询数）
qps_values = [total_queries / delay for delay in delays_s]

standard_fpga = qps_values[0]
standard_numa = qps_values[0]
standard_asic = qps_values[0]
standard_gem5 = qps_values[6]

# 0-2
for i in range(3):
    qps_values[i] = qps_values[i] / standard_fpga
# 3-5
for i in range(3, 6):
    qps_values[i] = qps_values[i] / standard_numa
# 6-8
for i in range(6, 9):
    qps_values[i] = qps_values[i] / standard_gem5
# # 9-11
# for i in range(9, 12):
#     qps_values[i] = qps_values[i] / standard_asic
# for i in range(12, 15):
#     qps_values[i] = qps_values[i] / standard_gem5
# # 定义柱状图的标签
labels = [
    "Cfg1. DDR-L:DDR-R=100%:0%",
    "Cfg2. 50%:50%",
    "Cfg3. 0%:100%",
    # "Cfg4. DDR-L:CXL-FPGA=100%:0%",
    # "Cfg5. 50%:50%",
    # "Cfg6. 0%:100%",
    # "Cfg7. CXL-MemSim$_L$:CXL-DMSim$_F$=100%:0%",
    # "Cfg8. 50%:50%",
    # "Cfg9. 0%:100%",
    "Cfg4. DDR-L:CXL-ASIC=100%:0%",
    "Cfg5. 50%:50%",
    "Cfg6. 0%:100%",
    "Cfg7. CXL-MemSim$_L$:CXL-DMSim$_A$=100%:0%",
    "Cfg8. 50%:50%",
    "Cfg9. 0%:100%",
]

confs = ['Cfg1', "Cfg2", "Cfg3", "Cfg4", "Cfg5", "Cfg6", "Cfg7", "Cfg8", "Cfg9"]
# 定义每个柱子的颜色
# colors = ['#FFF9C4', '#FFF59D', '#FFF176', '#B2EBF2', '#4DD0E1', '#00BCD4', '#C3CACA', '#AFB8B9', '#9BA6A8','#9467bd', '#c5b0d5', '#c49c94'] #后三个数据随意填充

# colors_legend = ['#FFF9C4',  '#B2EBF2','#C3CACA', '#FFF59D', '#4DD0E1','#AFB8B9', '#FFF176',  '#00BCD4',   '#9BA6A8', '#9C27B0', '#8E24AA', '#7B1FA2' ]#后三个数据随意填充
# colors_legend = ['#FFF9C4',  '#B2EBF2','#C3CACA', '#9C27B0','#FFF59D', '#4DD0E1', '#8E24AA','#AFB8B9', '#FFF176',  '#00BCD4',   '#9BA6A8',  '#7B1FA2' ]#后三个数据随意填充
colors = ['#FFF9C4', '#FFF59D', '#FFF176', '#B2EBF2', '#4DD0E1',  '#9BA6A8', '#F6CAE5',
          '#C4A5DE', '#A1A9D0', '#CFEAF1', '#96CCCB', '#8ECFC9']

# 定义每个柱子的样式
patterns = ['o', 'x', '*', '//', '||', '\\\\','.', 'xo','--']
plt.figure(figsize=(30, 9.5))
# 创建柱状图9
interval = 0.3  # 柱子之间的间隔
width = 0.3  # 柱子宽度
X = 1
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.6,
                wspace=None, hspace=None)
# for i in range(len(qps_values)):
# 	plt.bar(X+i*interval, qps_values[i], width = width, facecolor = colors[i], linewidth=2.5,edgecolor = 'black', hatch=patterns[i],label=labels[i])
range_index = [0,3,6,1,4,7,2,5,8]

for i in range_index:
    plt.bar(X+i*interval, qps_values[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
            hatch=patterns[i],label=labels[i])

# scale_ls = range(1,10)
scale_ls = [i * interval + 0.7 for i in range(1, 10)]
print(scale_ls)
# index_ls = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']


# 设置边框宽度
bwidth = 3.5
ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['bottom'].set_linewidth(bwidth)
ax.spines['left'].set_linewidth(bwidth)
ax.spines['top'].set_linewidth(bwidth)
ax.spines['right'].set_linewidth(bwidth)

# 取消坐标轴刻度
# plt.xticks([])  # 去x坐标刻度
# plt.yticks([])  # 去y坐标刻度
# plt.axis('off')  # 去坐标轴
scale_y = [0.0, 0.2,0.4,0.6, 0.8, 1.0,1.2,1.4, 1.6]
plt.xticks(scale_ls, confs, fontsize=40)  # weight='bold'
# 设置x轴和y轴的标签
# plt.xticks(fontsize=18,rotation=45)
plt.yticks(scale_y,fontsize=40)  # weight='bold'
plt.xlabel('Memory Configurations', fontsize=45)  # weight='bold'
plt.ylabel('Normalized QPS', fontsize=40)  # weight='bold'

# plt.rcParams.update({'font.size': 20})
# plt.legend(loc='lowest center',fontsize=18,frameon=False, ncol = 3)

# 设置字体样式 如加粗bold等
weights = ['ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi',
           'bold', 'heavy', 'extra bold', 'black']

# plt.text(0.5, -0.53, label1, fontsize=21)
# plt.text(0.5, -0.77, label2, fontsize=21)
# plt.text(0.5, -1, label3, fontsize=21)


plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
plt.legend(bbox_to_anchor=(1.02, 1.55), frameon=False, ncol=3, fontsize=40, edgecolor='black',fancybox=False,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3,columnspacing=0.5) # 图例放在最下方
#
# legend.get_texts()[0].set_font_properties(font)

# plt.tight_layout()  # 解决绘图时上下标题重合的现象

# 取消每一个的边框
# ax1 = plt.subplot(2, 3, 1)
# ax1.spines['right'].set_visible(False)  # 右边
# ax1.spines['top'].set_visible(False)  # 上边
# ax1.spines['left'].set_visible(False)  # 左边
# ax1.spines['bottom'].set_visible(False)  # 下边

# 取消savefig保存图片时的白色边框 pad_inches参数
plt.savefig('merci_0731_12.pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()
