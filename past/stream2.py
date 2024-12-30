import matplotlib.pyplot as plt
data="""Smallest time delta is    9.5367431640625000E-007
     Size  Iter     FILL      COPY     DAXPY       DOT
       30     3  25546.1   96605.1   72378.1   63362.5     101.5
       48     3  27660.6  132010.6   76662.1   69660.2      68.7
       77     3  29157.1  113335.5   78088.3   70421.9      45.1
      123     3  30242.0  152813.1   79338.5   71056.9      29.3
      197     3  31019.1  186591.6   80482.3   72996.5      18.8
      315     3  23738.7  147547.3   66831.6   73389.2       9.0
      504     3  28159.6  200549.3   72384.6   73791.5       6.7
      806     3  29110.8  227245.6   75168.8   74127.4       4.3
     1290     3  30293.8  237748.8   77720.4   72505.4       2.8
     2063     3  30699.9  244805.0   79218.5   73125.1       1.8
     3302     3  31181.4   89384.5   69833.1   61974.0       1.1
     5283     3  31419.9   52519.7   59480.0   45764.4       0.7
     8454     3  31591.6   53442.6   59462.7   45844.9       0.4
    13528     3  31663.4   54382.2   59438.1   45912.2       0.3
    21647     3  31697.1   54837.3   59510.5   45947.9       0.2
    34639     3  31770.8   55323.0   59616.6   45872.8       0.1
    55428     3  31850.4   55233.7   59693.3   45848.3       0.1
    88694     3  31853.1   55357.8   59718.1   45859.7       0.0
   141925     3  31849.5   31243.8   43792.7   32384.5       0.0
   227102     3  26441.0   32160.1   30052.0   21553.9       0.0
   363400     3  19929.3   27966.1   29242.5   20954.5       0.0
   581498     3  24633.6   28496.9   38293.8   27762.5       0.0
   930489     3  24506.8   28362.4   36884.1   27132.6       0.0
  1488931     3  23637.3   27862.9   24212.6   17744.5       0.0
  2382526     3  18902.5   27027.5   14398.5   10890.9       0.0
  3812421     3   8566.5   24559.1   10644.7    8073.4       0.0
  6100481     3   4759.4   16300.9    9065.5    6911.6       0.0
  9761740     3   4171.4   13281.5    8441.5    6447.3       0.0
 15620338     3   3845.6   11848.3    8032.5    6158.4       0.0
 24995027     3   3730.1   10922.5    7752.2    5861.7       0.0
 39996021     3   3674.6   10590.1    7664.9    5817.3       0.0
 64000000     3   3647.2   10494.9    7574.7    5843.1       0.0
 """

# 将数据按行分割
lines = data.strip().split('\n')

# 提取Size和带宽数据
sizes = []
fill_bandwidth = []
copy_bandwidth = []
daxpy_bandwidth = []
dot_bandwidth = []

for line in lines[2:]:
    values = line.split()
    sizes.append(int(values[0]))
    fill_bandwidth.append(float(values[2]) / 1000)  # MB/s to GB/s
    copy_bandwidth.append(float(values[3]) / 1000)
    daxpy_bandwidth.append(float(values[4]) / 1000)
    dot_bandwidth.append(float(values[5]) / 1000)

print("************************")
print("*****fill_bandwidth******")
print(fill_bandwidth)

print("************************")
print("*****copy_bandwidth******")
print(copy_bandwidth)


print("************************")
print("*****daxpy_bandwidth******")
print(daxpy_bandwidth)


print("************************")
print("*****dot_bandwidth******")
print(dot_bandwidth)

print(sizes)
# 绘制折线图
plt.figure(figsize=(20, 6))
plt.plot(range(1, len(sizes) + 1), fill_bandwidth, marker='o', label='FILL')
plt.plot(range(1, len(sizes) + 1), copy_bandwidth, marker='o', label='COPY')
plt.plot(range(1, len(sizes) + 1), daxpy_bandwidth, marker='o', label='DAXPY')
plt.plot(range(1, len(sizes) + 1), dot_bandwidth, marker='o', label='DOT')

# 设置横坐标刻度和标签
plt.xticks(range(1, len(sizes) + 1, 3), sizes[::3])

# 设置图例、标题和标签
plt.legend()
plt.title('Stream2 CXL Local Bandwidth vs Size')
plt.xlabel('Size')
plt.ylabel('Bandwidth (GB/s)')

# 显示网格
plt.grid(True)

# 显示图形
# plt.show()
plt.savefig("stream2_local.png")