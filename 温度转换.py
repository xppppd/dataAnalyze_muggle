import os
import numpy

file_name = 'data/data_temp/temp.csv'


def get_data():
    file_path = os.path.join(os.path.curdir, file_name)
    data_arr = numpy.loadtxt(file_path, delimiter=',', dtype='str', skiprows=1)
    return data_arr


# f = 1.8 *c + 32
def trans_data(data_arr):
    c_temp_str = data_arr[:, 1]
    c_temp = numpy.core.defchararray.replace(c_temp_str, 'C', '')
    f_temp = c_temp.astype('float') * 1.8 + 32
    print('摄氏温度数据：')
    print(c_temp)

    print('转换后的华氏温度数据：')
    print(f_temp)


def main():
    data_arr = get_data()
    trans_data(data_arr)


if __name__ == '__main__':
    main()
