import matplotlib.pyplot as plt
import numpy as np


# latency

ddrl_bw = [0, 469704,932669,1392731, 1840212,2284688,
    2715409, 3129527,3526123,3907345,4264252,4598346,
    4911569,5188912,5449453,5672418,5837793,5999001,
    6098516,6235210,6285299,6337279,6397977,6412998,
    6482428,6506161,6544237,6579346,6637887,6662118,
    6725594,6719817,6788691,6807969,6835063,6867832,
    6920686,6932993,6970763,6979710,7016766,
    7026491,
    7041941,
    7050823,
    7033558,
    7072634,
    7083689,
    7124153,
    7139799]
ddrr_bw = [0,358250,713237,1065843,1408071,1743652,2084628, 2404258,2719210, 3023060,3312664, 3590619,3858846,  4129984,
    4350870, 4584783, 4807598,4995244,5168755,
    5331856,5474423,5578822, 5689575,5773958,5861427,5901961,
    5949573,5998394,6034974,6062335, 6089830,
    6113604, 6137374,6165942,6189085,
    6195837, 6219571,6244943,6259298,
    6265244,6292287,6317251,6337374,
    6347253,6365583,6386060,6402012, 6426135, 6440319]

cxl_fpga = [0,211881, 419574, 627025, 828862, 1029986, 1225251, 1416502, 1604167, 1786566,
            1962357, 2136896, 2305287, 2462165, 2611796, 2752106, 2884861, 2989766, 3083505,
            3161000, 3233902,  3329098, 3283093,3370607, 3409770, 3455784, 3464537, 3483499,
            3507951, 3532733, 3543522, 3561776, 3588566, 3605972, 3628956, 3643540, 3654369,
            3669920, 3691279, 3704145,3721327, 3730123, 3747930, 3754749, 3767877, 3782124, 3792249,
            3800164, 3815851]

cxl_asic = [0,287264, 574503, 863423, 1147881, 1427280, 1698337, 1948166, 2195086,
            2434624, 2671991, 2909253, 3139703, 3365719, 3565008, 3740444, 3880218,
            3988931, 4079050, 4145565, 4189490, 4232491, 4264266, 4294676, 4322508,
            4328407,4372373, 4385440, 4413679, 4440728, 4461452, 4478095, 4505384, 4524511,
            4543352,4563331, 4571108, 4574880, 4581782, 4625248, 4643084, 4659374, 4678782,
            4686950, 4697587, 4711504, 4727455,4731632, 4737053]

ddr_fpga = [0,271855, 539414, 807252, 1073229, 1341510, 1601908, 1860101, 2125611, 2376783, 2632576, 2878332, 3128804, 3366670, 3603161, 3849235, 4088143, 4320228, 4538856, 4766353, 4982160, 5178176, 5369347, 5564145, 5750829, 5909695, 6071416, 6225511, 6372485, 6490542, 6609331, 6739028, 6802725, 6916243, 6957020, 6947014, 7044079, 7094357, 7075405, 7147232, 7189785, 7257598, 7268519, 7355588, 7366097, 7402567, 7410644, 7403766, 7424276]

ddr_asic = [0,343944, 686412, 1031907, 1373220, 1718067, 2057332, 2391030, 2727884, 3047783, 3353427,
            3649495, 3953279, 4241058, 4546733, 4855452, 5161382, 5477146, 5798130, 6111050, 6414167,
            6701819, 6969270, 7233704, 7463891, 7718703, 7931759, 8125217, 8295265, 8434999, 8595772,
            8698605, 8795741, 8842543, 8941077, 9014251,9004214, 9026868, 9119224, 9130342, 9202475, 9229296,
            9243613, 9242127, 9292598, 9336001, 9341752, 9375358, 9411216]
ddr_rddr = [0,403848, 806533, 1211529, 1610857, 2012409, 2406822, 2798017, 3183943, 3565713, 3953125,
            4324586, 4699410, 5068166, 5424429, 5773178, 6134341, 6474803, 6828481, 7159444, 7501407,
            7816394, 8129849, 8436799, 8751360, 9043081, 9328813, 9623219, 9885725, 10146275, 10391243,
            10641897, 10839714, 11070009, 11259230, 11446500, 11624704, 11751895, 11928853, 12041298,
            12154352, 12278592, 12343606, 12403987, 12481575, 12564522, 12614547, 12681300, 12704150]

print(len(ddrr_bw))

