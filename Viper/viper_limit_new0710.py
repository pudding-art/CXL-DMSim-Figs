import matplotlib.pyplot as plt
import numpy as np

# Data
operations = ['Insert', 'Select', 'Update', 'Delete']
kv_pairs_types = ['<16,200>',  '<100,900>']
memory_config = [ 'DDR-L', 'DDR-L+DDR-R','DDR-L+CXL-FPGA', 'DDR-L+CXL-ASIC','CXL-DMSim DDR-L', 'CXL-DMSim DDR-L+FPGA', 'CXL-DMSim DDR-L+ASIC']

""""
都归一化到<16,200>上
"""""
values_put = {
    # [2068370, 2057030, 2117250, 2099190]
    '<16,200>': [2068370/2068370,2099190/2068370, 2057030/2068370, 2117250/2068370, 1401120/1401120 , 1399750/1401120,  ],
    '<100,900>': [545408/2068370,779039/2068370, 693037/2068370, 795015/2068370, 293971/1401120, 431258/1401120] #[545408, 693037, 795015, 779039]
}

values_get = {
    # [1845050, 1892930, 1913380, 1886480]
    '<16,200>': [ 1845050/1845050, 1886480/1845050,1892930/1845050, 1913380/1845050, 2006020/2006020 , 1997970/2006020 ],
    '<100,900>': [49545/1845050,910191/1845050, 744402/1845050, 831515/1845050, 48624/2006020, 1046070/2006020] #[49545, 744402, 831515, 910191]
}

value_get1 = 862886/59384
value_get2 = 666678/59384
value_get3 = 1046070/48624

values_update = {
    '<16,200>': [1522700/1522700, 1554320/1522700 , 1544180/1522700, 1574070/1522700,2388250/2388250 ,2380620/2388250 ],#[1522700, 1544180, 1574070, 1554320]
    '<100,900>': [52091/1522700, 1244740/1522700,1126380/1522700, 1199380/1522700,52053/2388250 , 1595890/2388250 ]#[52091, 1126380, 1199380, 1244740]
}

value_update1 = 1174790/62592
value_update2 = 973438/62592
value_update3 = 1595890/52053

values_delete = {
    '<16,200>': [ 1200950/1200950, 1224720/1200950, 1218040/1200950, 1240380/1200950 ,1548380/1548380 , 1533370/1548380 ], #[1200950, 1218040, 1240380, 1224720]
    '<100,900>': [40568/1200950,  1045520/1200950 ,954070/1200950, 1008270/1200950,43314/1548380 , 1093760/1548380] #[40568, 954070, 1008270, 1045520]
}

value_delete1 = 987834/51738
value_delete2 = 822458/51738
value_delete3 = 1093760/43314





# 定义每个柱子的颜色
colors = ['#FFF176', '#B2EBF2', '#4DD0E1','#b39ddb', '#C3CACA', '#AFB8B9']
patterns = ['/', '\\', 'xx', 'x', '\\\\', '//', '+', '..', '++']
# y = [0,0.5, 1, 1.5]

fig, axs = plt.subplots(1, 4, figsize=(19, 2))

for i, (operation, values_dict) in enumerate(zip(operations, [values_put, values_get, values_update, values_delete])):
    for j, memory_type in enumerate(memory_config):
        values = [values_dict[k][j] for k in kv_pairs_types]
        x = np.array([0, 0.7])
        width = 0.1
        bars = axs[i].bar(x + j * width, [min(v, 2) for v in values], width, label=memory_type, color=colors[j], edgecolor='black', hatch=patterns[j])

        # 遍历每个柱子，如果原始值大于2，则在柱子上方添加文本标签
        for k, bar in enumerate(bars):
            if values[k] > 2:
                # 计算并四舍五入原始倍数
                original_value = round(values[k])
                axs[i].text(bar.get_x() + bar.get_width() / 2, 2.1, str(original_value), ha='center', va='bottom')

    axs[i].set_xticks(x + 2 * width)
    axs[i].set_xticklabels(kv_pairs_types)
    axs[i].set_xlabel(operation)
    axs[i].set_ylabel('Normalized QPS')

# axs[0].set_yticks(y)
# axs[1].set_yticks(y)
# axs[2].set_yticks(y)
# axs[3].set_yticks(y)

plt.legend(memory_config, loc='center', bbox_to_anchor=(-1.3, -0.38), ncol=6)
plt.tight_layout()

plt.savefig('viper_limit_new0710.pdf', bbox_inches='tight',pad_inches=0.0)
# plt.show()