import os

import WashData_phone_accel


def s_fun(x):
    return str(x)


def new_phone_accel_csv(x):
    data = WashData_phone_accel.convert_string_to_num(x)
    string1 = "/Pycharm/HumanActivityRecognition/phone/new_accel"
    string2 = string1 + "/accel_phone_" + s_fun(x) + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


def new_phone_gyro_csv(x):
    data = WashData_phone_accel.convert_string_to_num(x)
    string1 = "/Pycharm/HumanActivityRecognition/phone/new_gyro"
    string2 = string1 + "/gyro_phone_" + s_fun(x) + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


def new_watch_accel_csv(x):
    data = WashData_phone_accel.convert_string_to_num(x)
    string1 = "/Pycharm/HumanActivityRecognition/watch/new_accel"
    string2 = string1 + "/accel_watch_" + s_fun(x) + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


def new_watch_gyro_csv(x):
    data = WashData_phone_accel.convert_string_to_num(x)
    string1 = "/Pycharm/HumanActivityRecognition/watch/new_gyro"
    string2 = string1 + "/gyro_watch_" + s_fun(x) + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


for num in range(0, 51):
    new_phone_accel_csv(num)
    new_phone_gyro_csv(num)
    new_watch_accel_csv(num)
    new_watch_gyro_csv(num)
