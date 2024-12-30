import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties


"""
均方根误差(RMSE)
(1)测量值-真实值的差除以真实值的平方 求和 开方 再除以N
LMBench FPGA latency simulation error:  0.031840470777702884
LMBench ASIC latency simulation error:  0.03055929150066336
STREAM FPGA bandwidth simulation error:  0.08072315108560499
STREAM ASIC bandwidth simulation error:  0.047746756649779426
Redis QPS simulation error:  0.020044340549149477
Viper simulation error:  0.07418609849348726
MERCI QPS simulation error:  0.01399474156873183

(2)测量值-真实值的差除以真实值的平方 求和 除以N 再开方
LMBench FPGA latency simulation error:  0.18290957907777766
LMBench ASIC latency simulation error:  0.1755497644593778
STREAM FPGA bandwidth simulation error:  0.16144630217120998
STREAM ASIC bandwidth simulation error:  0.09549351329955885
Redis QPS simulation error:  0.03471781623533995
Viper simulation error:  0.1483721969869745
MERCI QPS simulation error:  0.01979155332840708
"""
def cal_error_rate(real_value, sim_value):
    real_array = np.array(real_value)
    sim_array = np.array(sim_value)

    diff_squard =((sim_array - real_array)/real_array) ** 2
    # print("diff_squard:", diff_squard)
    sum_squard = np.sum(diff_squard)
    n = len(real_value)
    # print("n = ", n)

    error_rate = np.sqrt(sum_squard)/n
    # error_rate = np.sqrt(sum_squard/n)
    return error_rate

"""
MSLE
LMBench FPGA latency simulation error:  0.022430807922205278
LMBench ASIC latency simulation error:  0.020948181691799905
STREAM FPGA bandwidth simulation error:  0.002420214626722106
STREAM ASIC bandwidth simulation error:  0.0018613208595445832
Redis QPS simulation error:  0.0003230081316370015
Viper simulation error:  0.0027759975993592216
MERCI QPS simulation error:  0.00011335893003394602
"""
# def cal_error_rate(real_value, pred_value):
#     """
#     计算 Mean Squared Logarithmic Error (MSLE)。
#
#     参数:
#     real_value -- 真实的值，可以是单个数字或数字数组。
#     pred_value -- 预测的值，可以是单个数字或数字数组。
#
#     返回:
#     msle -- 计算出的 MSLE 值。
#     """
#     # 将输入转换为 numpy 数组
#     real_array = np.array(real_value, dtype=float)
#     pred_array = np.array(pred_value, dtype=float)
#
#     # 避免对零或负数取对数，所以给所有值加上1
#     log_real = np.log1p(real_array)
#     log_pred = np.log1p(pred_array)
#
#     # 计算 MSLE
#     msle = np.mean((log_real - log_pred) ** 2)
#
#     return msle

"""
平均绝对百分比误差(Mean Absolute Percentage Error, MAPE)

    |y-f(x)|
sum{|------|} / n
    | f(x) |
    
LMBench FPGA latency simulation error:  0.14026444284842235
LMBench ASIC latency simulation error:  0.13124973296705653
STREAM FPGA bandwidth simulation error:  0.12839408367693297
STREAM ASIC bandwidth simulation error:  0.09489693159070038
Redis QPS simulation error:  0.02729824477423243
Viper simulation error:  0.14324931058471424
MERCI QPS simulation error:  0.01399474156873183
"""
# def cal_error_rate(real_value, sim_value):
#     real_array = np.array(real_value)
#     sim_array = np.array(sim_value)
#
#     diff_squard = np.sqrt(((sim_array - real_array)/real_array) ** 2)
#
#     sum_squard = np.sum(diff_squard)
#     n = len(real_value)
#     error_rate =sum_squard/n
#
#     return error_rate

# latency

rand_cxl_asic = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.529', '5.882', '7.117', '7.948', '7.949', '7.950', '8.123', '37.006', '38.152', '39.971', '43.852', '48.189', '48.501', '49.188', '49.275', '49.086', '50.277', '69.638',  '182.023', '213.302', '246.628', '264.098', '273.723', '283.118','284.086']
rand_cxl_asic = ['1.832', '1.832', '1.832', '1.832', '1.818', '1.813', '1.809', '5.259', '6.410', '6.409', '6.408', '7.441', '7.356', '15.609', '29.852', '48.525', '50.283', '50.359', '50.379', '50.391', '50.424', '50.442', '50.444', '50.456', '50.458', '86.246', '184.391', '249.754', '267.923', '279.647', '283.449', '285.993', '286.878']

