import os

import numpy as np
import pandas as pd

from CreateWord import create_word


def check_if_Iin(x, y):
    d = create_word(x, 'I')['words']
    word_to_keep = np.array(create_word(y, 'I')['words'])
    df = pd.DataFrame(np.array(d[d.isin(word_to_keep)]), columns=['words'])
    return df


def check_I0():
    data = pd.concat([check_if_Iin(0, 1), check_if_Iin(0, 2), check_if_Iin(0, 3), check_if_Iin(0, 4),
                      check_if_Iin(0, 5), check_if_Iin(0, 6), check_if_Iin(0, 7), check_if_Iin(0, 8),
                      check_if_Iin(0, 9), check_if_Iin(0, 10), check_if_Iin(0, 11), check_if_Iin(0, 12),
                      check_if_Iin(0, 13), check_if_Iin(0, 14), check_if_Iin(0, 15), check_if_Iin(0, 16),
                      check_if_Iin(0, 17), check_if_Iin(0, 18), check_if_Iin(0, 19), check_if_Iin(0, 20),
                      check_if_Iin(0, 21), check_if_Iin(0, 22), check_if_Iin(0, 23), check_if_Iin(0, 24),
                      check_if_Iin(0, 25), check_if_Iin(0, 26), check_if_Iin(0, 27), check_if_Iin(0, 28),
                      check_if_Iin(0, 29), check_if_Iin(0, 30), check_if_Iin(0, 31), check_if_Iin(0, 32),
                      check_if_Iin(0, 33), check_if_Iin(0, 34), check_if_Iin(0, 35), check_if_Iin(0, 36),
                      check_if_Iin(0, 37), check_if_Iin(0, 38), check_if_Iin(0, 39), check_if_Iin(0, 40),
                      check_if_Iin(0, 41), check_if_Iin(0, 42), check_if_Iin(0, 43), check_if_Iin(0, 44),
                      check_if_Iin(0, 45), check_if_Iin(0, 46), check_if_Iin(0, 47), check_if_Iin(0, 48),
                      check_if_Iin(0, 49), check_if_Iin(0, 50)], ignore_index=True)
    return data


def check_I1():
    data = pd.concat([check_if_Iin(1, 0), check_if_Iin(1, 2), check_if_Iin(1, 3), check_if_Iin(1, 4),
                      check_if_Iin(1, 5), check_if_Iin(1, 6), check_if_Iin(1, 7), check_if_Iin(1, 8),
                      check_if_Iin(1, 9), check_if_Iin(1, 10), check_if_Iin(1, 11), check_if_Iin(1, 12),
                      check_if_Iin(1, 13), check_if_Iin(1, 14), check_if_Iin(1, 15), check_if_Iin(1, 16),
                      check_if_Iin(1, 17), check_if_Iin(1, 18), check_if_Iin(1, 19), check_if_Iin(1, 20),
                      check_if_Iin(1, 21), check_if_Iin(1, 22), check_if_Iin(1, 23), check_if_Iin(1, 24),
                      check_if_Iin(1, 25), check_if_Iin(1, 26), check_if_Iin(1, 27), check_if_Iin(1, 28),
                      check_if_Iin(1, 29), check_if_Iin(1, 30), check_if_Iin(1, 31), check_if_Iin(1, 32),
                      check_if_Iin(1, 33), check_if_Iin(1, 34), check_if_Iin(1, 35), check_if_Iin(1, 36),
                      check_if_Iin(1, 37), check_if_Iin(1, 38), check_if_Iin(1, 39), check_if_Iin(1, 40),
                      check_if_Iin(1, 41), check_if_Iin(1, 42), check_if_Iin(1, 43), check_if_Iin(1, 44),
                      check_if_Iin(1, 45), check_if_Iin(1, 46), check_if_Iin(1, 47), check_if_Iin(1, 48),
                      check_if_Iin(1, 49), check_if_Iin(1, 50)], ignore_index=True)
    return data


def check_I2():
    data = pd.concat([check_if_Iin(2, 0), check_if_Iin(2, 1), check_if_Iin(2, 3), check_if_Iin(2, 4),
                      check_if_Iin(2, 5), check_if_Iin(2, 6), check_if_Iin(2, 7), check_if_Iin(2, 8),
                      check_if_Iin(2, 9), check_if_Iin(2, 10), check_if_Iin(2, 11), check_if_Iin(2, 12),
                      check_if_Iin(2, 13), check_if_Iin(2, 14), check_if_Iin(2, 15), check_if_Iin(2, 16),
                      check_if_Iin(2, 17), check_if_Iin(2, 18), check_if_Iin(2, 19), check_if_Iin(2, 20),
                      check_if_Iin(2, 21), check_if_Iin(2, 22), check_if_Iin(2, 23), check_if_Iin(2, 24),
                      check_if_Iin(2, 25), check_if_Iin(2, 26), check_if_Iin(2, 27), check_if_Iin(2, 28),
                      check_if_Iin(2, 29), check_if_Iin(2, 30), check_if_Iin(2, 31), check_if_Iin(2, 32),
                      check_if_Iin(2, 33), check_if_Iin(2, 34), check_if_Iin(2, 35), check_if_Iin(2, 36),
                      check_if_Iin(2, 37), check_if_Iin(2, 38), check_if_Iin(2, 39), check_if_Iin(2, 40),
                      check_if_Iin(2, 41), check_if_Iin(2, 42), check_if_Iin(2, 43), check_if_Iin(2, 44),
                      check_if_Iin(2, 45), check_if_Iin(2, 46), check_if_Iin(2, 47), check_if_Iin(2, 48),
                      check_if_Iin(2, 49), check_if_Iin(2, 50)], ignore_index=True)
    return data


def check_I3():
    data = pd.concat([check_if_Iin(3, 0), check_if_Iin(3, 1), check_if_Iin(3, 2), check_if_Iin(3, 4),
                      check_if_Iin(3, 5), check_if_Iin(3, 6), check_if_Iin(3, 7), check_if_Iin(3, 8),
                      check_if_Iin(3, 9), check_if_Iin(3, 10), check_if_Iin(3, 11), check_if_Iin(3, 12),
                      check_if_Iin(3, 13), check_if_Iin(3, 14), check_if_Iin(3, 15), check_if_Iin(3, 16),
                      check_if_Iin(3, 17), check_if_Iin(3, 18), check_if_Iin(3, 19), check_if_Iin(3, 20),
                      check_if_Iin(3, 21), check_if_Iin(3, 22), check_if_Iin(3, 23), check_if_Iin(3, 24),
                      check_if_Iin(3, 25), check_if_Iin(3, 26), check_if_Iin(3, 27), check_if_Iin(3, 28),
                      check_if_Iin(3, 29), check_if_Iin(3, 30), check_if_Iin(3, 31), check_if_Iin(3, 32),
                      check_if_Iin(3, 33), check_if_Iin(3, 34), check_if_Iin(3, 35), check_if_Iin(3, 36),
                      check_if_Iin(3, 37), check_if_Iin(3, 38), check_if_Iin(3, 39), check_if_Iin(3, 40),
                      check_if_Iin(3, 41), check_if_Iin(3, 42), check_if_Iin(3, 43), check_if_Iin(3, 44),
                      check_if_Iin(3, 45), check_if_Iin(3, 46), check_if_Iin(3, 47), check_if_Iin(3, 48),
                      check_if_Iin(3, 49), check_if_Iin(3, 50)], ignore_index=True)
    return data


def check_I4():
    data = pd.concat([check_if_Iin(4, 0), check_if_Iin(4, 1), check_if_Iin(4, 2), check_if_Iin(4, 3),
                      check_if_Iin(4, 5), check_if_Iin(4, 6), check_if_Iin(4, 7), check_if_Iin(4, 8),
                      check_if_Iin(4, 9), check_if_Iin(4, 10), check_if_Iin(4, 11), check_if_Iin(4, 12),
                      check_if_Iin(4, 13), check_if_Iin(4, 14), check_if_Iin(4, 15), check_if_Iin(4, 16),
                      check_if_Iin(4, 17), check_if_Iin(4, 18), check_if_Iin(4, 19), check_if_Iin(4, 20),
                      check_if_Iin(4, 21), check_if_Iin(4, 22), check_if_Iin(4, 23), check_if_Iin(4, 24),
                      check_if_Iin(4, 25), check_if_Iin(4, 26), check_if_Iin(4, 27), check_if_Iin(4, 28),
                      check_if_Iin(4, 29), check_if_Iin(4, 30), check_if_Iin(4, 31), check_if_Iin(4, 32),
                      check_if_Iin(4, 33), check_if_Iin(4, 34), check_if_Iin(4, 35), check_if_Iin(4, 36),
                      check_if_Iin(4, 37), check_if_Iin(4, 38), check_if_Iin(4, 39), check_if_Iin(4, 40),
                      check_if_Iin(4, 41), check_if_Iin(4, 42), check_if_Iin(4, 43), check_if_Iin(4, 44),
                      check_if_Iin(4, 45), check_if_Iin(4, 46), check_if_Iin(4, 47), check_if_Iin(4, 48),
                      check_if_Iin(4, 49), check_if_Iin(4, 50)], ignore_index=True)
    return data


def check_I5():
    data = pd.concat([check_if_Iin(5, 0), check_if_Iin(5, 1), check_if_Iin(5, 2), check_if_Iin(5, 3),
                      check_if_Iin(5, 4), check_if_Iin(5, 6), check_if_Iin(5, 7), check_if_Iin(5, 8),
                      check_if_Iin(5, 9), check_if_Iin(5, 10), check_if_Iin(5, 11), check_if_Iin(5, 12),
                      check_if_Iin(5, 13), check_if_Iin(5, 14), check_if_Iin(5, 15), check_if_Iin(5, 16),
                      check_if_Iin(5, 17), check_if_Iin(5, 18), check_if_Iin(5, 19), check_if_Iin(5, 20),
                      check_if_Iin(5, 21), check_if_Iin(5, 22), check_if_Iin(5, 23), check_if_Iin(5, 24),
                      check_if_Iin(5, 25), check_if_Iin(5, 26), check_if_Iin(5, 27), check_if_Iin(5, 28),
                      check_if_Iin(5, 29), check_if_Iin(5, 30), check_if_Iin(5, 31), check_if_Iin(5, 32),
                      check_if_Iin(5, 33), check_if_Iin(5, 34), check_if_Iin(5, 35), check_if_Iin(5, 36),
                      check_if_Iin(5, 37), check_if_Iin(5, 38), check_if_Iin(5, 39), check_if_Iin(5, 40),
                      check_if_Iin(5, 41), check_if_Iin(5, 42), check_if_Iin(5, 43), check_if_Iin(5, 44),
                      check_if_Iin(5, 45), check_if_Iin(5, 46), check_if_Iin(5, 47), check_if_Iin(5, 48),
                      check_if_Iin(5, 49), check_if_Iin(5, 50)], ignore_index=True)
    return data


