import matplotlib.pyplot as plt

# 定义块大小和P99延迟值
block_sizes = ['4k', '8k', '16k', '32k', '64k', '128k', '256k', '512k']
p99_latency_ddr = [233, 359, 627, 1172, 2245, 4228, 8717, 19006]
p99_latency_cxl = [285, 474, 832, 1582, 3032, 5932, 12125, 30016]

# 创建柱状图
plt.figure(figsize=(15, 6))
bar_width = 0.35
index = range(len(block_sizes))

plt.bar(index, p99_latency_ddr, bar_width, color="",label='DDR Local')
plt.bar([i + bar_width for i in index], p99_latency_cxl, bar_width, label='CXL Local')

plt.xlabel('Block Size (Bytes)')
plt.ylabel('P99 Latency (us)')
plt.title('P99 Latency values of FIO for various block sizes')
plt.xticks([i + bar_width/2 for i in index], block_sizes)
plt.yscale('log')  # 使用对数刻度显示y轴
plt.yticks([1, 10, 100, 1000, 10000], ['1', '10', '100', '1000', '10000'])

plt.legend()
plt.show()
