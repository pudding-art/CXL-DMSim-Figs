import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
# Data
operations = ['Insert', 'Select', 'Update', 'Delete']
kv_pairs_types = ['<16,200>',  '<100,900>']
memory_config = [ 'DDR-L', 'DDR-L+DDR-R','DDR-L+CXL-FPGA', 'DDR-L+CXL-ASIC','CXL-DMSim$_L$', 'CXL-DMSim$_L$+CXL-DMSim$_F$', 'CXL-DMSim$_L$+CXL-DMSim$_A$']

""""
都归一化到<16,200>上
"""""
values_put = {
    # [2068370, 2057030, 2117250, 2099190]
    '<16,200>': [2068370/2068370,2099190/2068370, 2057030/2068370, 2117250/2068370, 1243870/1243870, 1243870/1243870, 1246380/1243870],
    '<100,900>': [545408/2068370,779039/2068370, 693037/2068370, 795015/2068370, 113031/1246380,398038/1246380, 405062/1246380] #[545408, 693037, 795015, 779039]
}

values_get = {
    # [1845050, 1892930, 1913380, 1886480]
    # '<16,200>': [ 1845050/1845050, 1886480/1845050,1892930/1845050, 1913380/1845050, 2390120/2390120, 2390120/2390120, 2367810/2390120],
    # '<100,900>': [49545/1845050,910191/1845050, 744402/1845050, 831515/1845050, 83655/2390120, 1241390/2390120,1286000/2390120] #[49545, 744402, 831515, 910191]
    '<16,200>': [1845050 / 1845050, 1886480 / 1845050,  2390120 / 2390120,
                 2390120 / 2390120, 2367810 / 2390120],
    '<100,900>': [49545 / 1845050, 910191 / 1845050,  83655 / 2390120,
                  1241390 / 2390120, 1286000 / 2390120]  # [49545, 744402, 831515, 910191]

}


values_update = {
    # '<16,200>': [1522700/1522700, 1554320/1522700 , 1544180/1522700, 1574070/1522700,2524520/2524520,2529270/2524520, 2522270/2524520 ],#[1522700, 1544180, 1574070, 1554320]
    # '<100,900>': [52091/1522700, 1244740/1522700,1126380/1522700, 1199380/1522700,64883/2530270, 1726990/2522270, 1820660/2529270]#[52091, 1126380, 1199380, 1244740]
    '<16,200>': [1522700/1522700, 1554320/1522700 , 1544180/1522700, 2529270/2524520, 2522270/2524520 ],#[1522700, 1544180, 1574070, 1554320]
    '<100,900>': [52091/1522700, 1244740/1522700,1126380/1522700, 1726990/2522270, 1820660/2529270]#[52091, 1126380, 1199380, 1244740]



}



values_delete = {
    '<16,200>': [ 1200950/1200950, 1224720/1200950, 1218040/1200950, 1240380/1200950 ,1856430/1856430,1856940/1856430,1857700/1856430], #[1200950, 1218040, 1240380, 1224720]
    '<100,900>': [40568/1200950,  1045520/1200950 ,954070/1200950, 1008270/1200950, 66433/1856430,1297970/1850720, 1343600/1857700] #[40568, 954070, 1008270, 1045520]
}



#  '#FFF9C4', '#FFF59D', '#9DC3E7', '#5F97D2', '#C4A5DE','#8983BF'

# 定义每个柱子的颜色
colors = ['#FFF9C4','#B2EBF2', '#4DD0E1','#9DC3E7','#FFF176','#b39ddb',  '#8983BF','#C3CACA', '#AFB8B9','#5F97D2', '#C4A5DE']
patterns = ['/', '+', '..', 'x', 'o', '\\\\', '+', '..', '++','o']
# y = [0,0.5, 1, 1.5]

fig, axs = plt.subplots(1, 4, figsize=(50, 4))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=None)
for i, (operation, values_dict) in enumerate(zip(operations, [values_put, values_get, values_update, values_delete])):
    for j, memory_type in enumerate(memory_config):
        values = [values_dict[k][j] for k in kv_pairs_types]
        x = np.array([0, 0.7])
        width = 0.09
        bars = axs[i].bar(x + j * width, [min(v, 2) for v in values], width, label=memory_type, color=colors[j], edgecolor='black',linewidth=3, hatch=patterns[j])

        # 遍历每个柱子，如果原始值大于2，则在柱子上方添加文本标签
        for k, bar in enumerate(bars):
            if values[k] > 2:
                # 计算并四舍五入原始倍数
                original_value = round(values[k])
                axs[i].text(bar.get_x() + bar.get_width() / 2, 2.1, str(original_value), ha='center', va='bottom',fontsize=40)

    axs[i].set_xticks(x + 3 * width)
    # axs[i].set_yticks(fontsize=35)
    y = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    axs[i].set_yticklabels(y, fontsize=40)
    axs[i].set_xticklabels(kv_pairs_types,fontsize=40)
    axs[i].set_xlabel(operation,fontsize=40)
    axs[i].set_ylabel('Normalized QPS',y=0.42, fontsize=40)
    # 设置边框宽度
    bwidth = 3
    # axs[i] = plt.gca()  # 获取边框
    axs[i].spines['bottom'].set_linewidth(bwidth)
    axs[i].spines['left'].set_linewidth(bwidth)
    axs[i].spines['top'].set_linewidth(bwidth)
    axs[i].spines['right'].set_linewidth(bwidth)





plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125


plt.legend(memory_config, loc='center', bbox_to_anchor=(-1.35, 1.25), ncol=7,frameon=False,fontsize=40,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3 ,columnspacing=0.4)
plt.tight_layout()

# plt.savefig('viper_limit_0715.pdf', bbox_inches='tight',pad_inches=0.0)
plt.show()