def check_I6():
    data = pd.concat([check_if_Iin(6, 0), check_if_Iin(6, 1), check_if_Iin(6, 2), check_if_Iin(6, 3),
                      check_if_Iin(6, 4), check_if_Iin(6, 5), check_if_Iin(6, 7), check_if_Iin(6, 8),
                      check_if_Iin(6, 9), check_if_Iin(6, 10), check_if_Iin(6, 11), check_if_Iin(6, 12),
                      check_if_Iin(6, 13), check_if_Iin(6, 14), check_if_Iin(6, 15), check_if_Iin(6, 16),
                      check_if_Iin(6, 17), check_if_Iin(6, 18), check_if_Iin(6, 19), check_if_Iin(6, 20),
                      check_if_Iin(6, 21), check_if_Iin(6, 22), check_if_Iin(6, 23), check_if_Iin(6, 24),
                      check_if_Iin(6, 25), check_if_Iin(6, 26), check_if_Iin(6, 27), check_if_Iin(6, 28),
                      check_if_Iin(6, 29), check_if_Iin(6, 30), check_if_Iin(6, 31), check_if_Iin(6, 32),
                      check_if_Iin(6, 33), check_if_Iin(6, 34), check_if_Iin(6, 35), check_if_Iin(6, 36),
                      check_if_Iin(6, 37), check_if_Iin(6, 38), check_if_Iin(6, 39), check_if_Iin(6, 40),
                      check_if_Iin(6, 41), check_if_Iin(6, 42), check_if_Iin(6, 43), check_if_Iin(6, 44),
                      check_if_Iin(6, 45), check_if_Iin(6, 46), check_if_Iin(6, 47), check_if_Iin(6, 48),
                      check_if_Iin(6, 49), check_if_Iin(6, 50)], ignore_index=True)
    return data


def check_I7():
    data = pd.concat([check_if_Iin(7, 0), check_if_Iin(7, 1), check_if_Iin(7, 2), check_if_Iin(7, 3),
                      check_if_Iin(7, 4), check_if_Iin(7, 5), check_if_Iin(7, 6), check_if_Iin(7, 8),
                      check_if_Iin(7, 9), check_if_Iin(7, 10), check_if_Iin(7, 11), check_if_Iin(7, 12),
                      check_if_Iin(7, 13), check_if_Iin(7, 14), check_if_Iin(7, 15), check_if_Iin(7, 16),
                      check_if_Iin(7, 17), check_if_Iin(7, 18), check_if_Iin(7, 19), check_if_Iin(7, 20),
                      check_if_Iin(7, 21), check_if_Iin(7, 22), check_if_Iin(7, 23), check_if_Iin(7, 24),
                      check_if_Iin(7, 25), check_if_Iin(7, 26), check_if_Iin(7, 27), check_if_Iin(7, 28),
                      check_if_Iin(7, 29), check_if_Iin(7, 30), check_if_Iin(7, 31), check_if_Iin(7, 32),
                      check_if_Iin(7, 33), check_if_Iin(7, 34), check_if_Iin(7, 35), check_if_Iin(7, 36),
                      check_if_Iin(7, 37), check_if_Iin(7, 38), check_if_Iin(7, 39), check_if_Iin(7, 40),
                      check_if_Iin(7, 41), check_if_Iin(7, 42), check_if_Iin(7, 43), check_if_Iin(7, 44),
                      check_if_Iin(7, 45), check_if_Iin(7, 46), check_if_Iin(7, 47), check_if_Iin(7, 48),
                      check_if_Iin(7, 49), check_if_Iin(7, 50)], ignore_index=True)
    return data


def check_I8():
    data = pd.concat([check_if_Iin(8, 0), check_if_Iin(8, 1), check_if_Iin(8, 2), check_if_Iin(8, 3),
                      check_if_Iin(8, 4), check_if_Iin(8, 5), check_if_Iin(8, 6), check_if_Iin(8, 7),
                      check_if_Iin(8, 9), check_if_Iin(8, 10), check_if_Iin(8, 11), check_if_Iin(8, 12),
                      check_if_Iin(8, 13), check_if_Iin(8, 14), check_if_Iin(8, 15), check_if_Iin(8, 16),
                      check_if_Iin(8, 17), check_if_Iin(8, 18), check_if_Iin(8, 19), check_if_Iin(8, 20),
                      check_if_Iin(8, 21), check_if_Iin(8, 22), check_if_Iin(8, 23), check_if_Iin(8, 24),
                      check_if_Iin(8, 25), check_if_Iin(8, 26), check_if_Iin(8, 27), check_if_Iin(8, 28),
                      check_if_Iin(8, 29), check_if_Iin(8, 30), check_if_Iin(8, 31), check_if_Iin(8, 32),
                      check_if_Iin(8, 33), check_if_Iin(8, 34), check_if_Iin(8, 35), check_if_Iin(8, 36),
                      check_if_Iin(8, 37), check_if_Iin(8, 38), check_if_Iin(8, 39), check_if_Iin(8, 40),
                      check_if_Iin(8, 41), check_if_Iin(8, 42), check_if_Iin(8, 43), check_if_Iin(8, 44),
                      check_if_Iin(8, 45), check_if_Iin(8, 46), check_if_Iin(8, 47), check_if_Iin(8, 48),
                      check_if_Iin(8, 49), check_if_Iin(8, 50)], ignore_index=True)
    return data


def check_I9():
    data = pd.concat([check_if_Iin(9, 0), check_if_Iin(9, 1), check_if_Iin(9, 2), check_if_Iin(9, 3),
                      check_if_Iin(9, 4), check_if_Iin(9, 5), check_if_Iin(9, 6), check_if_Iin(9, 7),
                      check_if_Iin(9, 8), check_if_Iin(9, 10), check_if_Iin(9, 11), check_if_Iin(9, 12),
                      check_if_Iin(9, 13), check_if_Iin(9, 14), check_if_Iin(9, 15), check_if_Iin(9, 16),
                      check_if_Iin(9, 17), check_if_Iin(9, 18), check_if_Iin(9, 19), check_if_Iin(9, 20),
                      check_if_Iin(9, 21), check_if_Iin(9, 22), check_if_Iin(9, 23), check_if_Iin(9, 24),
                      check_if_Iin(9, 25), check_if_Iin(9, 26), check_if_Iin(9, 27), check_if_Iin(9, 28),
                      check_if_Iin(9, 29), check_if_Iin(9, 30), check_if_Iin(9, 31), check_if_Iin(9, 32),
                      check_if_Iin(9, 33), check_if_Iin(9, 34), check_if_Iin(9, 35), check_if_Iin(9, 36),
                      check_if_Iin(9, 37), check_if_Iin(9, 38), check_if_Iin(9, 39), check_if_Iin(9, 40),
                      check_if_Iin(9, 41), check_if_Iin(9, 42), check_if_Iin(9, 43), check_if_Iin(9, 44),
                      check_if_Iin(9, 45), check_if_Iin(9, 46), check_if_Iin(9, 47), check_if_Iin(9, 48),
                      check_if_Iin(9, 49), check_if_Iin(9, 50)], ignore_index=True)
    return data


def check_I10():
    data = pd.concat([check_if_Iin(10, 0), check_if_Iin(10, 1), check_if_Iin(10, 2), check_if_Iin(10, 3),
                      check_if_Iin(10, 4), check_if_Iin(10, 5), check_if_Iin(10, 6), check_if_Iin(10, 7),
                      check_if_Iin(10, 8), check_if_Iin(10, 9), check_if_Iin(10, 11), check_if_Iin(10, 12),
                      check_if_Iin(10, 13), check_if_Iin(10, 14), check_if_Iin(10, 15), check_if_Iin(10, 16),
                      check_if_Iin(10, 17), check_if_Iin(10, 18), check_if_Iin(10, 19), check_if_Iin(10, 20),
                      check_if_Iin(10, 21), check_if_Iin(10, 22), check_if_Iin(10, 23), check_if_Iin(10, 24),
                      check_if_Iin(10, 25), check_if_Iin(10, 26), check_if_Iin(10, 27), check_if_Iin(10, 28),
                      check_if_Iin(10, 29), check_if_Iin(10, 30), check_if_Iin(10, 31), check_if_Iin(10, 32),
                      check_if_Iin(10, 33), check_if_Iin(10, 34), check_if_Iin(10, 35), check_if_Iin(10, 36),
                      check_if_Iin(10, 37), check_if_Iin(10, 38), check_if_Iin(10, 39), check_if_Iin(10, 40),
                      check_if_Iin(10, 41), check_if_Iin(10, 42), check_if_Iin(10, 43), check_if_Iin(10, 44),
                      check_if_Iin(10, 45), check_if_Iin(10, 46), check_if_Iin(10, 47), check_if_Iin(10, 48),
                      check_if_Iin(10, 49), check_if_Iin(10, 50)], ignore_index=True)
    return data


def check_I11():
    data = pd.concat([check_if_Iin(11, 0), check_if_Iin(11, 1), check_if_Iin(11, 2), check_if_Iin(11, 3),
                      check_if_Iin(11, 4), check_if_Iin(11, 5), check_if_Iin(11, 6), check_if_Iin(11, 7),
                      check_if_Iin(11, 8), check_if_Iin(11, 9), check_if_Iin(11, 10), check_if_Iin(11, 12),
                      check_if_Iin(11, 13), check_if_Iin(11, 14), check_if_Iin(11, 15), check_if_Iin(11, 16),
                      check_if_Iin(11, 17), check_if_Iin(11, 18), check_if_Iin(11, 19), check_if_Iin(11, 20),
                      check_if_Iin(11, 21), check_if_Iin(11, 22), check_if_Iin(11, 23), check_if_Iin(11, 24),
                      check_if_Iin(11, 25), check_if_Iin(11, 26), check_if_Iin(11, 27), check_if_Iin(11, 28),
                      check_if_Iin(11, 29), check_if_Iin(11, 30), check_if_Iin(11, 31), check_if_Iin(11, 32),
                      check_if_Iin(11, 33), check_if_Iin(11, 34), check_if_Iin(11, 35), check_if_Iin(11, 36),
                      check_if_Iin(11, 37), check_if_Iin(11, 38), check_if_Iin(11, 39), check_if_Iin(11, 40),
                      check_if_Iin(11, 41), check_if_Iin(11, 42), check_if_Iin(11, 43), check_if_Iin(11, 44),
                      check_if_Iin(11, 45), check_if_Iin(11, 46), check_if_Iin(11, 47), check_if_Iin(11, 48),
                      check_if_Iin(11, 49), check_if_Iin(11, 50)], ignore_index=True)
    return data


def check_I12():
    data = pd.concat([check_if_Iin(12, 0), check_if_Iin(12, 1), check_if_Iin(12, 2), check_if_Iin(12, 3),
                      check_if_Iin(12, 4), check_if_Iin(12, 5), check_if_Iin(12, 6), check_if_Iin(12, 7),
                      check_if_Iin(12, 8), check_if_Iin(12, 9), check_if_Iin(12, 10), check_if_Iin(12, 11),
                      check_if_Iin(12, 13), check_if_Iin(12, 14), check_if_Iin(12, 15), check_if_Iin(12, 16),
                      check_if_Iin(12, 17), check_if_Iin(12, 18), check_if_Iin(12, 19), check_if_Iin(12, 20),
                      check_if_Iin(12, 21), check_if_Iin(12, 22), check_if_Iin(12, 23), check_if_Iin(12, 24),
                      check_if_Iin(12, 25), check_if_Iin(12, 26), check_if_Iin(12, 27), check_if_Iin(12, 28),
                      check_if_Iin(12, 29), check_if_Iin(12, 30), check_if_Iin(12, 31), check_if_Iin(12, 32),
                      check_if_Iin(12, 33), check_if_Iin(12, 34), check_if_Iin(12, 35), check_if_Iin(12, 36),
                      check_if_Iin(12, 37), check_if_Iin(12, 38), check_if_Iin(12, 39), check_if_Iin(12, 40),
                      check_if_Iin(12, 41), check_if_Iin(12, 42), check_if_Iin(12, 43), check_if_Iin(12, 44),
                      check_if_Iin(12, 45), check_if_Iin(12, 46), check_if_Iin(12, 47), check_if_Iin(12, 48),
                      check_if_Iin(12, 49), check_if_Iin(12, 50)], ignore_index=True)
    return data


