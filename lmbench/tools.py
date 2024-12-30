


data_dict = {}
with open('data.txt', 'r') as file:
    for line in file:
        # 使用 split() 方法分割每一行，默认以空格为分隔符
        parts = line.strip().split()
        print(parts)
        if len(parts) == 2:  # 确保行中有两个部分
            key, value = parts
            # print(key)
            # print(value)
            # data_dict[float(key)] = float(value)  # 将字符串转换为浮点数
            data_dict[key] = value;
            print(data_dict[key])


specified_keys = [
    "0.00049", "0.00098", "0.00195", "0.00391", "0.00781", "0.01562", "0.03125", "0.04688",
    "0.09375", "0.18750", "0.37500", "0.75000", "1.00000", "1.50000", "2.00000", "3.00000",
    "4.00000", "6.00000", "8.00000", "12.00000", "16.00000", "24.00000", "32.00000", "48.00000",
    "64.00000", "96.00000", "128.00000", "192.00000", "256.00000", "384.00000", "512.00000",
    "768.00000", "1024.00000"
]

extracted_value = [ data_dict[key] for key in specified_keys]
print(extracted_value)
print(len(extracted_value))


"""
random read pattern
remote_numa 
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.528', '5.530', '6.891', '7.948', '7.948', '9.222', '16.030', '32.677', '39.516', '40.512', '44.969', '47.605', '48.788', '48.759', '51.412', '52.824', '57.331', '81.600', '123.150', '154.635', '174.327', '191.862', '195.603', '205.608', '216.556']

local ddr
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.530', '5.529', '6.728', '7.817', '8.418', '12.616', '19.553', '32.448', '39.265', '40.857', '45.775', '47.592', '49.394', '48.068', '49.929', '51.641', '57.727', '67.711', '89.340', '114.098', '120.938', '125.775', '131.057', '132.879', '137.527']

cxl-asic
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.529', '5.882', '7.117', '7.948', '7.949', '7.950', '8.123', '37.006', '38.152', '39.971', '43.852', '48.189', '48.501', '49.188', '49.275', '49.086', '50.277', '69.638', '121.049', '182.023', '213.302', '246.628', '264.098', '273.723', '283.118']

seq read pattern
remote numa
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.473', '5.471', '5.471', '5.529', '5.529', '6.750', '17.684', '28.285', '34.328', '35.210', '35.938', '34.773', '35.711', '34.772', '35.704', '37.608', '39.727', '56.906', '91.678', '148.216', '165.063', '179.765', '184.496', '188.242', '193.660']

local ddr
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.473', '5.472', '5.471', '5.532', '5.532', '6.307', '14.260', '29.070', '35.758', '34.960', '35.968', '34.491', '35.725', '34.499', '34.791', '37.042', '37.891', '51.086', '67.546', '96.613', '99.075', '106.990', '107.159', '113.084', '114.094']

cxl-asic
['1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.728', '1.729', '5.473', '5.471', '5.471', '5.530', '5.530', '5.532', '5.621', '34.648', '35.276', '36.178', '35.040', '35.712', '34.780', '35.708', '34.778', '35.707', '35.856', '62.978', '101.362', '160.892', '188.615', '218.716', '229.925', '245.020', '250.151']
"""


"""
gem5

rand read pattern
local ddr
['1.832', '1.832', '1.832', '1.832', '1.817', '1.813', '1.811', '4.494', '6.409', '6.408', '6.408', '7.339', '7.365', '11.515', '22.056', '36.033', '40.413', '45.328', '48.197', '50.029', '50.340', '50.442', '50.433', '50.454', '50.449', '63.258', '99.758', '123.203', '129.660', '133.772', '135.046', '135.886', '136.168']



seq read pattern without prefetch mechanism
local ddr
['1.832', '1.832', '1.832', '1.832', '1.817', '1.813', '1.808', '1.812', '6.410', '6.409', '6.408', '6.408', '6.408', '6.408', '10.108', '49.516', '49.516', '49.517', '49.517', '49.517', '49.517', '49.517', '49.519', '49.517', '49.517', '49.784', '137.353', '136.347', '135.921', '135.460', '135.202', '134.990', '134.864']

cxl-asic
['1.832', '1.832', '1.832', '1.832', '1.818', '1.813', '1.808', '1.812', '6.410', '6.409', '6.409', '6.408', '6.408', '6.408', '11.636', '49.516', '49.516', '49.517', '49.516', '49.517', '49.517', '49.517', '49.516', '49.516', '49.517', '50.331', '286.889', '286.886', '286.859', '286.896', '286.883', '286.884', '286.885']

"""