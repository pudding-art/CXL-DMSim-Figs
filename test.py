import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.legend_handler import HandlerBase

# 自定义图例渲染器
class LegendHandlerBar(HandlerBase):
    def create_artists(self, legend, orig_handle,
                        x0, y0, width, height, fontsize, trans):
        # 添加颜色框
        line = patches.Rectangle(xy=(x0, y0), width=width, height=height,
                                 facecolor=orig_handle.get_facecolor(),
                                 edgecolor=orig_handle.get_edgecolor())
        legend._legend_box = line   # 将颜色框赋值给_legend_box

        # 添加文字
        text = legend.get_texts()[0]
        text.set_text("Label")      # 设置文字内容
        text.set_color(orig_handle.get_edgecolor())  # 设置文字颜色
        text.set_position((x0, y0))  # 设置文字位置

        return [line, text]

# 注册自定义图例渲染器
plt.legend_handler_map[patches.Rectangle] = LegendHandlerBar()

# 创建一个条形图作为示例
fig, ax = plt.subplots()
bar = ax.bar(1, 1, color='skyblue')

# 添加图例
ax.legend([bar], ['Label'], handler_map={patches.Rectangle: LegendHandlerBar()})

# 显示图表
plt.tight_layout()
plt.show()