def check_I13():
    data = pd.concat([check_if_Iin(13, 0), check_if_Iin(13, 1), check_if_Iin(13, 2), check_if_Iin(13, 3),
                      check_if_Iin(13, 4), check_if_Iin(13, 5), check_if_Iin(13, 6), check_if_Iin(13, 7),
                      check_if_Iin(13, 8), check_if_Iin(13, 9), check_if_Iin(13, 10), check_if_Iin(13, 11),
                      check_if_Iin(13, 12), check_if_Iin(13, 14), check_if_Iin(13, 15), check_if_Iin(13, 16),
                      check_if_Iin(13, 17), check_if_Iin(13, 18), check_if_Iin(13, 19), check_if_Iin(13, 20),
                      check_if_Iin(13, 21), check_if_Iin(13, 22), check_if_Iin(13, 23), check_if_Iin(13, 24),
                      check_if_Iin(13, 25), check_if_Iin(13, 26), check_if_Iin(13, 27), check_if_Iin(13, 28),
                      check_if_Iin(13, 29), check_if_Iin(13, 30), check_if_Iin(13, 31), check_if_Iin(13, 32),
                      check_if_Iin(13, 33), check_if_Iin(13, 34), check_if_Iin(13, 35), check_if_Iin(13, 36),
                      check_if_Iin(13, 37), check_if_Iin(13, 38), check_if_Iin(13, 39), check_if_Iin(13, 40),
                      check_if_Iin(13, 41), check_if_Iin(13, 42), check_if_Iin(13, 43), check_if_Iin(13, 44),
                      check_if_Iin(13, 45), check_if_Iin(13, 46), check_if_Iin(13, 47), check_if_Iin(13, 48),
                      check_if_Iin(13, 49), check_if_Iin(13, 50)], ignore_index=True)
    return data


def check_I14():
    data = pd.concat([check_if_Iin(14, 0), check_if_Iin(14, 1), check_if_Iin(14, 2), check_if_Iin(14, 3),
                      check_if_Iin(14, 4), check_if_Iin(14, 5), check_if_Iin(14, 6), check_if_Iin(14, 7),
                      check_if_Iin(14, 8), check_if_Iin(14, 9), check_if_Iin(14, 10), check_if_Iin(14, 11),
                      check_if_Iin(14, 12), check_if_Iin(14, 13), check_if_Iin(14, 15), check_if_Iin(14, 16),
                      check_if_Iin(14, 17), check_if_Iin(14, 18), check_if_Iin(14, 19), check_if_Iin(14, 20),
                      check_if_Iin(14, 21), check_if_Iin(14, 22), check_if_Iin(14, 23), check_if_Iin(14, 24),
                      check_if_Iin(14, 25), check_if_Iin(14, 26), check_if_Iin(14, 27), check_if_Iin(14, 28),
                      check_if_Iin(14, 29), check_if_Iin(14, 30), check_if_Iin(14, 31), check_if_Iin(14, 32),
                      check_if_Iin(14, 33), check_if_Iin(14, 34), check_if_Iin(14, 35), check_if_Iin(14, 36),
                      check_if_Iin(14, 37), check_if_Iin(14, 38), check_if_Iin(14, 39), check_if_Iin(14, 40),
                      check_if_Iin(14, 41), check_if_Iin(14, 42), check_if_Iin(14, 43), check_if_Iin(14, 44),
                      check_if_Iin(14, 45), check_if_Iin(14, 46), check_if_Iin(14, 47), check_if_Iin(14, 48),
                      check_if_Iin(14, 49), check_if_Iin(14, 50)], ignore_index=True)
    return data


def check_I15():
    data = pd.concat([check_if_Iin(15, 0), check_if_Iin(15, 1), check_if_Iin(15, 2), check_if_Iin(15, 3),
                      check_if_Iin(15, 4), check_if_Iin(15, 5), check_if_Iin(15, 6), check_if_Iin(15, 7),
                      check_if_Iin(15, 8), check_if_Iin(15, 9), check_if_Iin(15, 10), check_if_Iin(15, 11),
                      check_if_Iin(15, 12), check_if_Iin(15, 13), check_if_Iin(15, 14), check_if_Iin(15, 16),
                      check_if_Iin(15, 17), check_if_Iin(15, 18), check_if_Iin(15, 19), check_if_Iin(15, 20),
                      check_if_Iin(15, 21), check_if_Iin(15, 22), check_if_Iin(15, 23), check_if_Iin(15, 24),
                      check_if_Iin(15, 25), check_if_Iin(15, 26), check_if_Iin(15, 27), check_if_Iin(15, 28),
                      check_if_Iin(15, 29), check_if_Iin(15, 30), check_if_Iin(15, 31), check_if_Iin(15, 32),
                      check_if_Iin(15, 33), check_if_Iin(15, 34), check_if_Iin(15, 35), check_if_Iin(15, 36),
                      check_if_Iin(15, 37), check_if_Iin(15, 38), check_if_Iin(15, 39), check_if_Iin(15, 40),
                      check_if_Iin(15, 41), check_if_Iin(15, 42), check_if_Iin(15, 43), check_if_Iin(15, 44),
                      check_if_Iin(15, 45), check_if_Iin(15, 46), check_if_Iin(15, 47), check_if_Iin(15, 48),
                      check_if_Iin(15, 49), check_if_Iin(15, 50)], ignore_index=True)
    return data


def check_I16():
    data = pd.concat([check_if_Iin(16, 0), check_if_Iin(16, 1), check_if_Iin(16, 2), check_if_Iin(16, 3),
                      check_if_Iin(16, 4), check_if_Iin(16, 5), check_if_Iin(16, 6), check_if_Iin(16, 7),
                      check_if_Iin(16, 8), check_if_Iin(16, 9), check_if_Iin(16, 10), check_if_Iin(16, 11),
                      check_if_Iin(16, 12), check_if_Iin(16, 13), check_if_Iin(16, 14), check_if_Iin(16, 15),
                      check_if_Iin(16, 17), check_if_Iin(16, 18), check_if_Iin(16, 19), check_if_Iin(16, 20),
                      check_if_Iin(16, 21), check_if_Iin(16, 22), check_if_Iin(16, 23), check_if_Iin(16, 24),
                      check_if_Iin(16, 25), check_if_Iin(16, 26), check_if_Iin(16, 27), check_if_Iin(16, 28),
                      check_if_Iin(16, 29), check_if_Iin(16, 30), check_if_Iin(16, 31), check_if_Iin(16, 32),
                      check_if_Iin(16, 33), check_if_Iin(16, 34), check_if_Iin(16, 35), check_if_Iin(16, 36),
                      check_if_Iin(16, 37), check_if_Iin(16, 38), check_if_Iin(16, 39), check_if_Iin(16, 40),
                      check_if_Iin(16, 41), check_if_Iin(16, 42), check_if_Iin(16, 43), check_if_Iin(16, 44),
                      check_if_Iin(16, 45), check_if_Iin(16, 46), check_if_Iin(16, 47), check_if_Iin(16, 48),
                      check_if_Iin(16, 49), check_if_Iin(16, 50)], ignore_index=True)
    return data


def check_I17():
    data = pd.concat([check_if_Iin(17, 0), check_if_Iin(17, 1), check_if_Iin(17, 2), check_if_Iin(17, 3),
                      check_if_Iin(17, 4), check_if_Iin(17, 5), check_if_Iin(17, 6), check_if_Iin(17, 7),
                      check_if_Iin(17, 8), check_if_Iin(17, 9), check_if_Iin(17, 10), check_if_Iin(17, 11),
                      check_if_Iin(17, 12), check_if_Iin(17, 13), check_if_Iin(17, 14), check_if_Iin(17, 15),
                      check_if_Iin(17, 16), check_if_Iin(17, 18), check_if_Iin(17, 19), check_if_Iin(17, 20),
                      check_if_Iin(17, 21), check_if_Iin(17, 22), check_if_Iin(17, 23), check_if_Iin(17, 24),
                      check_if_Iin(17, 25), check_if_Iin(17, 26), check_if_Iin(17, 27), check_if_Iin(17, 28),
                      check_if_Iin(17, 29), check_if_Iin(17, 30), check_if_Iin(17, 31), check_if_Iin(17, 32),
                      check_if_Iin(17, 33), check_if_Iin(17, 34), check_if_Iin(17, 35), check_if_Iin(17, 36),
                      check_if_Iin(17, 37), check_if_Iin(17, 38), check_if_Iin(17, 39), check_if_Iin(17, 40),
                      check_if_Iin(17, 41), check_if_Iin(17, 42), check_if_Iin(17, 43), check_if_Iin(17, 44),
                      check_if_Iin(17, 45), check_if_Iin(17, 46), check_if_Iin(17, 47), check_if_Iin(17, 48),
                      check_if_Iin(17, 49), check_if_Iin(17, 50)], ignore_index=True)
    return data


def check_I18():
    data = pd.concat([check_if_Iin(18, 0), check_if_Iin(18, 1), check_if_Iin(18, 2), check_if_Iin(18, 3),
                      check_if_Iin(18, 4), check_if_Iin(18, 5), check_if_Iin(18, 6), check_if_Iin(18, 7),
                      check_if_Iin(18, 8), check_if_Iin(18, 9), check_if_Iin(18, 10), check_if_Iin(18, 11),
                      check_if_Iin(18, 12), check_if_Iin(18, 13), check_if_Iin(18, 14), check_if_Iin(18, 15),
                      check_if_Iin(18, 16), check_if_Iin(18, 17), check_if_Iin(18, 19), check_if_Iin(18, 20),
                      check_if_Iin(18, 21), check_if_Iin(18, 22), check_if_Iin(18, 23), check_if_Iin(18, 24),
                      check_if_Iin(18, 25), check_if_Iin(18, 26), check_if_Iin(18, 27), check_if_Iin(18, 28),
                      check_if_Iin(18, 29), check_if_Iin(18, 30), check_if_Iin(18, 31), check_if_Iin(18, 32),
                      check_if_Iin(18, 33), check_if_Iin(18, 34), check_if_Iin(18, 35), check_if_Iin(18, 36),
                      check_if_Iin(18, 37), check_if_Iin(18, 38), check_if_Iin(18, 39), check_if_Iin(18, 40),
                      check_if_Iin(18, 41), check_if_Iin(18, 42), check_if_Iin(18, 43), check_if_Iin(18, 44),
                      check_if_Iin(18, 45), check_if_Iin(18, 46), check_if_Iin(18, 47), check_if_Iin(18, 48),
                      check_if_Iin(18, 49), check_if_Iin(18, 50)], ignore_index=True)
    return data


