import os

import numpy as np
import pandas as pd

from CreateWord import create_word


def check_if_Bin(x, y):
    d = create_word(x, 'B')['words']
    word_to_keep = np.array(create_word(y, 'B')['words'])
    df = pd.DataFrame(np.array(d[d.isin(word_to_keep)]), columns=['words'])
    return df


def check_B0():
    data = pd.concat([check_if_Bin(0, 1), check_if_Bin(0, 2), check_if_Bin(0, 3), check_if_Bin(0, 4),
                      check_if_Bin(0, 5), check_if_Bin(0, 6), check_if_Bin(0, 7), check_if_Bin(0, 8),
                      check_if_Bin(0, 9), check_if_Bin(0, 10), check_if_Bin(0, 11), check_if_Bin(0, 12),
                      check_if_Bin(0, 13), check_if_Bin(0, 14), check_if_Bin(0, 15), check_if_Bin(0, 16),
                      check_if_Bin(0, 17), check_if_Bin(0, 18), check_if_Bin(0, 19), check_if_Bin(0, 20),
                      check_if_Bin(0, 21), check_if_Bin(0, 22), check_if_Bin(0, 23), check_if_Bin(0, 24),
                      check_if_Bin(0, 25), check_if_Bin(0, 26), check_if_Bin(0, 27), check_if_Bin(0, 28),
                      check_if_Bin(0, 29), check_if_Bin(0, 30), check_if_Bin(0, 31), check_if_Bin(0, 32),
                      check_if_Bin(0, 33), check_if_Bin(0, 34), check_if_Bin(0, 35), check_if_Bin(0, 36),
                      check_if_Bin(0, 37), check_if_Bin(0, 38), check_if_Bin(0, 39), check_if_Bin(0, 40),
                      check_if_Bin(0, 41), check_if_Bin(0, 42), check_if_Bin(0, 43), check_if_Bin(0, 44),
                      check_if_Bin(0, 45), check_if_Bin(0, 46), check_if_Bin(0, 47), check_if_Bin(0, 48),
                      check_if_Bin(0, 49), check_if_Bin(0, 50)], ignore_index=True)
    print('0', data)
    return data


def check_B1():
    data = pd.concat([check_if_Bin(1, 0), check_if_Bin(1, 2), check_if_Bin(1, 3), check_if_Bin(1, 4),
                      check_if_Bin(1, 5), check_if_Bin(1, 6), check_if_Bin(1, 7), check_if_Bin(1, 8),
                      check_if_Bin(1, 9), check_if_Bin(1, 10), check_if_Bin(1, 11), check_if_Bin(1, 12),
                      check_if_Bin(1, 13), check_if_Bin(1, 14), check_if_Bin(1, 15), check_if_Bin(1, 16),
                      check_if_Bin(1, 17), check_if_Bin(1, 18), check_if_Bin(1, 19), check_if_Bin(1, 20),
                      check_if_Bin(1, 21), check_if_Bin(1, 22), check_if_Bin(1, 23), check_if_Bin(1, 24),
                      check_if_Bin(1, 25), check_if_Bin(1, 26), check_if_Bin(1, 27), check_if_Bin(1, 28),
                      check_if_Bin(1, 29), check_if_Bin(1, 30), check_if_Bin(1, 31), check_if_Bin(1, 32),
                      check_if_Bin(1, 33), check_if_Bin(1, 34), check_if_Bin(1, 35), check_if_Bin(1, 36),
                      check_if_Bin(1, 37), check_if_Bin(1, 38), check_if_Bin(1, 39), check_if_Bin(1, 40),
                      check_if_Bin(1, 41), check_if_Bin(1, 42), check_if_Bin(1, 43), check_if_Bin(1, 44),
                      check_if_Bin(1, 45), check_if_Bin(1, 46), check_if_Bin(1, 47), check_if_Bin(1, 48),
                      check_if_Bin(1, 49), check_if_Bin(1, 50)], ignore_index=True)
    print('1', data)
    return data


def check_B2():
    data = pd.concat([check_if_Bin(2, 0), check_if_Bin(2, 1), check_if_Bin(2, 3), check_if_Bin(2, 4),
                      check_if_Bin(2, 5), check_if_Bin(2, 6), check_if_Bin(2, 7), check_if_Bin(2, 8),
                      check_if_Bin(2, 9), check_if_Bin(2, 10), check_if_Bin(2, 11), check_if_Bin(2, 12),
                      check_if_Bin(2, 13), check_if_Bin(2, 14), check_if_Bin(2, 15), check_if_Bin(2, 16),
                      check_if_Bin(2, 17), check_if_Bin(2, 18), check_if_Bin(2, 19), check_if_Bin(2, 20),
                      check_if_Bin(2, 21), check_if_Bin(2, 22), check_if_Bin(2, 23), check_if_Bin(2, 24),
                      check_if_Bin(2, 25), check_if_Bin(2, 26), check_if_Bin(2, 27), check_if_Bin(2, 28),
                      check_if_Bin(2, 29), check_if_Bin(2, 30), check_if_Bin(2, 31), check_if_Bin(2, 32),
                      check_if_Bin(2, 33), check_if_Bin(2, 34), check_if_Bin(2, 35), check_if_Bin(2, 36),
                      check_if_Bin(2, 37), check_if_Bin(2, 38), check_if_Bin(2, 39), check_if_Bin(2, 40),
                      check_if_Bin(2, 41), check_if_Bin(2, 42), check_if_Bin(2, 43), check_if_Bin(2, 44),
                      check_if_Bin(2, 45), check_if_Bin(2, 46), check_if_Bin(2, 47), check_if_Bin(2, 48),
                      check_if_Bin(2, 49), check_if_Bin(2, 50)], ignore_index=True)
    print(data)
    return data


def check_B3():
    data = pd.concat([check_if_Bin(3, 0), check_if_Bin(3, 1), check_if_Bin(3, 2), check_if_Bin(3, 4),
                      check_if_Bin(3, 5), check_if_Bin(3, 6), check_if_Bin(3, 7), check_if_Bin(3, 8),
                      check_if_Bin(3, 9), check_if_Bin(3, 10), check_if_Bin(3, 11), check_if_Bin(3, 12),
                      check_if_Bin(3, 13), check_if_Bin(3, 14), check_if_Bin(3, 15), check_if_Bin(3, 16),
                      check_if_Bin(3, 17), check_if_Bin(3, 18), check_if_Bin(3, 19), check_if_Bin(3, 20),
                      check_if_Bin(3, 21), check_if_Bin(3, 22), check_if_Bin(3, 23), check_if_Bin(3, 24),
                      check_if_Bin(3, 25), check_if_Bin(3, 26), check_if_Bin(3, 27), check_if_Bin(3, 28),
                      check_if_Bin(3, 29), check_if_Bin(3, 30), check_if_Bin(3, 31), check_if_Bin(3, 32),
                      check_if_Bin(3, 33), check_if_Bin(3, 34), check_if_Bin(3, 35), check_if_Bin(3, 36),
                      check_if_Bin(3, 37), check_if_Bin(3, 38), check_if_Bin(3, 39), check_if_Bin(3, 40),
                      check_if_Bin(3, 41), check_if_Bin(3, 42), check_if_Bin(3, 43), check_if_Bin(3, 44),
                      check_if_Bin(3, 45), check_if_Bin(3, 46), check_if_Bin(3, 47), check_if_Bin(3, 48),
                      check_if_Bin(3, 49), check_if_Bin(3, 50)], ignore_index=True)
    print(data)
    return data


def check_B4():
    data = pd.concat([check_if_Bin(4, 0), check_if_Bin(4, 1), check_if_Bin(4, 2), check_if_Bin(4, 3),
                      check_if_Bin(4, 5), check_if_Bin(4, 6), check_if_Bin(4, 7), check_if_Bin(4, 8),
                      check_if_Bin(4, 9), check_if_Bin(4, 10), check_if_Bin(4, 11), check_if_Bin(4, 12),
                      check_if_Bin(4, 13), check_if_Bin(4, 14), check_if_Bin(4, 15), check_if_Bin(4, 16),
                      check_if_Bin(4, 17), check_if_Bin(4, 18), check_if_Bin(4, 19), check_if_Bin(4, 20),
                      check_if_Bin(4, 21), check_if_Bin(4, 22), check_if_Bin(4, 23), check_if_Bin(4, 24),
                      check_if_Bin(4, 25), check_if_Bin(4, 26), check_if_Bin(4, 27), check_if_Bin(4, 28),
                      check_if_Bin(4, 29), check_if_Bin(4, 30), check_if_Bin(4, 31), check_if_Bin(4, 32),
                      check_if_Bin(4, 33), check_if_Bin(4, 34), check_if_Bin(4, 35), check_if_Bin(4, 36),
                      check_if_Bin(4, 37), check_if_Bin(4, 38), check_if_Bin(4, 39), check_if_Bin(4, 40),
                      check_if_Bin(4, 41), check_if_Bin(4, 42), check_if_Bin(4, 43), check_if_Bin(4, 44),
                      check_if_Bin(4, 45), check_if_Bin(4, 46), check_if_Bin(4, 47), check_if_Bin(4, 48),
                      check_if_Bin(4, 49), check_if_Bin(4, 50)], ignore_index=True)
    print(data)
    return data


def check_B5():
    data = pd.concat([check_if_Bin(5, 0), check_if_Bin(5, 1), check_if_Bin(5, 2), check_if_Bin(5, 3),
                      check_if_Bin(5, 4), check_if_Bin(5, 6), check_if_Bin(5, 7), check_if_Bin(5, 8),
                      check_if_Bin(5, 9), check_if_Bin(5, 10), check_if_Bin(5, 11), check_if_Bin(5, 12),
                      check_if_Bin(5, 13), check_if_Bin(5, 14), check_if_Bin(5, 15), check_if_Bin(5, 16),
                      check_if_Bin(5, 17), check_if_Bin(5, 18), check_if_Bin(5, 19), check_if_Bin(5, 20),
                      check_if_Bin(5, 21), check_if_Bin(5, 22), check_if_Bin(5, 23), check_if_Bin(5, 24),
                      check_if_Bin(5, 25), check_if_Bin(5, 26), check_if_Bin(5, 27), check_if_Bin(5, 28),
                      check_if_Bin(5, 29), check_if_Bin(5, 30), check_if_Bin(5, 31), check_if_Bin(5, 32),
                      check_if_Bin(5, 33), check_if_Bin(5, 34), check_if_Bin(5, 35), check_if_Bin(5, 36),
                      check_if_Bin(5, 37), check_if_Bin(5, 38), check_if_Bin(5, 39), check_if_Bin(5, 40),
                      check_if_Bin(5, 41), check_if_Bin(5, 42), check_if_Bin(5, 43), check_if_Bin(5, 44),
                      check_if_Bin(5, 45), check_if_Bin(5, 46), check_if_Bin(5, 47), check_if_Bin(5, 48),
                      check_if_Bin(5, 49), check_if_Bin(5, 50)], ignore_index=True)
    print(data)
    return data


