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

labels = ['raw gem5', 'adjusted gem5', 'CXL-DMSim$_L$', 'CXL-DMSim$_A$']

# latency s
lmbench_lat = [115427/115427, 137361/115427, 138533/115427,138533/115427]
# lmbench_lat_timing = [20351/20351, 31687/20351, 29166/20351, 28173/20351]
merci_lat = [63548/63548,38108/63548,58292.5/63548,66658/63548]
stream_lat = [20000/20000,24599/20000,24288/20000,25972/20000]

# memory space KB
lmbench_mem =[10458708/10458708, 11005460/10458708, 19479588/10458708, 19479584/10458708]
merci_mem = [34887416/34887416,46996588/34887416,66262464/34887416,66252224/34887416]
stream_mem = [30975348/30975348,43170544/30975348,49207784/30975348,49274344/30975348]

standard = 1000000

"""
横坐标是不同的应用[lmbench, merci, stream]
每个应用组中有4个柱子， 分别代表不同的内存配置，每组中属于同一种的内存配置相同
"""

workloads = ['LMBench', 'MERCI', 'STREAM']
colors = ['#FFF9C4',  '#B2EBF2',  '#F6CAE5','#8ECFC9']


patterns = ['*', '//', 'o', 'x.', '-', '////', 'o', '|||', 'XXX', '\\']
plt.figure(figsize=(15, 4.5))
# 创建柱状图9
interval = 0.3  # 柱子之间的间隔
width = 0.3  # 柱子宽度
X = 1
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.6,
                wspace=None, hspace=None)


# overhead time

# for i in range(4):
#     plt.bar(X+i*interval, lmbench_lat[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
#             hatch=patterns[i])
#
# for i in range(4):
#     plt.bar(X+i*interval+1.5, merci_lat[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
#             hatch=patterns[i])
#
# for i in range(4):
#     plt.bar(X+i*interval+3, stream_lat[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
#             hatch=patterns[i])
#

# overhead occupied time

#
for i in range(4):
    plt.bar(X+i*interval, lmbench_mem[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
            hatch=patterns[i])

for i in range(4):
    plt.bar(X+i*interval+1.5, merci_mem[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
            hatch=patterns[i])

for i in range(4):
    plt.bar(X+i*interval+3, stream_mem[i], width=width, facecolor=colors[i],linewidth=3.5, edgecolor='black',
            hatch=patterns[i])



plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
plt.legend(labels, fontsize=24,bbox_to_anchor=(0.99, 1.3),frameon=False,edgecolor='black', ncol=4,columnspacing=1,fancybox=False,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.2)


# 设置边框宽度
bwidth = 2.5
ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['bottom'].set_linewidth(bwidth)
ax.spines['left'].set_linewidth(bwidth)
ax.spines['top'].set_linewidth(bwidth)
ax.spines['right'].set_linewidth(bwidth)


locs = [1.45, 2.95, 4.45]
plt.xticks(locs,workloads,fontsize=24)
plt.yticks(fontsize=24)
# plt.xlabel('Index')
# plt.ylabel('Normalized\nexecution time',fontsize=24)
plt.ylabel('Normalized\n occupied memory',fontsize=24)

plt.xlabel('Workloads',fontsize=24)

# plt.tight_layout()
# plt.title('Bandwidth')
# plt.show()
plt.savefig('overhead_mem.pdf', bbox_inches='tight',pad_inches=0.0)