def check_I19():
    data = pd.concat([check_if_Iin(19, 0), check_if_Iin(19, 1), check_if_Iin(19, 2), check_if_Iin(19, 3),
                      check_if_Iin(19, 4), check_if_Iin(19, 5), check_if_Iin(19, 6), check_if_Iin(19, 7),
                      check_if_Iin(19, 8), check_if_Iin(19, 9), check_if_Iin(19, 10), check_if_Iin(19, 11),
                      check_if_Iin(19, 12), check_if_Iin(19, 13), check_if_Iin(19, 14), check_if_Iin(19, 15),
                      check_if_Iin(19, 16), check_if_Iin(19, 17), check_if_Iin(19, 18), check_if_Iin(19, 20),
                      check_if_Iin(19, 21), check_if_Iin(19, 22), check_if_Iin(19, 23), check_if_Iin(19, 24),
                      check_if_Iin(19, 25), check_if_Iin(19, 26), check_if_Iin(19, 27), check_if_Iin(19, 28),
                      check_if_Iin(19, 29), check_if_Iin(19, 30), check_if_Iin(19, 31), check_if_Iin(19, 32),
                      check_if_Iin(19, 33), check_if_Iin(19, 34), check_if_Iin(19, 35), check_if_Iin(19, 36),
                      check_if_Iin(19, 37), check_if_Iin(19, 38), check_if_Iin(19, 39), check_if_Iin(19, 40),
                      check_if_Iin(19, 41), check_if_Iin(19, 42), check_if_Iin(19, 43), check_if_Iin(19, 44),
                      check_if_Iin(19, 45), check_if_Iin(19, 46), check_if_Iin(19, 47), check_if_Iin(19, 48),
                      check_if_Iin(19, 49), check_if_Iin(19, 50)], ignore_index=True)
    return data


def check_I20():
    data = pd.concat([check_if_Iin(20, 0), check_if_Iin(20, 1), check_if_Iin(20, 2), check_if_Iin(20, 3),
                      check_if_Iin(20, 4), check_if_Iin(20, 5), check_if_Iin(20, 6), check_if_Iin(20, 7),
                      check_if_Iin(20, 8), check_if_Iin(20, 9), check_if_Iin(20, 10), check_if_Iin(20, 11),
                      check_if_Iin(20, 12), check_if_Iin(20, 13), check_if_Iin(20, 14), check_if_Iin(20, 15),
                      check_if_Iin(20, 16), check_if_Iin(20, 17), check_if_Iin(20, 18), check_if_Iin(20, 19),
                      check_if_Iin(20, 21), check_if_Iin(20, 22), check_if_Iin(20, 23), check_if_Iin(20, 24),
                      check_if_Iin(20, 25), check_if_Iin(20, 26), check_if_Iin(20, 27), check_if_Iin(20, 28),
                      check_if_Iin(20, 29), check_if_Iin(20, 30), check_if_Iin(20, 31), check_if_Iin(20, 32),
                      check_if_Iin(20, 33), check_if_Iin(20, 34), check_if_Iin(20, 35), check_if_Iin(20, 36),
                      check_if_Iin(20, 37), check_if_Iin(20, 38), check_if_Iin(20, 39), check_if_Iin(20, 40),
                      check_if_Iin(20, 41), check_if_Iin(20, 42), check_if_Iin(20, 43), check_if_Iin(20, 44),
                      check_if_Iin(20, 45), check_if_Iin(20, 46), check_if_Iin(20, 47), check_if_Iin(20, 48),
                      check_if_Iin(20, 49), check_if_Iin(20, 50)], ignore_index=True)
    return data


def check_I21():
    data = pd.concat([check_if_Iin(21, 0), check_if_Iin(21, 1), check_if_Iin(21, 2), check_if_Iin(21, 3),
                      check_if_Iin(21, 4), check_if_Iin(21, 5), check_if_Iin(21, 6), check_if_Iin(21, 7),
                      check_if_Iin(21, 8), check_if_Iin(21, 9), check_if_Iin(21, 10), check_if_Iin(21, 11),
                      check_if_Iin(21, 12), check_if_Iin(21, 13), check_if_Iin(21, 14), check_if_Iin(21, 15),
                      check_if_Iin(21, 16), check_if_Iin(21, 17), check_if_Iin(21, 18), check_if_Iin(21, 19),
                      check_if_Iin(21, 20), check_if_Iin(21, 22), check_if_Iin(21, 23), check_if_Iin(21, 24),
                      check_if_Iin(21, 25), check_if_Iin(21, 26), check_if_Iin(21, 27), check_if_Iin(21, 28),
                      check_if_Iin(21, 29), check_if_Iin(21, 30), check_if_Iin(21, 31), check_if_Iin(21, 32),
                      check_if_Iin(21, 33), check_if_Iin(21, 34), check_if_Iin(21, 35), check_if_Iin(21, 36),
                      check_if_Iin(21, 37), check_if_Iin(21, 38), check_if_Iin(21, 39), check_if_Iin(21, 40),
                      check_if_Iin(21, 41), check_if_Iin(21, 42), check_if_Iin(21, 43), check_if_Iin(21, 44),
                      check_if_Iin(21, 45), check_if_Iin(21, 46), check_if_Iin(21, 47), check_if_Iin(21, 48),
                      check_if_Iin(21, 49), check_if_Iin(21, 50)], ignore_index=True)
    return data


def check_I22():
    data = pd.concat([check_if_Iin(22, 0), check_if_Iin(22, 1), check_if_Iin(22, 2), check_if_Iin(22, 3),
                      check_if_Iin(22, 4), check_if_Iin(22, 5), check_if_Iin(22, 6), check_if_Iin(22, 7),
                      check_if_Iin(22, 8), check_if_Iin(22, 9), check_if_Iin(22, 10), check_if_Iin(22, 11),
                      check_if_Iin(22, 12), check_if_Iin(22, 13), check_if_Iin(22, 14), check_if_Iin(22, 15),
                      check_if_Iin(22, 16), check_if_Iin(22, 17), check_if_Iin(22, 18), check_if_Iin(22, 19),
                      check_if_Iin(22, 20), check_if_Iin(22, 21), check_if_Iin(22, 23), check_if_Iin(22, 24),
                      check_if_Iin(22, 25), check_if_Iin(22, 26), check_if_Iin(22, 27), check_if_Iin(22, 28),
                      check_if_Iin(22, 29), check_if_Iin(22, 30), check_if_Iin(22, 31), check_if_Iin(22, 32),
                      check_if_Iin(22, 33), check_if_Iin(22, 34), check_if_Iin(22, 35), check_if_Iin(22, 36),
                      check_if_Iin(22, 37), check_if_Iin(22, 38), check_if_Iin(22, 39), check_if_Iin(22, 40),
                      check_if_Iin(22, 41), check_if_Iin(22, 42), check_if_Iin(22, 43), check_if_Iin(22, 44),
                      check_if_Iin(22, 45), check_if_Iin(22, 46), check_if_Iin(22, 47), check_if_Iin(22, 48),
                      check_if_Iin(22, 49), check_if_Iin(22, 50)], ignore_index=True)
    return data


def check_I23():
    data = pd.concat([check_if_Iin(23, 0), check_if_Iin(23, 1), check_if_Iin(23, 2), check_if_Iin(23, 3),
                      check_if_Iin(23, 4), check_if_Iin(23, 5), check_if_Iin(23, 6), check_if_Iin(23, 7),
                      check_if_Iin(23, 8), check_if_Iin(23, 9), check_if_Iin(23, 10), check_if_Iin(23, 11),
                      check_if_Iin(23, 12), check_if_Iin(23, 13), check_if_Iin(23, 14), check_if_Iin(23, 15),
                      check_if_Iin(23, 16), check_if_Iin(23, 17), check_if_Iin(23, 18), check_if_Iin(23, 19),
                      check_if_Iin(23, 20), check_if_Iin(23, 21), check_if_Iin(23, 22), check_if_Iin(23, 24),
                      check_if_Iin(23, 25), check_if_Iin(23, 26), check_if_Iin(23, 27), check_if_Iin(23, 28),
                      check_if_Iin(23, 29), check_if_Iin(23, 30), check_if_Iin(23, 31), check_if_Iin(23, 32),
                      check_if_Iin(23, 33), check_if_Iin(23, 34), check_if_Iin(23, 35), check_if_Iin(23, 36),
                      check_if_Iin(23, 37), check_if_Iin(23, 38), check_if_Iin(23, 39), check_if_Iin(23, 40),
                      check_if_Iin(23, 41), check_if_Iin(23, 42), check_if_Iin(23, 43), check_if_Iin(23, 44),
                      check_if_Iin(23, 45), check_if_Iin(23, 46), check_if_Iin(23, 47), check_if_Iin(23, 48),
                      check_if_Iin(23, 49), check_if_Iin(23, 50)], ignore_index=True)
    return data


def check_I24():
    data = pd.concat([check_if_Iin(24, 0), check_if_Iin(24, 1), check_if_Iin(24, 2), check_if_Iin(24, 3),
                      check_if_Iin(24, 4), check_if_Iin(24, 5), check_if_Iin(24, 6), check_if_Iin(24, 7),
                      check_if_Iin(24, 8), check_if_Iin(24, 9), check_if_Iin(24, 10), check_if_Iin(24, 11),
                      check_if_Iin(24, 12), check_if_Iin(24, 13), check_if_Iin(24, 14), check_if_Iin(24, 15),
                      check_if_Iin(24, 16), check_if_Iin(24, 17), check_if_Iin(24, 18), check_if_Iin(24, 19),
                      check_if_Iin(24, 20), check_if_Iin(24, 21), check_if_Iin(24, 22), check_if_Iin(24, 23),
                      check_if_Iin(24, 25), check_if_Iin(24, 26), check_if_Iin(24, 27), check_if_Iin(24, 28),
                      check_if_Iin(24, 29), check_if_Iin(24, 30), check_if_Iin(24, 31), check_if_Iin(24, 32),
                      check_if_Iin(24, 33), check_if_Iin(24, 34), check_if_Iin(24, 35), check_if_Iin(24, 36),
                      check_if_Iin(24, 37), check_if_Iin(24, 38), check_if_Iin(24, 39), check_if_Iin(24, 40),
                      check_if_Iin(24, 41), check_if_Iin(24, 42), check_if_Iin(24, 43), check_if_Iin(24, 44),
                      check_if_Iin(24, 45), check_if_Iin(24, 46), check_if_Iin(24, 47), check_if_Iin(24, 48),
                      check_if_Iin(24, 49), check_if_Iin(24, 50)], ignore_index=True)
    return data


def check_I25():
    data = pd.concat([check_if_Iin(25, 0), check_if_Iin(25, 1), check_if_Iin(25, 2), check_if_Iin(25, 3),
                      check_if_Iin(25, 4), check_if_Iin(25, 5), check_if_Iin(25, 6), check_if_Iin(25, 7),
                      check_if_Iin(25, 8), check_if_Iin(25, 9), check_if_Iin(25, 10), check_if_Iin(25, 11),
                      check_if_Iin(25, 12), check_if_Iin(25, 13), check_if_Iin(25, 14), check_if_Iin(25, 15),
                      check_if_Iin(25, 16), check_if_Iin(25, 17), check_if_Iin(25, 18), check_if_Iin(25, 19),
                      check_if_Iin(25, 20), check_if_Iin(25, 21), check_if_Iin(25, 22), check_if_Iin(25, 23),
                      check_if_Iin(25, 24), check_if_Iin(25, 26), check_if_Iin(25, 27), check_if_Iin(25, 28),
                      check_if_Iin(25, 29), check_if_Iin(25, 30), check_if_Iin(25, 31), check_if_Iin(25, 32),
                      check_if_Iin(25, 33), check_if_Iin(25, 34), check_if_Iin(25, 35), check_if_Iin(25, 36),
                      check_if_Iin(25, 37), check_if_Iin(25, 38), check_if_Iin(25, 39), check_if_Iin(25, 40),
                      check_if_Iin(25, 41), check_if_Iin(25, 42), check_if_Iin(25, 43), check_if_Iin(25, 44),
                      check_if_Iin(25, 45), check_if_Iin(25, 46), check_if_Iin(25, 47), check_if_Iin(25, 48),
                      check_if_Iin(25, 49), check_if_Iin(25, 50)], ignore_index=True)
    return data