def check_B6():
    data = pd.concat([check_if_Bin(6, 0), check_if_Bin(6, 1), check_if_Bin(6, 2), check_if_Bin(6, 3),
                      check_if_Bin(6, 4), check_if_Bin(6, 5), check_if_Bin(6, 7), check_if_Bin(6, 8),
                      check_if_Bin(6, 9), check_if_Bin(6, 10), check_if_Bin(6, 11), check_if_Bin(6, 12),
                      check_if_Bin(6, 13), check_if_Bin(6, 14), check_if_Bin(6, 15), check_if_Bin(6, 16),
                      check_if_Bin(6, 17), check_if_Bin(6, 18), check_if_Bin(6, 19), check_if_Bin(6, 20),
                      check_if_Bin(6, 21), check_if_Bin(6, 22), check_if_Bin(6, 23), check_if_Bin(6, 24),
                      check_if_Bin(6, 25), check_if_Bin(6, 26), check_if_Bin(6, 27), check_if_Bin(6, 28),
                      check_if_Bin(6, 29), check_if_Bin(6, 30), check_if_Bin(6, 31), check_if_Bin(6, 32),
                      check_if_Bin(6, 33), check_if_Bin(6, 34), check_if_Bin(6, 35), check_if_Bin(6, 36),
                      check_if_Bin(6, 37), check_if_Bin(6, 38), check_if_Bin(6, 39), check_if_Bin(6, 40),
                      check_if_Bin(6, 41), check_if_Bin(6, 42), check_if_Bin(6, 43), check_if_Bin(6, 44),
                      check_if_Bin(6, 45), check_if_Bin(6, 46), check_if_Bin(6, 47), check_if_Bin(6, 48),
                      check_if_Bin(6, 49), check_if_Bin(6, 50)], ignore_index=True)
    print(data)
    return data


def check_B7():
    data = pd.concat([check_if_Bin(7, 0), check_if_Bin(7, 1), check_if_Bin(7, 2), check_if_Bin(7, 3),
                      check_if_Bin(7, 4), check_if_Bin(7, 5), check_if_Bin(7, 6), check_if_Bin(7, 8),
                      check_if_Bin(7, 9), check_if_Bin(7, 10), check_if_Bin(7, 11), check_if_Bin(7, 12),
                      check_if_Bin(7, 13), check_if_Bin(7, 14), check_if_Bin(7, 15), check_if_Bin(7, 16),
                      check_if_Bin(7, 17), check_if_Bin(7, 18), check_if_Bin(7, 19), check_if_Bin(7, 20),
                      check_if_Bin(7, 21), check_if_Bin(7, 22), check_if_Bin(7, 23), check_if_Bin(7, 24),
                      check_if_Bin(7, 25), check_if_Bin(7, 26), check_if_Bin(7, 27), check_if_Bin(7, 28),
                      check_if_Bin(7, 29), check_if_Bin(7, 30), check_if_Bin(7, 31), check_if_Bin(7, 32),
                      check_if_Bin(7, 33), check_if_Bin(7, 34), check_if_Bin(7, 35), check_if_Bin(7, 36),
                      check_if_Bin(7, 37), check_if_Bin(7, 38), check_if_Bin(7, 39), check_if_Bin(7, 40),
                      check_if_Bin(7, 41), check_if_Bin(7, 42), check_if_Bin(7, 43), check_if_Bin(7, 44),
                      check_if_Bin(7, 45), check_if_Bin(7, 46), check_if_Bin(7, 47), check_if_Bin(7, 48),
                      check_if_Bin(7, 49), check_if_Bin(7, 50)], ignore_index=True)
    print(data)
    return data


def check_B8():
    data = pd.concat([check_if_Bin(8, 0), check_if_Bin(8, 1), check_if_Bin(8, 2), check_if_Bin(8, 3),
                      check_if_Bin(8, 4), check_if_Bin(8, 5), check_if_Bin(8, 6), check_if_Bin(8, 7),
                      check_if_Bin(8, 9), check_if_Bin(8, 10), check_if_Bin(8, 11), check_if_Bin(8, 12),
                      check_if_Bin(8, 13), check_if_Bin(8, 14), check_if_Bin(8, 15), check_if_Bin(8, 16),
                      check_if_Bin(8, 17), check_if_Bin(8, 18), check_if_Bin(8, 19), check_if_Bin(8, 20),
                      check_if_Bin(8, 21), check_if_Bin(8, 22), check_if_Bin(8, 23), check_if_Bin(8, 24),
                      check_if_Bin(8, 25), check_if_Bin(8, 26), check_if_Bin(8, 27), check_if_Bin(8, 28),
                      check_if_Bin(8, 29), check_if_Bin(8, 30), check_if_Bin(8, 31), check_if_Bin(8, 32),
                      check_if_Bin(8, 33), check_if_Bin(8, 34), check_if_Bin(8, 35), check_if_Bin(8, 36),
                      check_if_Bin(8, 37), check_if_Bin(8, 38), check_if_Bin(8, 39), check_if_Bin(8, 40),
                      check_if_Bin(8, 41), check_if_Bin(8, 42), check_if_Bin(8, 43), check_if_Bin(8, 44),
                      check_if_Bin(8, 45), check_if_Bin(8, 46), check_if_Bin(8, 47), check_if_Bin(8, 48),
                      check_if_Bin(8, 49), check_if_Bin(8, 50)], ignore_index=True)
    print(data)
    return data


def check_B9():
    data = pd.concat([check_if_Bin(9, 0), check_if_Bin(9, 1), check_if_Bin(9, 2), check_if_Bin(9, 3),
                      check_if_Bin(9, 4), check_if_Bin(9, 5), check_if_Bin(9, 6), check_if_Bin(9, 7),
                      check_if_Bin(9, 8), check_if_Bin(9, 10), check_if_Bin(9, 11), check_if_Bin(9, 12),
                      check_if_Bin(9, 13), check_if_Bin(9, 14), check_if_Bin(9, 15), check_if_Bin(9, 16),
                      check_if_Bin(9, 17), check_if_Bin(9, 18), check_if_Bin(9, 19), check_if_Bin(9, 20),
                      check_if_Bin(9, 21), check_if_Bin(9, 22), check_if_Bin(9, 23), check_if_Bin(9, 24),
                      check_if_Bin(9, 25), check_if_Bin(9, 26), check_if_Bin(9, 27), check_if_Bin(9, 28),
                      check_if_Bin(9, 29), check_if_Bin(9, 30), check_if_Bin(9, 31), check_if_Bin(9, 32),
                      check_if_Bin(9, 33), check_if_Bin(9, 34), check_if_Bin(9, 35), check_if_Bin(9, 36),
                      check_if_Bin(9, 37), check_if_Bin(9, 38), check_if_Bin(9, 39), check_if_Bin(9, 40),
                      check_if_Bin(9, 41), check_if_Bin(9, 42), check_if_Bin(9, 43), check_if_Bin(9, 44),
                      check_if_Bin(9, 45), check_if_Bin(9, 46), check_if_Bin(9, 47), check_if_Bin(9, 48),
                      check_if_Bin(9, 49), check_if_Bin(9, 50)], ignore_index=True)
    print(data)
    return data


def check_B10():
    data = pd.concat([check_if_Bin(10, 0), check_if_Bin(10, 1), check_if_Bin(10, 2), check_if_Bin(10, 3),
                      check_if_Bin(10, 4), check_if_Bin(10, 5), check_if_Bin(10, 6), check_if_Bin(10, 7),
                      check_if_Bin(10, 8), check_if_Bin(10, 9), check_if_Bin(10, 11), check_if_Bin(10, 12),
                      check_if_Bin(10, 13), check_if_Bin(10, 14), check_if_Bin(10, 15), check_if_Bin(10, 16),
                      check_if_Bin(10, 17), check_if_Bin(10, 18), check_if_Bin(10, 19), check_if_Bin(10, 20),
                      check_if_Bin(10, 21), check_if_Bin(10, 22), check_if_Bin(10, 23), check_if_Bin(10, 24),
                      check_if_Bin(10, 25), check_if_Bin(10, 26), check_if_Bin(10, 27), check_if_Bin(10, 28),
                      check_if_Bin(10, 29), check_if_Bin(10, 30), check_if_Bin(10, 31), check_if_Bin(10, 32),
                      check_if_Bin(10, 33), check_if_Bin(10, 34), check_if_Bin(10, 35), check_if_Bin(10, 36),
                      check_if_Bin(10, 37), check_if_Bin(10, 38), check_if_Bin(10, 39), check_if_Bin(10, 40),
                      check_if_Bin(10, 41), check_if_Bin(10, 42), check_if_Bin(10, 43), check_if_Bin(10, 44),
                      check_if_Bin(10, 45), check_if_Bin(10, 46), check_if_Bin(10, 47), check_if_Bin(10, 48),
                      check_if_Bin(10, 49), check_if_Bin(10, 50)], ignore_index=True)
    print('10', data)
    return data


def check_B11():
    data = pd.concat([check_if_Bin(11, 0), check_if_Bin(11, 1), check_if_Bin(11, 2), check_if_Bin(11, 3),
                      check_if_Bin(11, 4), check_if_Bin(11, 5), check_if_Bin(11, 6), check_if_Bin(11, 7),
                      check_if_Bin(11, 8), check_if_Bin(11, 9), check_if_Bin(11, 10), check_if_Bin(11, 12),
                      check_if_Bin(11, 13), check_if_Bin(11, 14), check_if_Bin(11, 15), check_if_Bin(11, 16),
                      check_if_Bin(11, 17), check_if_Bin(11, 18), check_if_Bin(11, 19), check_if_Bin(11, 20),
                      check_if_Bin(11, 21), check_if_Bin(11, 22), check_if_Bin(11, 23), check_if_Bin(11, 24),
                      check_if_Bin(11, 25), check_if_Bin(11, 26), check_if_Bin(11, 27), check_if_Bin(11, 28),
                      check_if_Bin(11, 29), check_if_Bin(11, 30), check_if_Bin(11, 31), check_if_Bin(11, 32),
                      check_if_Bin(11, 33), check_if_Bin(11, 34), check_if_Bin(11, 35), check_if_Bin(11, 36),
                      check_if_Bin(11, 37), check_if_Bin(11, 38), check_if_Bin(11, 39), check_if_Bin(11, 40),
                      check_if_Bin(11, 41), check_if_Bin(11, 42), check_if_Bin(11, 43), check_if_Bin(11, 44),
                      check_if_Bin(11, 45), check_if_Bin(11, 46), check_if_Bin(11, 47), check_if_Bin(11, 48),
                      check_if_Bin(11, 49), check_if_Bin(11, 50)], ignore_index=True)
    print(data)
    return data


def check_B12():
    data = pd.concat([check_if_Bin(12, 0), check_if_Bin(12, 1), check_if_Bin(12, 2), check_if_Bin(12, 3),
                      check_if_Bin(12, 4), check_if_Bin(12, 5), check_if_Bin(12, 6), check_if_Bin(12, 7),
                      check_if_Bin(12, 8), check_if_Bin(12, 9), check_if_Bin(12, 10), check_if_Bin(12, 11),
                      check_if_Bin(12, 13), check_if_Bin(12, 14), check_if_Bin(12, 15), check_if_Bin(12, 16),
                      check_if_Bin(12, 17), check_if_Bin(12, 18), check_if_Bin(12, 19), check_if_Bin(12, 20),
                      check_if_Bin(12, 21), check_if_Bin(12, 22), check_if_Bin(12, 23), check_if_Bin(12, 24),
                      check_if_Bin(12, 25), check_if_Bin(12, 26), check_if_Bin(12, 27), check_if_Bin(12, 28),
                      check_if_Bin(12, 29), check_if_Bin(12, 30), check_if_Bin(12, 31), check_if_Bin(12, 32),
                      check_if_Bin(12, 33), check_if_Bin(12, 34), check_if_Bin(12, 35), check_if_Bin(12, 36),
                      check_if_Bin(12, 37), check_if_Bin(12, 38), check_if_Bin(12, 39), check_if_Bin(12, 40),
                      check_if_Bin(12, 41), check_if_Bin(12, 42), check_if_Bin(12, 43), check_if_Bin(12, 44),
                      check_if_Bin(12, 45), check_if_Bin(12, 46), check_if_Bin(12, 47), check_if_Bin(12, 48),
                      check_if_Bin(12, 49), check_if_Bin(12, 50)], ignore_index=True)
    print(data)
    return data


