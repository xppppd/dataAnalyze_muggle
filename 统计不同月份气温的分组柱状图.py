'''
5. 练习：统计不同气温的分组柱状图
* 题目描述：绘制1-3月的每月零上气温和零下气温天数的分组柱状图 

* 题目要求: 
* 使用Matplotlib进行分组柱状图的绘制 

* 数据文件： 
* 数据源下载地址：https://video.mugglecode.com/temp2.csv（数据源与第二节练习相同） 
* temp2.csv，包含了2018年1-3月北京的气温（每日的最低温度）。每行记录为1天的数据。 
* 共2列数据，第1列month为月份，第2列temperature为摄氏温度 
'''

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# mac系统获取中文字体
def get_chinese_font():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


filename = './data/data_temp/temp2.csv'
output_path = './output'

if not os.path.exists(output_path):
    os.makedirs(output_path)


def collect_process_data():
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    positive_data = []
    nagetive_data = []
    for i in range(3):
        month_data = data[data[:, 0] == i + 1]
        positive_data.append(month_data[month_data[:, 1] >= 0].shape[0])
        nagetive_data.append(month_data[month_data[:, 1] < 0].shape[0])
    return (positive_data, nagetive_data)


def show_data(data):
    bar_locs = np.arange(3)
    bar_width = 0.35  # 柱子宽度
    xtick_labels = ['{}月份'.format(i + 1) for i in range(3)]
    positve_data = data[0]
    nagetive_data = data[1]
    plt.figure()
    plt.bar(bar_locs, positve_data, width=bar_width, color='r', alpha=0.7, label='零上')
    plt.bar(bar_locs + bar_width, nagetive_data, width=bar_width, color='g', alpha=0.7, label='零下')
    plt.xticks(bar_locs + bar_width / 2, xtick_labels, rotation=45, fontproperties=get_chinese_font())
    plt.ylabel('单位：天', fontproperties=get_chinese_font())
    plt.title('零上零下气温天数', fontproperties=get_chinese_font())
    plt.legend(loc='best', prop=get_chinese_font())

    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'temp_count.png'))
    plt.show()


if __name__ == '__main__':
    data = collect_process_data()
    show_data(data)
