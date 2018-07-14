'''
1. 添加一列diff用于比较中国环保部和美国使馆检测的PM2.5值的差异（两列数据的绝对值差） 
2. 找出差别最大的10天的记录 
3. 使用分组柱状图比较中国环保部和美国使馆检测的每年平均PM2.5的值 

* 题目要求: 
* 使用Pandas进行数据分析及可视化 

* 数据文件： 
* 数据源下载地址：https://video.mugglecode.com/Beijing_PM.csv （数据源与上节课相同） 
* Beijing_PM.csv，包含了2013-2015年北京每小时的PM2.5值。每行记录为1小时的数据。 
* 共7列数据，分别表示： 
1. year: 年，2013-2015 
2. month: 月，1-12 
3. day: 日，1-31 
4. hour: 小时，0-23 
5. season：季度，1-4 
6. PM_China: 中国环保部检测的PM2.5值 
7. PM_US: 美国使馆检测的PM2.5值
'''

import os
import pandas as pd
import matplotlib.pyplot as plt

filepath = 'data/data_pd/Beijing_PM.csv'
output_path = 'output'

data_pd = pd.read_csv(filepath)

print('数据基本信息：')
print(data_pd.info())
print(data_pd.head())
print(data_pd.describe())

cln_data_pd = data_pd.dropna(inplace=False).copy()

cln_data_pd['diff'] = abs(cln_data_pd['PM_China'] - cln_data_pd['PM_US'])

top_10_diff_data = cln_data_pd.sort_values(by='diff', ascending=False).head(10)
print('差别最大的10条数据')
print(top_10_diff_data)

year_mean_data = cln_data_pd.groupby('year')[['PM_China', 'PM_US']].mean()

year_mean_data.plot(kind='bar')
plt.tight_layout()
plt.show()
