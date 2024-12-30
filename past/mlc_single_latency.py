import matplotlib.pyplot as plt

# 定义内存类型和操作延迟数据
memory_types = ['DDR Local', 'DDR Remote(NUMA)', 'CXL Local']
load_delays = [253, 311, 512]
store_delays = [447, 631, 930]
nt_store_delays = [223, 364, 360]

# 创建一个大图，包含三个子图
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# 绘制load操作延迟柱状图
axs[0].bar(memory_types, load_delays, color=['#E8E8B9', '#BCBD46', '#A5DFE7'])
axs[0].set_xlabel('Memory Type')
axs[0].set_ylabel('Delay (ns)')
axs[0].set_title('Load Operation Delay')
axs[0].grid(axis='y')
axs[0].legend(memory_types)

# 绘制store操作延迟柱状图
axs[1].bar(memory_types, store_delays, color=['#E8E8B9', '#BCBD46', '#A5DFE7'])
axs[1].set_xlabel('Memory Type')
axs[1].set_ylabel('Delay (ns)')
axs[1].set_title('Store Operation Delay')
axs[1].grid(axis='y')
axs[1].legend(memory_types)

# 绘制nt-store操作延迟柱状图
axs[2].bar(memory_types, nt_store_delays, color=['#E8E8B9', '#BCBD46', '#A5DFE7'])
axs[2].set_xlabel('Memory Type')
axs[2].set_ylabel('Delay (ns)')
axs[2].set_title('Non-Temporal Store Operation Delay')
axs[2].grid(axis='y')
axs[2].legend(memory_types)

plt.tight_layout()
# plt.show()
plt.savefig("memo.png")