def check_B13():
    data = pd.concat([check_if_Bin(13, 0), check_if_Bin(13, 1), check_if_Bin(13, 2), check_if_Bin(13, 3),
                      check_if_Bin(13, 4), check_if_Bin(13, 5), check_if_Bin(13, 6), check_if_Bin(13, 7),
                      check_if_Bin(13, 8), check_if_Bin(13, 9), check_if_Bin(13, 10), check_if_Bin(13, 11),
                      check_if_Bin(13, 12), check_if_Bin(13, 14), check_if_Bin(13, 15), check_if_Bin(13, 16),
                      check_if_Bin(13, 17), check_if_Bin(13, 18), check_if_Bin(13, 19), check_if_Bin(13, 20),
                      check_if_Bin(13, 21), check_if_Bin(13, 22), check_if_Bin(13, 23), check_if_Bin(13, 24),
                      check_if_Bin(13, 25), check_if_Bin(13, 26), check_if_Bin(13, 27), check_if_Bin(13, 28),
                      check_if_Bin(13, 29), check_if_Bin(13, 30), check_if_Bin(13, 31), check_if_Bin(13, 32),
                      check_if_Bin(13, 33), check_if_Bin(13, 34), check_if_Bin(13, 35), check_if_Bin(13, 36),
                      check_if_Bin(13, 37), check_if_Bin(13, 38), check_if_Bin(13, 39), check_if_Bin(13, 40),
                      check_if_Bin(13, 41), check_if_Bin(13, 42), check_if_Bin(13, 43), check_if_Bin(13, 44),
                      check_if_Bin(13, 45), check_if_Bin(13, 46), check_if_Bin(13, 47), check_if_Bin(13, 48),
                      check_if_Bin(13, 49), check_if_Bin(13, 50)], ignore_index=True)
    print(data)
    return data


def check_B14():
    data = pd.concat([check_if_Bin(14, 0), check_if_Bin(14, 1), check_if_Bin(14, 2), check_if_Bin(14, 3),
                      check_if_Bin(14, 4), check_if_Bin(14, 5), check_if_Bin(14, 6), check_if_Bin(14, 7),
                      check_if_Bin(14, 8), check_if_Bin(14, 9), check_if_Bin(14, 10), check_if_Bin(14, 11),
                      check_if_Bin(14, 12), check_if_Bin(14, 13), check_if_Bin(14, 15), check_if_Bin(14, 16),
                      check_if_Bin(14, 17), check_if_Bin(14, 18), check_if_Bin(14, 19), check_if_Bin(14, 20),
                      check_if_Bin(14, 21), check_if_Bin(14, 22), check_if_Bin(14, 23), check_if_Bin(14, 24),
                      check_if_Bin(14, 25), check_if_Bin(14, 26), check_if_Bin(14, 27), check_if_Bin(14, 28),
                      check_if_Bin(14, 29), check_if_Bin(14, 30), check_if_Bin(14, 31), check_if_Bin(14, 32),
                      check_if_Bin(14, 33), check_if_Bin(14, 34), check_if_Bin(14, 35), check_if_Bin(14, 36),
                      check_if_Bin(14, 37), check_if_Bin(14, 38), check_if_Bin(14, 39), check_if_Bin(14, 40),
                      check_if_Bin(14, 41), check_if_Bin(14, 42), check_if_Bin(14, 43), check_if_Bin(14, 44),
                      check_if_Bin(14, 45), check_if_Bin(14, 46), check_if_Bin(14, 47), check_if_Bin(14, 48),
                      check_if_Bin(14, 49), check_if_Bin(14, 50)], ignore_index=True)
    print(data)
    return data


def check_B15():
    data = pd.concat([check_if_Bin(15, 0), check_if_Bin(15, 1), check_if_Bin(15, 2), check_if_Bin(15, 3),
                      check_if_Bin(15, 4), check_if_Bin(15, 5), check_if_Bin(15, 6), check_if_Bin(15, 7),
                      check_if_Bin(15, 8), check_if_Bin(15, 9), check_if_Bin(15, 10), check_if_Bin(15, 11),
                      check_if_Bin(15, 12), check_if_Bin(15, 13), check_if_Bin(15, 14), check_if_Bin(15, 16),
                      check_if_Bin(15, 17), check_if_Bin(15, 18), check_if_Bin(15, 19), check_if_Bin(15, 20),
                      check_if_Bin(15, 21), check_if_Bin(15, 22), check_if_Bin(15, 23), check_if_Bin(15, 24),
                      check_if_Bin(15, 25), check_if_Bin(15, 26), check_if_Bin(15, 27), check_if_Bin(15, 28),
                      check_if_Bin(15, 29), check_if_Bin(15, 30), check_if_Bin(15, 31), check_if_Bin(15, 32),
                      check_if_Bin(15, 33), check_if_Bin(15, 34), check_if_Bin(15, 35), check_if_Bin(15, 36),
                      check_if_Bin(15, 37), check_if_Bin(15, 38), check_if_Bin(15, 39), check_if_Bin(15, 40),
                      check_if_Bin(15, 41), check_if_Bin(15, 42), check_if_Bin(15, 43), check_if_Bin(15, 44),
                      check_if_Bin(15, 45), check_if_Bin(15, 46), check_if_Bin(15, 47), check_if_Bin(15, 48),
                      check_if_Bin(15, 49), check_if_Bin(15, 50)], ignore_index=True)
    print(data)
    return data


def check_B16():
    data = pd.concat([check_if_Bin(16, 0), check_if_Bin(16, 1), check_if_Bin(16, 2), check_if_Bin(16, 3),
                      check_if_Bin(16, 4), check_if_Bin(16, 5), check_if_Bin(16, 6), check_if_Bin(16, 7),
                      check_if_Bin(16, 8), check_if_Bin(16, 9), check_if_Bin(16, 10), check_if_Bin(16, 11),
                      check_if_Bin(16, 12), check_if_Bin(16, 13), check_if_Bin(16, 14), check_if_Bin(16, 15),
                      check_if_Bin(16, 17), check_if_Bin(16, 18), check_if_Bin(16, 19), check_if_Bin(16, 20),
                      check_if_Bin(16, 21), check_if_Bin(16, 22), check_if_Bin(16, 23), check_if_Bin(16, 24),
                      check_if_Bin(16, 25), check_if_Bin(16, 26), check_if_Bin(16, 27), check_if_Bin(16, 28),
                      check_if_Bin(16, 29), check_if_Bin(16, 30), check_if_Bin(16, 31), check_if_Bin(16, 32),
                      check_if_Bin(16, 33), check_if_Bin(16, 34), check_if_Bin(16, 35), check_if_Bin(16, 36),
                      check_if_Bin(16, 37), check_if_Bin(16, 38), check_if_Bin(16, 39), check_if_Bin(16, 40),
                      check_if_Bin(16, 41), check_if_Bin(16, 42), check_if_Bin(16, 43), check_if_Bin(16, 44),
                      check_if_Bin(16, 45), check_if_Bin(16, 46), check_if_Bin(16, 47), check_if_Bin(16, 48),
                      check_if_Bin(16, 49), check_if_Bin(16, 50)], ignore_index=True)
    print(data)
    return data


def check_B17():
    data = pd.concat([check_if_Bin(17, 0), check_if_Bin(17, 1), check_if_Bin(17, 2), check_if_Bin(17, 3),
                      check_if_Bin(17, 4), check_if_Bin(17, 5), check_if_Bin(17, 6), check_if_Bin(17, 7),
                      check_if_Bin(17, 8), check_if_Bin(17, 9), check_if_Bin(17, 10), check_if_Bin(17, 11),
                      check_if_Bin(17, 12), check_if_Bin(17, 13), check_if_Bin(17, 14), check_if_Bin(17, 15),
                      check_if_Bin(17, 16), check_if_Bin(17, 18), check_if_Bin(17, 19), check_if_Bin(17, 20),
                      check_if_Bin(17, 21), check_if_Bin(17, 22), check_if_Bin(17, 23), check_if_Bin(17, 24),
                      check_if_Bin(17, 25), check_if_Bin(17, 26), check_if_Bin(17, 27), check_if_Bin(17, 28),
                      check_if_Bin(17, 29), check_if_Bin(17, 30), check_if_Bin(17, 31), check_if_Bin(17, 32),
                      check_if_Bin(17, 33), check_if_Bin(17, 34), check_if_Bin(17, 35), check_if_Bin(17, 36),
                      check_if_Bin(17, 37), check_if_Bin(17, 38), check_if_Bin(17, 39), check_if_Bin(17, 40),
                      check_if_Bin(17, 41), check_if_Bin(17, 42), check_if_Bin(17, 43), check_if_Bin(17, 44),
                      check_if_Bin(17, 45), check_if_Bin(17, 46), check_if_Bin(17, 47), check_if_Bin(17, 48),
                      check_if_Bin(17, 49), check_if_Bin(17, 50)], ignore_index=True)
    print(data)
    return data


def check_B18():
    data = pd.concat([check_if_Bin(18, 0), check_if_Bin(18, 1), check_if_Bin(18, 2), check_if_Bin(18, 3),
                      check_if_Bin(18, 4), check_if_Bin(18, 5), check_if_Bin(18, 6), check_if_Bin(18, 7),
                      check_if_Bin(18, 8), check_if_Bin(18, 9), check_if_Bin(18, 10), check_if_Bin(18, 11),
                      check_if_Bin(18, 12), check_if_Bin(18, 13), check_if_Bin(18, 14), check_if_Bin(18, 15),
                      check_if_Bin(18, 16), check_if_Bin(18, 17), check_if_Bin(18, 19), check_if_Bin(18, 20),
                      check_if_Bin(18, 21), check_if_Bin(18, 22), check_if_Bin(18, 23), check_if_Bin(18, 24),
                      check_if_Bin(18, 25), check_if_Bin(18, 26), check_if_Bin(18, 27), check_if_Bin(18, 28),
                      check_if_Bin(18, 29), check_if_Bin(18, 30), check_if_Bin(18, 31), check_if_Bin(18, 32),
                      check_if_Bin(18, 33), check_if_Bin(18, 34), check_if_Bin(18, 35), check_if_Bin(18, 36),
                      check_if_Bin(18, 37), check_if_Bin(18, 38), check_if_Bin(18, 39), check_if_Bin(18, 40),
                      check_if_Bin(18, 41), check_if_Bin(18, 42), check_if_Bin(18, 43), check_if_Bin(18, 44),
                      check_if_Bin(18, 45), check_if_Bin(18, 46), check_if_Bin(18, 47), check_if_Bin(18, 48),
                      check_if_Bin(18, 49), check_if_Bin(18, 50)], ignore_index=True)
    print(data)
    return data


