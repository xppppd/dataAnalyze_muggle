'''
* 题目描述：对PM2.5值按年月两列进行统计分析,并使用分组柱状图可视化分析结果

* 题目要求:
* 使用Pandas进行数据分析及可视化

* 数据文件：
* 数据源下载地址：https://video.mugglecode.com/pm2.csv
* pm2.csv，包含了2013-2015年某地区每天的PM2.5值。每行记录为1天的数据。
* 共4列数据，分别表示：
1. Year: 年
2. Month: 月
3. Day: 日
4. PM: PM2.5值
'''

import pandas as pd
import matplotlib.pyplot as plt

filename_path = 'data/data_pd/pm2.csv'

data_df = pd.read_csv(filename_path)

print('数据基本信息：')
print(data_df.head())
print(data_df.info())
print(data_df.describe())
print(data_df.shape)

year_month_data = data_df.groupby(by=['Year', 'Month'])['PM'].mean()

pivot_results = pd.pivot_table(data_df, index='Year', columns='Month',
                               values=['PM'], aggfunc='mean')

pivot_results.plot(kind='bar')
plt.legend(loc='best')
plt.tight_layout()
plt.show()
