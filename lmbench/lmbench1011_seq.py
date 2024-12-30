import matplotlib.pyplot as plt
import numpy as np

# rand_without_prefetch
rand_remote_numa = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.528', '5.530', '6.891', '7.948', '7.948', '9.222', '16.030', '32.677', '39.516', '40.512', '44.969', '47.605', '48.788', '48.759', '51.412', '52.824', '57.331', '81.600', '123.150', '154.635', '174.327', '191.862', '195.603', '205.608', '216.556']
rand_local_ddr = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.530', '5.529', '6.728', '7.817', '8.418', '12.616', '19.553', '32.448', '39.265', '40.857', '45.775', '47.592', '49.394', '48.068', '49.929', '51.641', '57.727', '67.711', '89.340', '114.098', '120.938', '125.775', '131.057', '132.879', '137.527']
rand_cxl_asic = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.529', '5.882', '7.117', '7.948', '7.949', '7.950', '8.123', '37.006', '38.152', '39.971', '43.852', '48.189', '48.501', '49.188', '49.275', '49.086', '50.277', '69.638',  '182.023', '213.302', '246.628', '264.098', '273.723', '283.118','284.086']
rand_local_ddr_gem5 = ['1.832', '1.832', '1.832', '1.832', '1.818', '1.813', '1.809', '5.259', '6.409', '6.409', '6.408', '7.442', '7.356', '15.608', '29.824', '48.523', '50.283', '50.361', '50.378', '50.394', '50.426', '50.439', '50.449', '50.454', '50.633', '64.463', '99.695', '123.228', '129.668', '133.781', '135.063', '135.901', '136.186']
rand_cxl_asic_gem5 = ['1.832', '1.832', '1.832', '1.832', '1.818', '1.813', '1.809', '5.259', '6.410', '6.409', '6.408', '7.441', '7.356', '15.609', '29.852', '48.525', '50.283', '50.359', '50.379', '50.391', '50.424', '50.442', '50.444', '50.456', '50.458', '86.246', '184.391', '249.754', '267.923', '279.647', '283.449', '285.993', '286.878']
rand_cxl_fpga_gem5 = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.528', '6.229', '6.493', '7.885', '7.950', '7.950', '8.142', '38.844', '38.716', '42.446', '44.436', '50.234', '49.291', '51.063', '49.639', '51.316', '49.831', '108.059', '191.718', '257.843', '304.369', '344.860', '360.653', '376.948', '379.749']


rand_remote_numa = [float(i) for i in rand_remote_numa]
rand_local_ddr = [float(i) for i in rand_local_ddr]
rand_cxl_asic = [float(i) for i in rand_cxl_asic]
rand_local_ddr_gem5 = [float(i) for i in rand_local_ddr_gem5]
rand_cxl_asic_gem5 = [float(i) for i  in rand_cxl_asic_gem5]
rand_cxl_fpga_gem5 = [float(i) for i in rand_cxl_fpga_gem5]

# random
data = {
    "Stride": [0.00049, 0.00098, 0.00195, 0.00391, 0.00781, 0.01562, 0.03125, 0.04688, 0.09375, 0.1875, 0.375, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512,768, 1024],
     "DDR-L": rand_local_ddr,
    "CXL-DMSim(L)" : rand_local_ddr_gem5,
    "DDR-R": rand_remote_numa,
    "CXL-FPGA": rand_cxl_fpga_gem5,
    "CXL-DMSim(F)": [1.418, 1.418, 1.418, 1.418, 1.409, 1.406, 1.403, 1.403, 5.623, 5.622, 5.621, 6.178, 6.192, 7.317,
                     21.203, 34.977, 39.763, 44.431, 47.268, 48.995, 49.373, 49.467, 49.481, 49.499, 49.496, 99.100,
                     236.342, 327.165, 352.460, 368.803, 374.073, 377.660, 378.818],
    "CXL-ASIC": rand_cxl_asic,
    "CXL-DMSim(A)": rand_cxl_asic_gem5
}








"""
seq read pattern
remote numa
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.473', '5.471', '5.471', '5.529', '5.529', '6.750', '17.684', '28.285', '34.328', '35.210', '35.938', '34.773', '35.711', '34.772', '35.704', '37.608', '39.727', '56.906', '91.678', '148.216', '165.063', '179.765', '184.496', '188.242', '193.660']
local ddr
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.473', '5.472', '5.471', '5.532', '5.532', '6.307', '14.260', '29.070', '35.758', '34.960', '35.968', '34.491', '35.725', '34.499', '34.791', '37.042', '37.891', '51.086', '67.546', '96.613', '99.075', '106.990', '107.159', '113.084', '114.094']
cxl-asic
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.473', '5.471', '5.471', '5.530', '5.530', '5.532', '5.621', '34.648', '35.276', '36.178', '35.040', '35.712', '34.780', '35.708', '34.778', '35.707', '35.856', '62.978', '101.362', '160.892', '188.615', '218.716', '229.925', '245.020', '250.151']
"
seq read pattern without prefetch mechanism
local ddr
['1.832', '1.832', '1.832', '1.832', '1.817', '1.813', '1.808', '1.812', '6.410', '6.409', '6.408', '6.408', '6.408', '6.408', '10.108', '49.516', '49.516', '49.517', '49.517', '49.517', '49.517', '49.517', '49.519', '49.517', '49.517', '49.784', '137.353', '136.347', '135.921', '135.460', '135.202', '134.990', '134.864']
cxl-asic
['1.832', '1.832', '1.832', '1.832', '1.818', '1.813', '1.808', '1.812', '6.410', '6.409', '6.409', '6.408', '6.408', '6.408', '11.636', '49.516', '49.516', '49.517', '49.516', '49.517', '49.517', '49.517', '49.516', '49.516', '49.517', '50.331', '286.889', '286.886', '286.859', '286.896', '286.883', '286.884', '286.885']

"""



