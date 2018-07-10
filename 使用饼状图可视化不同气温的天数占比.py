# 麻瓜编程
# 练习
# 3. 练习：使用饼状图可视化不同气温的天数占比
# * 题目描述：将1-3个月份的气温数据进行合并，并使用饼状图可视化所有数据的零上气温和零下气温的天数占比情况。
#
# * 题目要求:
# * 使用NumPy进行数组合并
# * 使用Matplotlib进行可视化
#
# * 数据文件：
# * 数据源下载地址：https://video.mugglecode.com/data_temp.zip，下载压缩包后解压即可
# * 201801_temp.csv、201802_temp.csv、201803_temp.csv分别包含了2018年1-3月北京的气温（每日的最低温度）。每行记录为1天的数据。
# * 每个文件中只包含一列气温数据：temperature为摄氏温度

'''
* 问题拆解提示：
1. 如何使用NumPy读取csv数据文件？
2. 如何使用NumPy进行数组合并？
3. 如何构造布尔型数组并进行过滤？
4. 如何进行饼状图可视化占比？
* 问题解决提示：
1. 利用NumPy模块中的loadtxt()(https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html)方法读取csv数据文件，需要指定2个参数的值
* delimiter=','：csv文件的数据分隔符，默认为空格；
* skiprows=1：跳过第一行（表头），默认为0，表示数据包含第一行；
* 可以不指定dtype参数。由于csv中的数据全部可以转换为float类型，所以dtype使用默认的float即可；
2. 使用NumPy模块中的concatenate()(https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.concatenate.html)方法进行数组合并，其中参数为包含多个数组的序列。
3. 使用一列数据和0做比较，构造布尔型数组；将布尔型数组放在向量的索引操作中；
4. 使用Matplotlib提供的pie()(https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html)进行饼状图可视化。
'''
import numpy as np
import os
import matplotlib.pyplot as plt

data_path = './data/data_temp'
filename = ['201801_temp.csv', '201802_temp.csv', '201803_temp.csv']


def collect_data():
    data_list = []
    for f in filename:
        filepath = os.path.join(data_path, f)
        data = np.loadtxt(filepath, dtype=float, delimiter=',', skiprows=1)
        data_list.append(data)
    return np.concatenate(data_list, 0)


def process_data(data):
    positive_count = data[data >= 0].shape[0]
    nagetive_count = data[data < 0].shape[0]
    return [positive_count, nagetive_count]


def show_data(data):
    plt.figure()
    plt.pie(data,labels=['>=0','<0'],autopct='%.2f%%',explode=[0.02,0])
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(os.path.join(data_path,'result.png'))
    plt.show()


if __name__ == '__main__':
    data = collect_data()
    processed_data = process_data(data)
    show_data(processed_data)