def check_B19():
    data = pd.concat([check_if_Bin(19, 0), check_if_Bin(19, 1), check_if_Bin(19, 2), check_if_Bin(19, 3),
                      check_if_Bin(19, 4), check_if_Bin(19, 5), check_if_Bin(19, 6), check_if_Bin(19, 7),
                      check_if_Bin(19, 8), check_if_Bin(19, 9), check_if_Bin(19, 10), check_if_Bin(19, 11),
                      check_if_Bin(19, 12), check_if_Bin(19, 13), check_if_Bin(19, 14), check_if_Bin(19, 15),
                      check_if_Bin(19, 16), check_if_Bin(19, 17), check_if_Bin(19, 18), check_if_Bin(19, 20),
                      check_if_Bin(19, 21), check_if_Bin(19, 22), check_if_Bin(19, 23), check_if_Bin(19, 24),
                      check_if_Bin(19, 25), check_if_Bin(19, 26), check_if_Bin(19, 27), check_if_Bin(19, 28),
                      check_if_Bin(19, 29), check_if_Bin(19, 30), check_if_Bin(19, 31), check_if_Bin(19, 32),
                      check_if_Bin(19, 33), check_if_Bin(19, 34), check_if_Bin(19, 35), check_if_Bin(19, 36),
                      check_if_Bin(19, 37), check_if_Bin(19, 38), check_if_Bin(19, 39), check_if_Bin(19, 40),
                      check_if_Bin(19, 41), check_if_Bin(19, 42), check_if_Bin(19, 43), check_if_Bin(19, 44),
                      check_if_Bin(19, 45), check_if_Bin(19, 46), check_if_Bin(19, 47), check_if_Bin(19, 48),
                      check_if_Bin(19, 49), check_if_Bin(19, 50)], ignore_index=True)
    print(data)
    return data


def check_B20():
    data = pd.concat([check_if_Bin(20, 0), check_if_Bin(20, 1), check_if_Bin(20, 2), check_if_Bin(20, 3),
                      check_if_Bin(20, 4), check_if_Bin(20, 5), check_if_Bin(20, 6), check_if_Bin(20, 7),
                      check_if_Bin(20, 8), check_if_Bin(20, 9), check_if_Bin(20, 10), check_if_Bin(20, 11),
                      check_if_Bin(20, 12), check_if_Bin(20, 13), check_if_Bin(20, 14), check_if_Bin(20, 15),
                      check_if_Bin(20, 16), check_if_Bin(20, 17), check_if_Bin(20, 18), check_if_Bin(20, 19),
                      check_if_Bin(20, 21), check_if_Bin(20, 22), check_if_Bin(20, 23), check_if_Bin(20, 24),
                      check_if_Bin(20, 25), check_if_Bin(20, 26), check_if_Bin(20, 27), check_if_Bin(20, 28),
                      check_if_Bin(20, 29), check_if_Bin(20, 30), check_if_Bin(20, 31), check_if_Bin(20, 32),
                      check_if_Bin(20, 33), check_if_Bin(20, 34), check_if_Bin(20, 35), check_if_Bin(20, 36),
                      check_if_Bin(20, 37), check_if_Bin(20, 38), check_if_Bin(20, 39), check_if_Bin(20, 40),
                      check_if_Bin(20, 41), check_if_Bin(20, 42), check_if_Bin(20, 43), check_if_Bin(20, 44),
                      check_if_Bin(20, 45), check_if_Bin(20, 46), check_if_Bin(20, 47), check_if_Bin(20, 48),
                      check_if_Bin(20, 49), check_if_Bin(20, 50)], ignore_index=True)
    print('20', data)
    return data


def check_B21():
    data = pd.concat([check_if_Bin(21, 0), check_if_Bin(21, 1), check_if_Bin(21, 2), check_if_Bin(21, 3),
                      check_if_Bin(21, 4), check_if_Bin(21, 5), check_if_Bin(21, 6), check_if_Bin(21, 7),
                      check_if_Bin(21, 8), check_if_Bin(21, 9), check_if_Bin(21, 10), check_if_Bin(21, 11),
                      check_if_Bin(21, 12), check_if_Bin(21, 13), check_if_Bin(21, 14), check_if_Bin(21, 15),
                      check_if_Bin(21, 16), check_if_Bin(21, 17), check_if_Bin(21, 18), check_if_Bin(21, 19),
                      check_if_Bin(21, 20), check_if_Bin(21, 22), check_if_Bin(21, 23), check_if_Bin(21, 24),
                      check_if_Bin(21, 25), check_if_Bin(21, 26), check_if_Bin(21, 27), check_if_Bin(21, 28),
                      check_if_Bin(21, 29), check_if_Bin(21, 30), check_if_Bin(21, 31), check_if_Bin(21, 32),
                      check_if_Bin(21, 33), check_if_Bin(21, 34), check_if_Bin(21, 35), check_if_Bin(21, 36),
                      check_if_Bin(21, 37), check_if_Bin(21, 38), check_if_Bin(21, 39), check_if_Bin(21, 40),
                      check_if_Bin(21, 41), check_if_Bin(21, 42), check_if_Bin(21, 43), check_if_Bin(21, 44),
                      check_if_Bin(21, 45), check_if_Bin(21, 46), check_if_Bin(21, 47), check_if_Bin(21, 48),
                      check_if_Bin(21, 49), check_if_Bin(21, 50)], ignore_index=True)
    print(data)
    return data


def check_B22():
    data = pd.concat([check_if_Bin(22, 0), check_if_Bin(22, 1), check_if_Bin(22, 2), check_if_Bin(22, 3),
                      check_if_Bin(22, 4), check_if_Bin(22, 5), check_if_Bin(22, 6), check_if_Bin(22, 7),
                      check_if_Bin(22, 8), check_if_Bin(22, 9), check_if_Bin(22, 10), check_if_Bin(22, 11),
                      check_if_Bin(22, 12), check_if_Bin(22, 13), check_if_Bin(22, 14), check_if_Bin(22, 15),
                      check_if_Bin(22, 16), check_if_Bin(22, 17), check_if_Bin(22, 18), check_if_Bin(22, 19),
                      check_if_Bin(22, 20), check_if_Bin(22, 21), check_if_Bin(22, 23), check_if_Bin(22, 24),
                      check_if_Bin(22, 25), check_if_Bin(22, 26), check_if_Bin(22, 27), check_if_Bin(22, 28),
                      check_if_Bin(22, 29), check_if_Bin(22, 30), check_if_Bin(22, 31), check_if_Bin(22, 32),
                      check_if_Bin(22, 33), check_if_Bin(22, 34), check_if_Bin(22, 35), check_if_Bin(22, 36),
                      check_if_Bin(22, 37), check_if_Bin(22, 38), check_if_Bin(22, 39), check_if_Bin(22, 40),
                      check_if_Bin(22, 41), check_if_Bin(22, 42), check_if_Bin(22, 43), check_if_Bin(22, 44),
                      check_if_Bin(22, 45), check_if_Bin(22, 46), check_if_Bin(22, 47), check_if_Bin(22, 48),
                      check_if_Bin(22, 49), check_if_Bin(22, 50)], ignore_index=True)
    print(data)
    return data


def check_B23():
    data = pd.concat([check_if_Bin(23, 0), check_if_Bin(23, 1), check_if_Bin(23, 2), check_if_Bin(23, 3),
                      check_if_Bin(23, 4), check_if_Bin(23, 5), check_if_Bin(23, 6), check_if_Bin(23, 7),
                      check_if_Bin(23, 8), check_if_Bin(23, 9), check_if_Bin(23, 10), check_if_Bin(23, 11),
                      check_if_Bin(23, 12), check_if_Bin(23, 13), check_if_Bin(23, 14), check_if_Bin(23, 15),
                      check_if_Bin(23, 16), check_if_Bin(23, 17), check_if_Bin(23, 18), check_if_Bin(23, 19),
                      check_if_Bin(23, 20), check_if_Bin(23, 21), check_if_Bin(23, 22), check_if_Bin(23, 24),
                      check_if_Bin(23, 25), check_if_Bin(23, 26), check_if_Bin(23, 27), check_if_Bin(23, 28),
                      check_if_Bin(23, 29), check_if_Bin(23, 30), check_if_Bin(23, 31), check_if_Bin(23, 32),
                      check_if_Bin(23, 33), check_if_Bin(23, 34), check_if_Bin(23, 35), check_if_Bin(23, 36),
                      check_if_Bin(23, 37), check_if_Bin(23, 38), check_if_Bin(23, 39), check_if_Bin(23, 40),
                      check_if_Bin(23, 41), check_if_Bin(23, 42), check_if_Bin(23, 43), check_if_Bin(23, 44),
                      check_if_Bin(23, 45), check_if_Bin(23, 46), check_if_Bin(23, 47), check_if_Bin(23, 48),
                      check_if_Bin(23, 49), check_if_Bin(23, 50)], ignore_index=True)
    print(data)
    return data


def check_B24():
    data = pd.concat([check_if_Bin(24, 0), check_if_Bin(24, 1), check_if_Bin(24, 2), check_if_Bin(24, 3),
                      check_if_Bin(24, 4), check_if_Bin(24, 5), check_if_Bin(24, 6), check_if_Bin(24, 7),
                      check_if_Bin(24, 8), check_if_Bin(24, 9), check_if_Bin(24, 10), check_if_Bin(24, 11),
                      check_if_Bin(24, 12), check_if_Bin(24, 13), check_if_Bin(24, 14), check_if_Bin(24, 15),
                      check_if_Bin(24, 16), check_if_Bin(24, 17), check_if_Bin(24, 18), check_if_Bin(24, 19),
                      check_if_Bin(24, 20), check_if_Bin(24, 21), check_if_Bin(24, 22), check_if_Bin(24, 23),
                      check_if_Bin(24, 25), check_if_Bin(24, 26), check_if_Bin(24, 27), check_if_Bin(24, 28),
                      check_if_Bin(24, 29), check_if_Bin(24, 30), check_if_Bin(24, 31), check_if_Bin(24, 32),
                      check_if_Bin(24, 33), check_if_Bin(24, 34), check_if_Bin(24, 35), check_if_Bin(24, 36),
                      check_if_Bin(24, 37), check_if_Bin(24, 38), check_if_Bin(24, 39), check_if_Bin(24, 40),
                      check_if_Bin(24, 41), check_if_Bin(24, 42), check_if_Bin(24, 43), check_if_Bin(24, 44),
                      check_if_Bin(24, 45), check_if_Bin(24, 46), check_if_Bin(24, 47), check_if_Bin(24, 48),
                      check_if_Bin(24, 49), check_if_Bin(24, 50)], ignore_index=True)
    print(data)
    return data


def check_B25():
    data = pd.concat([check_if_Bin(25, 0), check_if_Bin(25, 1), check_if_Bin(25, 2), check_if_Bin(25, 3),
                      check_if_Bin(25, 4), check_if_Bin(25, 5), check_if_Bin(25, 6), check_if_Bin(25, 7),
                      check_if_Bin(25, 8), check_if_Bin(25, 9), check_if_Bin(25, 10), check_if_Bin(25, 11),
                      check_if_Bin(25, 12), check_if_Bin(25, 13), check_if_Bin(25, 14), check_if_Bin(25, 15),
                      check_if_Bin(25, 16), check_if_Bin(25, 17), check_if_Bin(25, 18), check_if_Bin(25, 19),
                      check_if_Bin(25, 20), check_if_Bin(25, 21), check_if_Bin(25, 22), check_if_Bin(25, 23),
                      check_if_Bin(25, 24), check_if_Bin(25, 26), check_if_Bin(25, 27), check_if_Bin(25, 28),
                      check_if_Bin(25, 29), check_if_Bin(25, 30), check_if_Bin(25, 31), check_if_Bin(25, 32),
                      check_if_Bin(25, 33), check_if_Bin(25, 34), check_if_Bin(25, 35), check_if_Bin(25, 36),
                      check_if_Bin(25, 37), check_if_Bin(25, 38), check_if_Bin(25, 39), check_if_Bin(25, 40),
                      check_if_Bin(25, 41), check_if_Bin(25, 42), check_if_Bin(25, 43), check_if_Bin(25, 44),
                      check_if_Bin(25, 45), check_if_Bin(25, 46), check_if_Bin(25, 47), check_if_Bin(25, 48),
                      check_if_Bin(25, 49), check_if_Bin(25, 50)], ignore_index=True)
    print(data)
    return data


