import matplotlib.pyplot as plt
import numpy as np

workloads_ABCDEF = ['Workload A', 'Workload B', 'Workload C','Workload D']
memory_configs = ['DDR-L:DDR-R=100%:0%',  'DDR-L:CXL=100%:0%', 'CXL-MemSim DDR-L:CXL=100%:0%',
                  'DDR-L:DDR-R=50%:50%',  'DDR-L:CXL=50%:50%', 'CXL-MemSim DDR-L:CXL=50%:50%',
                  'DDR-L:DDR-R=0%:100%', 'DDR-L:CXL=0%:100%', 'CXL-MemSim DDR-L:CXL=0%:100%']



labels = [
    "DDR-L:DDR-R=100%:0%",
    "50%:50%",
    "0%:100%",
    "DDR-L:CXL=100%:0%",
    "50%:50%",
    "0%:100%",
    "CXL-MemSim DDR-L:CXL=100%:0%",
    "50%:50%",
    "0%:100%"
]

qps_values = {
    'Workload A':[1,0.97602911, 0.962154819,1,0.928235168,0.866394537,1,0.956724368,0.88482024],
    'Workload B':[1,0.97957896, 0.964204665,1,0.921423258,0.856106933,1,0.94885971,0.886662059],
    'Workload C':[1,0.969573196, 0.958064601,1,0.90982228,0.839443698,1,0.949689869,0.853204686],
    'Workload D':[1,0.992541931, 0.979625196,1,0.939874043,0.893720204,1,0.881964809,0.870117188]
}
data_a = [1,0.97602911, 0.962154819,1,0.928235168,0.866394537,1,0.956724368,0.88482024]
data_b = [1,0.97957896, 0.964204665,1,0.921423258,0.856106933,1,0.94885971,0.886662059]
data_c = [1,0.969573196, 0.958064601,1,0.90982228,0.839443698,1,0.949689869,0.853204686]
data_d = [1,0.992541931, 0.979625196,1,0.939874043,0.893720204,1,0.881964809,0.870117188]
# data_e = [1,0.978338252,0.937274352,1,0.890827818,0.803243135,1,0.92449923,0.855161787]
# data_f = [1,0.973603909, 0.962968128,1,0.93021564, 0.882937641,1,0.916992188,0.881964809]

colors = ['#FFF9C4', '#FFF59D', '#FFF176', '#B2EBF2', '#4DD0E1', '#00BCD4', '#C3CACA', '#AFB8B9', '#9BA6A8']
patterns = ['/', '\\', 'xx', 'x', '\\\\', '/', '+', '..', '++']
interval = 0.2
index_ABCDEF = np.arange(len(workloads_ABCDEF))
plt.figure(figsize=(19, 2))
# plt.rcParams.update({'font.size': 13})
width = 0.2


for i, workload in enumerate(workloads_ABCDEF):
    plt.subplot(1,4,i+1)

    plt.bar( 0 * interval, qps_values[workload][0], width=width, facecolor=colors[0],  edgecolor='black',
            hatch=patterns[0], label=labels[0])
    plt.bar( 3 * interval, qps_values[workload][3], width=width, facecolor=colors[3], edgecolor='black',
            hatch=patterns[3], label=labels[1])
    plt.bar( 6 * interval, qps_values[workload][6], width=width, facecolor=colors[6], edgecolor='black',
            hatch=patterns[6], label=labels[2])
    plt.bar( 1 * interval, qps_values[workload][1], width=width, facecolor=colors[1], edgecolor='black',
            hatch=patterns[1], label=labels[3])
    plt.bar( 4 * interval, qps_values[workload][4], width=width, facecolor=colors[4], edgecolor='black',
            hatch=patterns[4], label=labels[4])
    plt.bar( 7 * interval, qps_values[workload][7], width=width, facecolor=colors[7], edgecolor='black',
            hatch=patterns[7], label=labels[5])
    plt.bar( 2 * interval, qps_values[workload][2], width=width, facecolor=colors[2], edgecolor='black',
            hatch=patterns[2], label=labels[6])
    plt.bar( 5 * interval, qps_values[workload][5], width=width, facecolor=colors[5], edgecolor='black',
            hatch=patterns[5], label=labels[7])
    plt.bar( 8 * interval, qps_values[workload][8], width=width, facecolor=colors[8], edgecolor='black',
            hatch=patterns[8], label=labels[8])

    plt.ylabel("Normalized QPS")
    # plt.set_xticks([])
    plt.xlabel(workload)
    plt.xticks([])

    # for j, label in enumerate(labels):
    #     plt.bar(j*bar_width, data_a[j], bar_width, color=colors[j], label=label, linewidth=1.5,edgecolor='black',zorder=2, hatch=patterns[j])
    #     plt.ylabel("Normalized QPS")
    #     # plt.set_xticks([])
    #     # plt.gca().axes.get_xaxis().set_visible(False)  # 隐藏x轴坐标
    #     plt.xlabel(workloads_ABCDEF[i])
    #     # plt.grid(True)  # 添加背景网格
    #     # plt.figtext( workload, ha='center', va='bottom')
    #     plt.xticks([])
    #     # plt.yticks(fontsize=15)


plt.legend(memory_configs, bbox_to_anchor=(0.05, -0.1), ncol=3)  # 图例放在最下方
# plt.suptitle('QPS Efficiency for Redis-YCSB')

# plt.tight_layout()
# plt.savefig('redis_qps.pdf', bbox_inches='tight',pad_inches=0.0)
plt.show()