fpga = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.528', '6.229', '6.493', '7.885', '7.950', '7.950', '8.142', '38.844', '38.716', '42.446', '44.436', '50.234', '49.291', '51.063', '49.639', '51.316', '49.831', '108.059', '191.718', '257.843', '304.369', '344.860', '360.653', '376.948', '379.749']

fpga = [float(i) for i in fpga]
asic = [float(i) for i in rand_cxl_asic]
# rand_cxl_asic_gem5 = [float(i) for i in rand_cxl_asic_gem5]


data_lat = {
"CXL-DMSim(F)": [1.418, 1.418,1.418, 1.418,1.409, 1.406, 1.403,1.403, 5.623, 5.622, 5.621,  6.178,6.192, 7.317, 21.203,34.977, 39.763,44.431, 47.268, 48.995,49.373,49.467, 49.481,49.499, 49.496,99.100,236.342,327.165, 352.460,368.803,374.073, 377.660, 378.818 ],
"CXL-FPGA": [1.728, 1.728, 1.728, 1.728, 1.728, 1.728,1.728, 1.729,5.528,5.528,6.569,7.808, 7.947, 7.949, 16.718, 33.676, 37.197, 38.544, 41.386, 46.658, 47.586, 47.792, 47.973, 48.163, 48.196, 75.845, 152.623,243.048,285.925,326.383 ,368.336,379.995, 382.928],
"CXL-DMSim(A)":  [1.418, 1.418,1.418, 1.418,1.409, 1.406, 1.403, 1.404, 5.622, 5.622, 5.621,6.187, 6.195, 7.324, 21.255, 35.054, 39.613, 44.453, 47.244, 49.021, 49.385, 49.474, 49.485, 49.494, 49.504, 85.349, 184.331, 249.589, 267.873, 279.605, 283.401, 285.972, 286.831 ],
"CXL-ASIC": [1.728, 1.728, 1.728, 1.728, 1.728, 1.728,1.728,1.729,5.527,5.527,7.22,7.882, 7.945, 7.987, 16.622, 34.522, 40.228, 40.993, 45.331, 50.047, 50.781, 50.96, 51.136, 51.211, 51.13, 66.528, 123.13, 185.858,216.799,264.898, 274.033, 278.522, 284.893]


}