def check_I26():
    data = pd.concat([check_if_Iin(26, 0), check_if_Iin(26, 1), check_if_Iin(26, 2), check_if_Iin(26, 3),
                      check_if_Iin(26, 4), check_if_Iin(26, 5), check_if_Iin(26, 6), check_if_Iin(26, 7),
                      check_if_Iin(26, 8), check_if_Iin(26, 9), check_if_Iin(26, 10), check_if_Iin(26, 11),
                      check_if_Iin(26, 12), check_if_Iin(26, 13), check_if_Iin(26, 14), check_if_Iin(26, 15),
                      check_if_Iin(26, 16), check_if_Iin(26, 17), check_if_Iin(26, 18), check_if_Iin(26, 19),
                      check_if_Iin(26, 20), check_if_Iin(26, 21), check_if_Iin(26, 22), check_if_Iin(26, 23),
                      check_if_Iin(26, 24), check_if_Iin(26, 25), check_if_Iin(26, 27), check_if_Iin(26, 28),
                      check_if_Iin(26, 29), check_if_Iin(26, 30), check_if_Iin(26, 31), check_if_Iin(26, 32),
                      check_if_Iin(26, 33), check_if_Iin(26, 34), check_if_Iin(26, 35), check_if_Iin(26, 36),
                      check_if_Iin(26, 37), check_if_Iin(26, 38), check_if_Iin(26, 39), check_if_Iin(26, 40),
                      check_if_Iin(26, 41), check_if_Iin(26, 42), check_if_Iin(26, 43), check_if_Iin(26, 44),
                      check_if_Iin(26, 45), check_if_Iin(26, 46), check_if_Iin(26, 47), check_if_Iin(26, 48),
                      check_if_Iin(26, 49), check_if_Iin(26, 50)], ignore_index=True)
    return data


def check_I27():
    data = pd.concat([check_if_Iin(27, 0), check_if_Iin(27, 1), check_if_Iin(27, 2), check_if_Iin(27, 3),
                      check_if_Iin(27, 4), check_if_Iin(27, 5), check_if_Iin(27, 6), check_if_Iin(27, 7),
                      check_if_Iin(27, 8), check_if_Iin(27, 9), check_if_Iin(27, 10), check_if_Iin(27, 11),
                      check_if_Iin(27, 12), check_if_Iin(27, 13), check_if_Iin(27, 14), check_if_Iin(27, 15),
                      check_if_Iin(27, 16), check_if_Iin(27, 17), check_if_Iin(27, 18), check_if_Iin(27, 19),
                      check_if_Iin(27, 20), check_if_Iin(27, 21), check_if_Iin(27, 22), check_if_Iin(27, 23),
                      check_if_Iin(27, 24), check_if_Iin(27, 25), check_if_Iin(27, 26), check_if_Iin(27, 28),
                      check_if_Iin(27, 29), check_if_Iin(27, 30), check_if_Iin(27, 31), check_if_Iin(27, 32),
                      check_if_Iin(27, 33), check_if_Iin(27, 34), check_if_Iin(27, 35), check_if_Iin(27, 36),
                      check_if_Iin(27, 37), check_if_Iin(27, 38), check_if_Iin(27, 39), check_if_Iin(27, 40),
                      check_if_Iin(27, 41), check_if_Iin(27, 42), check_if_Iin(27, 43), check_if_Iin(27, 44),
                      check_if_Iin(27, 45), check_if_Iin(27, 46), check_if_Iin(27, 47), check_if_Iin(27, 48),
                      check_if_Iin(27, 49), check_if_Iin(27, 50)], ignore_index=True)
    return data


def check_I28():
    data = pd.concat([check_if_Iin(28, 0), check_if_Iin(28, 1), check_if_Iin(28, 2), check_if_Iin(28, 3),
                      check_if_Iin(28, 4), check_if_Iin(28, 5), check_if_Iin(28, 6), check_if_Iin(28, 7),
                      check_if_Iin(28, 8), check_if_Iin(28, 9), check_if_Iin(28, 10), check_if_Iin(28, 11),
                      check_if_Iin(28, 12), check_if_Iin(28, 13), check_if_Iin(28, 14), check_if_Iin(28, 15),
                      check_if_Iin(28, 16), check_if_Iin(28, 17), check_if_Iin(28, 18), check_if_Iin(28, 19),
                      check_if_Iin(28, 20), check_if_Iin(28, 21), check_if_Iin(28, 22), check_if_Iin(28, 23),
                      check_if_Iin(28, 24), check_if_Iin(28, 25), check_if_Iin(28, 26), check_if_Iin(28, 27),
                      check_if_Iin(28, 29), check_if_Iin(28, 30), check_if_Iin(28, 31), check_if_Iin(28, 32),
                      check_if_Iin(28, 33), check_if_Iin(28, 34), check_if_Iin(28, 35), check_if_Iin(28, 36),
                      check_if_Iin(28, 37), check_if_Iin(28, 38), check_if_Iin(28, 39), check_if_Iin(28, 40),
                      check_if_Iin(28, 41), check_if_Iin(28, 42), check_if_Iin(28, 43), check_if_Iin(28, 44),
                      check_if_Iin(28, 45), check_if_Iin(28, 46), check_if_Iin(28, 47), check_if_Iin(28, 48),
                      check_if_Iin(28, 49), check_if_Iin(28, 50)], ignore_index=True)
    return data


def check_I29():
    data = pd.concat([check_if_Iin(29, 0), check_if_Iin(29, 1), check_if_Iin(29, 2), check_if_Iin(29, 3),
                      check_if_Iin(29, 4), check_if_Iin(29, 5), check_if_Iin(29, 6), check_if_Iin(29, 7),
                      check_if_Iin(29, 8), check_if_Iin(29, 9), check_if_Iin(29, 10), check_if_Iin(29, 11),
                      check_if_Iin(29, 12), check_if_Iin(29, 13), check_if_Iin(29, 14), check_if_Iin(29, 15),
                      check_if_Iin(29, 16), check_if_Iin(29, 17), check_if_Iin(29, 18), check_if_Iin(29, 19),
                      check_if_Iin(29, 20), check_if_Iin(29, 21), check_if_Iin(29, 22), check_if_Iin(29, 23),
                      check_if_Iin(29, 24), check_if_Iin(29, 25), check_if_Iin(29, 26), check_if_Iin(29, 27),
                      check_if_Iin(29, 28), check_if_Iin(29, 30), check_if_Iin(29, 31), check_if_Iin(29, 32),
                      check_if_Iin(29, 33), check_if_Iin(29, 34), check_if_Iin(29, 35), check_if_Iin(29, 36),
                      check_if_Iin(29, 37), check_if_Iin(29, 38), check_if_Iin(29, 39), check_if_Iin(29, 40),
                      check_if_Iin(29, 41), check_if_Iin(29, 42), check_if_Iin(29, 43), check_if_Iin(29, 44),
                      check_if_Iin(29, 45), check_if_Iin(29, 46), check_if_Iin(29, 47), check_if_Iin(29, 48),
                      check_if_Iin(29, 49), check_if_Iin(29, 50)], ignore_index=True)
    return data


def check_I30():
    data = pd.concat([check_if_Iin(30, 0), check_if_Iin(30, 1), check_if_Iin(30, 2), check_if_Iin(30, 3),
                      check_if_Iin(30, 4), check_if_Iin(30, 5), check_if_Iin(30, 6), check_if_Iin(30, 7),
                      check_if_Iin(30, 8), check_if_Iin(30, 9), check_if_Iin(30, 10), check_if_Iin(30, 11),
                      check_if_Iin(30, 12), check_if_Iin(30, 13), check_if_Iin(30, 14), check_if_Iin(30, 15),
                      check_if_Iin(30, 16), check_if_Iin(30, 17), check_if_Iin(30, 18), check_if_Iin(30, 19),
                      check_if_Iin(30, 20), check_if_Iin(30, 21), check_if_Iin(30, 22), check_if_Iin(30, 23),
                      check_if_Iin(30, 24), check_if_Iin(30, 25), check_if_Iin(30, 26), check_if_Iin(30, 27),
                      check_if_Iin(30, 28), check_if_Iin(30, 29), check_if_Iin(30, 31), check_if_Iin(30, 32),
                      check_if_Iin(30, 33), check_if_Iin(30, 34), check_if_Iin(30, 35), check_if_Iin(30, 36),
                      check_if_Iin(30, 37), check_if_Iin(30, 38), check_if_Iin(30, 39), check_if_Iin(30, 40),
                      check_if_Iin(30, 41), check_if_Iin(30, 42), check_if_Iin(30, 43), check_if_Iin(30, 44),
                      check_if_Iin(30, 45), check_if_Iin(30, 46), check_if_Iin(30, 47), check_if_Iin(30, 48),
                      check_if_Iin(30, 49), check_if_Iin(30, 50)], ignore_index=True)
    return data


def check_I31():
    data = pd.concat([check_if_Iin(31, 0), check_if_Iin(31, 1), check_if_Iin(31, 2), check_if_Iin(31, 3),
                      check_if_Iin(31, 4), check_if_Iin(31, 5), check_if_Iin(31, 6), check_if_Iin(31, 7),
                      check_if_Iin(31, 8), check_if_Iin(31, 9), check_if_Iin(31, 10), check_if_Iin(31, 11),
                      check_if_Iin(31, 12), check_if_Iin(31, 13), check_if_Iin(31, 14), check_if_Iin(31, 15),
                      check_if_Iin(31, 16), check_if_Iin(31, 17), check_if_Iin(31, 18), check_if_Iin(31, 19),
                      check_if_Iin(31, 20), check_if_Iin(31, 21), check_if_Iin(31, 22), check_if_Iin(31, 23),
                      check_if_Iin(31, 24), check_if_Iin(31, 25), check_if_Iin(31, 26), check_if_Iin(31, 27),
                      check_if_Iin(31, 28), check_if_Iin(31, 29), check_if_Iin(31, 30), check_if_Iin(31, 32),
                      check_if_Iin(31, 33), check_if_Iin(31, 34), check_if_Iin(31, 35), check_if_Iin(31, 36),
                      check_if_Iin(31, 37), check_if_Iin(31, 38), check_if_Iin(31, 39), check_if_Iin(31, 40),
                      check_if_Iin(31, 41), check_if_Iin(31, 42), check_if_Iin(31, 43), check_if_Iin(31, 44),
                      check_if_Iin(31, 45), check_if_Iin(31, 46), check_if_Iin(31, 47), check_if_Iin(31, 48),
                      check_if_Iin(31, 49), check_if_Iin(31, 50)], ignore_index=True)
    return data


