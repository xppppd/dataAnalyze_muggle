# * 题目描述：统计1-3月气温在-10℃~10℃的天数统计直方图
#
# * 题目要求:
# * 使用NumPy进行直方图统计
# * 使用Matplotlib进行直返图绘制
#
# * 数据文件：
# * 数据源下载地址：https://video.mugglecode.com/temp2.csv（数据源与第二节练习相同）
# * temp2.csv，包含了2018年1-3月北京的气温（每日的最低温度）。每行记录为1天的数据。
# * 共2列数据，第1列month为月份，第2列temperature为摄氏温度

import numpy as np
import os
import matplotlib.pyplot as plt

file_name = 'data/data_temp/temp.csv'
d_range = (-10, 10)
d_bins = 10


def collect_and_process_data():
    data = np.loadtxt(file_name, dtype=str, delimiter=',', skiprows=1)
    data = np.core.defchararray.replace(data, ' C', '')
    data = data.astype('int')
    bool_arr1 = []
    bool_arr2 = []
    bool_arr3 = []
    for i in data[:, 0]:
        bool_arr1.append(i == 1)
        bool_arr2.append(i == 2)
        bool_arr3.append(i == 3)
    month1_data = data[bool_arr1]
    month2_data = data[bool_arr2]
    month3_data = data[bool_arr3]
    # print(month1_data[0])
    # print(month1_data[1])
    return [month1_data, month2_data, month3_data]


def show_data(data_list):
    stats, edgs = np.histogram(data_list[2], range=d_range, bins=d_bins)
    print(stats)
    print(edgs)

    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2, sharey=ax1)
    ax3 = fig.add_subplot(1, 3, 3, sharey=ax1)

    ax1.hist(data_list[0], range=d_range, bins=d_bins, stacked=True)
    ax1.set_xticks(edgs)
    ax1.set_title('1')
    ax1.set_ylabel('Count')

    ax2.hist(data_list[1], range=d_range, bins=d_bins, stacked=True)
    ax2.set_xticks(edgs)
    ax2.set_title('2')
    ax2.set_ylabel('Count')

    ax3.hist(data_list[2], range=d_range, bins=d_bins, stacked=True,facecolor='g')
    ax3.set_xticks(edgs)
    ax3.set_title('3')
    ax3.set_ylabel('Count')
    ax3.set_yticks(range(0, 36, 5))

    plt.tight_layout()
    plt.savefig('result.png')
    plt.show()


def main():
    data = np.loadtxt(file_name, dtype=str, delimiter=',', skiprows=1)
    data = np.core.defchararray.replace(data, ' C', '')
    data_arr = data.astype('int')

    # 1. 统计直方图所需信息
    # 气温数据
    temp_arr = data_arr[:, 1]

    # 统计的数据范围范围
    hist_range = (-10, 10)

    # 分桶个数
    n_bins = 5

    # 2. 直方图统计
    stats, bin_edges = np.histogram(temp_arr, range=hist_range, bins=n_bins)
    print('气温直方图统计信息：{}, 直方图分组边界:{}'.format(stats, bin_edges))

    # 3. 可视化直方图
    plt.figure()
    plt.hist(temp_arr, range=hist_range, bins=n_bins)
    # 设置x轴坐标点显示为分组边界
    plt.xticks(bin_edges)
    plt.show()


if __name__ == '__main__':
    data = collect_and_process_data()
    show_data(data)
    # 读取csv数据文件