# 按CXL-MemSim的标准来,要明白是要跟谁比较
cache1 = np.log2(0.046)
cache2 = np.log2(2)
cache3 = np.log2(96)


stride_log10 = [np.log10(i) for i in data["Stride"]]
# plotcolor = Hstray_2plot
stride_log2 = [np.log2(i) for i in data["Stride"]]
print(stride_log2)
plt.figure(figsize=(13, 5))


color = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#999999','#4DD0E1']

# stride_log2 = stride_log2
stride = [-11, -10, -9, -8.4, -8, -7.4, -7, -6.4, -6, -5.4, -5, -4.4, -4, -3.4, -3, -2.4, -2, -1.4, -1, -0.4, 0, 0.6, 1, 1.6, 2 , 2.6, 3, 3.6, 4, 4.6, 5, 5.6, 6, 6.6, 7, 8, 9]

print(data["CXL-DMSim(L)"])

plt.plot(stride_log2, data["DDR-L"], marker='p',markersize=10,markeredgecolor="black", label="DDR-L", color=color[4])
plt.plot(stride_log2, data["CXL-DMSim(L)"], marker='d', markersize=10,markeredgecolor="black",label="CXL-DMSim$_L$", color=color[6])

plt.plot(stride_log2, data["DDR-R"], marker='^',markersize=10, markeredgecolor="black",label="DDR-R", color=color[5])
plt.plot(stride_log2, data["CXL-ASIC"], marker='s', markersize=10, markeredgecolor="black", label="CXL-ASIC", color=color[3])
plt.plot(stride_log2, data["CXL-DMSim(A)"], marker='H', markersize=10,markeredgecolor="black",label="CXL-DMSim$_A$", color=color[0])
plt.plot(stride_log2, data["CXL-FPGA"], marker='D', markersize=10, markeredgecolor="black", label="CXL-FPGA", color=color[1])
plt.plot(stride_log2, data["CXL-DMSim(F)"], marker='o', markersize=10,markeredgecolor="black",label="CXL-DMSim$_F$", color=color[2])



plt.axvline(x=stride_log2[0], linestyle='--', color='red')
plt.axvline(x=cache1, linestyle='--', color='red')
plt.axvline(x=cache2, linestyle='--', color='red')
plt.axvline(x=cache3, linestyle='--', color='red')
plt.axvline(x=stride_log2[32], linestyle='--', color='red')


plt.text(-9, 68, 'L1 cache', fontsize=20)
plt.text(-2.8, 68, 'L2 cache', fontsize=20)
plt.text(2.7, 68, 'L3 cache', fontsize=20)
plt.text(7.3, 54, 'Memory', fontsize=20)

plt.xlabel("Array Size (log2 MB)",fontsize=24)
plt.ylabel("Latency (ns)",fontsize=24)

plt.rcParams.update({'font.size': 20})
# plt.title("Comparison of Latency for Different Memory Types")
plt.legend(loc='upper left',bbox_to_anchor=(0.03, 1), ncol=3, columnspacing=2.5,fontsize=20,frameon=False, edgecolor='black',fancybox=False,borderpad = 0.1, labelspacing = 0.2, handletextpad = 0.2) # 图例放在最下方

# plt.grid(True)

# 设置边框宽度
bwidth = 2.5
ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['bottom'].set_linewidth(bwidth)
ax.spines['left'].set_linewidth(bwidth)
ax.spines['top'].set_linewidth(bwidth)
ax.spines['right'].set_linewidth(bwidth)

# log2显式
plt.xticks(np.log2(data["Stride"]), data["Stride"], fontsize=19,rotation=90)
# 等距离显式
# distance = [i for i in range(1,len(stride)+1)]
# plt.xticks(distance, data["Stride"], fontsize=15,rotation=90)
y_ticks = [0,50,100,150,200,250,300,350,400]
plt.yticks(y_ticks,[str(y_tick) for y_tick in y_ticks],fontsize=20)
# plt.yticks(fontsize=20)
plt.tight_layout()
# plt.tight_layout()
# plt.savefig('lmbench1011_seq.pdf', bbox_inches='tight',pad_inches=0.0)
plt.show()