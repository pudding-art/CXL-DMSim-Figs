import matplotlib.pyplot as plt
import numpy as np

# MB/s
native = [898.77, 1293.79, 716.11, 904.26, 1158.40, 939, 1045, 1106, 1216, 906, 756, 915, 783.15, 913.23, 811.59, 903.67, 909.88, 902.94, 824.51, 777.01, 747.01, 708.16, 691.2, 758.72]
modified = [908.66, 1206.81, 781.56, 905.88, 1258.59, 1152.03, 1230.94, 1259.82, 1288.53, 1153.23, 900, 1047, 1047.66, 933.13, 950.72, 1039.49, 1143.09, 1220.67, 1255.29, 1273.10, 1293.45, 1224.90, 1124.52, 1042.93]

# Generate more intermediate points between existing data points
times_native = np.linspace(5, 120, len(native) * 3)
times_modified = np.linspace(5, 120, len(modified) * 3)

# Use numpy's interp function to interpolate data points
native_interpolated = np.interp(times_native, np.arange(5, 121, 5), native)
modified_interpolated = np.interp(times_modified, np.arange(5, 121, 5), modified)

interval = 5
color = ['#f58231', '#4363d8', '#a9a9a9', '#469990']

plt.figure(figsize=(15, 3.5))

# Plot read latency
plt.plot(times_native, native_interpolated, marker='^', markerfacecolor='white', markeredgewidth=2, label='Native', color=color[1])
plt.plot(times_modified, modified_interpolated, marker='o', markerfacecolor='white', markeredgewidth=2, label='Modified', color=color[0])

# y_ticks
y_ticks = [0, 200, 400, 600, 800, 1000, 1200, 1400]
plt.yticks(y_ticks, [str(y_tick) for y_tick in y_ticks], fontsize=20)

# x_ticks
plt.xticks(np.arange(5, 121, 5), fontsize=20)
plt.xlabel('Execution Time(s)', fontsize=20)
plt.ylabel('Throughput (MB/s)', fontsize=20)

plt.legend(bbox_to_anchor=(1.0, 0.5), frameon=False, fontsize=20)

plt.axvline(x=20, linestyle='--', color='red')

plt.tight_layout()
plt.savefig('graph500.pdf', bbox_inches='tight',pad_inches=0.0)
# plt.show()