def check_B26():
    data = pd.concat([check_if_Bin(26, 0), check_if_Bin(26, 1), check_if_Bin(26, 2), check_if_Bin(26, 3),
                      check_if_Bin(26, 4), check_if_Bin(26, 5), check_if_Bin(26, 6), check_if_Bin(26, 7),
                      check_if_Bin(26, 8), check_if_Bin(26, 9), check_if_Bin(26, 10), check_if_Bin(26, 11),
                      check_if_Bin(26, 12), check_if_Bin(26, 13), check_if_Bin(26, 14), check_if_Bin(26, 15),
                      check_if_Bin(26, 16), check_if_Bin(26, 17), check_if_Bin(26, 18), check_if_Bin(26, 19),
                      check_if_Bin(26, 20), check_if_Bin(26, 21), check_if_Bin(26, 22), check_if_Bin(26, 23),
                      check_if_Bin(26, 24), check_if_Bin(26, 25), check_if_Bin(26, 27), check_if_Bin(26, 28),
                      check_if_Bin(26, 29), check_if_Bin(26, 30), check_if_Bin(26, 31), check_if_Bin(26, 32),
                      check_if_Bin(26, 33), check_if_Bin(26, 34), check_if_Bin(26, 35), check_if_Bin(26, 36),
                      check_if_Bin(26, 37), check_if_Bin(26, 38), check_if_Bin(26, 39), check_if_Bin(26, 40),
                      check_if_Bin(26, 41), check_if_Bin(26, 42), check_if_Bin(26, 43), check_if_Bin(26, 44),
                      check_if_Bin(26, 45), check_if_Bin(26, 46), check_if_Bin(26, 47), check_if_Bin(26, 48),
                      check_if_Bin(26, 49), check_if_Bin(26, 50)], ignore_index=True)
    print(data)
    return data


def check_B27():
    data = pd.concat([check_if_Bin(27, 0), check_if_Bin(27, 1), check_if_Bin(27, 2), check_if_Bin(27, 3),
                      check_if_Bin(27, 4), check_if_Bin(27, 5), check_if_Bin(27, 6), check_if_Bin(27, 7),
                      check_if_Bin(27, 8), check_if_Bin(27, 9), check_if_Bin(27, 10), check_if_Bin(27, 11),
                      check_if_Bin(27, 12), check_if_Bin(27, 13), check_if_Bin(27, 14), check_if_Bin(27, 15),
                      check_if_Bin(27, 16), check_if_Bin(27, 17), check_if_Bin(27, 18), check_if_Bin(27, 19),
                      check_if_Bin(27, 20), check_if_Bin(27, 21), check_if_Bin(27, 22), check_if_Bin(27, 23),
                      check_if_Bin(27, 24), check_if_Bin(27, 25), check_if_Bin(27, 26), check_if_Bin(27, 28),
                      check_if_Bin(27, 29), check_if_Bin(27, 30), check_if_Bin(27, 31), check_if_Bin(27, 32),
                      check_if_Bin(27, 33), check_if_Bin(27, 34), check_if_Bin(27, 35), check_if_Bin(27, 36),
                      check_if_Bin(27, 37), check_if_Bin(27, 38), check_if_Bin(27, 39), check_if_Bin(27, 40),
                      check_if_Bin(27, 41), check_if_Bin(27, 42), check_if_Bin(27, 43), check_if_Bin(27, 44),
                      check_if_Bin(27, 45), check_if_Bin(27, 46), check_if_Bin(27, 47), check_if_Bin(27, 48),
                      check_if_Bin(27, 49), check_if_Bin(27, 50)], ignore_index=True)
    print(data)
    return data


def check_B28():
    data = pd.concat([check_if_Bin(28, 0), check_if_Bin(28, 1), check_if_Bin(28, 2), check_if_Bin(28, 3),
                      check_if_Bin(28, 4), check_if_Bin(28, 5), check_if_Bin(28, 6), check_if_Bin(28, 7),
                      check_if_Bin(28, 8), check_if_Bin(28, 9), check_if_Bin(28, 10), check_if_Bin(28, 11),
                      check_if_Bin(28, 12), check_if_Bin(28, 13), check_if_Bin(28, 14), check_if_Bin(28, 15),
                      check_if_Bin(28, 16), check_if_Bin(28, 17), check_if_Bin(28, 18), check_if_Bin(28, 19),
                      check_if_Bin(28, 20), check_if_Bin(28, 21), check_if_Bin(28, 22), check_if_Bin(28, 23),
                      check_if_Bin(28, 24), check_if_Bin(28, 25), check_if_Bin(28, 26), check_if_Bin(28, 27),
                      check_if_Bin(28, 29), check_if_Bin(28, 30), check_if_Bin(28, 31), check_if_Bin(28, 32),
                      check_if_Bin(28, 33), check_if_Bin(28, 34), check_if_Bin(28, 35), check_if_Bin(28, 36),
                      check_if_Bin(28, 37), check_if_Bin(28, 38), check_if_Bin(28, 39), check_if_Bin(28, 40),
                      check_if_Bin(28, 41), check_if_Bin(28, 42), check_if_Bin(28, 43), check_if_Bin(28, 44),
                      check_if_Bin(28, 45), check_if_Bin(28, 46), check_if_Bin(28, 47), check_if_Bin(28, 48),
                      check_if_Bin(28, 49), check_if_Bin(28, 50)], ignore_index=True)
    print(data)
    return data


def check_B29():
    data = pd.concat([check_if_Bin(29, 0), check_if_Bin(29, 1), check_if_Bin(29, 2), check_if_Bin(29, 3),
                      check_if_Bin(29, 4), check_if_Bin(29, 5), check_if_Bin(29, 6), check_if_Bin(29, 7),
                      check_if_Bin(29, 8), check_if_Bin(29, 9), check_if_Bin(29, 10), check_if_Bin(29, 11),
                      check_if_Bin(29, 12), check_if_Bin(29, 13), check_if_Bin(29, 14), check_if_Bin(29, 15),
                      check_if_Bin(29, 16), check_if_Bin(29, 17), check_if_Bin(29, 18), check_if_Bin(29, 19),
                      check_if_Bin(29, 20), check_if_Bin(29, 21), check_if_Bin(29, 22), check_if_Bin(29, 23),
                      check_if_Bin(29, 24), check_if_Bin(29, 25), check_if_Bin(29, 26), check_if_Bin(29, 27),
                      check_if_Bin(29, 28), check_if_Bin(29, 30), check_if_Bin(29, 31), check_if_Bin(29, 32),
                      check_if_Bin(29, 33), check_if_Bin(29, 34), check_if_Bin(29, 35), check_if_Bin(29, 36),
                      check_if_Bin(29, 37), check_if_Bin(29, 38), check_if_Bin(29, 39), check_if_Bin(29, 40),
                      check_if_Bin(29, 41), check_if_Bin(29, 42), check_if_Bin(29, 43), check_if_Bin(29, 44),
                      check_if_Bin(29, 45), check_if_Bin(29, 46), check_if_Bin(29, 47), check_if_Bin(29, 48),
                      check_if_Bin(29, 49), check_if_Bin(29, 50)], ignore_index=True)
    print(data)
    return data


def check_B30():
    data = pd.concat([check_if_Bin(30, 0), check_if_Bin(30, 1), check_if_Bin(30, 2), check_if_Bin(30, 3),
                      check_if_Bin(30, 4), check_if_Bin(30, 5), check_if_Bin(30, 6), check_if_Bin(30, 7),
                      check_if_Bin(30, 8), check_if_Bin(30, 9), check_if_Bin(30, 10), check_if_Bin(30, 11),
                      check_if_Bin(30, 12), check_if_Bin(30, 13), check_if_Bin(30, 14), check_if_Bin(30, 15),
                      check_if_Bin(30, 16), check_if_Bin(30, 17), check_if_Bin(30, 18), check_if_Bin(30, 19),
                      check_if_Bin(30, 20), check_if_Bin(30, 21), check_if_Bin(30, 22), check_if_Bin(30, 23),
                      check_if_Bin(30, 24), check_if_Bin(30, 25), check_if_Bin(30, 26), check_if_Bin(30, 27),
                      check_if_Bin(30, 28), check_if_Bin(30, 29), check_if_Bin(30, 31), check_if_Bin(30, 32),
                      check_if_Bin(30, 33), check_if_Bin(30, 34), check_if_Bin(30, 35), check_if_Bin(30, 36),
                      check_if_Bin(30, 37), check_if_Bin(30, 38), check_if_Bin(30, 39), check_if_Bin(30, 40),
                      check_if_Bin(30, 41), check_if_Bin(30, 42), check_if_Bin(30, 43), check_if_Bin(30, 44),
                      check_if_Bin(30, 45), check_if_Bin(30, 46), check_if_Bin(30, 47), check_if_Bin(30, 48),
                      check_if_Bin(30, 49), check_if_Bin(30, 50)], ignore_index=True)
    print('30', data)
    return data


def check_B31():
    data = pd.concat([check_if_Bin(31, 0), check_if_Bin(31, 1), check_if_Bin(31, 2), check_if_Bin(31, 3),
                      check_if_Bin(31, 4), check_if_Bin(31, 5), check_if_Bin(31, 6), check_if_Bin(31, 7),
                      check_if_Bin(31, 8), check_if_Bin(31, 9), check_if_Bin(31, 10), check_if_Bin(31, 11),
                      check_if_Bin(31, 12), check_if_Bin(31, 13), check_if_Bin(31, 14), check_if_Bin(31, 15),
                      check_if_Bin(31, 16), check_if_Bin(31, 17), check_if_Bin(31, 18), check_if_Bin(31, 19),
                      check_if_Bin(31, 20), check_if_Bin(31, 21), check_if_Bin(31, 22), check_if_Bin(31, 23),
                      check_if_Bin(31, 24), check_if_Bin(31, 25), check_if_Bin(31, 26), check_if_Bin(31, 27),
                      check_if_Bin(31, 28), check_if_Bin(31, 29), check_if_Bin(31, 30), check_if_Bin(31, 32),
                      check_if_Bin(31, 33), check_if_Bin(31, 34), check_if_Bin(31, 35), check_if_Bin(31, 36),
                      check_if_Bin(31, 37), check_if_Bin(31, 38), check_if_Bin(31, 39), check_if_Bin(31, 40),
                      check_if_Bin(31, 41), check_if_Bin(31, 42), check_if_Bin(31, 43), check_if_Bin(31, 44),
                      check_if_Bin(31, 45), check_if_Bin(31, 46), check_if_Bin(31, 47), check_if_Bin(31, 48),
                      check_if_Bin(31, 49), check_if_Bin(31, 50)], ignore_index=True)
    print(data)
    return data


