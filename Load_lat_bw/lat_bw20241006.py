import matplotlib.pyplot as plt

# 定义内存访问时延区间的边界
latency_boundaries = [0, 100, 150, 200, 250]  # 假设的边界值

# 定义负载类型
load_conditions = ['Light Load', 'Moderate Overload', 'Optimal Load', 'Severe Overload']

# 创建图形和轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制分隔线
for i in range(len(latency_boundaries) - 1):
    ax.axvline(x=latency_boundaries[i], color='gray', linestyle='--', linewidth=0.7)

# 绘制区域
for i in range(len(latency_boundaries) - 1):
    ax.fill_between([latency_boundaries[i], latency_boundaries[i+1]],
                    -0.5, 0.5, label=load_conditions[i], alpha=0.3)

# 标注负载类型
for i, condition in enumerate(load_conditions):
    ax.text((latency_boundaries[i] + latency_boundaries[i+1]) * 0.5, -0.3, condition,
            ha='center', va='center', fontsize=10, rotation=90)

# 设置y轴的显示范围
ax.set_ylim(-0.5, 0.5)

# 隐藏y轴的刻度
ax.yaxis.set_visible(False)

# 隐藏x轴的刻度
ax.xaxis.set_ticks([])

# 隐藏右侧和上侧的边框线
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# 移动左侧的边框线
ax.spines['left'].set_position(('data', 0))

# 设置标题
ax.set_title('Memory Access Latency vs. Load Conditions')
ax.set_xlabel("Used Memory Bandwidth")
ax.set_ylabel("Memory Access Latency")

# 显示图例
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# 显示图形
plt.show()