def check_I32():
    data = pd.concat([check_if_Iin(32, 0), check_if_Iin(32, 1), check_if_Iin(32, 2), check_if_Iin(32, 3),
                      check_if_Iin(32, 4), check_if_Iin(32, 5), check_if_Iin(32, 6), check_if_Iin(32, 7),
                      check_if_Iin(32, 8), check_if_Iin(32, 9), check_if_Iin(32, 10), check_if_Iin(32, 11),
                      check_if_Iin(32, 12), check_if_Iin(32, 13), check_if_Iin(32, 14), check_if_Iin(32, 15),
                      check_if_Iin(32, 16), check_if_Iin(32, 17), check_if_Iin(32, 18), check_if_Iin(32, 19),
                      check_if_Iin(32, 20), check_if_Iin(32, 21), check_if_Iin(32, 22), check_if_Iin(32, 23),
                      check_if_Iin(32, 24), check_if_Iin(32, 25), check_if_Iin(32, 26), check_if_Iin(32, 27),
                      check_if_Iin(32, 28), check_if_Iin(32, 29), check_if_Iin(32, 30), check_if_Iin(32, 31),
                      check_if_Iin(32, 33), check_if_Iin(32, 34), check_if_Iin(32, 35), check_if_Iin(32, 36),
                      check_if_Iin(32, 37), check_if_Iin(32, 38), check_if_Iin(32, 39), check_if_Iin(32, 40),
                      check_if_Iin(32, 41), check_if_Iin(32, 42), check_if_Iin(32, 43), check_if_Iin(32, 44),
                      check_if_Iin(32, 45), check_if_Iin(32, 46), check_if_Iin(32, 47), check_if_Iin(32, 48),
                      check_if_Iin(32, 49), check_if_Iin(32, 50)], ignore_index=True)
    return data


def check_I33():
    data = pd.concat([check_if_Iin(33, 0), check_if_Iin(33, 1), check_if_Iin(33, 2), check_if_Iin(33, 3),
                      check_if_Iin(33, 4), check_if_Iin(33, 5), check_if_Iin(33, 6), check_if_Iin(33, 7),
                      check_if_Iin(33, 8), check_if_Iin(33, 9), check_if_Iin(33, 10), check_if_Iin(33, 11),
                      check_if_Iin(33, 12), check_if_Iin(33, 13), check_if_Iin(33, 14), check_if_Iin(33, 15),
                      check_if_Iin(33, 16), check_if_Iin(33, 17), check_if_Iin(33, 18), check_if_Iin(33, 19),
                      check_if_Iin(33, 20), check_if_Iin(33, 21), check_if_Iin(33, 22), check_if_Iin(33, 23),
                      check_if_Iin(33, 24), check_if_Iin(33, 25), check_if_Iin(33, 26), check_if_Iin(33, 27),
                      check_if_Iin(33, 28), check_if_Iin(33, 29), check_if_Iin(33, 30), check_if_Iin(33, 31),
                      check_if_Iin(33, 32), check_if_Iin(33, 34), check_if_Iin(33, 35), check_if_Iin(33, 36),
                      check_if_Iin(33, 37), check_if_Iin(33, 38), check_if_Iin(33, 39), check_if_Iin(33, 40),
                      check_if_Iin(33, 41), check_if_Iin(33, 42), check_if_Iin(33, 43), check_if_Iin(33, 44),
                      check_if_Iin(33, 45), check_if_Iin(33, 46), check_if_Iin(33, 47), check_if_Iin(33, 48),
                      check_if_Iin(33, 49), check_if_Iin(33, 50)], ignore_index=True)
    return data


def check_I34():
    data = pd.concat([check_if_Iin(34, 0), check_if_Iin(34, 1), check_if_Iin(34, 2), check_if_Iin(34, 3),
                      check_if_Iin(34, 4), check_if_Iin(34, 5), check_if_Iin(34, 6), check_if_Iin(34, 7),
                      check_if_Iin(34, 8), check_if_Iin(34, 9), check_if_Iin(34, 10), check_if_Iin(34, 11),
                      check_if_Iin(34, 12), check_if_Iin(34, 13), check_if_Iin(34, 14), check_if_Iin(34, 15),
                      check_if_Iin(34, 16), check_if_Iin(34, 17), check_if_Iin(34, 18), check_if_Iin(34, 19),
                      check_if_Iin(34, 20), check_if_Iin(34, 21), check_if_Iin(34, 22), check_if_Iin(34, 23),
                      check_if_Iin(34, 24), check_if_Iin(34, 25), check_if_Iin(34, 26), check_if_Iin(34, 27),
                      check_if_Iin(34, 28), check_if_Iin(34, 29), check_if_Iin(34, 30), check_if_Iin(34, 31),
                      check_if_Iin(34, 32), check_if_Iin(34, 33), check_if_Iin(34, 35), check_if_Iin(34, 36),
                      check_if_Iin(34, 37), check_if_Iin(34, 38), check_if_Iin(34, 39), check_if_Iin(34, 40),
                      check_if_Iin(34, 41), check_if_Iin(34, 42), check_if_Iin(34, 43), check_if_Iin(34, 44),
                      check_if_Iin(34, 45), check_if_Iin(34, 46), check_if_Iin(34, 47), check_if_Iin(34, 48),
                      check_if_Iin(34, 49), check_if_Iin(34, 50)], ignore_index=True)
    return data


def check_I35():
    data = pd.concat([check_if_Iin(35, 0), check_if_Iin(35, 1), check_if_Iin(35, 2), check_if_Iin(35, 3),
                      check_if_Iin(35, 4), check_if_Iin(35, 5), check_if_Iin(35, 6), check_if_Iin(35, 7),
                      check_if_Iin(35, 8), check_if_Iin(35, 9), check_if_Iin(35, 10), check_if_Iin(35, 11),
                      check_if_Iin(35, 12), check_if_Iin(35, 13), check_if_Iin(35, 14), check_if_Iin(35, 15),
                      check_if_Iin(35, 16), check_if_Iin(35, 17), check_if_Iin(35, 18), check_if_Iin(35, 19),
                      check_if_Iin(35, 20), check_if_Iin(35, 21), check_if_Iin(35, 22), check_if_Iin(35, 23),
                      check_if_Iin(35, 24), check_if_Iin(35, 25), check_if_Iin(35, 26), check_if_Iin(35, 27),
                      check_if_Iin(35, 28), check_if_Iin(35, 29), check_if_Iin(35, 30), check_if_Iin(35, 31),
                      check_if_Iin(35, 32), check_if_Iin(35, 33), check_if_Iin(35, 34), check_if_Iin(35, 36),
                      check_if_Iin(35, 37), check_if_Iin(35, 38), check_if_Iin(35, 39), check_if_Iin(35, 40),
                      check_if_Iin(35, 41), check_if_Iin(35, 42), check_if_Iin(35, 43), check_if_Iin(35, 44),
                      check_if_Iin(35, 45), check_if_Iin(35, 46), check_if_Iin(35, 47), check_if_Iin(35, 48),
                      check_if_Iin(35, 49), check_if_Iin(35, 50)], ignore_index=True)
    return data


def check_I36():
    data = pd.concat([check_if_Iin(36, 0), check_if_Iin(36, 1), check_if_Iin(36, 2), check_if_Iin(36, 3),
                      check_if_Iin(36, 4), check_if_Iin(36, 5), check_if_Iin(36, 6), check_if_Iin(36, 7),
                      check_if_Iin(36, 8), check_if_Iin(36, 9), check_if_Iin(36, 10), check_if_Iin(36, 11),
                      check_if_Iin(36, 12), check_if_Iin(36, 13), check_if_Iin(36, 14), check_if_Iin(36, 15),
                      check_if_Iin(36, 16), check_if_Iin(36, 17), check_if_Iin(36, 18), check_if_Iin(36, 19),
                      check_if_Iin(36, 20), check_if_Iin(36, 21), check_if_Iin(36, 22), check_if_Iin(36, 23),
                      check_if_Iin(36, 24), check_if_Iin(36, 25), check_if_Iin(36, 26), check_if_Iin(36, 27),
                      check_if_Iin(36, 28), check_if_Iin(36, 29), check_if_Iin(36, 30), check_if_Iin(36, 31),
                      check_if_Iin(36, 32), check_if_Iin(36, 33), check_if_Iin(36, 34), check_if_Iin(36, 35),
                      check_if_Iin(36, 37), check_if_Iin(36, 38), check_if_Iin(36, 39), check_if_Iin(36, 40),
                      check_if_Iin(36, 41), check_if_Iin(36, 42), check_if_Iin(36, 43), check_if_Iin(36, 44),
                      check_if_Iin(36, 45), check_if_Iin(36, 46), check_if_Iin(36, 47), check_if_Iin(36, 48),
                      check_if_Iin(36, 49), check_if_Iin(36, 50)], ignore_index=True)
    return data


def check_I37():
    data = pd.concat([check_if_Iin(37, 0), check_if_Iin(37, 1), check_if_Iin(37, 2), check_if_Iin(37, 3),
                      check_if_Iin(37, 4), check_if_Iin(37, 5), check_if_Iin(37, 6), check_if_Iin(37, 7),
                      check_if_Iin(37, 8), check_if_Iin(37, 9), check_if_Iin(37, 10), check_if_Iin(37, 11),
                      check_if_Iin(37, 12), check_if_Iin(37, 13), check_if_Iin(37, 14), check_if_Iin(37, 15),
                      check_if_Iin(37, 16), check_if_Iin(37, 17), check_if_Iin(37, 18), check_if_Iin(37, 19),
                      check_if_Iin(37, 20), check_if_Iin(37, 21), check_if_Iin(37, 22), check_if_Iin(37, 23),
                      check_if_Iin(37, 24), check_if_Iin(37, 25), check_if_Iin(37, 26), check_if_Iin(37, 27),
                      check_if_Iin(37, 28), check_if_Iin(37, 29), check_if_Iin(37, 30), check_if_Iin(37, 31),
                      check_if_Iin(37, 32), check_if_Iin(37, 33), check_if_Iin(37, 34), check_if_Iin(37, 35),
                      check_if_Iin(37, 36), check_if_Iin(37, 38), check_if_Iin(37, 39), check_if_Iin(37, 40),
                      check_if_Iin(37, 41), check_if_Iin(37, 42), check_if_Iin(37, 43), check_if_Iin(37, 44),
                      check_if_Iin(37, 45), check_if_Iin(37, 46), check_if_Iin(37, 47), check_if_Iin(37, 48),
                      check_if_Iin(37, 49), check_if_Iin(37, 50)], ignore_index=True)
    return data


def check_I38():
    data = pd.concat([check_if_Iin(38, 0), check_if_Iin(38, 1), check_if_Iin(38, 2), check_if_Iin(38, 3),
                      check_if_Iin(38, 4), check_if_Iin(38, 5), check_if_Iin(38, 6), check_if_Iin(38, 7),
                      check_if_Iin(38, 8), check_if_Iin(38, 9), check_if_Iin(38, 10), check_if_Iin(38, 11),
                      check_if_Iin(38, 12), check_if_Iin(38, 13), check_if_Iin(38, 14), check_if_Iin(38, 15),
                      check_if_Iin(38, 16), check_if_Iin(38, 17), check_if_Iin(38, 18), check_if_Iin(38, 19),
                      check_if_Iin(38, 20), check_if_Iin(38, 21), check_if_Iin(38, 22), check_if_Iin(38, 23),
                      check_if_Iin(38, 24), check_if_Iin(38, 25), check_if_Iin(38, 26), check_if_Iin(38, 27),
                      check_if_Iin(38, 28), check_if_Iin(38, 29), check_if_Iin(38, 30), check_if_Iin(38, 31),
                      check_if_Iin(38, 32), check_if_Iin(38, 33), check_if_Iin(38, 34), check_if_Iin(38, 35),
                      check_if_Iin(38, 36), check_if_Iin(38, 37), check_if_Iin(38, 39), check_if_Iin(38, 40),
                      check_if_Iin(38, 41), check_if_Iin(38, 42), check_if_Iin(38, 43), check_if_Iin(38, 44),
                      check_if_Iin(38, 45), check_if_Iin(38, 46), check_if_Iin(38, 47), check_if_Iin(38, 48),
                      check_if_Iin(38, 49), check_if_Iin(38, 50)], ignore_index=True)
    return data


