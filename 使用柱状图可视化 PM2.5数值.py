# * 题目要求:
# * 使用Pandas查看数据文件的基本信息
# * 使用Pandas进行数据分析及可视化
#
# * 数据文件：
# * 数据源下载地址：https://video.mugglecode.com/Beijing_PM.csv
# * Beijing_PM.csv，包含了2013-2015年北京每小时的PM2.5值。每行记录为1小时的数据。
# * 共7列数据，分别表示：
# 1. year: 年，2013-2015
# 2. month: 月，1-12
# 3. day: 日，1-31
# 4. hour: 小时，0-23
# 5. season：季度，1-4
# 6. PM_China: 中国环保部检测的PM2.5值
# 7. PM_US: 美国使馆检测的PM2.5值

import os
import pandas as pd
import matplotlib.pyplot as plt


filepath = 'data/data_pd/Beijing_PM.csv'
output_path = 'output'


data_pd = pd.read_csv(filepath)

print('数据基本信息：')
print(data_pd.info())

year_data = data_pd.groupby('year')
year_mean_data = year_data['PM_US'].mean()
print(year_mean_data)

year_mean_data.to_csv(os.path.join(output_path,'Beijing_year_mean.csv'))

year_mean_data.plot(kind='bar')
plt.title('Beijing average PM')
plt.tight_layout()
plt.savefig(os.path.join(output_path,'Beijing_average_PM.png'))
