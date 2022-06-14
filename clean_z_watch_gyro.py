import pandas as pd

import OpenData_watch_gyro


def clean_z(x):
    data = OpenData_watch_gyro.csv_file(x)
    s = pd.Series(data['z'])
    for x in range(0, len(data)):
        if 'E' in s.loc[x]:
            s = s.replace(s.loc[x], '0')
        if 'e' in s.loc[x]:
            s = s.replace(s.loc[x], '0')
    data['z'] = s
    data = data[data['z'] != '0']
    return data
