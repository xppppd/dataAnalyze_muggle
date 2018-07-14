'''
* 题目描述：分析房屋价格数据 
1. 通过盒形图可视化不同卧室个数对应的房屋价格的分布 
2. 通过双变量图观察卫生间个数与房屋价格的关系 
3. 通过热图可视化变量间的关系 

* 题目要求: 
* 使用Pandas和Seaborn进行数据分析及可视化 

* 数据文件： 
* 数据源下载地址：https://video.mugglecode.com/house_data.csv 
* house_data.csv，包含了某美国城市的房屋价格。每行记录为单个房屋的数据。 
* 共5列数据，分别表示： 
1. price: 房屋价格，单位：美元 
2. bedrooms: 卧室个数 
3. bathrooms: 卫生间个数 
4. area: 房屋面积，单位：平方米 
5. yr_built：房屋建造的年份
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datafile_path = 'data/data_pd/house_data.csv'


def collect_data():
    """
        数据获取
    """
    data_df = pd.read_csv(datafile_path)
    return data_df


def inspect_data(data_df):
    """
        查看数据
    """
    print('数据一共有{}行，{}列'.format(data_df.shape[0], data_df.shape[1]))

    print('数据预览：')
    print(data_df.head())

    print('数据基本信息：')
    print(data_df.info())

    print('数据统计信息：')
    print(data_df.describe())


def process_data(data_df):
    cln_data = data_df.dropna()

    sns.boxplot(x='bedrooms', y='price', data=cln_data)
    plt.show()

    sns.jointplot(x='bathrooms', y='price', data=cln_data)
    plt.show()

    corr_result = cln_data.corr()
    sns.heatmap(data=corr_result,annot=True)
    plt.show()


if __name__ == '__main__':
    data_df = collect_data()
    inspect_data(data_df)
    process_data(data_df)