# rand_remote_numa = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.528', '5.530', '6.891', '7.948', '7.948', '9.222', '16.030', '32.677', '39.516', '40.512', '44.969', '47.605', '48.788', '48.759', '51.412', '52.824', '57.331', '81.600', '123.150', '154.635', '174.327', '191.862', '195.603', '205.608', '216.556']
# rand_local_ddr = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.530', '5.529', '6.728', '7.817', '8.418', '12.616', '19.553', '32.448', '39.265', '40.857', '45.775', '47.592', '49.394', '48.068', '49.929', '51.641', '57.727', '67.711', '89.340', '114.098', '120.938', '125.775', '131.057', '132.879', '137.527']
#
# rand_cxl_asic = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.529', '5.882', '7.117', '7.948', '7.949', '7.950', '8.123', '37.006', '38.152', '39.971', '43.852', '48.189', '48.501', '49.188', '49.275', '49.086', '50.277', '69.638',  '182.023', '213.302', '246.628', '264.098', '273.723', '283.118','284.086']
# rand_local_ddr_gem5 = ['1.832', '1.832', '1.832', '1.832', '1.818', '1.813', '1.809', '5.259', '6.409', '6.409', '6.408', '7.442', '7.356', '15.608', '29.824', '48.523', '50.283', '50.361', '50.378', '50.394', '50.426', '50.439', '50.449', '50.454', '50.633', '64.463', '99.695', '123.228', '129.668', '133.781', '135.063', '135.901', '136.186']
#
# rand_cxl_asic_gem5 = ['1.832', '1.832', '1.832', '1.832', '1.818', '1.813', '1.809', '5.259', '6.410', '6.409', '6.408', '7.441', '7.356', '15.609', '29.852', '48.525', '50.283', '50.359', '50.379', '50.391', '50.424', '50.442', '50.444', '50.456', '50.458', '86.246', '184.391', '249.754', '267.923', '279.647', '283.449', '285.993', '286.878']
# rand_cxl_fpga = ['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.528', '6.229', '6.493', '7.885', '7.950', '7.950', '8.142', '38.844', '38.716', '42.446', '44.436', '50.234', '49.291', '51.063', '49.639', '51.316', '49.831', '108.059', '191.718', '257.843', '304.369', '344.860', '360.653', '376.948', '379.749']
#
#
# rand_remote_numa = [float(i) for i in rand_remote_numa]
# rand_local_ddr = [float(i) for i in rand_local_ddr]
# rand_cxl_asic = [float(i) for i in rand_cxl_asic]
# rand_local_ddr_gem5 = [float(i) for i in rand_local_ddr_gem5]
# rand_cxl_asic_gem5 = [float(i) for i  in rand_cxl_asic_gem5]
# rand_cxl_fpga = [float(i) for i in rand_cxl_fpga]
#
# # random
# data_lat = {
#     "Stride": [0.00049, 0.00098, 0.00195, 0.00391, 0.00781, 0.01562, 0.03125, 0.04688, 0.09375, 0.1875, 0.375, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512,768, 1024],
#      "DDR-L": rand_local_ddr,
#     "CXL-DMSim(L)" : rand_local_ddr_gem5,
#     "DDR-R": rand_remote_numa,
#     "CXL-FPGA": rand_cxl_fpga,
#     "CXL-DMSim(F)": [1.418, 1.418, 1.418, 1.418, 1.409, 1.406, 1.403, 1.403, 5.623, 5.622, 5.621, 6.178, 6.192, 7.317,
#                      21.203, 34.977, 39.763, 44.431, 47.268, 48.995, 49.373, 49.467, 49.481, 49.499, 49.496, 99.100,
#                      236.342, 327.165, 352.460, 368.803, 374.073, 377.660, 378.818],
#     "CXL-ASIC": rand_cxl_asic,
#     "CXL-DMSim(A)": rand_cxl_asic_gem5
# }

# bandwidth

data_bw = {
    'DDR-L': [20327.1/20327.1, 20358.5/20358.5, 22928.5/22928.5, 22927.8/22927.8],
    'DDR-R': [13999.1/20327.1, 14057.1/20358.5, 16869.7/22928.5, 16842.7/22927.8],
    'CXL-FPGA': [13094.5/20327.1, 9171.1/20358.5, 10424.8/22928.5, 10473.0/22927.8],
    'CXL-DMSim(F)': [11430.3/ 19203.1,10788.1/18464.,10142.4/20574.4,10071.5/20872.9],
    'CXL-ASIC': [16940.5/20327.1, 16819.7/20358.5, 18869.2/22928.5, 18858.9/22927.8],
    'CXL-DMSim(A)': [17780.5/19203.1, 16554.3/18464.3, 15486.2/20574.4, 15486.2/20872.9]
}


# redis
# 0-2 9+
qps_values = {
    'Workload A':[1.0, 0.9667, 0.9431,1, 0.9981, 0.9763, 8.46308/8.46308, 8.05387/8.46308, 7.87697/8.46308],
    'Workload B':[1.0, 0.9947, 0.9897,1, 0.9463, 0.8954,7.66102/7.66102, 7.52691/7.66102, 7.44505/7.66102],
    'Workload C':[1.0, 0.9707, 0.8996,1, 0.9443, 0.9163, 7.7402/7.7402, 7.57801/7.7402, 7.40554/7.7402],
    'Workload D':[1.0, 0.9575, 0.9170,1, 0.9691, 0.9150, 6.99039/6.99039, 6.72432/6.99039, 6.53979/6.99039,1]
}

# final redis qps data
data_redis_qps = {
    "WorkloadA_asic": [1, 0.9981, 0.9763],
    "WorkloadA_sim": [8.46308/8.46308, 8.05387/8.46308, 7.87697/8.46308],
    "WorkloadB_asic": [1, 0.9463, 0.8954,],
    "WorkloadB_sim": [7.66102/7.66102, 7.52691/7.66102, 7.44505/7.66102],
    "WorkloadC_asic": [1, 0.9443, 0.9163],
    "WorkloadC_sim": [7.7402/7.7402, 7.57801/7.7402, 7.40554/7.7402],
    "WorkloadD_asic": [1, 0.9691, 0.9150],
    "WorkloadD_sim": [6.99039/6.99039, 6.72432/6.99039, 6.53979/6.99039]
}




