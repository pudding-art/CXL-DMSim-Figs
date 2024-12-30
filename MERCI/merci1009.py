import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
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
delays_s = [delay / 1000 for delay in delays_ms_24]
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

text = ['DDR-L:DDR-R=','DDR-L:CXL-ASIC=','CXL-DMSim$_L$:CXL-DMSim$_A$=']
labels = [
    "Cfg1. 100%:0%",
    "Cfg4. 100%:0%",
    "Cfg7. 100%:0%",
    "Cfg2. 50%:50%",
    "Cfg5. 50%:50%",
    "Cfg8. 50%:50%",
    "Cfg3. 0%:100%",
    # "Cfg4. DDR-L:CXL-FPGA=100%:0%",
    # "Cfg5. 50%:50%",
    # "Cfg6. 0%:100%",
    # "Cfg7. CXL-MemSim$_L$:CXL-DMSim$_F$=100%:0%",
    # "Cfg8. 50%:50%",
    # "Cfg9. 0%:100%",
    "Cfg6. 0%:100%",
    "Cfg9. 0%:100%"
]

"""
48cores:

dram.avgBusLat 
dram: 3632.00
dram+cxl: 3632.00
cxl: 3632.00

dram.avgQLat # Average queueing delay per DRAM burst ((Tick/Count))
dram: 246165.20
dram+cxl: 114614.60
cxl: 53078.50

dram.avgMemAccLat
ctrl0:
dram: 264342.20
dram+cxl: 132791.60
cxl: 71255.50
ctrl1:
dram: 110835.54
dram+cxl: 116291.55
cxl: 71255.50
两个控制器的平均数值：
dram:255253.7
cxl+dram:124541.575


l3cache.overallAvgMissLatency # average overall miss latency ((Tick/Count))
dram: 759516.312867
dram+cxl: 624414.496201
cxl: 1239314.960285
"""


avgQLat = [246165.20,114614.60,0]
avgMemAccLat = [110835.54,116291.55,0]
avgMissLat = [759516.312867,624414.496201,1239314.960285]

avg = [759516.312867/759516.312867,624414.496201/759516.312867,1239314.960285/759516.312867,255253.7/255253.7,124541.575/255253.7,0,246165.20/246165.20,114614.60/246165.20,0/246165.20]


# 定义每个柱子的颜色

colors = ['#FFF9C4', '#FFF59D', '#FFF176', '#B2EBF2', '#4DD0E1',  '#9BA6A8', '#F6CAE5',
          '#C4A5DE', '#A1A9D0', '#CFEAF1', '#96CCCB', '#8ECFC9']

# 定义每个柱子的样式
patterns = ['o', 'x', '*', '//', '||', '\\\\','.', 'xo','--']

# 创建柱状图9
interval = 0.2  # 柱子之间的间隔
width = 0.3  # 柱子宽度
X = 1

# fig, axs = plt.subplots(1, 2, figsize=(30, 9.5))
# plt.yticks(fontsize=24)

# 创建一个gridspec对象
fig = plt.figure(figsize=(37, 12))
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
gs = gridspec.GridSpec(1, 2, width_ratios=[5.7, 4.3])  # 左边子图占70%，右边子图占30%

ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])


for i in [0,3,6]:

    bars = ax2.bar(i, avg[i],facecolor=colors[6],linewidth=3.5, edgecolor='black',
         hatch=patterns[6],label=labels[i])

for i in [1,4,7]:
    bars = ax2.bar(i, avg[i],facecolor=colors[7],linewidth=3.5, edgecolor='black',
            hatch=patterns[7],label=labels[i])
for i in [2,5,8]:
    bars = ax2.bar(i, avg[i],facecolor=colors[8],linewidth=3.5, edgecolor='black',
            hatch=patterns[8],label=labels[i])




# scale_ls = range(1,10)
scale_ls = [i * interval + 0.7 for i in range(1, 10)]
print(scale_ls)
# index_ls = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']


# 设置边框宽度
bwidth = 3.5

ax2.spines['bottom'].set_linewidth(bwidth)
ax2.spines['left'].set_linewidth(bwidth)
ax2.spines['top'].set_linewidth(bwidth)
ax2.spines['right'].set_linewidth(bwidth)


ax2.tick_params(axis='y',width=8,length=12)#修改刻度线线粗细width参数，修改刻度字体labelsize参数



plt.subplots_adjust(left=None, bottom=None, right=None, top=0.6,
                wspace=None, hspace=None)
# for i in range(len(qps_values)):
# 	plt.bar(X+i*interval, qps_values[i], width = width, facecolor = colors[i], linewidth=2.5,edgecolor = 'black', hatch=patterns[i],label=labels[i])
range_index = [0,3,6,1,4,7,2,5,8]

