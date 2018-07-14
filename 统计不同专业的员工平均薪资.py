'''
* 题目描述：统计不同专业背景的员工的平均薪资，并用柱状图显示结果 

* 题目要求: 
* 使用Pandas进行数据分析及可视化 

* 数据文件： 
* 数据源下载地址：https://video.mugglecode.com/data_employee.zip，下载压缩包后解压即可 
* employee_info.csv，包含了员工的基本信息，共4列数据，分别表示： 
1. EmployeeNumber: 员工编号 
2. Age: 年龄 
3. Department: 所处部门 
4. MonthlyIncome: 月收入 

* employee_edu.csv，包含部分员工的专业背景，共2列数据： 
* EmployeeNumber: 员工编号 
* EducationField: 专业背景
'''
import os
import pandas as pd
import matplotlib.pyplot as plt

datafile_path1 = 'data/data_employee/employee_edu.csv'
datafile_path2 = 'data/data_employee/employee_info.csv'

# 结果保存路径
output_path = 'output'
if not os.path.exists(output_path):
    os.makedirs(output_path)


def collect_data():
    """
        数据获取
    """
    edu_data_df = pd.read_csv(datafile_path1)
    info_data_df = pd.read_csv(datafile_path2)
    return edu_data_df, info_data_df


def inspect_data(edu_data_df, info_data_df):
    """
        查看数据
    """
    print('数据一共有{}行，{}列'.format(edu_data_df.shape[0], edu_data_df.shape[1]))

    print('数据预览：')
    print(edu_data_df.head())

    print('数据基本信息：')
    print(edu_data_df.info())

    print('数据统计信息：')
    print(edu_data_df.describe())

    print('数据一共有{}行，{}列'.format(info_data_df.shape[0], info_data_df.shape[1]))

    print('数据预览：')
    print(info_data_df.head())

    print('数据基本信息：')
    print(info_data_df.info())

    print('数据统计信息：')
    print(info_data_df.describe())


def process_data(edu_data_df, info_data_df):
    merged_data_df = pd.merge(edu_data_df, info_data_df, how='inner', on='EmployeeNumber')

    mean_income_ser = merged_data_df.groupby('EducationField')['MonthlyIncome'].mean()

    mean_income_ser.plot(kind='bar',rot=45)
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    edu_data_df, info_data_df = collect_data()
    inspect_data(edu_data_df, info_data_df)
    process_data(edu_data_df, info_data_df)