def check_I39():
    data = pd.concat([check_if_Iin(39, 0), check_if_Iin(39, 1), check_if_Iin(39, 2), check_if_Iin(39, 3),
                      check_if_Iin(39, 4), check_if_Iin(39, 5), check_if_Iin(39, 6), check_if_Iin(39, 7),
                      check_if_Iin(39, 8), check_if_Iin(39, 9), check_if_Iin(39, 10), check_if_Iin(39, 11),
                      check_if_Iin(39, 12), check_if_Iin(39, 13), check_if_Iin(39, 14), check_if_Iin(39, 15),
                      check_if_Iin(39, 16), check_if_Iin(39, 17), check_if_Iin(39, 18), check_if_Iin(39, 19),
                      check_if_Iin(39, 20), check_if_Iin(39, 21), check_if_Iin(39, 22), check_if_Iin(39, 23),
                      check_if_Iin(39, 24), check_if_Iin(39, 25), check_if_Iin(39, 26), check_if_Iin(39, 27),
                      check_if_Iin(39, 28), check_if_Iin(39, 29), check_if_Iin(39, 30), check_if_Iin(39, 31),
                      check_if_Iin(39, 32), check_if_Iin(39, 33), check_if_Iin(39, 34), check_if_Iin(39, 35),
                      check_if_Iin(39, 36), check_if_Iin(39, 37), check_if_Iin(39, 38), check_if_Iin(39, 40),
                      check_if_Iin(39, 41), check_if_Iin(39, 42), check_if_Iin(39, 43), check_if_Iin(39, 44),
                      check_if_Iin(39, 45), check_if_Iin(39, 46), check_if_Iin(39, 47), check_if_Iin(39, 48),
                      check_if_Iin(39, 49), check_if_Iin(39, 50)], ignore_index=True)
    return data


def check_I40():
    data = pd.concat([check_if_Iin(40, 0), check_if_Iin(40, 1), check_if_Iin(40, 2), check_if_Iin(40, 3),
                      check_if_Iin(40, 4), check_if_Iin(40, 5), check_if_Iin(40, 6), check_if_Iin(40, 7),
                      check_if_Iin(40, 8), check_if_Iin(40, 9), check_if_Iin(40, 10), check_if_Iin(40, 11),
                      check_if_Iin(40, 12), check_if_Iin(40, 13), check_if_Iin(40, 14), check_if_Iin(40, 15),
                      check_if_Iin(40, 16), check_if_Iin(40, 17), check_if_Iin(40, 18), check_if_Iin(40, 19),
                      check_if_Iin(40, 20), check_if_Iin(40, 21), check_if_Iin(40, 22), check_if_Iin(40, 23),
                      check_if_Iin(40, 24), check_if_Iin(40, 25), check_if_Iin(40, 26), check_if_Iin(40, 27),
                      check_if_Iin(40, 28), check_if_Iin(40, 29), check_if_Iin(40, 30), check_if_Iin(40, 31),
                      check_if_Iin(40, 32), check_if_Iin(40, 33), check_if_Iin(40, 34), check_if_Iin(40, 35),
                      check_if_Iin(40, 36), check_if_Iin(40, 37), check_if_Iin(40, 38), check_if_Iin(40, 39),
                      check_if_Iin(40, 41), check_if_Iin(40, 42), check_if_Iin(40, 43), check_if_Iin(40, 44),
                      check_if_Iin(40, 45), check_if_Iin(40, 46), check_if_Iin(40, 47), check_if_Iin(40, 48),
                      check_if_Iin(40, 49), check_if_Iin(40, 50)], ignore_index=True)
    return data


def check_I41():
    data = pd.concat([check_if_Iin(41, 0), check_if_Iin(41, 1), check_if_Iin(41, 2), check_if_Iin(41, 3),
                      check_if_Iin(41, 4), check_if_Iin(41, 5), check_if_Iin(41, 6), check_if_Iin(41, 7),
                      check_if_Iin(41, 8), check_if_Iin(41, 9), check_if_Iin(41, 10), check_if_Iin(41, 11),
                      check_if_Iin(41, 12), check_if_Iin(41, 13), check_if_Iin(41, 14), check_if_Iin(41, 15),
                      check_if_Iin(41, 16), check_if_Iin(41, 17), check_if_Iin(41, 18), check_if_Iin(41, 19),
                      check_if_Iin(41, 20), check_if_Iin(41, 21), check_if_Iin(41, 22), check_if_Iin(41, 23),
                      check_if_Iin(41, 24), check_if_Iin(41, 25), check_if_Iin(41, 26), check_if_Iin(41, 27),
                      check_if_Iin(41, 28), check_if_Iin(41, 29), check_if_Iin(41, 30), check_if_Iin(41, 31),
                      check_if_Iin(41, 32), check_if_Iin(41, 33), check_if_Iin(41, 34), check_if_Iin(41, 35),
                      check_if_Iin(41, 36), check_if_Iin(41, 37), check_if_Iin(41, 38), check_if_Iin(41, 39),
                      check_if_Iin(41, 40), check_if_Iin(41, 42), check_if_Iin(41, 43), check_if_Iin(41, 44),
                      check_if_Iin(41, 45), check_if_Iin(41, 46), check_if_Iin(41, 47), check_if_Iin(41, 48),
                      check_if_Iin(41, 49), check_if_Iin(41, 50)], ignore_index=True)
    return data


def check_I42():
    data = pd.concat([check_if_Iin(42, 0), check_if_Iin(42, 1), check_if_Iin(42, 2), check_if_Iin(42, 3),
                      check_if_Iin(42, 4), check_if_Iin(42, 5), check_if_Iin(42, 6), check_if_Iin(42, 7),
                      check_if_Iin(42, 8), check_if_Iin(42, 9), check_if_Iin(42, 10), check_if_Iin(42, 11),
                      check_if_Iin(42, 12), check_if_Iin(42, 13), check_if_Iin(42, 14), check_if_Iin(42, 15),
                      check_if_Iin(42, 16), check_if_Iin(42, 17), check_if_Iin(42, 18), check_if_Iin(42, 19),
                      check_if_Iin(42, 20), check_if_Iin(42, 21), check_if_Iin(42, 22), check_if_Iin(42, 23),
                      check_if_Iin(42, 24), check_if_Iin(42, 25), check_if_Iin(42, 26), check_if_Iin(42, 27),
                      check_if_Iin(42, 28), check_if_Iin(42, 29), check_if_Iin(42, 30), check_if_Iin(42, 31),
                      check_if_Iin(42, 32), check_if_Iin(42, 33), check_if_Iin(42, 34), check_if_Iin(42, 35),
                      check_if_Iin(42, 36), check_if_Iin(42, 37), check_if_Iin(42, 38), check_if_Iin(42, 39),
                      check_if_Iin(42, 40), check_if_Iin(42, 41), check_if_Iin(42, 43), check_if_Iin(42, 44),
                      check_if_Iin(42, 45), check_if_Iin(42, 46), check_if_Iin(42, 47), check_if_Iin(42, 48),
                      check_if_Iin(42, 49), check_if_Iin(42, 50)], ignore_index=True)
    return data


def check_I43():
    data = pd.concat([check_if_Iin(43, 0), check_if_Iin(43, 1), check_if_Iin(43, 2), check_if_Iin(43, 3),
                      check_if_Iin(43, 4), check_if_Iin(43, 5), check_if_Iin(43, 6), check_if_Iin(43, 7),
                      check_if_Iin(43, 8), check_if_Iin(43, 9), check_if_Iin(43, 10), check_if_Iin(43, 11),
                      check_if_Iin(43, 12), check_if_Iin(43, 13), check_if_Iin(43, 14), check_if_Iin(43, 15),
                      check_if_Iin(43, 16), check_if_Iin(43, 17), check_if_Iin(43, 18), check_if_Iin(43, 19),
                      check_if_Iin(43, 20), check_if_Iin(43, 21), check_if_Iin(43, 22), check_if_Iin(43, 23),
                      check_if_Iin(43, 24), check_if_Iin(43, 25), check_if_Iin(43, 26), check_if_Iin(43, 27),
                      check_if_Iin(43, 28), check_if_Iin(43, 29), check_if_Iin(43, 30), check_if_Iin(43, 31),
                      check_if_Iin(43, 32), check_if_Iin(43, 33), check_if_Iin(43, 34), check_if_Iin(43, 35),
                      check_if_Iin(43, 36), check_if_Iin(43, 37), check_if_Iin(43, 38), check_if_Iin(43, 39),
                      check_if_Iin(43, 40), check_if_Iin(43, 41), check_if_Iin(43, 42), check_if_Iin(43, 44),
                      check_if_Iin(43, 45), check_if_Iin(43, 46), check_if_Iin(43, 47), check_if_Iin(43, 48),
                      check_if_Iin(43, 49), check_if_Iin(43, 50)], ignore_index=True)
    return data


def check_I44():
    data = pd.concat([check_if_Iin(44, 0), check_if_Iin(44, 1), check_if_Iin(44, 2), check_if_Iin(44, 3),
                      check_if_Iin(44, 4), check_if_Iin(44, 5), check_if_Iin(44, 6), check_if_Iin(44, 7),
                      check_if_Iin(44, 8), check_if_Iin(44, 9), check_if_Iin(44, 10), check_if_Iin(44, 11),
                      check_if_Iin(44, 12), check_if_Iin(44, 13), check_if_Iin(44, 14), check_if_Iin(44, 15),
                      check_if_Iin(44, 16), check_if_Iin(44, 17), check_if_Iin(44, 18), check_if_Iin(44, 19),
                      check_if_Iin(44, 20), check_if_Iin(44, 21), check_if_Iin(44, 22), check_if_Iin(44, 23),
                      check_if_Iin(44, 24), check_if_Iin(44, 25), check_if_Iin(44, 26), check_if_Iin(44, 27),
                      check_if_Iin(44, 28), check_if_Iin(44, 29), check_if_Iin(44, 30), check_if_Iin(44, 31),
                      check_if_Iin(44, 32), check_if_Iin(44, 33), check_if_Iin(44, 34), check_if_Iin(44, 35),
                      check_if_Iin(44, 36), check_if_Iin(44, 37), check_if_Iin(44, 38), check_if_Iin(44, 39),
                      check_if_Iin(44, 40), check_if_Iin(44, 41), check_if_Iin(44, 42), check_if_Iin(44, 43),
                      check_if_Iin(44, 45), check_if_Iin(44, 46), check_if_Iin(44, 47), check_if_Iin(44, 48),
                      check_if_Iin(44, 49), check_if_Iin(44, 50)], ignore_index=True)
    return data