# index
index_rddr = [0, 1, 2, 4, 8, 16, 32, 47]
index_fpga = [0, 1, 2, 4, 8, 16, 32, 47]
index_asic = [0, 1, 2, 4, 8, 16, 32, 47]

index_rddr = [i+1 for i in range(48)]

index = [i for i in range(8)]
patterns = ['++', 'xx', 'o',  '+', '..', '/', 'x','\\']
# labels
memory_config_rddr = [ 'DDR-L', 'DDR-L+DDR-R','DDR-R']
memory_config_fpga = [ 'DDR-L','DDR-L+CXL-FPGA','CXL-FPGA']
memory_config_asic = ['DDR-L', 'DDR-L+CXL-ASIC','CXL-ASIC']


colors = ['#FFF9C4', '#FFF59D', '#9DC3E7', '#5F97D2', '#C4A5DE','#8983BF']

# Plotting
plt.figure(figsize=(15, 9))
# Latency Line Plot
index = range(len(index_rddr))
bar_width = 0.3



plt.subplot(3,1,1)
for i in index_rddr:

    plt.bar(i + bar_width, ddrl_bw[i], bar_width, color=colors[0],label='DDR-L',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[0])
    plt.bar(i + bar_width * 2, ddr_rddr[i], bar_width,color=colors[1], label='DDR-L+DDR-R',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[1])
    plt.bar(i + bar_width * 3, ddrr_bw[i], bar_width, color=colors[2], label='DDR-R',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[2])


y_loc=[0,2,4,6,8,10]
y_label=['0','2','4','6','8','10']
plt.yticks(y_loc, y_label)
plt.xticks([i + bar_width * 2 for i in index_rddr], [str(i) for i in index_rddr])
plt.xlabel('CPU Cores Number')
plt.ylabel('Bandwidth (Lookups/s)')


plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125


legend = plt.legend(memory_config_rddr,bbox_to_anchor=(1, 1.2), ncol=3,  columnspacing=0.1,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3 , frameon=False)
  # 图例放在最下方
plt.axvline(x=15.2, linestyle='--', color='red')



plt.subplot(3,1,2)
for i in index_rddr:

    plt.bar(i + bar_width, ddrl_bw[i], bar_width, color=colors[0],label='DDR-L',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[0])
    plt.bar(i + bar_width * 2, ddr_fpga[i], bar_width,color=colors[3], label='DDR-L+CXL-FPGA',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[3])
    plt.bar(i + bar_width * 3, cxl_fpga[i], bar_width, color=colors[4], label='CXL-FPGA',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[4])



plt.xticks([i + bar_width * 2 for i in index_rddr], [str(i) for i in index_rddr])
plt.xlabel('CPU Cores Number')
y_loc=[0,2,4,6,8,10]
y_label=['0','2','4','6','8','10']
plt.yticks(y_loc, y_label)
plt.ylabel('Bandwidth (Lookups/s)')



plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125


legend = plt.legend(memory_config_fpga,bbox_to_anchor=(1, 1.2),ncol=3,   columnspacing=0.1,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3 , frameon=False)
 # 图例放在最下方
plt.axvline(x=31.2, linestyle='--', color='red')

plt.subplot(3,1,3)
for i in index_rddr:

    plt.bar(i + bar_width, ddrl_bw[i], bar_width, color=colors[0],label='DDR-L',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[0])
    plt.bar(i + bar_width * 2, ddr_asic[i], bar_width,color=colors[4], label='DDR-L+CXL-ASIC',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[4])
    plt.bar(i + bar_width * 3, cxl_asic[i], bar_width, color=colors[5], label='CXL-ASIC',edgecolor='black', linewidth=1,zorder=2,hatch=patterns[5])


y_loc=[0,2,4,6,8,10]
y_label=['0','2','4','6','8','10']
plt.yticks(y_loc, y_label)
plt.xticks([i + bar_width * 2 for i in index_rddr], [str(i) for i in index_rddr])
plt.xlabel('CPU Cores Number')
plt.ylabel('Bandwidth (Lookups/s)')
# plt.title('Bandwidth Comparison')
# 设置边框宽度


plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125


legend = plt.legend(memory_config_asic,bbox_to_anchor=(0.65, 1.2), ncol=3, columnspacing=6,borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3 , frameon=False)
  # 图例放在最下方
plt.axvline(x=20.2, linestyle='--', color='red')

plt.tight_layout()
plt.show()