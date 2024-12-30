import matplotlib.pyplot as plt
import numpy as np

# Data in MB/s
data = {
    'ALL Reads': [27.1905/32, 18.6342/25.6, 27.1200/32, 18.6979/25.6],
    '3:1 Reads-Writes': [27.5420/32, 15.1509/25.6, 27.4878/32, 15.1767/25.6],
    '2:1 Reads-Writes': [25.9865/32, 13.9413/25.6, 25.6206/32, 13.9308/25.6],
    '1:1 Reads-Writes': [21.1466/32, 13.2267/25.6, 21.1327/32, 13.1184/25.6],
    'Stream-triad like': [25.0379/32, 13.4177/25.6, 25.0407/32, 13.4150/25.6]
}

# Convert MB/s to GB/s
for key in data:
    data[key] = [x for x in data[key]]

# Plotting the data with low saturation colors
labels = list(data.keys())
DDR_Local = [data[key][0] for key in data]
DDR_Remote = [data[key][2] for key in data]
CXL_Local = [data[key][1] for key in data]
CXL_Remote = [data[key][3] for key in data]

x = np.arange(len(labels))
width = 0.2

fig, ax = plt.subplots(figsize=(17, 5))
rects1 = ax.bar(x - 1.5*width, DDR_Local, width, label='DDR Local', color='lightblue')
rects2 = ax.bar(x - 0.5*width, DDR_Remote, width, label='DDR Remote', color='lightgreen')
rects3 = ax.bar(x + 0.5*width, CXL_Local, width, label='CXL Local', color='lightsalmon')
rects4 = ax.bar(x + 1.5*width, CXL_Remote, width, label='CXL Remote', color='lightcoral')


ax.set_ylabel('Bandwidth Efficiency')
ax.set_xlabel('Read/Write Ratio')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.title("MLC with various read and write ratios")

plt.savefig("bw.png")

plt.show()
