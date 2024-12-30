import matplotlib.pyplot as plt
import numpy as np

operations = ['Copy', 'Scale', 'Add', 'Triad']
mem_configs = ['DDR-L', 'DDR-R',  'CXL-ASIC', 'CXL-DMSim(A)', 'CXL-FPGA','CXL-DMSim(F)']
labels=['DDR-L', 'DDR-R', 'CXL-ASIC', 'CXL-DMSim$_A$',  'CXL-FPGA','CXL-DMSim$_F$']


# CXL-DMSim DDR-L: 19203.1, 18464.3, 20574.4, 20872.9
# CXL-DMSim ASIC 17780.5, 16554.3, 15486.2, 15486.2
# CXL-DMSim FPGA 12469.3, 11709.2, 10910.7, 10910.7

# old: [18826.1/24619.1,18115.9/20428.6, 17352.2/17351.9, 17352.1/22860.8]
# new: [17780.5/19203.1, 16554.3/18464.3, 15486.2/20574.4, 15486.2/20872.9]

# 20240731 FPGA 11430.3	10788.1	10142.4	10071.5
# CXL-DMSim_L 19203.1	18464.3	20574.4	20872.9
# [11430.3/ 19203.1,10788.1/18464.,10142.4/20574.4,10071.5/20872.9]

# 【17145.6, 16273.7, 15486.2, 15486.2]
data = {
    'DDR-L': [20327.1/20327.1, 20358.5/20358.5, 22928.5/22928.5, 22927.8/22927.8],
    'DDR-R': [13999.1/20327.1, 14057.1/20358.5, 16869.7/22928.5, 16842.7/22927.8],
    'CXL-FPGA': [13094.5/20327.1, 9171.1/20358.5, 10424.8/22928.5, 10473.0/22927.8],
    'CXL-DMSim(F)': [11430.3/ 19203.1,10788.1/18464.,10142.4/20574.4,10071.5/20872.9],
    'CXL-ASIC': [16940.5/20327.1, 16819.7/20358.5, 18869.2/22928.5, 18858.9/22927.8],
    'CXL-DMSim(A)': [17780.5/19203.1, 16554.3/18464.3, 15486.2/20574.4, 15486.2/20872.9]
}

# new_color = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#999999']
colors = ['#FFF9C4', '#FFF59D', '#9DC3E7', '#5F97D2', '#C4A5DE','#8983BF']
patterns = ['/', '\\', 'xx', 'x', 'o',  '+', '..', '++']

bar_width = 0.15
index = np.arange(len(operations))
print(index)
# index = [0.1,1,1.9,2.8 ]

plt.figure(figsize=(30, 7))
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
plt.rcParams.update({'font.size': 40})
for i, mem_config in enumerate(mem_configs):
    print(i, mem_config)
    print(data[mem_config])
    plt.bar(index + i*bar_width, data[mem_config], bar_width, color=colors[i], label=mem_config, edgecolor='black', linewidth=4,zorder=2,hatch=patterns[i])

# 设置边框宽度
bwidth = 4
ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['bottom'].set_linewidth(bwidth)
ax.spines['left'].set_linewidth(bwidth)
ax.spines['top'].set_linewidth(bwidth)
ax.spines['right'].set_linewidth(bwidth)



plt.xlabel('Operation Type', fontsize=55)
plt.ylabel('Norm. B/W',y=0.45,fontsize=55)
plt.xticks(index + bar_width*(len(mem_configs)-1)/2, operations, fontsize=55)
y_ticks = [0.0,0.2,0.4,0.6,0.8,1.0]
plt.yticks(y_ticks,[str(i) for i in y_ticks],fontsize=55)
# plt.legend(loc='upper right',bbox_to_anchor=(0.96, 1.0),fontsize=20,frameon=False)
plt.tick_params(axis='y',width=6)#修改刻度线线粗细width参数，修改刻度字体labelsize参数

# 刻度线长度调整
# plt.tick_params(axis='x', length=10)  # 设置x轴刻度线长度为10
plt.tick_params(axis='y', length=10)  # 设置y轴刻度线长度为10

plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125

legend = plt.legend(labels, bbox_to_anchor=(1, 1.2), fontsize=50, columnspacing=0.1,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3 , frameon=False)
# legend = plt.legend(labels, bbox_to_anchor=(0.06, 0.95), fontsize=45, ncol=6, columnspacing=0.2,borderpad = 0.1, labelspacing = 0.2, handletextpad = 0.1 , frameon=False)

# plt.title('Bandwidth Efficiency under Different Memory Configurations and Operations', fontsize=16)

#  plt.rcParams.update({'font.size': 40})
# # 绘制背景横线
# for i in range(1, 6):
#     plt.axhline(y=i*0.2, color='gray', linestyle='--', linewidth=0.5,zorder=1)

plt.tight_layout()
plt.savefig('Stream.pdf', bbox_inches='tight',pad_inches=0.0)
plt.show()