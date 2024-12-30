import matplotlib.pyplot as plt
import numpy as np

workloads_ABCDEF = ['Workload A', 'Workload B', 'Workload C','Workload D', 'Workload E','Workload F']


memory_configs = ['DDR-L:DDR-R=100%:0%', 'DDR-L:DDR-R=50%:50%', 'DDR-L:DDR-R=0%:100%',
                  'DDR-L:CXL-FPGA=100%:0%',  'DDR-L:CXL-FPGA=50%:50%', 'DDR-L:CXL-FPGA=0%:100%',
                  # 'CXL-DMSim$_L$:CXL-DMSim$_F$=100%:0%',  'CXL-DMSim$_L$:CXL-DMSim$_F$=50%:50%', 'CXL-DMSim$_L$:CXL-DMSim$_F$=0%:100%',
                  'DDR-L:CXL-ASIC=100%:0%', 'DDR-L:CXL-ASIC=50%:50%','DDR-L:CXL-ASIC=0%:100%'
                  # 'CXL-DMSim$_L$:CXL-DMSim$_A$=100%:0%','CXL-DMSim$_L$:CXL-DMSim$_A$=50%:50%','CXL-DMSim$_L$:CXL-DMSim$_A$=0%:100%'

                  ]



labels = [
    "DDR-L:DDR-R=100%:0%",
    "50%:50%",
    "0%:100%",
    "DDR-L:CXL-FPGA=100%:0%",
    "50%:50%",
    "0%:100%",
    # "CXL-DMSim$_L$:CXL-DMSim$_F$=100%:0%",
    # "50%:50%",
    # "0%:100%",
    "DDR-L:CXL-ASIC=100%:0%",
    "50%:50%",
    "0%:100%",
    # "CXL-DMSim$_L$:CXL-DMSim$_A$=100%:0%",
    # "50%:50%",
    # "0%:100%"
]




# 最后一行数据需要更新
# qps_values = {
#     'Workload A':[1.0, 0.9667, 0.9431,1, 0.9525, 0.9194,  8.46308/8.46308, 8.05387/8.46308, 7.87697/8.46308, 1, 0.9981, 0.9763, 8.46308/8.46308, 8.05387/8.46308, 7.87697/8.46308],
#     'Workload B':[1.0, 0.9947, 0.9897,1,  0.8801, 0.8376,7.66102/7.66102, 7.52691/7.66102, 7.52691/7.66102,1, 0.9463, 0.8954,7.66102/7.66102, 7.52691/7.66102, 7.52691/7.66102],
#     'Workload C':[1.0, 0.9707, 0.8996,1,  0.9365, 0.8740, 7.7402/7.7402, 7.57801/7.7402, 7.40554/7.7402, 1,0.9443, 0.9163, 7.7402/7.7402, 7.57801/7.7402, 7.40554/7.7402],
#     'Workload D':[1.0, 0.9575, 0.9170,1,  0.9159, 0.8297,6.99039/6.99039, 6.72432/6.99039, 6.53979/6.99039,1,  0.9691, 0.9150, 6.99039/6.99039, 6.72432/6.99039, 6.53979/6.99039,1]
# }


qps_values = {
    'Workload A':[1,0.97602911, 0.962154819,1,0.928235168,0.866394537,1,0.956724368,0.88482024],
    'Workload B':[1,0.97957896, 0.964204665,1,0.921423258,0.856106933,1,0.94885971,0.886662059],
    'Workload C': [1,0.969573196, 0.958064601,1,0.90982228,0.839443698,1,0.949689869,0.853204686],
    'Workload D':[1,0.992541931, 0.979625196,1,0.939874043,0.893720204,1,0.881964809,0.870117188],
    'Workload E':[1,0.978338252,0.937274352,1,0.890827818,0.803243135,1,0.92449923,0.855161787],
    'Workload F':[1,0.973603909, 0.962968128,1,0.93021564, 0.882937641,1,0.916992188,0.881964809]
}

# data_a = [1,0.97602911, 0.962154819,1,0.928235168,0.866394537,1,0.956724368,0.88482024]
# data_b = [1,0.97957896, 0.964204665,1,0.921423258,0.856106933,1,0.94885971,0.886662059]
# data_c = [1,0.969573196, 0.958064601,1,0.90982228,0.839443698,1,0.949689869,0.853204686]
# data_d = [1,0.992541931, 0.979625196,1,0.939874043,0.893720204,1,0.881964809,0.870117188]
# data_e = [1,0.978338252,0.937274352,1,0.890827818,0.803243135,1,0.92449923,0.855161787]
# data_f = [1,0.973603909, 0.962968128,1,0.93021564, 0.882937641,1,0.916992188,0.881964809]


