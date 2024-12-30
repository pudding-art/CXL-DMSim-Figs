import matplotlib.pyplot as plt
import numpy as np

# Data
operations = ['Insert', 'Select', 'Update', 'Delete']
kv_pairs_types = ['<16,200>',  '<100,900>']
memory_config = [ 'DDR-L', 'DDR-L+DDR-R','DDR-L+CXL', 'CXL-MemSim DDR-L', 'CXL-MemSim DDR-L+CXL']

# 归一化到自己键值对的DRAM大小的数据上
# values_put = {
#     '<16,200>': [2138320/2138320 , 2184830/2138320 ,2139240/2138320 ,1401120/1401120 , 1399750/1401120 ],
#     '<100,900>': [504563/504563 ,  866285/504563 ,790427/504563 ,293971/293971, 431258/293971]
# }
#
# values_get = {
#     '<16,200>': [1727480/1727480 ,  1741910/1727480 ,1726870/1727480 ,2006020/2006020 , 1997970/2006020 ],
#     '<100,900>': [59384/59384,  862886/59384,666678/59384,48624/48624, 1046070/48624 ]
# }
#
# value_get1 = 862886/59384
# value_get2 = 666678/59384
# value_get3 = 1046070/48624
#
# values_update = {
#     '<16,200>': [1462010/1462010 ,  1485820/1462010 ,1447900/1462010 ,2388250/2388250 ,2380620/2388250 ],
#     '<100,900>': [62592/62592 ,  1174790/62592 ,973438/62592 ,52053/52053 , 1595890/52053 ]
# }
#
# value_update1 = 1174790/62592
# value_update2 = 973438/62592
# value_update3 = 1595890/52053
#
# values_delete = {
#     '<16,200>': [ 1147090/1147090 , 1170490/1147090 ,1145350/1147090 ,1548380/1548380 , 1533370/1548380 ],
#     '<100,900>': [51738/51738 , 987834/51738 ,822458/51738 ,43314/43314 , 1093760/43314 ]
# }
#
# value_delete1 = 987834/51738
# value_delete2 = 822458/51738
# value_delete3 = 1093760/43314



""""
都归一化到<16,200>上
"""""
values_put = {
    '<16,200>': [2138320/2138320 , 2184830/2138320 ,2139240/2138320 ,1401120/1401120 , 1399750/1401120 ],
    '<100,900>': [504563/2138320 ,  866285/2138320 ,790427/2138320,293971/1401120, 431258/1401120]
}

values_get = {
    '<16,200>': [1727480/1727480 ,  1741910/1727480 ,1726870/1727480 ,2006020/2006020 , 1997970/2006020 ],
    '<100,900>': [59384/1727480,  862886/1727480,666678/1727480,48624/2006020, 1046070/2006020]
}

value_get1 = 862886/59384
value_get2 = 666678/59384
value_get3 = 1046070/48624

values_update = {
    '<16,200>': [1462010/1462010 ,  1485820/1462010 ,1447900/1462010 ,2388250/2388250 ,2380620/2388250 ],
    '<100,900>': [62592/1462010 ,  1174790/1462010 ,973438/1462010 ,52053/2388250 , 1595890/2388250 ]
}

value_update1 = 1174790/62592
value_update2 = 973438/62592
value_update3 = 1595890/52053

values_delete = {
    '<16,200>': [ 1147090/1147090 , 1170490/1147090 ,1145350/1147090 ,1548380/1548380 , 1533370/1548380 ],
    '<100,900>': [51738/1147090 , 987834/1147090 ,822458/1147090 ,43314/1548380 , 1093760/1548380]
}

value_delete1 = 987834/51738
value_delete2 = 822458/51738
value_delete3 = 1093760/43314

# 定义每个柱子的颜色
colors = ['#FFF176', '#B2EBF2', '#4DD0E1', '#C3CACA', '#AFB8B9','#b39ddb']
patterns = ['/', '\\', 'xx', 'x', '\\\\', '//', '+', '..', '++']
# y = [0,0.5, 1, 1.5]

fig, axs = plt.subplots(1, 4, figsize=(19, 2))

for i, (operation, values_dict) in enumerate(zip(operations, [values_put, values_get, values_update, values_delete])):
    for j, memory_type in enumerate(memory_config):
        values = [values_dict[k][j] for k in kv_pairs_types]
        x = np.array([0, 0.6])
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

plt.legend(memory_config, loc='center', bbox_to_anchor=(-1.3, -0.38), ncol=5)
plt.tight_layout()

# plt.savefig('viper_limit_new.pdf', bbox_inches='tight',pad_inches=0.0)
plt.show()