def check_I45():
    data = pd.concat([check_if_Iin(45, 0), check_if_Iin(45, 1), check_if_Iin(45, 2), check_if_Iin(45, 3),
                      check_if_Iin(45, 4), check_if_Iin(45, 5), check_if_Iin(45, 6), check_if_Iin(45, 7),
                      check_if_Iin(45, 8), check_if_Iin(45, 9), check_if_Iin(45, 10), check_if_Iin(45, 11),
                      check_if_Iin(45, 12), check_if_Iin(45, 13), check_if_Iin(45, 14), check_if_Iin(45, 15),
                      check_if_Iin(45, 16), check_if_Iin(45, 17), check_if_Iin(45, 18), check_if_Iin(45, 19),
                      check_if_Iin(45, 20), check_if_Iin(45, 21), check_if_Iin(45, 22), check_if_Iin(45, 23),
                      check_if_Iin(45, 24), check_if_Iin(45, 25), check_if_Iin(45, 26), check_if_Iin(45, 27),
                      check_if_Iin(45, 28), check_if_Iin(45, 29), check_if_Iin(45, 30), check_if_Iin(45, 31),
                      check_if_Iin(45, 32), check_if_Iin(45, 33), check_if_Iin(45, 34), check_if_Iin(45, 35),
                      check_if_Iin(45, 36), check_if_Iin(45, 37), check_if_Iin(45, 38), check_if_Iin(45, 39),
                      check_if_Iin(45, 40), check_if_Iin(45, 41), check_if_Iin(45, 42), check_if_Iin(45, 43),
                      check_if_Iin(45, 44), check_if_Iin(45, 46), check_if_Iin(45, 47), check_if_Iin(45, 48),
                      check_if_Iin(45, 49), check_if_Iin(45, 50)], ignore_index=True)
    return data


def check_I46():
    data = pd.concat([check_if_Iin(46, 0), check_if_Iin(46, 1), check_if_Iin(46, 2), check_if_Iin(46, 3),
                      check_if_Iin(46, 4), check_if_Iin(46, 5), check_if_Iin(46, 6), check_if_Iin(46, 7),
                      check_if_Iin(46, 8), check_if_Iin(46, 9), check_if_Iin(46, 10), check_if_Iin(46, 11),
                      check_if_Iin(46, 12), check_if_Iin(46, 13), check_if_Iin(46, 14), check_if_Iin(46, 15),
                      check_if_Iin(46, 16), check_if_Iin(46, 17), check_if_Iin(46, 18), check_if_Iin(46, 19),
                      check_if_Iin(46, 20), check_if_Iin(46, 21), check_if_Iin(46, 22), check_if_Iin(46, 23),
                      check_if_Iin(46, 24), check_if_Iin(46, 25), check_if_Iin(46, 26), check_if_Iin(46, 27),
                      check_if_Iin(46, 28), check_if_Iin(46, 29), check_if_Iin(46, 30), check_if_Iin(46, 31),
                      check_if_Iin(46, 32), check_if_Iin(46, 33), check_if_Iin(46, 34), check_if_Iin(46, 35),
                      check_if_Iin(46, 36), check_if_Iin(46, 37), check_if_Iin(46, 38), check_if_Iin(46, 39),
                      check_if_Iin(46, 40), check_if_Iin(46, 41), check_if_Iin(46, 42), check_if_Iin(46, 43),
                      check_if_Iin(46, 44), check_if_Iin(46, 45), check_if_Iin(46, 47), check_if_Iin(46, 48),
                      check_if_Iin(46, 49), check_if_Iin(46, 50)], ignore_index=True)
    return data


def check_I47():
    data = pd.concat([check_if_Iin(47, 0), check_if_Iin(47, 1), check_if_Iin(47, 2), check_if_Iin(47, 3),
                      check_if_Iin(47, 4), check_if_Iin(47, 5), check_if_Iin(47, 6), check_if_Iin(47, 7),
                      check_if_Iin(47, 8), check_if_Iin(47, 9), check_if_Iin(47, 10), check_if_Iin(47, 11),
                      check_if_Iin(47, 12), check_if_Iin(47, 13), check_if_Iin(47, 14), check_if_Iin(47, 15),
                      check_if_Iin(47, 16), check_if_Iin(47, 17), check_if_Iin(47, 18), check_if_Iin(47, 19),
                      check_if_Iin(47, 20), check_if_Iin(47, 21), check_if_Iin(47, 22), check_if_Iin(47, 23),
                      check_if_Iin(47, 24), check_if_Iin(47, 25), check_if_Iin(47, 26), check_if_Iin(47, 27),
                      check_if_Iin(47, 28), check_if_Iin(47, 29), check_if_Iin(47, 30), check_if_Iin(47, 31),
                      check_if_Iin(47, 32), check_if_Iin(47, 33), check_if_Iin(47, 34), check_if_Iin(47, 35),
                      check_if_Iin(47, 36), check_if_Iin(47, 37), check_if_Iin(47, 38), check_if_Iin(47, 39),
                      check_if_Iin(47, 40), check_if_Iin(47, 41), check_if_Iin(47, 42), check_if_Iin(47, 43),
                      check_if_Iin(47, 44), check_if_Iin(47, 45), check_if_Iin(47, 46), check_if_Iin(47, 48),
                      check_if_Iin(47, 49), check_if_Iin(47, 50)], ignore_index=True)
    return data


def check_I48():
    data = pd.concat([check_if_Iin(48, 0), check_if_Iin(48, 1), check_if_Iin(48, 2), check_if_Iin(48, 3),
                      check_if_Iin(48, 4), check_if_Iin(48, 5), check_if_Iin(48, 6), check_if_Iin(48, 7),
                      check_if_Iin(48, 8), check_if_Iin(48, 9), check_if_Iin(48, 10), check_if_Iin(48, 11),
                      check_if_Iin(48, 12), check_if_Iin(48, 13), check_if_Iin(48, 14), check_if_Iin(48, 15),
                      check_if_Iin(48, 16), check_if_Iin(48, 17), check_if_Iin(48, 18), check_if_Iin(48, 19),
                      check_if_Iin(48, 20), check_if_Iin(48, 21), check_if_Iin(48, 22), check_if_Iin(48, 23),
                      check_if_Iin(48, 24), check_if_Iin(48, 25), check_if_Iin(48, 26), check_if_Iin(48, 27),
                      check_if_Iin(48, 28), check_if_Iin(48, 29), check_if_Iin(48, 30), check_if_Iin(48, 31),
                      check_if_Iin(48, 32), check_if_Iin(48, 33), check_if_Iin(48, 34), check_if_Iin(48, 35),
                      check_if_Iin(48, 36), check_if_Iin(48, 37), check_if_Iin(48, 38), check_if_Iin(48, 39),
                      check_if_Iin(48, 40), check_if_Iin(48, 41), check_if_Iin(48, 42), check_if_Iin(48, 43),
                      check_if_Iin(48, 44), check_if_Iin(48, 45), check_if_Iin(48, 46), check_if_Iin(48, 47),
                      check_if_Iin(48, 49), check_if_Iin(48, 50)], ignore_index=True)
    return data


def check_I49():
    data = pd.concat([check_if_Iin(49, 0), check_if_Iin(49, 1), check_if_Iin(49, 2), check_if_Iin(49, 3),
                      check_if_Iin(49, 4), check_if_Iin(49, 5), check_if_Iin(49, 6), check_if_Iin(49, 7),
                      check_if_Iin(49, 8), check_if_Iin(49, 9), check_if_Iin(49, 10), check_if_Iin(49, 11),
                      check_if_Iin(49, 12), check_if_Iin(49, 13), check_if_Iin(49, 14), check_if_Iin(49, 15),
                      check_if_Iin(49, 16), check_if_Iin(49, 17), check_if_Iin(49, 18), check_if_Iin(49, 19),
                      check_if_Iin(49, 20), check_if_Iin(49, 21), check_if_Iin(49, 22), check_if_Iin(49, 23),
                      check_if_Iin(49, 24), check_if_Iin(49, 25), check_if_Iin(49, 26), check_if_Iin(49, 27),
                      check_if_Iin(49, 28), check_if_Iin(49, 29), check_if_Iin(49, 30), check_if_Iin(49, 31),
                      check_if_Iin(49, 32), check_if_Iin(49, 33), check_if_Iin(49, 34), check_if_Iin(49, 35),
                      check_if_Iin(49, 36), check_if_Iin(49, 37), check_if_Iin(49, 38), check_if_Iin(49, 39),
                      check_if_Iin(49, 40), check_if_Iin(49, 41), check_if_Iin(49, 42), check_if_Iin(49, 43),
                      check_if_Iin(49, 44), check_if_Iin(49, 45), check_if_Iin(49, 46), check_if_Iin(49, 47),
                      check_if_Iin(49, 48), check_if_Iin(49, 50)], ignore_index=True)
    return data


def check_I50():
    data = pd.concat([check_if_Iin(50, 0), check_if_Iin(50, 1), check_if_Iin(50, 2), check_if_Iin(50, 3),
                      check_if_Iin(50, 4), check_if_Iin(50, 5), check_if_Iin(50, 6), check_if_Iin(50, 7),
                      check_if_Iin(50, 8), check_if_Iin(50, 9), check_if_Iin(50, 10), check_if_Iin(50, 11),
                      check_if_Iin(50, 12), check_if_Iin(50, 13), check_if_Iin(50, 14), check_if_Iin(50, 15),
                      check_if_Iin(50, 16), check_if_Iin(50, 17), check_if_Iin(50, 18), check_if_Iin(50, 19),
                      check_if_Iin(50, 20), check_if_Iin(50, 21), check_if_Iin(50, 22), check_if_Iin(50, 23),
                      check_if_Iin(50, 24), check_if_Iin(50, 25), check_if_Iin(50, 26), check_if_Iin(50, 27),
                      check_if_Iin(50, 28), check_if_Iin(50, 29), check_if_Iin(50, 30), check_if_Iin(50, 31),
                      check_if_Iin(50, 32), check_if_Iin(50, 33), check_if_Iin(50, 34), check_if_Iin(50, 35),
                      check_if_Iin(50, 36), check_if_Iin(50, 37), check_if_Iin(50, 38), check_if_Iin(50, 39),
                      check_if_Iin(50, 40), check_if_Iin(50, 41), check_if_Iin(50, 42), check_if_Iin(50, 43),
                      check_if_Iin(50, 44), check_if_Iin(50, 45), check_if_Iin(50, 46), check_if_Iin(50, 47),
                      check_if_Iin(50, 48), check_if_Iin(50, 49)], ignore_index=True)
    return data


def check():
    data = pd.concat([check_I1(), check_I2(), check_I3(), check_I4(),
                      check_I5(), check_I6(), check_I7(), check_I8(),
                      check_I9(), check_I10(), check_I11(), check_I12(),
                      check_I13(), check_I14(), check_I15(), check_I16(),
                      check_I17(), check_I18(), check_I19(), check_I20(),
                      check_I21(), check_I22(), check_I23(), check_I24(),
                      check_I25(), check_I26(), check_I27(), check_I28(),
                      check_I29(), check_I30(), check_I31(), check_I32(),
                      check_I33(), check_I34(), check_I35(), check_I36(),
                      check_I37(), check_I38(), check_I39(), check_I40(),
                      check_I41(), check_I42(), check_I43(), check_I44(),
                      check_I45(), check_I46(), check_I47(), check_I48(),
                      check_I49(), check_I50()], ignore_index=True)
    return data


def check_I_csv():
    data = check()
    string1 = "/Pycharm/HumanActivityRecognition/check"
    string2 = string1 + "/check_I" + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


check_I_csv()