colors = ['#FFF9C4', '#FFF59D', '#FFF176', '#B2EBF2', '#4DD0E1', '#00BCD4', '#C3CACA', '#AFB8B9', '#9BA6A8','#F6CAE5','#C4A5DE','#A1A9D0','#CFEAF1', '#96CCCB', '#8ECFC9']
patterns = ['+', '\\', '*', 'O','x', '\\\\','*', '//', '+', '.','-', '/','o','|','X','\\']
interval = 0.1
index_ABCDEF = np.arange(len(workloads_ABCDEF))
plt.figure(figsize=(40, 5))
# plt.rcParams.update({'font.size': 13})
width = 0.1


for i, workload in enumerate(workloads_ABCDEF):
    plt.subplot(1,6,i+1)
    plt.subplots_adjust(left=None, bottom=0.1, right=None, top=0.7,
                        wspace=0.45, hspace=0.5)
    # plt.bar( i * interval, qps_values[workload][i], width=width, facecolor=colors[i], edgecolor='black',
    #          hatch=patterns[i], label=memory_configs[i])
    plt.bar( 0 * interval, qps_values[workload][0], width=width, facecolor=colors[0], linewidth=3,  edgecolor='black',
            hatch=patterns[0], label=memory_configs[0])
    plt.bar(1 * interval, qps_values[workload][1], width=width, facecolor=colors[1],linewidth=3,  edgecolor='black',
            hatch=patterns[1], label=memory_configs[1])
    plt.bar(2 * interval, qps_values[workload][2], width=width, facecolor=colors[2],linewidth=3,  edgecolor='black',
            hatch=patterns[2], label=memory_configs[2])

    plt.bar( 3 * interval, qps_values[workload][3], width=width, facecolor=colors[3],linewidth=3,  edgecolor='black',
            hatch=patterns[3], label=memory_configs[3])
    plt.bar(4 * interval, qps_values[workload][4], width=width, facecolor=colors[4],linewidth=3,  edgecolor='black',
            hatch=patterns[4], label=memory_configs[4])
    plt.bar(5 * interval, qps_values[workload][5], width=width, facecolor=colors[5],linewidth=3,  edgecolor='black',
            hatch=patterns[5], label=memory_configs[5])


    plt.bar( 6 * interval, qps_values[workload][6], width=width, facecolor=colors[6],linewidth=3,  edgecolor='black',
            hatch=patterns[6], label=memory_configs[6])
    plt.bar(7 * interval, qps_values[workload][7], width=width, facecolor=colors[7],linewidth=3,  edgecolor='black',
            hatch=patterns[7], label=memory_configs[7])
    plt.bar(8 * interval, qps_values[workload][8], width=width, facecolor=colors[8],linewidth=3,  edgecolor='black',
            hatch=patterns[8], label=memory_configs[8])
    # NEW ADDed
    # plt.bar(3 * interval, qps_values[workload][9], width=width, facecolor=colors[9], linewidth=3, edgecolor='black',
    #         hatch=patterns[9], label=memory_configs[9])
    # # new added
    # plt.bar(4 * interval, qps_values[workload][10], width=width, facecolor=colors[10],linewidth=3,  edgecolor='black',
    #         hatch=patterns[10], label=memory_configs[10])
    # # new added
    # plt.bar(5 * interval, qps_values[workload][11], width=width, facecolor=colors[11],linewidth=3,  edgecolor='black',
    #         hatch=patterns[11], label=memory_configs[11])
    # plt.bar(6 * interval, qps_values[workload][12], width=width, facecolor=colors[12],linewidth=3,  edgecolor='black',
    #         hatch=patterns[12], label=memory_configs[12])
    #
    # plt.bar(7 * interval, qps_values[workload][13], width=width, facecolor=colors[13], linewidth=3, edgecolor='black',
    #         hatch=patterns[13], label=memory_configs[13])
    #
    # plt.bar(8 * interval, qps_values[workload][14], width=width, facecolor=colors[14], linewidth=3, edgecolor='black',
    #         hatch=patterns[14], label=memory_configs[14])

    # plt.tick_params(axis='x', pad=60)  # pad 就是标签与轴的距离

    plt.ylabel("Normalized QPS",y=0.43,fontsize=38)
    plt.xticks([])
    plt.xlabel(workload,fontsize=40,labelpad=15)

    # plt.xticks(workload,fontsize=40)
    plt.yticks(fontsize=40)
    bwidth = 3
    ax= plt.gca()  # 获取边框
    ax.spines['bottom'].set_linewidth(bwidth)
    ax.spines['left'].set_linewidth(bwidth)
    ax.spines['top'].set_linewidth(bwidth)
    ax.spines['right'].set_linewidth(bwidth)






plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125

# fancybox	缺省情况下legend是圆角，改为False后为直角
# edgecolor	边框颜色
# borderpad	图例边框的内边距
# labelspacing	图例条目之间的垂直间距
# handletextpad	图例句柄的长度
plt.legend(bbox_to_anchor=(0.5, 1.95),ncol=3, frameon=False, edgecolor='black',fancybox=False,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.2 ,columnspacing=4,fontsize=40) # 图例放在最下方

# bbox_to_anchor=(0.2, 1.4),

# plt.tight_layout()
plt.savefig('redis_graduation.pdf', bbox_inches='tight',pad_inches=0.0)
# plt.show()