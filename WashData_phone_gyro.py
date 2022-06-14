import pandas as pd

import OpenData_phone_gyro
import clean_z_phone_gyro


def label_count_phone_gyro(x):
    count = OpenData_phone_gyro.csv_file(x)['label'].value_counts()
    return count


def label_A_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'A'].head(count[0])
    return label_data


def label_B_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'B'].head(count[0])
    return label_data


def label_C_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'C'].head(count[0])
    #    print(label_data)
    return label_data


def label_D_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'D'].head(count[0])
    return label_data


def label_E_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    label_data = data[data['label'] == 'E'].head(count[0])
    return label_data


def label_F_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'F'].head(count[0])
    return label_data


def label_G_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'G'].head(count[0])
    return label_data


def label_H_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'H'].head(count[0])
    return label_data


def label_I_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'I'].head(count[0])
    return label_data


def label_J_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'J'].head(count[0])
    return label_data


def label_K_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'K'].head(count[0])
    return label_data


def label_L_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'L'].head(count[0])
    return label_data


def label_M_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'M'].head(count[0])
    return label_data


def label_N_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'N'].head(count[0])
    return label_data


def label_O_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'O'].head(count[0])
    #    print(label_data)
    return label_data


def label_P_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'P'].head(count[0])
    #    print(label_data)
    return label_data


def label_Q_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'Q'].head(count[0])
    #    print(label_data)
    return label_data


def label_R_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'R'].head(count[0])
    #    print(label_data)
    return label_data


def label_S_select_phone_gyro(x):
    data = clean_z_phone_gyro.clean_z(x)
    count = label_count_phone_gyro(x)
    count = sorted(count)
    label_data = data[data['label'] == 'S'].head(count[0])
    return label_data


def label_sample_phone_gyro(x):
    if 'A' in label_count_phone_gyro(x):
        data1 = label_A_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data1 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'B' in label_count_phone_gyro(x):
        data2 = label_B_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data2 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'C' in label_count_phone_gyro(x):
        data3 = label_C_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data3 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'D' in label_count_phone_gyro(x):
        data4 = label_D_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data4 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'E' in label_count_phone_gyro(x):
        data5 = label_E_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data5 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'F' in label_count_phone_gyro(x):
        data6 = label_F_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data6 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'G' in label_count_phone_gyro(x):
        data7 = label_G_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data7 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'H' in label_count_phone_gyro(x):
        data8 = label_H_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data8 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'I' in label_count_phone_gyro(x):
        data9 = label_I_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data9 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'J' in label_count_phone_gyro(x):
        data10 = label_J_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data10 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'K' in label_count_phone_gyro(x):
        data11 = label_K_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data11 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'L' in label_count_phone_gyro(x):
        data12 = label_L_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data12 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'M' in label_count_phone_gyro(x):
        data13 = label_M_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data13 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'N' in label_count_phone_gyro(x):
        data14 = label_N_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data14 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'O' in label_count_phone_gyro(x):
        data15 = label_O_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data15 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'P' in label_count_phone_gyro(x):
        data16 = label_P_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data16 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'Q' in label_count_phone_gyro(x):
        data17 = label_Q_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data17 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'R' in label_count_phone_gyro(x):
        data18 = label_R_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data18 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    if 'S' in label_count_phone_gyro(x):
        data19 = label_S_select_phone_gyro(x).sort_values(by=['time'])
    else:
        data19 = pd.DataFrame(columns=['id', 'label', 'time', 'x', 'y', 'z'])

    data = pd.concat([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10,
                      data11, data12, data13, data14, data15, data16, data17, data18, data19], ignore_index=True)
    return data


def convert_string_to_num(x):
    data_original = label_sample_phone_gyro(x)
    for item in range(len(data_original)):
        data_original['z'].loc[item] = data_original['z'].loc[item][0:len(data_original['z'].loc[item]) - 2]
    data_converted = pd.to_numeric(data_original['z'])
    data_original['z'] = data_converted
    print(data_original)
    return data_original
