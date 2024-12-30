import matplotlib.pyplot as plt
import numpy as np



"""
LMBench		
	       hostTimg/s	hostMemory/KB
Raw gem5	    165378	11786608
Adjusted gem5	240703	12614268
CXL-DMSim-D	    237906	14566188
CXL-DMSim-C-Asic	325225	14581548


Merci		
	      hostTimg/s	hostMemory/KB
Raw gem5	89579	34887416
Adjusted gem5	83831	46996588
CXL-DMSim-D	72020	66262464
CXL-DMSim-C-Asic	82735	66252224


Stream		
	       hostTimg/s	hostMemory/KB
Raw gem5	20000	30975348
Adjusted gem5	24599	43170544
CXL-DMSim-D	24288	49207784
CXL-DMSim-C-Asic	25972	49274344
"""
# 'raw gem5'
labels = [ 'raw gem5', 'CXL-DMSim$_L$', 'CXL-DMSim$_A$']

# latency s
lmbench_lat = [137361/137361, 138533/137361,181261/137361]
# lmbench_lat_timing = [20351/20351, 31687/20351, 29166/20351, 28173/20351]
# merci_lat = [38108/38108,58292.5/38108,66658/38108] # old version
merci_lat = [20586/20586, 21691/20586, 22688/20586]
stream_lat = [24599/24599,24288/24599,25972/24599]


# memory space KB (old version)
# lmbench_mem =[12588900/12588900, 21062000/12588900, 21078384/12588900]
# # merci_mem = [47562068/47562068,57686188/47562068,57681068/47562068] # old version
# merci_mem = [19638324/19638324,28271504/19638324,28267404/19638324]
# stream_mem = [43170544/43170544,49207784/43170544,49274344/43170544]

# new version 20241015
lmbench_mem = [10563584/10563584, 10799104/10563584, 11059540/10563584]
merci_mem = [17076224/17076224,17359872/17076224,17374208/17076224]
stream_mem = [42417152/42417152,44234872/42417152,44108020/42417152]

standard = 1000000

"""
横坐标是不同的应用[lmbench, merci, stream]
每个应用组中有4个柱子， 分别代表不同的内存配置，每组中属于同一种的内存配置相同
"""

workloads = ['LMBench', 'STREAM', 'MERCI']
colors = ['#FFF9C4',  '#B2EBF2',  '#F6CAE5','#8ECFC9']


patterns = ['*', '//', 'o', 'x.', '-', '////', 'o', '|||', 'XXX', '\\']
plt.figure(figsize=(11, 4.5))

# 创建柱状图9
interval = 0.3  # 柱子之间的间隔
width = 0.3  # 柱子宽度
X = 1
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.6,
                wspace=None, hspace=None)
# 注意下面调整刻度朝向语句的放置位置，放在后面绘图之后可能对结果没有什么影响
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

# overhead time

# for i in range(3):
#     plt.bar(X+i*interval, lmbench_lat[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
#             hatch=patterns[i])
#
# for i in range(3):
#     plt.bar(X+i*interval+1, merci_lat[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
#             hatch=patterns[i])
#
# for i in range(3):
#     plt.bar(X+i*interval+2, stream_lat[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
#             hatch=patterns[i])


# overhead occupied time

#
# for i in range(3):
#     plt.bar(X+i*interval, lmbench_mem[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
#             hatch=patterns[i])
#
# for i in range(3):
#     plt.bar(X+i*interval+1, merci_mem[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
#             hatch=patterns[i])
#
# for i in range(3):
#     plt.bar(X+i*interval+2, stream_mem[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
#             hatch=patterns[i])
locs = [1.3, 2.3, 3.3]
fig, axs = plt.subplots(1, 2, figsize=(14, 2))
plt.yticks(fontsize=24)

plt.ylim(bottom=0.6)
# 绘制execution time的柱状图
for i in range(3):
    axs[0].bar(X+i*interval, lmbench_lat[i], width=width, facecolor=colors[i], linewidth=2.5, edgecolor='black', hatch=patterns[i])
for i in range(3):
    axs[0].bar(X+i*interval+1, stream_lat[i], width=width, facecolor=colors[i], linewidth=2.5, edgecolor='black', hatch=patterns[i])