for i in range_index:
    ax1.bar(i, qps_values[i],facecolor=colors[i],linewidth=3.5, edgecolor='black',
            hatch=patterns[i],label=labels[i])
bwidth = 3.5
# ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax1.spines['bottom'].set_linewidth(bwidth)
ax1.spines['left'].set_linewidth(bwidth)
ax1.spines['top'].set_linewidth(bwidth)
ax1.spines['right'].set_linewidth(bwidth)
scale_x = [0.0, 0.2,0.4,0.6, 0.8, 1.0,1.2,1.4, 1.6]

# 设置x轴和y轴的标签
scale_y = [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4]
scale_y_label = ['0.0','0.2','0.4','0.6','0.8','1.0','1.2','1.4']
ax1.set_yticks(scale_y,scale_y_label,fontsize=50)
# plt.yticks(scale_y,fontsize=40)  # weight='bold'
ax1.set_xlabel('Memory Configurations\n(a) Application execution QPS', fontsize=50)  # weight='bold'
ax1.set_ylabel('Normalized QPS', fontsize=50)  # weight='bold'

# #
# plt.text(4.80, 0.05, '100% CXL-DMSim$_A$ is 0',color='red', rotation=90, fontsize=45)
# plt.text(7.80, 0.05, '100% CXL-DMSim$_A$ is 0',color='red', rotation=90, fontsize=45)
ax1.tick_params(axis='y',width=8,length=12)#修改刻度线线粗细width参数，修改刻度字体labelsize参数


# #
# # version 1
plt.text(-13.57, 2.36, text[0],fontsize=50)
plt.text(-14.33, 2.1, text[1], fontsize=50)
plt.text(-17.2 , 1.85, text[2],fontsize=50)

# # version 2
# text1 = ['DDR-L:DDR-R','DDR-L:CXL-ASIC','CXL-MemSim$_L$:CXL-DMSim$_A$']
# plt.text(-1.92, 12.33, text1[0],fontsize=40)
# plt.text(-2.05, 10.93, text1[1], fontsize=40)
# plt.text(-2.64, 9.53, text1[2],fontsize=40)

# version 3
# text1 = ['DDR-L:DDR-R','DDR-L:CXL-ASIC','CXL-MemSim$_L$:CXL-DMSim$_A$']
# plt.text(-2.61, 12.33, text1[0],fontsize=40)
# plt.text(-2.61, 10.93, text1[1], fontsize=40)
# plt.text(-2.61, 9.53, text1[2],fontsize=40)

#
# version 4
# plt.text(-2.67, 12.33, text[0],fontsize=40)
# plt.text(-2.67, 10.93, text[1], fontsize=40)
# plt.text(-2.67, 9.53, text[2],fontsize=40)

scale_x = [0.0, 0.2,0.4,0.6, 0.8, 1.0,1.2,1.4, 1.6]
confs = ['Cfg1', "Cfg2", "Cfg3", "Cfg4", "Cfg5", "Cfg6", "Cfg7", "Cfg8", "Cfg9"]
ax1.set_xticks([i-0.3 for i in range(9)],confs, fontsize=50, rotation=15)  # weight='bold'


plt.subplots_adjust(wspace=0.15)

# params = ['dram.avgQLat','dram.avgMem-\nAccLat','l3cache.overall-\nAvgMissLatency']
params = ['llc.\nAvgMissLat','dram.\navgMemAccLat','dram.\navgQLat']
plt.xticks([0.8,4.0,7.2],params,y=0.05, fontsize=45, rotation=10)  # weight='bold'
# 设置x轴和y轴的标签
scale_y = [0.0,0.4,0.8,1.2,1.6]

ax2.set_yticks(scale_y,[str(ytick) for ytick in scale_y],fontsize=50)

# plt.xticks(fontsize=40)
# plt.yticks(scale_y,fontsize=40)  # weight='bold'
# plt.ylabel('Memory\nConfigurations', fontsize=45)  # weight='bold'
plt.ylabel('Normalized Latency', y=0.45,fontsize=50)  # weight='bold' (b) Latency metrics
plt.xlabel('(b) Latency metrics', fontsize=55)


# 设置字体样式 如加粗bold等
weights = ['ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi',
           'bold', 'heavy', 'extra bold', 'black']



plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
ax1.legend(labels, bbox_to_anchor=(1.9, 1.55), frameon=False, ncol=3, fontsize=50, edgecolor='black',fancybox=False,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3,columnspacing=1) # 图例放在最下方

# plt.tight_layout()
# 取消savefig保存图片时的白色边框 pad_inches参数
plt.savefig('merci_1009_h.pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()
