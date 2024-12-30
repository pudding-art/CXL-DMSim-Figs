import matplotlib.pyplot as plt
import numpy as np

operations = ['Copy', 'Scale', 'Add', 'Triad']
mem_configs = ['DDR-L', 'DDR-R',  'CXL','CXL-MemSim']

data = {
    'DDR-L': [24904.5/24904.5, 17890.1/17890.1, 20123.8/20123.8, 20146.9/20146.9],
    'DDR-R': [15614.0/24904.5, 12171.1/17890.1, 14869.3/20123.8, 14942.1/20146.9],
    'CXL': [12794.0/24904.5, 9476.1/17890.1, 12395.4/20123.8, 12530.1/20146.9],
    'CXL-MemSim': [1558.1/3021.2, 1599.6/2873.1, 1683.1/3219.9, 1635.9/3033.9]
}


colors = ['#FFF9C4', '#FFF59D', '#B2EBF2', '#C3CACA']
patterns = ['/', '\\', 'xx', 'x', '\\\\', '//', '+', '..', '++']

bar_width = 0.2
index = np.arange(len(operations))
# index = [0.1,1,1.9,2.8 ]

plt.figure(figsize=(18, 7))

for i, mem_config in enumerate(mem_configs):
    plt.bar(index + i*bar_width, data[mem_config], bar_width, color=colors[i], label=mem_config, edgecolor='black', linewidth=2.5,zorder=2,hatch=patterns[i])

# 设置边框宽度
bwidth = 2.5
ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['bottom'].set_linewidth(bwidth)
ax.spines['left'].set_linewidth(bwidth)
ax.spines['top'].set_linewidth(bwidth)
ax.spines['right'].set_linewidth(bwidth)



plt.xlabel('Operation Type', fontsize=30)
plt.ylabel('Normalized Bandwidth', fontsize=30)
plt.xticks(index + bar_width*(len(mem_configs)-1)/2, operations, fontsize=30)
plt.yticks(fontsize=30)
plt.legend(loc='upper right',bbox_to_anchor=(1.01, 1.03),fontsize=20,frameon=False)
# plt.title('Bandwidth Efficiency under Different Memory Configurations and Operations', fontsize=16)

plt.rcParams.update({'font.size': 20})
# # 绘制背景横线
# for i in range(1, 6):
#     plt.axhline(y=i*0.2, color='gray', linestyle='--', linewidth=0.5,zorder=1)

plt.tight_layout()
plt.savefig('Stream.pdf', bbox_inches='tight',pad_inches=0.0)
# plt.show()