for i in range(3):
    axs[0].bar(X+i*interval+2, merci_lat[i], width=width, facecolor=colors[i], linewidth=2.5, edgecolor='black', hatch=patterns[i])

locs = [1.3, 2.3, 3.3]
locs_y_label = ['0.6', '0.9', '1.2','1.5']
locs_y = [float(i) for i in locs_y_label]
# 设置execution time的图例和其他配置
axs[0].set_xticks(locs,workloads)
axs[0].set_xticklabels(workloads, fontsize=23)
axs[0].set_yticks(locs_y,locs_y_label,fontsize=23)
axs[0].set_ylim(bottom=0.6)
axs[0].set_ylabel('Norm. Exec. Time',y=0.45, fontsize=22)
axs[0].set_xlabel('(a) HostSeconds', fontsize=25)
axs[0].tick_params(axis='y',width=3)#修改刻度线线粗细width参数，修改刻度字体labelsize参数

# 刻度线长度调整
# plt.tick_params(axis='x', length=10)  # 设置x轴刻度线长度为10
axs[0].tick_params(axis='y', length=5)  # 设置y轴刻度线长度为10

# 设置边框宽度
bwidth = 2.5

# ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
axs[0].spines['bottom'].set_linewidth(bwidth)
axs[0].spines['left'].set_linewidth(bwidth)
axs[0].spines['top'].set_linewidth(bwidth)
axs[0].spines['right'].set_linewidth(bwidth)

# 绘制occupied memory的柱状图
# 注意这里需要重新设置X坐标，因为每个子图有自己的坐标轴
X_mem = 1
for i in range(3):
    axs[1].bar(X_mem+i*interval, lmbench_mem[i], width=width, facecolor=colors[i], linewidth=2.5, edgecolor='black', hatch=patterns[i])
for i in range(3):
    axs[1].bar(X_mem+i*interval+1, stream_mem[i], width=width, facecolor=colors[i], linewidth=2.5, edgecolor='black', hatch=patterns[i])
for i in range(3):
    axs[1].bar(X_mem+i*interval+2, merci_mem[i], width=width, facecolor=colors[i], linewidth=2.5, edgecolor='black', hatch=patterns[i])
plt.yticks(fontsize=24)
locs = [1.3, 2.3, 3.3]
# locs_y = [0.0, 0.25, 0.50, 0.75, 1.00, 1.25,1.50, 1.75]
locs_y_label = ['0.6', '0.8', '1.0', '1.2']
locs_y = [float(i) for i in locs_y_label]
# 设置occupied memory的图例和其他配置
axs[1].set_xticks(locs,workloads)
axs[1].set_xticklabels(workloads, fontsize=23)
axs[1].set_yticks(locs_y,locs_y_label,fontsize=23)

# axs[1].set_ylabel('Normalized Occ-\nupied Memory', y=0.41,fontsize=20)
axs[1].set_ylabel('Norm. Occup-\nied Memory', y=0.41,fontsize=22)
axs[1].set_xlabel('(b) HostPhyMemory', fontsize=25)

# 调整子图间距
plt.subplots_adjust(wspace=0.28)


plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
plt.legend(labels, fontsize=23,bbox_to_anchor=(0.9, 1.49),frameon=False,edgecolor='black', ncol=3, columnspacing=5,fancybox=False,borderpad = 0.4, labelspacing = 0.4, handletextpad = 0.2)
plt.tick_params(axis='y',width=3)#修改刻度线线粗细width参数，修改刻度字体labelsize参数
# plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内


# 设置边框宽度
bwidth = 2.5
# ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
axs[1].spines['bottom'].set_linewidth(bwidth)
axs[1].spines['left'].set_linewidth(bwidth)
axs[1].spines['top'].set_linewidth(bwidth)
axs[1].spines['right'].set_linewidth(bwidth)
axs[1].tick_params(axis='y', length=5)  # 设置y轴刻度线长度为10

# plt.tight_layout()
# plt.title('Bandwidth')
# plt.show()
plt.savefig('overhead1013.pdf', bbox_inches='tight',pad_inches=0.0)