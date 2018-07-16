'''
* 题目描述：根据PM2.5值添加对应的等级，统计每年各等级的占比天数,并使用堆叠柱状图进行可视化。等级规则如下：
* 0-50: excellent（优）
* 50-100: good（良）
* 100-500: bad（污染）

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

data_df['Level'] = pd.cut(data_df['PM'], bins=[0, 50, 100, 500], labels=['excellent', 'good', 'bad'])

year_level_count_df = pd.pivot_table(data=data_df, index='Year', columns='Level', values='Day', aggfunc='count')

print(year_level_count_df.head())

year_level_count_df.plot(kind='bar', stacked=True)
plt.title('year_level_count')
plt.show()