def check_B32():
    data = pd.concat([check_if_Bin(32, 0), check_if_Bin(32, 1), check_if_Bin(32, 2), check_if_Bin(32, 3),
                      check_if_Bin(32, 4), check_if_Bin(32, 5), check_if_Bin(32, 6), check_if_Bin(32, 7),
                      check_if_Bin(32, 8), check_if_Bin(32, 9), check_if_Bin(32, 10), check_if_Bin(32, 11),
                      check_if_Bin(32, 12), check_if_Bin(32, 13), check_if_Bin(32, 14), check_if_Bin(32, 15),
                      check_if_Bin(32, 16), check_if_Bin(32, 17), check_if_Bin(32, 18), check_if_Bin(32, 19),
                      check_if_Bin(32, 20), check_if_Bin(32, 21), check_if_Bin(32, 22), check_if_Bin(32, 23),
                      check_if_Bin(32, 24), check_if_Bin(32, 25), check_if_Bin(32, 26), check_if_Bin(32, 27),
                      check_if_Bin(32, 28), check_if_Bin(32, 29), check_if_Bin(32, 30), check_if_Bin(32, 31),
                      check_if_Bin(32, 33), check_if_Bin(32, 34), check_if_Bin(32, 35), check_if_Bin(32, 36),
                      check_if_Bin(32, 37), check_if_Bin(32, 38), check_if_Bin(32, 39), check_if_Bin(32, 40),
                      check_if_Bin(32, 41), check_if_Bin(32, 42), check_if_Bin(32, 43), check_if_Bin(32, 44),
                      check_if_Bin(32, 45), check_if_Bin(32, 46), check_if_Bin(32, 47), check_if_Bin(32, 48),
                      check_if_Bin(32, 49), check_if_Bin(32, 50)], ignore_index=True)
    print(data)
    return data


def check_B33():
    data = pd.concat([check_if_Bin(33, 0), check_if_Bin(33, 1), check_if_Bin(33, 2), check_if_Bin(33, 3),
                      check_if_Bin(33, 4), check_if_Bin(33, 5), check_if_Bin(33, 6), check_if_Bin(33, 7),
                      check_if_Bin(33, 8), check_if_Bin(33, 9), check_if_Bin(33, 10), check_if_Bin(33, 11),
                      check_if_Bin(33, 12), check_if_Bin(33, 13), check_if_Bin(33, 14), check_if_Bin(33, 15),
                      check_if_Bin(33, 16), check_if_Bin(33, 17), check_if_Bin(33, 18), check_if_Bin(33, 19),
                      check_if_Bin(33, 20), check_if_Bin(33, 21), check_if_Bin(33, 22), check_if_Bin(33, 23),
                      check_if_Bin(33, 24), check_if_Bin(33, 25), check_if_Bin(33, 26), check_if_Bin(33, 27),
                      check_if_Bin(33, 28), check_if_Bin(33, 29), check_if_Bin(33, 30), check_if_Bin(33, 31),
                      check_if_Bin(33, 32), check_if_Bin(33, 34), check_if_Bin(33, 35), check_if_Bin(33, 36),
                      check_if_Bin(33, 37), check_if_Bin(33, 38), check_if_Bin(33, 39), check_if_Bin(33, 40),
                      check_if_Bin(33, 41), check_if_Bin(33, 42), check_if_Bin(33, 43), check_if_Bin(33, 44),
                      check_if_Bin(33, 45), check_if_Bin(33, 46), check_if_Bin(33, 47), check_if_Bin(33, 48),
                      check_if_Bin(33, 49), check_if_Bin(33, 50)], ignore_index=True)
    print(data)
    return data


def check_B34():
    data = pd.concat([check_if_Bin(34, 0), check_if_Bin(34, 1), check_if_Bin(34, 2), check_if_Bin(34, 3),
                      check_if_Bin(34, 4), check_if_Bin(34, 5), check_if_Bin(34, 6), check_if_Bin(34, 7),
                      check_if_Bin(34, 8), check_if_Bin(34, 9), check_if_Bin(34, 10), check_if_Bin(34, 11),
                      check_if_Bin(34, 12), check_if_Bin(34, 13), check_if_Bin(34, 14), check_if_Bin(34, 15),
                      check_if_Bin(34, 16), check_if_Bin(34, 17), check_if_Bin(34, 18), check_if_Bin(34, 19),
                      check_if_Bin(34, 20), check_if_Bin(34, 21), check_if_Bin(34, 22), check_if_Bin(34, 23),
                      check_if_Bin(34, 24), check_if_Bin(34, 25), check_if_Bin(34, 26), check_if_Bin(34, 27),
                      check_if_Bin(34, 28), check_if_Bin(34, 29), check_if_Bin(34, 30), check_if_Bin(34, 31),
                      check_if_Bin(34, 32), check_if_Bin(34, 33), check_if_Bin(34, 35), check_if_Bin(34, 36),
                      check_if_Bin(34, 37), check_if_Bin(34, 38), check_if_Bin(34, 39), check_if_Bin(34, 40),
                      check_if_Bin(34, 41), check_if_Bin(34, 42), check_if_Bin(34, 43), check_if_Bin(34, 44),
                      check_if_Bin(34, 45), check_if_Bin(34, 46), check_if_Bin(34, 47), check_if_Bin(34, 48),
                      check_if_Bin(34, 49), check_if_Bin(34, 50)], ignore_index=True)
    print(data)
    return data


def check_B35():
    data = pd.concat([check_if_Bin(35, 0), check_if_Bin(35, 1), check_if_Bin(35, 2), check_if_Bin(35, 3),
                      check_if_Bin(35, 4), check_if_Bin(35, 5), check_if_Bin(35, 6), check_if_Bin(35, 7),
                      check_if_Bin(35, 8), check_if_Bin(35, 9), check_if_Bin(35, 10), check_if_Bin(35, 11),
                      check_if_Bin(35, 12), check_if_Bin(35, 13), check_if_Bin(35, 14), check_if_Bin(35, 15),
                      check_if_Bin(35, 16), check_if_Bin(35, 17), check_if_Bin(35, 18), check_if_Bin(35, 19),
                      check_if_Bin(35, 20), check_if_Bin(35, 21), check_if_Bin(35, 22), check_if_Bin(35, 23),
                      check_if_Bin(35, 24), check_if_Bin(35, 25), check_if_Bin(35, 26), check_if_Bin(35, 27),
                      check_if_Bin(35, 28), check_if_Bin(35, 29), check_if_Bin(35, 30), check_if_Bin(35, 31),
                      check_if_Bin(35, 32), check_if_Bin(35, 33), check_if_Bin(35, 34), check_if_Bin(35, 36),
                      check_if_Bin(35, 37), check_if_Bin(35, 38), check_if_Bin(35, 39), check_if_Bin(35, 40),
                      check_if_Bin(35, 41), check_if_Bin(35, 42), check_if_Bin(35, 43), check_if_Bin(35, 44),
                      check_if_Bin(35, 45), check_if_Bin(35, 46), check_if_Bin(35, 47), check_if_Bin(35, 48),
                      check_if_Bin(35, 49), check_if_Bin(35, 50)], ignore_index=True)
    print(data)
    return data


def check_B36():
    data = pd.concat([check_if_Bin(36, 0), check_if_Bin(36, 1), check_if_Bin(36, 2), check_if_Bin(36, 3),
                      check_if_Bin(36, 4), check_if_Bin(36, 5), check_if_Bin(36, 6), check_if_Bin(36, 7),
                      check_if_Bin(36, 8), check_if_Bin(36, 9), check_if_Bin(36, 10), check_if_Bin(36, 11),
                      check_if_Bin(36, 12), check_if_Bin(36, 13), check_if_Bin(36, 14), check_if_Bin(36, 15),
                      check_if_Bin(36, 16), check_if_Bin(36, 17), check_if_Bin(36, 18), check_if_Bin(36, 19),
                      check_if_Bin(36, 20), check_if_Bin(36, 21), check_if_Bin(36, 22), check_if_Bin(36, 23),
                      check_if_Bin(36, 24), check_if_Bin(36, 25), check_if_Bin(36, 26), check_if_Bin(36, 27),
                      check_if_Bin(36, 28), check_if_Bin(36, 29), check_if_Bin(36, 30), check_if_Bin(36, 31),
                      check_if_Bin(36, 32), check_if_Bin(36, 33), check_if_Bin(36, 34), check_if_Bin(36, 35),
                      check_if_Bin(36, 37), check_if_Bin(36, 38), check_if_Bin(36, 39), check_if_Bin(36, 40),
                      check_if_Bin(36, 41), check_if_Bin(36, 42), check_if_Bin(36, 43), check_if_Bin(36, 44),
                      check_if_Bin(36, 45), check_if_Bin(36, 46), check_if_Bin(36, 47), check_if_Bin(36, 48),
                      check_if_Bin(36, 49), check_if_Bin(36, 50)], ignore_index=True)
    print(data)
    return data


def check_B37():
    data = pd.concat([check_if_Bin(37, 0), check_if_Bin(37, 1), check_if_Bin(37, 2), check_if_Bin(37, 3),
                      check_if_Bin(37, 4), check_if_Bin(37, 5), check_if_Bin(37, 6), check_if_Bin(37, 7),
                      check_if_Bin(37, 8), check_if_Bin(37, 9), check_if_Bin(37, 10), check_if_Bin(37, 11),
                      check_if_Bin(37, 12), check_if_Bin(37, 13), check_if_Bin(37, 14), check_if_Bin(37, 15),
                      check_if_Bin(37, 16), check_if_Bin(37, 17), check_if_Bin(37, 18), check_if_Bin(37, 19),
                      check_if_Bin(37, 20), check_if_Bin(37, 21), check_if_Bin(37, 22), check_if_Bin(37, 23),
                      check_if_Bin(37, 24), check_if_Bin(37, 25), check_if_Bin(37, 26), check_if_Bin(37, 27),
                      check_if_Bin(37, 28), check_if_Bin(37, 29), check_if_Bin(37, 30), check_if_Bin(37, 31),
                      check_if_Bin(37, 32), check_if_Bin(37, 33), check_if_Bin(37, 34), check_if_Bin(37, 35),
                      check_if_Bin(37, 36), check_if_Bin(37, 38), check_if_Bin(37, 39), check_if_Bin(37, 40),
                      check_if_Bin(37, 41), check_if_Bin(37, 42), check_if_Bin(37, 43), check_if_Bin(37, 44),
                      check_if_Bin(37, 45), check_if_Bin(37, 46), check_if_Bin(37, 47), check_if_Bin(37, 48),
                      check_if_Bin(37, 49), check_if_Bin(37, 50)], ignore_index=True)
    print(data)
    return data


def check_B38():
    data = pd.concat([check_if_Bin(38, 0), check_if_Bin(38, 1), check_if_Bin(38, 2), check_if_Bin(38, 3),
                      check_if_Bin(38, 4), check_if_Bin(38, 5), check_if_Bin(38, 6), check_if_Bin(38, 7),
                      check_if_Bin(38, 8), check_if_Bin(38, 9), check_if_Bin(38, 10), check_if_Bin(38, 11),
                      check_if_Bin(38, 12), check_if_Bin(38, 13), check_if_Bin(38, 14), check_if_Bin(38, 15),
                      check_if_Bin(38, 16), check_if_Bin(38, 17), check_if_Bin(38, 18), check_if_Bin(38, 19),
                      check_if_Bin(38, 20), check_if_Bin(38, 21), check_if_Bin(38, 22), check_if_Bin(38, 23),
                      check_if_Bin(38, 24), check_if_Bin(38, 25), check_if_Bin(38, 26), check_if_Bin(38, 27),
                      check_if_Bin(38, 28), check_if_Bin(38, 29), check_if_Bin(38, 30), check_if_Bin(38, 31),
                      check_if_Bin(38, 32), check_if_Bin(38, 33), check_if_Bin(38, 34), check_if_Bin(38, 35),
                      check_if_Bin(38, 36), check_if_Bin(38, 37), check_if_Bin(38, 39), check_if_Bin(38, 40),
                      check_if_Bin(38, 41), check_if_Bin(38, 42), check_if_Bin(38, 43), check_if_Bin(38, 44),
                      check_if_Bin(38, 45), check_if_Bin(38, 46), check_if_Bin(38, 47), check_if_Bin(38, 48),
                      check_if_Bin(38, 49), check_if_Bin(38, 50)], ignore_index=True)
    print(data)
    return data


