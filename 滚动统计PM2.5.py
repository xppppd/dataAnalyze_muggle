'''
* 题目描述：滚动统计PM2.5指标的3日均值、5日均值、7日均值，并对结果进行可视化

* 题目要求:
* 使用Pandas进行数据分析及可视化

* 数据文件：
* 数据源下载地址：https://video.mugglecode.com/pm1.csv
* pm1.csv，包含了2013-2015年某地区每小时的PM2.5值。每行记录为1小时的数据。
* 共2列数据，分别表示：
1. Timestamp: 年月日及小时
2. PM: PM2.5值
'''

import pandas as pd
import matplotlib.pyplot as plt

filename_path = 'data/data_pd/pm1.csv'

data_df = pd.read_csv(filename_path)
data_df.dropna(inplace=True)
print('基本信息：')
print(data_df.head())
print(data_df.info())
print(data_df.describe())

data_df['Timestamp'] = pd.to_datetime(data_df['Timestamp'])
data_df.set_index('Timestamp',inplace=True)
resample_data_df = data_df.resample('D').mean()
print(resample_data_df.head())

resample_data_df['M 3'] = resample_data_df['PM'].rolling(window=3).mean()
resample_data_df['M 5'] = resample_data_df['PM'].rolling(window=5).mean()
resample_data_df['M 7'] = resample_data_df['PM'].rolling(window=7).mean()

resample_data_df[['M 3','M 5','M 7']].plot()
plt.tight_layout()
plt.show()