# viper
""""
都归一化到<16,200>上
"""""


values_put = {

    '<100,900>': [545408/2068370,779039/2068370, 795015/2068370, 113031/1246380, 405062/1246380]
}

values_get = {
    '<100,900>': [49545/1845050,910191/1845050, 831515/1845050, 83655/2390120, 1286000/2390120]

}


values_update = {
    '<100,900>': [52091/1522700, 1244740/1522700,1199380/1522700,64883/2530270, 1820660/2529270]


}


values_delete = {
    '<100,900>': [40568/1200950,  1045520/1200950 ,1008270/1200950,66433/1850720, 1343600/1857700]
}


# merci

delays_ms_96 = [30.2934, 15.372, 30.0796,  30.2934, 23.6173, 54.8686, 72.9889, 59.9909, 117.982]  # -3，-6 三个数据为旧gem5的结果数据


delays_ms_12 = [35.9181, 32.8975, 45.41, 35.9181,46.2586, 71.5609, 72.9889, 59.9909, 117.982]
delays_ms_24 = [35.6533, 25.0249, 39.0689, 35.6533,30.1243, 45.3497, 72.9889, 59.9909, 117.982]
delays_ms_36 = [33.4911, 20.8325, 37.5185, 33.4911,24.4222, 34.8731, 72.9889, 59.9909, 117.982]
delays_ms_48 = [40.826, 35.1592, 40.1844,40.826, 35.3696, 35.8453, 72.9889, 59.9909, 117.982]

total_queries = 103591

# 将延迟从毫秒转换为秒
delays_s = [delay / 1000 for delay in delays_ms_24]
# 计算QPS（每秒查询数）
qps_values = [total_queries / delay for delay in delays_s]



standard_fpga = qps_values[0]
standard_numa = qps_values[0]
standard_asic = qps_values[0]
standard_gem5 = qps_values[6]

# 0-2
for i in range(3):
    qps_values[i] = qps_values[i] / standard_fpga
# 3-5
for i in range(3, 6):
    qps_values[i] = qps_values[i] / standard_numa
# 6-8
for i in range(6, 9):
    qps_values[i] = qps_values[i] / standard_gem5



# viper-SSD
# viper-SSD暂时由于没有硬件设备无法校准也就暂时没有simulation error



# fpga lat error rate
real_fpga_lat = np.array(data_lat["CXL-FPGA"])
sim_fpga_lat = np.array(data_lat["CXL-DMSim(F)"])
# print(real_fpga_lat)
# print(sim_fpga_lat)

# diff_squard = (sim_fpga_lat - real_fpga_lat)**2
# sum_squard = np.sum(diff_squard)
# n = len(real_fpga_lat)
# res = np.sqrt(sum_squard / n)

fpga_lat_error_rate = cal_error_rate(real_fpga_lat,sim_fpga_lat)

print("LMBench FPGA latency simulation error: ", fpga_lat_error_rate)


## asic lat error rate

real_asic_lat = np.array(data_lat["CXL-ASIC"])
sim_asic_lat = np.array(data_lat["CXL-DMSim(A)"])
# real_asic_lat = np.array(rand_cxl_asic)
# sim_asic_lat = np.array(rand_cxl_asic_gem5)

asic_lat_error_rate = cal_error_rate(real_asic_lat,sim_asic_lat)

print("LMBench ASIC latency simulation error: ", asic_lat_error_rate)

lat_error_rate = (fpga_lat_error_rate + asic_lat_error_rate)/2


##  bandwidth


real_fpga_bw = np.array(data_bw["CXL-FPGA"])
sim_fpga_bw = np.array(data_bw["CXL-DMSim(F)"])

fpga_bw_error_rate = cal_error_rate(real_fpga_bw, sim_fpga_bw)

print("STREAM FPGA bandwidth simulation error: ", fpga_bw_error_rate)


real_asic_bw = np.array(data_bw["CXL-ASIC"])
sim_asic_bw = np.array(data_bw["CXL-DMSim(A)"])



asic_bw_error_rate = cal_error_rate(real_asic_bw, sim_asic_bw)

print("STREAM ASIC bandwidth simulation error: ", asic_bw_error_rate)


