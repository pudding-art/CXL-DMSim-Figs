import matplotlib.pyplot as plt
import numpy as np

# Data
operations = ['Insert', 'Select', 'Update', 'Delete']
kv_pairs_types = ['<16,200>', '<32,500>', '<100,900>']
memory_config = [ 'DDR-L', 'DDR-L+DDR-R','DDR-L+CXL', 'CXL-MemSim DDR-L', 'CXL-MemSim DDR-L+CXL']

values_put = {
    '<16,200>': [2190010,  2195240,2190890,1401120, 1399750],
    '<32,500>': [1410530,  1469530,1478010,63736, 746498],
    '<100,900>': [498441, 1072740, 1064640,9570, 419154]
}

values_get = {
    '<16,200>': [1893950,  1898190,1891190,2006020, 1997970],
    '<32,500>': [974403,  1156960,1176990,97998, 1450210],
    '<100,900>': [925205,  1028270,1035790,1865, 953998 ]
}

values_update = {
    '<16,200>': [1616660,  1616290,1616730,2388250,2380620 ],
    '<32,500>': [ 1375890,  1412950,1473860,1813790, 2034760],
    '<100,900>': [1296660,  1413790,1419050,2183, 1454070]
}

values_delete = {
    '<16,200>': [ 1229710,  1229570,1229120,1593500, 1608940],
    '<32,500>': [1147310,  1137790,1172060,1459740, 1513760],
    '<100,900>': [1112610,  1182170,1185370,1417, 1057370]
}

# 定义每个柱子的颜色
colors = ['#FFF176', '#B2EBF2', '#4DD0E1','#C3CACA', '#AFB8B9',  '#00BCD4',  '#9BA6A8']
patterns = ['/', '\\', 'xx', 'x', '\\\\', '//', '+', '..', '++']

fig, axs = plt.subplots(1, 4, figsize=(16, 3))

for i, (operation, values_dict) in enumerate(zip(operations, [values_put, values_get, values_update, values_delete])):
    for j, memory_type in enumerate(memory_config):
        values = [values_dict[k][j] for k in kv_pairs_types]
        # x = np.arange(len(kv_pairs_types))
        x = np.array([0, 0.6, 1.2])
        print(type(x))
        print(x)
        width = 0.1
        axs[i].bar(x + j*width, values, width, label=memory_type, color=colors[j], edgecolor='black', hatch=patterns[j])

    axs[i].set_xticks(x + 2*width)
    axs[i].set_xticklabels(kv_pairs_types)
    axs[i].set_xlabel(operation)
    axs[0].set_ylabel('QPS')
    # axs[i].legend()

plt.legend(memory_config, loc='center', bbox_to_anchor=(-1.3, -0.25), ncol=5)
plt.tight_layout()

# plt.savefig('viper_limit_.pdf', bbox_inches='tight')
plt.show()
