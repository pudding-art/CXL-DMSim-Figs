import matplotlib.pyplot as plt
import numpy as np



# xsbench large 48 cores

lat_large48=[2.380, 1.335,2.639, 2.380, 2.274, 4.475,2.380, 1.792, 3.611]
bw_large48=[7143634, 12737765,  6442406,7143634,7476090,3779083,  9409012,7143634, 4707603]

# xsbench small 48 cores
lat_small48=[0.260,0.243,  0.278, 0.260,0.365, 0.294, 0.272,0.260, 0.315]
bw_small48=[65348256,  69939373,61183032, 65348256, 57770821,46534362,  62539989, 65348256, 54051200]

# xsbench small 12 cores
lat_small12=[0.883, 0.921,0.952, 0.883,1.059, 1.261, 0.883, 0.964, 1.075]
bw_small12=[19248361,  18457454,17850973, 19248361,16047329,13476047,  19248361, 17626882,15816355]


memory_config = [ 'DDR-L', 'DDR-L+DDR-R','DDR-R', 'DDR-L','CXL FPGA','DDR-L+CXL FPGA','DDR-L', 'DDR-L+CXL ASIC','CXL ASIC']


# Plotting
plt.figure(figsize=(12, 6))

# Latency Line Plot
plt.subplot(1, 2, 1)
index = range(len(memory_config))
bar_width = 0.3
plt.bar(index, lat_large48, bar_width, label='Large 48 Cores')
plt.bar([i + bar_width for i in index], lat_small48, bar_width, label='Small 48 Cores')
plt.bar([i + 2*bar_width for i in index], lat_small12, bar_width, label='Small 12 Cores')
plt.xticks([i + bar_width for i in index], memory_config, rotation=45)
plt.xticks(rotation=45)
plt.xlabel('Memory Configuration')
plt.ylabel('Latency (s)')
plt.title('Latency Comparison')
plt.legend()

# Bandwidth Bar Plot
plt.subplot(1, 2, 2)
bar_width = 0.3
index = range(len(memory_config))
plt.bar(index, bw_large48, bar_width, label='Large 48 Cores')
plt.bar([i + bar_width for i in index], bw_small48, bar_width, label='Small 48 Cores')
plt.bar([i + 2*bar_width for i in index], bw_small12, bar_width, label='Small 12 Cores')
plt.xticks([i + bar_width for i in index], memory_config, rotation=45)
plt.xlabel('Memory Configuration')
plt.ylabel('Bandwidth')
plt.title('Bandwidth Comparison')
plt.legend()

plt.tight_layout()
plt.show()