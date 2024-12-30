import matplotlib.pyplot as plt
import numpy as np

# Data
operations = ['Put', 'Get', 'Update', 'Delete']
kv_pairs_types = ['<16,200>', '<32,500>', '<100,900>']
memory_config = ['gem5 DDR-L', 'gem5 DDR-L+CXL', 'DDR-L', 'DDR-L+CXL', 'DDR-L+DDR-R']

values_put = {
    '<16,200>': [1401120/1401120, 1399750/1401120, 2190010/2190010, 2196890/2190010, 2215240/2190010],
    '<32,500>': [63736/63736, 746498/63736, 1410530/1410530, 1478010/1410530, 1469530/1410530],
    '<100,900>': [9570/9570, 419154/9570, 498441/498441, 1064640/498441, 1072740/498441]
}

values_get = {
    '<16,200>': [2006020/2006020, 419154/2006020, 1863950/1863950, 1911190/1863950, 1898190/1863950],
    '<32,500>': [97998/97998, 1450210/97998, 974403/974403, 1176990/974403, 1156960/974403],
    '<100,900>': [1865/1865, 1450210/1865, 925205/925205, 1035790/925205, 1028270/925205]
}

values_update = {
    '<16,200>': [2388250/2388250, 953998/2388250, 1583660/1583660, 1616730/1583660, 1616290/1583660],
    '<32,500>': [1813790/1813790, 2034760/1813790, 1375890/1375890, 1473860/1375890, 1412950/1375890],
    '<100,900>': [2183/2183, 1454070/2183, 1296660/1296660, 1419050/1296660, 1413790/1296660]
}

values_delete = {
    '<16,200>': [1593500/1593500, 1608940/1593500, 1229710/1229710, 1255120/1229710, 1229570/1229710],
    '<32,500>': [1459740/1459740, 1513760/1459740, 1147310/1147310, 1172060/1147310, 1137790/1147310],
    '<100,900>': [1417/1417, 1057370/1417, 1112610/1112610, 1185370/1112610, 1182170/1112610]
}

# 定义每个柱子的颜色
colors = ['#C3CACA', '#AFB8B9', '#FFF176', '#B2EBF2', '#4DD0E1', '#00BCD4',  '#9BA6A8']
patterns = ['/', '\\', 'xx', 'x', '\\\\', '//', '+', '..', '++']


fig, axs = plt.subplots(4, 1, figsize=(12, 16))

for i, (operation, values_dict) in enumerate(zip(operations, [values_put, values_get, values_update, values_delete])):
    for j, memory_type in enumerate(memory_config):
        values = [values_dict[k][j] for k in kv_pairs_types]
        x = np.arange(len(kv_pairs_types))
        width = 0.2
        axs[i].bar(x + j*width, np.log10(values), width, label=memory_type, alpha=0.7,color=colors[j], edgecolor='black',hatch=patterns[j])

    axs[i].set_xticks(x + 2*width)
    axs[i].set_xticklabels(kv_pairs_types)
    axs[i].set_title(operation)
    axs[i].set_ylabel('Normalized QPS')
    axs[i].legend()

plt.tight_layout()
plt.show()