bw_error_rate = (fpga_bw_error_rate + asic_bw_error_rate) / 2
## redis


a_asic_qps = np.array(data_redis_qps["WorkloadA_asic"])
a_sim_qps = np.array(data_redis_qps["WorkloadA_sim"])
b_asic_qps = np.array(data_redis_qps["WorkloadB_asic"])
b_sim_qps = np.array(data_redis_qps["WorkloadB_sim"])
c_asic_qps = np.array(data_redis_qps["WorkloadC_asic"])
c_sim_qps = np.array(data_redis_qps["WorkloadC_sim"])
d_asic_qps = np.array(data_redis_qps["WorkloadD_asic"])
d_sim_qps = np.array(data_redis_qps["WorkloadD_sim"])



a_redis_error_rate = cal_error_rate(a_asic_qps, a_sim_qps)
b_redis_error_rate = cal_error_rate(b_asic_qps, b_sim_qps)
c_redis_error_rate = cal_error_rate(c_asic_qps, c_sim_qps)
d_redis_error_rate = cal_error_rate(d_asic_qps, d_sim_qps)


sum_redis_error_rate = (a_redis_error_rate + b_redis_error_rate + c_redis_error_rate + d_redis_error_rate) / 4
print("Redis QPS simulation error: ", sum_redis_error_rate)

## viper


asic_viper_ddrl = np.array([values_put['<100,900>'][0],values_get['<100,900>'][0], values_update['<100,900>'][0], values_delete['<100,900>'][0]])
asic_viper_cxl = np.array([values_put['<100,900>'][2],values_get['<100,900>'][2], values_update['<100,900>'][2], values_delete['<100,900>'][2]])
sim_viper_ddrl = np.array([values_put['<100,900>'][3],values_get['<100,900>'][3], values_update['<100,900>'][3], values_delete['<100,900>'][3]])
sim_viper_cxl = np.array([values_put['<100,900>'][4],values_get['<100,900>'][4], values_update['<100,900>'][4], values_delete['<100,900>'][4]])

# 不考虑gem5对ddr模型的仿真
# ddr_viper_error_rate = cal_error_rate(asic_viper_ddrl, sim_viper_ddrl)
cxl_viper_error_rate = cal_error_rate(asic_viper_cxl, sim_viper_cxl)

print("Viper simulation error: ", cxl_viper_error_rate)




## merci


asic_merci = np.array(qps_values[3:5])
sim_merci = np.array(qps_values[6:8])


merci_qps_error_rate = cal_error_rate(asic_merci, sim_merci)


print("MERCI QPS simulation error: ", merci_qps_error_rate)





"""
simulation error bar
"""

workloads = ['LMBench', 'STREAM', 'Redis', 'Viper', 'MERCI', 'CXL-DMSim', 'Mess', 'gem5Tune', 'native gem5']
# workloads = ['STREAM', 'Redis', 'Viper', 'MERCI']


cxl = 0
# other simulators simulation error
native_gem5 = 15.0 # MESS gem5+Mess simulation error
mess = 6.0 #  MICRO 24 MESS simulation error 0.4%-6%
gem5tune = 6.2 # TC 24 gem5tune simulation error


lat_error_rate = lat_error_rate * 100
bw_error_rate = bw_error_rate * 100
sum_redis_error_rate = sum_redis_error_rate * 100
cxl_viper_error_rate = cxl_viper_error_rate * 100
merci_qps_error_rate = merci_qps_error_rate * 100



cxl_simulation_error = [lat_error_rate, bw_error_rate,sum_redis_error_rate, cxl_viper_error_rate, merci_qps_error_rate]
# simulation_error = [ bw_error_rate,sum_redis_error_rate, cxl_viper_error_rate, merci_qps_error_rate]

print(cxl_simulation_error)

cxl_simulation_error =  np.array(cxl_simulation_error)
cxl_simulation_error_sum = np.sum(cxl_simulation_error)
error_rate_size = len(cxl_simulation_error)
# CXL-DMSim average simulation error
cxl = cxl_simulation_error_sum / error_rate_size

# all simulation error set
simulation_error = [lat_error_rate, bw_error_rate,sum_redis_error_rate, cxl_viper_error_rate, merci_qps_error_rate,
                    cxl, mess, gem5tune, native_gem5]


