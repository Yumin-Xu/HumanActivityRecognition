import math

import numpy as np
import pandas as pd

import OpenData_watch_accel
import OpenData_watch_gyro


def if_in_count_watch_accel(x, c):
    data1 = OpenData_watch_accel.csv_new_file(x)
    count = data1['label'].value_counts()
    if c in count:
        return data1[data1['label'] == c]
    else:
        data = pd.DataFrame(np.array([[data1['id'].loc[0], c, 0, 0, 0, 0], [data1['id'].loc[0], c, 1, 1, 1, 1]]),
                            columns=['id', 'label', 'time', 'x', 'y', 'z'])
        data['id'] = data['id'].astype(float)
        data['time'] = data['time'].astype(float)
        data['x'] = data['x'].astype(float)
        data['y'] = data['y'].astype(float)
        data['z'] = data['z'].astype(float)
        return data


def if_in_count_watch_gyro(x, c):
    data2 = OpenData_watch_gyro.csv_new_file(x)
    count = data2['label'].value_counts()
    if c in count:
        return data2[data2['label'] == c]
    else:
        data = pd.DataFrame(np.array([[data2['id'].loc[0], c, 0, 0, 0, 0], [data2['id'].loc[0], c, 1, 1, 1, 1]]),
                            columns=['id', 'label', 'time', 'x', 'y', 'z'])
        data['id'] = data['id'].astype(float)
        data['time'] = data['time'].astype(float)
        data['x'] = data['x'].astype(float)
        data['y'] = data['y'].astype(float)
        data['z'] = data['z'].astype(float)
        return data


def create_word_watch_accel_x(x, c):
    data1 = if_in_count_watch_accel(x, c)

    x1_data1 = pd.array(data1['x'].loc[data1.index[1]: data1.index[len(data1) - 1]])
    x2_data1 = pd.array(data1['x'].loc[data1.index[0]: data1.index[len(data1) - 2]])
    time1_data1 = pd.array(data1['time'].loc[data1.index[1]: data1.index[len(data1) - 1]])
    time2_data1 = pd.array(data1['time'].loc[data1.index[0]: data1.index[len(data1) - 2]])
    array1 = pd.array(x1_data1 - x2_data1)
    array_time_data1 = pd.array(time1_data1 - time2_data1)
    if 0 in array_time_data1:
        result_data1 = array1 * array_time_data1
    else:
        result_data1 = array1 / array_time_data1

    #for item in range(len(result_data1)):
    #   if result_data1[item] > 0:
    #       result_data1[item] = math.log(result_data1[item], math.e)
    #   elif result_data1[item] == 0:
    #       result_data1[item] = 0
    #   elif result_data1[item] < 0:
    #       result_data1[item] = math.fabs(math.log(math.fabs(result_data1[item]), math.e))
    return result_data1


def create_word_watch_gyro_x(x, c):
    data2 = if_in_count_watch_gyro(x, c)

    x1_data2 = pd.array(data2['x'].loc[data2.index[1]: data2.index[len(data2) - 1]])
    x2_data2 = pd.array(data2['x'].loc[data2.index[0]: data2.index[len(data2) - 2]])
    time1_data2 = pd.array(data2['time'].loc[data2.index[1]: data2.index[len(data2) - 1]])
    time2_data2 = pd.array(data2['time'].loc[data2.index[0]: data2.index[len(data2) - 2]])
    array2 = pd.array(x1_data2 - x2_data2)
    array_time_data2 = pd.array(time1_data2 - time2_data2)
    if 0 in array_time_data2:
        result_data2 = array2 * array_time_data2
    else:
        result_data2 = array2 / array_time_data2

    #for item in range(len(result_data2)):
    #   if result_data2[item] > 0:
    #        result_data2[item] = math.log(result_data2[item], math.e)
    #   elif result_data2[item] == 0:
    #       result_data2[item] = 0
    #    elif result_data2[item] < 0:
    #        result_data2[item] = math.fabs(math.log(math.fabs(result_data2[item]), math.e))
    # prfloat(result_data2)
    return result_data2



