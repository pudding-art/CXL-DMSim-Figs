import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(4.5,4))
sns.set_style("whitegrid", {"font.sans_serif":["simhei", "Arial"]}) # 白色单线格，且展示中文
sns.set(font="simhei")#遇到标签需要汉字的可以在绘图前加上这句

# print(type(np.random.rand(4,4)))


percentage_data = [
    [63.39, 63.55, 43.48, 40.03],
    [27.03, 63.70, 32.71, 43.85],
    [41.23, 41.22, 72.62, 72.55],
    [45.71, 50.73, 33.69, 72.31]
]



df = pd.DataFrame(
    np.array(percentage_data),
    index = ["Seq \n Read","Rand \nRead","Seq \nWrite","Rand \nWrite"],
    columns = ["Seq \nRead","Rand \nRead","Seq \nWrite","Rand \nWrite"]
)
sns.set(font_scale=1.5)  # 修改字体比例
# plt.rc('font',family='Times New Roman',size=12)
cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8,as_cmap = True)

ax = sns.heatmap(df, linewidths=5,annot=True, linecolor='white',annot_kws={'size':15,'weight':'bold', 'color':'black'},
                 fmt=".2f", vmax= 100,center=50 ,cmap = "OrRd_r",square=True,
                 cbar_kws={"shrink": 1.0, 'pad':0.015,"ticks":[0,10,20,30,40,50,60,70,80,90,100]})  # 颜色刻度条的设置)

# 获取颜色刻度条对象
cbar = ax.collections[0].colorbar
cbar_ax = cbar.ax

# 设置颜色刻度条的边框颜色和线宽
cbar_ax.spines['top'].set_visible(True)
cbar_ax.spines['right'].set_visible(True)
cbar_ax.spines['bottom'].set_visible(True)
cbar_ax.spines['left'].set_linewidth(2)
cbar_ax.spines['left'].set_edgecolor('black')
cbar.ax.tick_params(labelsize=15)


"""
data：矩阵数据集，可以使numpy的数组（array），如果是pandas的dataframe，则df的index/column信息会分别对应到heatmap的columns和rows
vmax,vmin, 图例中最大值和最小值的显示值，没有该参数时默认不显示
linewidths,热力图矩阵之间的间隔大小
cmap，热力图颜色
ax，绘制图的坐标轴，否则使用当前活动的坐标轴。
annot，annotate的缩写，annot默认为False，当annot为True时，在heatmap中每个方格写入数据。
annot_kws，当annot为True时，可设置各个参数，包括大小，颜色，加粗，斜体字等：
sns.heatmap(x, annot=True, ax=ax2, annot_kws={'size':9,'weight':'bold', 'color':'blue'}) 
fmt，格式设置，决定annot注释的数字格式，小数点后几位等；
cbar : 是否画一个颜色条
cbar_kws : 颜色条的参数，关键字同 fig.colorbar，可以参考：matplotlib自定义colorbar颜色条-以及matplotlib中的内置色条。
mask，遮罩
"""





plt.title("Normalized to Maximum")
plt.xlabel("Workload A")
plt.ylabel("Workload B")

plt.tight_layout()

# plt.show()

plt.savefig('heatmap.pdf', bbox_inches='tight',pad_inches=0.0)