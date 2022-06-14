import math

import numpy as np
import pandas as pd

from CreateWord_phone_x import create_word_phone_accel_x, create_word_phone_gyro_x
from CreateWord_phone_y import create_word_phone_accel_y, create_word_phone_gyro_y
from CreateWord_phone_z import create_word_phone_accel_z, create_word_phone_gyro_z
from CreateWord_watch_x import create_word_watch_accel_x, create_word_watch_gyro_x
from CreateWord_watch_y import create_word_watch_accel_y, create_word_watch_gyro_y
from CreateWord_watch_z import create_word_watch_accel_z, create_word_watch_gyro_z


def create_word_phone_accel(x, c):
    d_x = create_word_phone_accel_x(x, c)
    d_y = create_word_phone_accel_y(x, c)
    d_z = create_word_phone_accel_z(x, c)

    for item in range(len(d_x)):
        if d_x[item] > 0:
            d_x[item] = math.log(d_x[item], math.e)
        elif d_x[item] == 0:
            d_x[item] = 0
        elif d_x[item] < 0:
            d_x[item] = math.fabs(math.log(math.fabs(d_x[item]), math.e))
    d_x = np.array(d_x)

    for item in range(len(d_y)):
        if d_y[item] > 0:
            d_y[item] = math.log(d_y[item], math.e)
        elif d_y[item] == 0:
            d_y[item] = 0
        elif d_y[item] < 0:
            d_y[item] = math.fabs(math.log(math.fabs(d_y[item]), math.e))
    d_y = np.array(d_y)

    for item in range(len(d_z)):
        if d_z[item] > 0:
            d_z[item] = math.log(d_z[item], math.e)
        elif d_z[item] == 0:
            d_z[item] = 0
        elif d_z[item] < 0:
            d_z[item] = math.fabs(math.log(math.fabs(d_z[item]), math.e))
    d_z = np.array(d_z)

    collect = {'x': d_x, 'y': d_y, 'z': d_z}
    data = pd.DataFrame(collect)
    # data = pd.array(data)
    # count = pd.DataFrame(data).value_counts()
    return data


def create_word_phone_gyro(x, c):
    d_x = create_word_phone_gyro_x(x, c)
    d_y = create_word_phone_gyro_y(x, c)
    d_z = create_word_phone_gyro_z(x, c)

    for item in range(len(d_x)):
        if d_x[item] > 0:
            d_x[item] = math.log(d_x[item], math.e)
        elif d_x[item] == 0:
            d_x[item] = 0
        elif d_x[item] < 0:
            d_x[item] = math.fabs(math.log(math.fabs(d_x[item]), math.e))
    d_x = np.array(d_x)

    for item in range(len(d_y)):
        if d_y[item] > 0:
            d_y[item] = math.log(d_y[item], math.e)
        elif d_y[item] == 0:
            d_y[item] = 0
        elif d_y[item] < 0:
            d_y[item] = math.fabs(math.log(math.fabs(d_y[item]), math.e))
    d_y = np.array(d_y)

    for item in range(len(d_z)):
        if d_z[item] > 0:
            d_z[item] = math.log(d_z[item], math.e)
        elif d_z[item] == 0:
            d_z[item] = 0
        elif d_z[item] < 0:
            d_z[item] = math.fabs(math.log(math.fabs(d_z[item]), math.e))
    d_z = np.array(d_z)

    collect = {'x': d_x, 'y': d_y, 'z': d_z}
    data = pd.DataFrame(collect)
    # data = pd.array(data)
    # count = pd.DataFrame(data).value_counts()
    return data


def create_word_watch_accel(x, c):
    d_x = create_word_watch_accel_x(x, c)
    d_y = create_word_watch_accel_y(x, c)
    d_z = create_word_watch_accel_z(x, c)

    for item in range(len(d_x)):
        if d_x[item] > 0:
            d_x[item] = math.log(d_x[item], math.e)
        elif d_x[item] == 0:
            d_x[item] = 0
        elif d_x[item] < 0:
            d_x[item] = math.fabs(math.log(math.fabs(d_x[item]), math.e))
    d_x = np.array(d_x)

    for item in range(len(d_y)):
        if d_y[item] > 0:
            d_y[item] = math.log(d_y[item], math.e)
        elif d_y[item] == 0:
            d_y[item] = 0
        elif d_y[item] < 0:
            d_y[item] = math.fabs(math.log(math.fabs(d_y[item]), math.e))
    d_y = np.array(d_y)

    for item in range(len(d_z)):
        if d_z[item] > 0:
            d_z[item] = math.log(d_z[item], math.e)
        elif d_z[item] == 0:
            d_z[item] = 0
        elif d_z[item] < 0:
            d_z[item] = math.fabs(math.log(math.fabs(d_z[item]), math.e))
    d_z = np.array(d_z)

    collect = {'x': d_x, 'y': d_y, 'z': d_z}
    data = pd.DataFrame(collect)
    # data = pd.array(data)
    # count = pd.DataFrame(data).value_counts()
    return data


def create_word_watch_gyro(x, c):
    d_x = create_word_watch_gyro_x(x, c)
    d_y = create_word_watch_gyro_y(x, c)
    d_z = create_word_watch_gyro_z(x, c)

    for item in range(len(d_x)):
        if d_x[item] > 0:
            d_x[item] = math.log(d_x[item], math.e)
        elif d_x[item] == 0:
            d_x[item] = 0
        elif d_x[item] < 0:
            d_x[item] = math.fabs(math.log(math.fabs(d_x[item]), math.e))
    d_x = np.array(d_x)

    for item in range(len(d_y)):
        if d_y[item] > 0:
            d_y[item] = math.log(d_y[item], math.e)
        elif d_y[item] == 0:
            d_y[item] = 0
        elif d_y[item] < 0:
            d_y[item] = math.fabs(math.log(math.fabs(d_y[item]), math.e))
    d_y = np.array(d_y)

    for item in range(len(d_z)):
        if d_z[item] > 0:
            d_z[item] = math.log(d_z[item], math.e)
        elif d_z[item] == 0:
            d_z[item] = 0
        elif d_z[item] < 0:
            d_z[item] = math.fabs(math.log(math.fabs(d_z[item]), math.e))
    d_z = np.array(d_z)

    collect = {'x': d_x, 'y': d_y, 'z': d_z}
    data = pd.DataFrame(collect)
    # data = pd.array(data)

    # count = pd.DataFrame(data).value_counts()
    return data


def create_word(x, c):
    d1 = create_word_phone_accel(x, c)
    d2 = create_word_phone_gyro(x, c)
    d3 = create_word_watch_accel(x, c)
    d4 = create_word_watch_gyro(x, c)

    t = np.arange(len(d1))
    var = 0
    for item in range(len(d1)):
        x = np.dot(d1.loc[item], d2.loc[item])
        y = np.dot(x, d3.loc[item])
        t[var] = np.dot(y, d4.loc[item])
        var += 1
    data = pd.DataFrame({'label': c, 'words': pd.DataFrame(np.sort(np.array(pd.DataFrame(t))))[0]})
    return data


print(create_word(0, 'A'))