def check_B39():
    data = pd.concat([check_if_Bin(39, 0), check_if_Bin(39, 1), check_if_Bin(39, 2), check_if_Bin(39, 3),
                      check_if_Bin(39, 4), check_if_Bin(39, 5), check_if_Bin(39, 6), check_if_Bin(39, 7),
                      check_if_Bin(39, 8), check_if_Bin(39, 9), check_if_Bin(39, 10), check_if_Bin(39, 11),
                      check_if_Bin(39, 12), check_if_Bin(39, 13), check_if_Bin(39, 14), check_if_Bin(39, 15),
                      check_if_Bin(39, 16), check_if_Bin(39, 17), check_if_Bin(39, 18), check_if_Bin(39, 19),
                      check_if_Bin(39, 20), check_if_Bin(39, 21), check_if_Bin(39, 22), check_if_Bin(39, 23),
                      check_if_Bin(39, 24), check_if_Bin(39, 25), check_if_Bin(39, 26), check_if_Bin(39, 27),
                      check_if_Bin(39, 28), check_if_Bin(39, 29), check_if_Bin(39, 30), check_if_Bin(39, 31),
                      check_if_Bin(39, 32), check_if_Bin(39, 33), check_if_Bin(39, 34), check_if_Bin(39, 35),
                      check_if_Bin(39, 36), check_if_Bin(39, 37), check_if_Bin(39, 38), check_if_Bin(39, 40),
                      check_if_Bin(39, 41), check_if_Bin(39, 42), check_if_Bin(39, 43), check_if_Bin(39, 44),
                      check_if_Bin(39, 45), check_if_Bin(39, 46), check_if_Bin(39, 47), check_if_Bin(39, 48),
                      check_if_Bin(39, 49), check_if_Bin(39, 50)], ignore_index=True)
    print(data)
    return data


def check_B40():
    data = pd.concat([check_if_Bin(40, 0), check_if_Bin(40, 1), check_if_Bin(40, 2), check_if_Bin(40, 3),
                      check_if_Bin(40, 4), check_if_Bin(40, 5), check_if_Bin(40, 6), check_if_Bin(40, 7),
                      check_if_Bin(40, 8), check_if_Bin(40, 9), check_if_Bin(40, 10), check_if_Bin(40, 11),
                      check_if_Bin(40, 12), check_if_Bin(40, 13), check_if_Bin(40, 14), check_if_Bin(40, 15),
                      check_if_Bin(40, 16), check_if_Bin(40, 17), check_if_Bin(40, 18), check_if_Bin(40, 19),
                      check_if_Bin(40, 20), check_if_Bin(40, 21), check_if_Bin(40, 22), check_if_Bin(40, 23),
                      check_if_Bin(40, 24), check_if_Bin(40, 25), check_if_Bin(40, 26), check_if_Bin(40, 27),
                      check_if_Bin(40, 28), check_if_Bin(40, 29), check_if_Bin(40, 30), check_if_Bin(40, 31),
                      check_if_Bin(40, 32), check_if_Bin(40, 33), check_if_Bin(40, 34), check_if_Bin(40, 35),
                      check_if_Bin(40, 36), check_if_Bin(40, 37), check_if_Bin(40, 38), check_if_Bin(40, 39),
                      check_if_Bin(40, 41), check_if_Bin(40, 42), check_if_Bin(40, 43), check_if_Bin(40, 44),
                      check_if_Bin(40, 45), check_if_Bin(40, 46), check_if_Bin(40, 47), check_if_Bin(40, 48),
                      check_if_Bin(40, 49), check_if_Bin(40, 50)], ignore_index=True)
    print('40', data)
    return data


def check_B41():
    data = pd.concat([check_if_Bin(41, 0), check_if_Bin(41, 1), check_if_Bin(41, 2), check_if_Bin(41, 3),
                      check_if_Bin(41, 4), check_if_Bin(41, 5), check_if_Bin(41, 6), check_if_Bin(41, 7),
                      check_if_Bin(41, 8), check_if_Bin(41, 9), check_if_Bin(41, 10), check_if_Bin(41, 11),
                      check_if_Bin(41, 12), check_if_Bin(41, 13), check_if_Bin(41, 14), check_if_Bin(41, 15),
                      check_if_Bin(41, 16), check_if_Bin(41, 17), check_if_Bin(41, 18), check_if_Bin(41, 19),
                      check_if_Bin(41, 20), check_if_Bin(41, 21), check_if_Bin(41, 22), check_if_Bin(41, 23),
                      check_if_Bin(41, 24), check_if_Bin(41, 25), check_if_Bin(41, 26), check_if_Bin(41, 27),
                      check_if_Bin(41, 28), check_if_Bin(41, 29), check_if_Bin(41, 30), check_if_Bin(41, 31),
                      check_if_Bin(41, 32), check_if_Bin(41, 33), check_if_Bin(41, 34), check_if_Bin(41, 35),
                      check_if_Bin(41, 36), check_if_Bin(41, 37), check_if_Bin(41, 38), check_if_Bin(41, 39),
                      check_if_Bin(41, 40), check_if_Bin(41, 42), check_if_Bin(41, 43), check_if_Bin(41, 44),
                      check_if_Bin(41, 45), check_if_Bin(41, 46), check_if_Bin(41, 47), check_if_Bin(41, 48),
                      check_if_Bin(41, 49), check_if_Bin(41, 50)], ignore_index=True)
    print(data)
    return data


def check_B42():
    data = pd.concat([check_if_Bin(42, 0), check_if_Bin(42, 1), check_if_Bin(42, 2), check_if_Bin(42, 3),
                      check_if_Bin(42, 4), check_if_Bin(42, 5), check_if_Bin(42, 6), check_if_Bin(42, 7),
                      check_if_Bin(42, 8), check_if_Bin(42, 9), check_if_Bin(42, 10), check_if_Bin(42, 11),
                      check_if_Bin(42, 12), check_if_Bin(42, 13), check_if_Bin(42, 14), check_if_Bin(42, 15),
                      check_if_Bin(42, 16), check_if_Bin(42, 17), check_if_Bin(42, 18), check_if_Bin(42, 19),
                      check_if_Bin(42, 20), check_if_Bin(42, 21), check_if_Bin(42, 22), check_if_Bin(42, 23),
                      check_if_Bin(42, 24), check_if_Bin(42, 25), check_if_Bin(42, 26), check_if_Bin(42, 27),
                      check_if_Bin(42, 28), check_if_Bin(42, 29), check_if_Bin(42, 30), check_if_Bin(42, 31),
                      check_if_Bin(42, 32), check_if_Bin(42, 33), check_if_Bin(42, 34), check_if_Bin(42, 35),
                      check_if_Bin(42, 36), check_if_Bin(42, 37), check_if_Bin(42, 38), check_if_Bin(42, 39),
                      check_if_Bin(42, 40), check_if_Bin(42, 41), check_if_Bin(42, 43), check_if_Bin(42, 44),
                      check_if_Bin(42, 45), check_if_Bin(42, 46), check_if_Bin(42, 47), check_if_Bin(42, 48),
                      check_if_Bin(42, 49), check_if_Bin(42, 50)], ignore_index=True)
    print(data)
    return data


def check_B43():
    data = pd.concat([check_if_Bin(43, 0), check_if_Bin(43, 1), check_if_Bin(43, 2), check_if_Bin(43, 3),
                      check_if_Bin(43, 4), check_if_Bin(43, 5), check_if_Bin(43, 6), check_if_Bin(43, 7),
                      check_if_Bin(43, 8), check_if_Bin(43, 9), check_if_Bin(43, 10), check_if_Bin(43, 11),
                      check_if_Bin(43, 12), check_if_Bin(43, 13), check_if_Bin(43, 14), check_if_Bin(43, 15),
                      check_if_Bin(43, 16), check_if_Bin(43, 17), check_if_Bin(43, 18), check_if_Bin(43, 19),
                      check_if_Bin(43, 20), check_if_Bin(43, 21), check_if_Bin(43, 22), check_if_Bin(43, 23),
                      check_if_Bin(43, 24), check_if_Bin(43, 25), check_if_Bin(43, 26), check_if_Bin(43, 27),
                      check_if_Bin(43, 28), check_if_Bin(43, 29), check_if_Bin(43, 30), check_if_Bin(43, 31),
                      check_if_Bin(43, 32), check_if_Bin(43, 33), check_if_Bin(43, 34), check_if_Bin(43, 35),
                      check_if_Bin(43, 36), check_if_Bin(43, 37), check_if_Bin(43, 38), check_if_Bin(43, 39),
                      check_if_Bin(43, 40), check_if_Bin(43, 41), check_if_Bin(43, 42), check_if_Bin(43, 44),
                      check_if_Bin(43, 45), check_if_Bin(43, 46), check_if_Bin(43, 47), check_if_Bin(43, 48),
                      check_if_Bin(43, 49), check_if_Bin(43, 50)], ignore_index=True)
    print(data)
    return data


def check_B44():
    data = pd.concat([check_if_Bin(44, 0), check_if_Bin(44, 1), check_if_Bin(44, 2), check_if_Bin(44, 3),
                      check_if_Bin(44, 4), check_if_Bin(44, 5), check_if_Bin(44, 6), check_if_Bin(44, 7),
                      check_if_Bin(44, 8), check_if_Bin(44, 9), check_if_Bin(44, 10), check_if_Bin(44, 11),
                      check_if_Bin(44, 12), check_if_Bin(44, 13), check_if_Bin(44, 14), check_if_Bin(44, 15),
                      check_if_Bin(44, 16), check_if_Bin(44, 17), check_if_Bin(44, 18), check_if_Bin(44, 19),
                      check_if_Bin(44, 20), check_if_Bin(44, 21), check_if_Bin(44, 22), check_if_Bin(44, 23),
                      check_if_Bin(44, 24), check_if_Bin(44, 25), check_if_Bin(44, 26), check_if_Bin(44, 27),
                      check_if_Bin(44, 28), check_if_Bin(44, 29), check_if_Bin(44, 30), check_if_Bin(44, 31),
                      check_if_Bin(44, 32), check_if_Bin(44, 33), check_if_Bin(44, 34), check_if_Bin(44, 35),
                      check_if_Bin(44, 36), check_if_Bin(44, 37), check_if_Bin(44, 38), check_if_Bin(44, 39),
                      check_if_Bin(44, 40), check_if_Bin(44, 41), check_if_Bin(44, 42), check_if_Bin(44, 43),
                      check_if_Bin(44, 45), check_if_Bin(44, 46), check_if_Bin(44, 47), check_if_Bin(44, 48),
                      check_if_Bin(44, 49), check_if_Bin(44, 50)], ignore_index=True)
    print(data)
    return data