simulation_error = [round(lat_error_rate, 1), round(bw_error_rate, 1), round(sum_redis_error_rate, 1), round(cxl_viper_error_rate, 1), round(merci_qps_error_rate, 1),
                    round(cxl, 1), round(mess, 1), round(gem5tune, 1), round(native_gem5, 1)]
print("============================================================")
print(simulation_error)
print("============================================================")



# 定义每个柱子的颜色
colors = ['#FFF9C4', '#FFF59D', '#FFF176', '#B2EBF2', '#4DD0E1',  '#9BA6A8', '#F6CAE5',
          '#C4A5DE', '#A1A9D0', '#CFEAF1', '#96CCCB', '#8ECFC9']

# 定义每个柱子的样式
patterns = ['o', 'x', '*', '//', '||', '\\\\','.', 'xo','--']

bar_width = 0.6
# index = np.arange(len(operations))
# print(index)
# index = [0.1,1,1.9,2.8 ]
scale_x = [i+7 for i in range(9)]


plt.figure(figsize=(25, 10))
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
plt.rcParams.update({'font.size': 45})
plt.tick_params(axis='y',width=6)#修改刻度线线粗细width参数，修改刻度字体labelsize参数
plt.tick_params(axis='y', length=10)  # 设置y轴刻度线长度为10
for i, mem_config in enumerate(workloads):
    print(i, mem_config)
    # print(data[mem_config])
    plt.bar(scale_x[i], simulation_error[i], bar_width, color=colors[i], label=mem_config, edgecolor='black', linewidth=4,zorder=2,hatch=patterns[i])


# 设置边框宽度
bwidth = 4
ax = plt.gca()  # 获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.spines['bottom'].set_linewidth(bwidth)
ax.spines['left'].set_linewidth(bwidth)
ax.spines['top'].set_linewidth(bwidth)
ax.spines['right'].set_linewidth(bwidth)

# 刻度线长度调整
# plt.tick_params(axis='x', length=10)  # 设置x轴刻度线长度为10


plt.axvline(x=scale_x[5]+0.5, linestyle='--', color='red', linewidth = 4)

# plt.xlabel('Workload', fontsize=40)
plt.ylabel('Simulation Error (%)',y=0.47,fontsize=50)


y_ticks = [0,2,4,6,8,10,12,14,16,18]

plt.yticks(y_ticks, [str(y_tick) for y_tick in y_ticks], fontsize=50)

scale_x_label = ['LMbench','STREAM', 'Redis', 'Viper','MERCI', 'Avg.', 'Mess','gem5Tune', 'native gem5' ] # original gem5, gem5Tune(TC'24), MESS(MICRO'24)


# scale_x = np.array(scale_x)
# xlabel的位置不用bar的标签了
xlabel_loc = [scale_x[0]-0.5, scale_x[1]-0.45, scale_x[2]-0.25,scale_x[3]-0.25, scale_x[4]-0.35, scale_x[5]-0.15, scale_x[6]-0.25, scale_x[7]-0.65, scale_x[8]-0.7]

plt.xticks(xlabel_loc,scale_x_label,fontsize=50,rotation=20)




# added label in fig
plt.text(6.63,3.8 , str(simulation_error[0])+'%',fontsize=50)
plt.text(7.63,7.2 , str(simulation_error[1])+'%',fontsize=50)
plt.text(8.63,2.8, str(simulation_error[2])+'%',fontsize=50)
plt.text(9.63,8.15 , str(simulation_error[3])+'%',fontsize=50)
plt.text(10.63,2.3 , str(simulation_error[4])+'%',fontsize=50)
plt.text(11.63,4.8, str(simulation_error[5])+'%',fontsize=50)
plt.text(12.63,6.5, str(simulation_error[6])+'%',fontsize=50)
plt.text(13.63,6.7 , str(simulation_error[7])+'%',fontsize=50)
plt.text(14.59,15.46, str(simulation_error[8])+'%',fontsize=50)





plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1.125
#
# legend = plt.legend(workloads, bbox_to_anchor=(1.02, 1.05), fontsize=45, ncol=1, columnspacing=0.2,borderpad = 0.1, labelspacing = 0.5, handletextpad = 0.1 , frameon=False)
#



plt.tight_layout()
plt.savefig('sim_error.pdf', bbox_inches='tight',pad_inches=0.0)
plt.show()