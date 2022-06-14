import pandas as pd

import ReadNewData
import ReadRawData


def path():
    var1 = 0
    file_path = pd.Series(len(ReadRawData.read_data_phone_gyro()))
    for file in range(0, len(ReadRawData.read_data_phone_gyro())):
        file_path[var1] = ReadRawData.read_data_phone_gyro()[file]
        var1 += 1
    return file_path


def select_file(x):
    return path().loc[x]


def string_convert(x):
    string = str(path()[x])
    string = string[0:len(string) - 3] + 'c' + 's' + 'v'
    return string


def open_file(x):
    df = pd.read_csv(select_file(x))
    return df.to_csv(string_convert(x),
                     header=["id", "label", "time", "x", "y", "z"], index=False)


def create_csv():
    for file in range(0, len(ReadRawData.read_data_phone_gyro())):
        open_file(file)


def csv_file(x):
    p = ReadRawData.read_csv_phone_gyro()[x]
    f1 = pd.read_csv(p)
#    print(pd.DataFrame(f1))
    return pd.DataFrame(f1)


def csv_new_file(x):
    p = ReadNewData.read_csv_phone_accel()[x]
    f = pd.read_csv(p, index_col=None)
    f = pd.DataFrame(f)
    sub = {'id': f['id'], 'label': f['label'], 'time': f['time'],
           'x': f['x'], 'y': f['y'], 'z': f['z']}
    data = pd.DataFrame(sub)
    return pd.DataFrame(data)