def check_B45():
    data = pd.concat([check_if_Bin(45, 0), check_if_Bin(45, 1), check_if_Bin(45, 2), check_if_Bin(45, 3),
                      check_if_Bin(45, 4), check_if_Bin(45, 5), check_if_Bin(45, 6), check_if_Bin(45, 7),
                      check_if_Bin(45, 8), check_if_Bin(45, 9), check_if_Bin(45, 10), check_if_Bin(45, 11),
                      check_if_Bin(45, 12), check_if_Bin(45, 13), check_if_Bin(45, 14), check_if_Bin(45, 15),
                      check_if_Bin(45, 16), check_if_Bin(45, 17), check_if_Bin(45, 18), check_if_Bin(45, 19),
                      check_if_Bin(45, 20), check_if_Bin(45, 21), check_if_Bin(45, 22), check_if_Bin(45, 23),
                      check_if_Bin(45, 24), check_if_Bin(45, 25), check_if_Bin(45, 26), check_if_Bin(45, 27),
                      check_if_Bin(45, 28), check_if_Bin(45, 29), check_if_Bin(45, 30), check_if_Bin(45, 31),
                      check_if_Bin(45, 32), check_if_Bin(45, 33), check_if_Bin(45, 34), check_if_Bin(45, 35),
                      check_if_Bin(45, 36), check_if_Bin(45, 37), check_if_Bin(45, 38), check_if_Bin(45, 39),
                      check_if_Bin(45, 40), check_if_Bin(45, 41), check_if_Bin(45, 42), check_if_Bin(45, 43),
                      check_if_Bin(45, 44), check_if_Bin(45, 46), check_if_Bin(45, 47), check_if_Bin(45, 48),
                      check_if_Bin(45, 49), check_if_Bin(45, 50)], ignore_index=True)
    print(data)
    return data


def check_B46():
    data = pd.concat([check_if_Bin(46, 0), check_if_Bin(46, 1), check_if_Bin(46, 2), check_if_Bin(46, 3),
                      check_if_Bin(46, 4), check_if_Bin(46, 5), check_if_Bin(46, 6), check_if_Bin(46, 7),
                      check_if_Bin(46, 8), check_if_Bin(46, 9), check_if_Bin(46, 10), check_if_Bin(46, 11),
                      check_if_Bin(46, 12), check_if_Bin(46, 13), check_if_Bin(46, 14), check_if_Bin(46, 15),
                      check_if_Bin(46, 16), check_if_Bin(46, 17), check_if_Bin(46, 18), check_if_Bin(46, 19),
                      check_if_Bin(46, 20), check_if_Bin(46, 21), check_if_Bin(46, 22), check_if_Bin(46, 23),
                      check_if_Bin(46, 24), check_if_Bin(46, 25), check_if_Bin(46, 26), check_if_Bin(46, 27),
                      check_if_Bin(46, 28), check_if_Bin(46, 29), check_if_Bin(46, 30), check_if_Bin(46, 31),
                      check_if_Bin(46, 32), check_if_Bin(46, 33), check_if_Bin(46, 34), check_if_Bin(46, 35),
                      check_if_Bin(46, 36), check_if_Bin(46, 37), check_if_Bin(46, 38), check_if_Bin(46, 39),
                      check_if_Bin(46, 40), check_if_Bin(46, 41), check_if_Bin(46, 42), check_if_Bin(46, 43),
                      check_if_Bin(46, 44), check_if_Bin(46, 45), check_if_Bin(46, 47), check_if_Bin(46, 48),
                      check_if_Bin(46, 49), check_if_Bin(46, 50)], ignore_index=True)
    print(data)
    return data


def check_B47():
    data = pd.concat([check_if_Bin(47, 0), check_if_Bin(47, 1), check_if_Bin(47, 2), check_if_Bin(47, 3),
                      check_if_Bin(47, 4), check_if_Bin(47, 5), check_if_Bin(47, 6), check_if_Bin(47, 7),
                      check_if_Bin(47, 8), check_if_Bin(47, 9), check_if_Bin(47, 10), check_if_Bin(47, 11),
                      check_if_Bin(47, 12), check_if_Bin(47, 13), check_if_Bin(47, 14), check_if_Bin(47, 15),
                      check_if_Bin(47, 16), check_if_Bin(47, 17), check_if_Bin(47, 18), check_if_Bin(47, 19),
                      check_if_Bin(47, 20), check_if_Bin(47, 21), check_if_Bin(47, 22), check_if_Bin(47, 23),
                      check_if_Bin(47, 24), check_if_Bin(47, 25), check_if_Bin(47, 26), check_if_Bin(47, 27),
                      check_if_Bin(47, 28), check_if_Bin(47, 29), check_if_Bin(47, 30), check_if_Bin(47, 31),
                      check_if_Bin(47, 32), check_if_Bin(47, 33), check_if_Bin(47, 34), check_if_Bin(47, 35),
                      check_if_Bin(47, 36), check_if_Bin(47, 37), check_if_Bin(47, 38), check_if_Bin(47, 39),
                      check_if_Bin(47, 40), check_if_Bin(47, 41), check_if_Bin(47, 42), check_if_Bin(47, 43),
                      check_if_Bin(47, 44), check_if_Bin(47, 45), check_if_Bin(47, 46), check_if_Bin(47, 48),
                      check_if_Bin(47, 49), check_if_Bin(47, 50)], ignore_index=True)
    print(data)
    return data


def check_B48():
    data = pd.concat([check_if_Bin(48, 0), check_if_Bin(48, 1), check_if_Bin(48, 2), check_if_Bin(48, 3),
                      check_if_Bin(48, 4), check_if_Bin(48, 5), check_if_Bin(48, 6), check_if_Bin(48, 7),
                      check_if_Bin(48, 8), check_if_Bin(48, 9), check_if_Bin(48, 10), check_if_Bin(48, 11),
                      check_if_Bin(48, 12), check_if_Bin(48, 13), check_if_Bin(48, 14), check_if_Bin(48, 15),
                      check_if_Bin(48, 16), check_if_Bin(48, 17), check_if_Bin(48, 18), check_if_Bin(48, 19),
                      check_if_Bin(48, 20), check_if_Bin(48, 21), check_if_Bin(48, 22), check_if_Bin(48, 23),
                      check_if_Bin(48, 24), check_if_Bin(48, 25), check_if_Bin(48, 26), check_if_Bin(48, 27),
                      check_if_Bin(48, 28), check_if_Bin(48, 29), check_if_Bin(48, 30), check_if_Bin(48, 31),
                      check_if_Bin(48, 32), check_if_Bin(48, 33), check_if_Bin(48, 34), check_if_Bin(48, 35),
                      check_if_Bin(48, 36), check_if_Bin(48, 37), check_if_Bin(48, 38), check_if_Bin(48, 39),
                      check_if_Bin(48, 40), check_if_Bin(48, 41), check_if_Bin(48, 42), check_if_Bin(48, 43),
                      check_if_Bin(48, 44), check_if_Bin(48, 45), check_if_Bin(48, 46), check_if_Bin(48, 47),
                      check_if_Bin(48, 49), check_if_Bin(48, 50)], ignore_index=True)
    print(data)
    return data


def check_B49():
    data = pd.concat([check_if_Bin(49, 0), check_if_Bin(49, 1), check_if_Bin(49, 2), check_if_Bin(49, 3),
                      check_if_Bin(49, 4), check_if_Bin(49, 5), check_if_Bin(49, 6), check_if_Bin(49, 7),
                      check_if_Bin(49, 8), check_if_Bin(49, 9), check_if_Bin(49, 10), check_if_Bin(49, 11),
                      check_if_Bin(49, 12), check_if_Bin(49, 13), check_if_Bin(49, 14), check_if_Bin(49, 15),
                      check_if_Bin(49, 16), check_if_Bin(49, 17), check_if_Bin(49, 18), check_if_Bin(49, 19),
                      check_if_Bin(49, 20), check_if_Bin(49, 21), check_if_Bin(49, 22), check_if_Bin(49, 23),
                      check_if_Bin(49, 24), check_if_Bin(49, 25), check_if_Bin(49, 26), check_if_Bin(49, 27),
                      check_if_Bin(49, 28), check_if_Bin(49, 29), check_if_Bin(49, 30), check_if_Bin(49, 31),
                      check_if_Bin(49, 32), check_if_Bin(49, 33), check_if_Bin(49, 34), check_if_Bin(49, 35),
                      check_if_Bin(49, 36), check_if_Bin(49, 37), check_if_Bin(49, 38), check_if_Bin(49, 39),
                      check_if_Bin(49, 40), check_if_Bin(49, 41), check_if_Bin(49, 42), check_if_Bin(49, 43),
                      check_if_Bin(49, 44), check_if_Bin(49, 45), check_if_Bin(49, 46), check_if_Bin(49, 47),
                      check_if_Bin(49, 48), check_if_Bin(49, 50)], ignore_index=True)
    print(data)
    return data


def check_B50():
    data = pd.concat([check_if_Bin(50, 0), check_if_Bin(50, 1), check_if_Bin(50, 2), check_if_Bin(50, 3),
                      check_if_Bin(50, 4), check_if_Bin(50, 5), check_if_Bin(50, 6), check_if_Bin(50, 7),
                      check_if_Bin(50, 8), check_if_Bin(50, 9), check_if_Bin(50, 10), check_if_Bin(50, 11),
                      check_if_Bin(50, 12), check_if_Bin(50, 13), check_if_Bin(50, 14), check_if_Bin(50, 15),
                      check_if_Bin(50, 16), check_if_Bin(50, 17), check_if_Bin(50, 18), check_if_Bin(50, 19),
                      check_if_Bin(50, 20), check_if_Bin(50, 21), check_if_Bin(50, 22), check_if_Bin(50, 23),
                      check_if_Bin(50, 24), check_if_Bin(50, 25), check_if_Bin(50, 26), check_if_Bin(50, 27),
                      check_if_Bin(50, 28), check_if_Bin(50, 29), check_if_Bin(50, 30), check_if_Bin(50, 31),
                      check_if_Bin(50, 32), check_if_Bin(50, 33), check_if_Bin(50, 34), check_if_Bin(50, 35),
                      check_if_Bin(50, 36), check_if_Bin(50, 37), check_if_Bin(50, 38), check_if_Bin(50, 39),
                      check_if_Bin(50, 40), check_if_Bin(50, 41), check_if_Bin(50, 42), check_if_Bin(50, 43),
                      check_if_Bin(50, 44), check_if_Bin(50, 45), check_if_Bin(50, 46), check_if_Bin(50, 47),
                      check_if_Bin(50, 48), check_if_Bin(50, 49)], ignore_index=True)
    print('50', data)
    return data


def check():
    data = pd.concat([check_B1(), check_B2(), check_B3(), check_B4(),
                      check_B5(), check_B6(), check_B7(), check_B8(),
                      check_B9(), check_B10(), check_B11(), check_B12(),
                      check_B13(), check_B14(), check_B15(), check_B16(),
                      check_B17(), check_B18(), check_B19(), check_B20(),
                      check_B21(), check_B22(), check_B23(), check_B24(),
                      check_B25(), check_B26(), check_B27(), check_B28(),
                      check_B29(), check_B30(), check_B31(), check_B32(),
                      check_B33(), check_B34(), check_B35(), check_B36(),
                      check_B37(), check_B38(), check_B39(), check_B40(),
                      check_B41(), check_B42(), check_B43(), check_B44(),
                      check_B45(), check_B46(), check_B47(), check_B48(),
                      check_B49(), check_B50()], ignore_index=True)
    print('check', data)
    return data


def check_B_csv():
    data = check()
    string1 = "/Pycharm/HumanActivityRecognition/check"
    string2 = string1 + "/check_B" + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


check_B_csv()
