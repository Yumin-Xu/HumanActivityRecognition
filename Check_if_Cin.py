import os

import numpy as np
import pandas as pd

from CreateWord import create_word


def check_if_Cin(x, y):
    d = create_word(x, 'C')['words']
    word_to_keep = np.array(create_word(y, 'C')['words'])
    df = pd.DataFrame(np.array(d[d.isin(word_to_keep)]), columns=['words'])
    return df


def check_C0():
    data = pd.concat([check_if_Cin(0, 1), check_if_Cin(0, 2), check_if_Cin(0, 3), check_if_Cin(0, 4),
                      check_if_Cin(0, 5), check_if_Cin(0, 6), check_if_Cin(0, 7), check_if_Cin(0, 8),
                      check_if_Cin(0, 9), check_if_Cin(0, 10), check_if_Cin(0, 11), check_if_Cin(0, 12),
                      check_if_Cin(0, 13), check_if_Cin(0, 14), check_if_Cin(0, 15), check_if_Cin(0, 16),
                      check_if_Cin(0, 17), check_if_Cin(0, 18), check_if_Cin(0, 19), check_if_Cin(0, 20),
                      check_if_Cin(0, 21), check_if_Cin(0, 22), check_if_Cin(0, 23), check_if_Cin(0, 24),
                      check_if_Cin(0, 25), check_if_Cin(0, 26), check_if_Cin(0, 27), check_if_Cin(0, 28),
                      check_if_Cin(0, 29), check_if_Cin(0, 30), check_if_Cin(0, 31), check_if_Cin(0, 32),
                      check_if_Cin(0, 33), check_if_Cin(0, 34), check_if_Cin(0, 35), check_if_Cin(0, 36),
                      check_if_Cin(0, 37), check_if_Cin(0, 38), check_if_Cin(0, 39), check_if_Cin(0, 40),
                      check_if_Cin(0, 41), check_if_Cin(0, 42), check_if_Cin(0, 43), check_if_Cin(0, 44),
                      check_if_Cin(0, 45), check_if_Cin(0, 46), check_if_Cin(0, 47), check_if_Cin(0, 48),
                      check_if_Cin(0, 49), check_if_Cin(0, 50)], ignore_index=True)
    return data


def check_C1():
    data = pd.concat([check_if_Cin(1, 0), check_if_Cin(1, 2), check_if_Cin(1, 3), check_if_Cin(1, 4),
                      check_if_Cin(1, 5), check_if_Cin(1, 6), check_if_Cin(1, 7), check_if_Cin(1, 8),
                      check_if_Cin(1, 9), check_if_Cin(1, 10), check_if_Cin(1, 11), check_if_Cin(1, 12),
                      check_if_Cin(1, 13), check_if_Cin(1, 14), check_if_Cin(1, 15), check_if_Cin(1, 16),
                      check_if_Cin(1, 17), check_if_Cin(1, 18), check_if_Cin(1, 19), check_if_Cin(1, 20),
                      check_if_Cin(1, 21), check_if_Cin(1, 22), check_if_Cin(1, 23), check_if_Cin(1, 24),
                      check_if_Cin(1, 25), check_if_Cin(1, 26), check_if_Cin(1, 27), check_if_Cin(1, 28),
                      check_if_Cin(1, 29), check_if_Cin(1, 30), check_if_Cin(1, 31), check_if_Cin(1, 32),
                      check_if_Cin(1, 33), check_if_Cin(1, 34), check_if_Cin(1, 35), check_if_Cin(1, 36),
                      check_if_Cin(1, 37), check_if_Cin(1, 38), check_if_Cin(1, 39), check_if_Cin(1, 40),
                      check_if_Cin(1, 41), check_if_Cin(1, 42), check_if_Cin(1, 43), check_if_Cin(1, 44),
                      check_if_Cin(1, 45), check_if_Cin(1, 46), check_if_Cin(1, 47), check_if_Cin(1, 48),
                      check_if_Cin(1, 49), check_if_Cin(1, 50)], ignore_index=True)
    return data


def check_C2():
    data = pd.concat([check_if_Cin(2, 0), check_if_Cin(2, 1), check_if_Cin(2, 3), check_if_Cin(2, 4),
                      check_if_Cin(2, 5), check_if_Cin(2, 6), check_if_Cin(2, 7), check_if_Cin(2, 8),
                      check_if_Cin(2, 9), check_if_Cin(2, 10), check_if_Cin(2, 11), check_if_Cin(2, 12),
                      check_if_Cin(2, 13), check_if_Cin(2, 14), check_if_Cin(2, 15), check_if_Cin(2, 16),
                      check_if_Cin(2, 17), check_if_Cin(2, 18), check_if_Cin(2, 19), check_if_Cin(2, 20),
                      check_if_Cin(2, 21), check_if_Cin(2, 22), check_if_Cin(2, 23), check_if_Cin(2, 24),
                      check_if_Cin(2, 25), check_if_Cin(2, 26), check_if_Cin(2, 27), check_if_Cin(2, 28),
                      check_if_Cin(2, 29), check_if_Cin(2, 30), check_if_Cin(2, 31), check_if_Cin(2, 32),
                      check_if_Cin(2, 33), check_if_Cin(2, 34), check_if_Cin(2, 35), check_if_Cin(2, 36),
                      check_if_Cin(2, 37), check_if_Cin(2, 38), check_if_Cin(2, 39), check_if_Cin(2, 40),
                      check_if_Cin(2, 41), check_if_Cin(2, 42), check_if_Cin(2, 43), check_if_Cin(2, 44),
                      check_if_Cin(2, 45), check_if_Cin(2, 46), check_if_Cin(2, 47), check_if_Cin(2, 48),
                      check_if_Cin(2, 49), check_if_Cin(2, 50)], ignore_index=True)
    return data


def check_C3():
    data = pd.concat([check_if_Cin(3, 0), check_if_Cin(3, 1), check_if_Cin(3, 2), check_if_Cin(3, 4),
                      check_if_Cin(3, 5), check_if_Cin(3, 6), check_if_Cin(3, 7), check_if_Cin(3, 8),
                      check_if_Cin(3, 9), check_if_Cin(3, 10), check_if_Cin(3, 11), check_if_Cin(3, 12),
                      check_if_Cin(3, 13), check_if_Cin(3, 14), check_if_Cin(3, 15), check_if_Cin(3, 16),
                      check_if_Cin(3, 17), check_if_Cin(3, 18), check_if_Cin(3, 19), check_if_Cin(3, 20),
                      check_if_Cin(3, 21), check_if_Cin(3, 22), check_if_Cin(3, 23), check_if_Cin(3, 24),
                      check_if_Cin(3, 25), check_if_Cin(3, 26), check_if_Cin(3, 27), check_if_Cin(3, 28),
                      check_if_Cin(3, 29), check_if_Cin(3, 30), check_if_Cin(3, 31), check_if_Cin(3, 32),
                      check_if_Cin(3, 33), check_if_Cin(3, 34), check_if_Cin(3, 35), check_if_Cin(3, 36),
                      check_if_Cin(3, 37), check_if_Cin(3, 38), check_if_Cin(3, 39), check_if_Cin(3, 40),
                      check_if_Cin(3, 41), check_if_Cin(3, 42), check_if_Cin(3, 43), check_if_Cin(3, 44),
                      check_if_Cin(3, 45), check_if_Cin(3, 46), check_if_Cin(3, 47), check_if_Cin(3, 48),
                      check_if_Cin(3, 49), check_if_Cin(3, 50)], ignore_index=True)
    return data


def check_C4():
    data = pd.concat([check_if_Cin(4, 0), check_if_Cin(4, 1), check_if_Cin(4, 2), check_if_Cin(4, 3),
                      check_if_Cin(4, 5), check_if_Cin(4, 6), check_if_Cin(4, 7), check_if_Cin(4, 8),
                      check_if_Cin(4, 9), check_if_Cin(4, 10), check_if_Cin(4, 11), check_if_Cin(4, 12),
                      check_if_Cin(4, 13), check_if_Cin(4, 14), check_if_Cin(4, 15), check_if_Cin(4, 16),
                      check_if_Cin(4, 17), check_if_Cin(4, 18), check_if_Cin(4, 19), check_if_Cin(4, 20),
                      check_if_Cin(4, 21), check_if_Cin(4, 22), check_if_Cin(4, 23), check_if_Cin(4, 24),
                      check_if_Cin(4, 25), check_if_Cin(4, 26), check_if_Cin(4, 27), check_if_Cin(4, 28),
                      check_if_Cin(4, 29), check_if_Cin(4, 30), check_if_Cin(4, 31), check_if_Cin(4, 32),
                      check_if_Cin(4, 33), check_if_Cin(4, 34), check_if_Cin(4, 35), check_if_Cin(4, 36),
                      check_if_Cin(4, 37), check_if_Cin(4, 38), check_if_Cin(4, 39), check_if_Cin(4, 40),
                      check_if_Cin(4, 41), check_if_Cin(4, 42), check_if_Cin(4, 43), check_if_Cin(4, 44),
                      check_if_Cin(4, 45), check_if_Cin(4, 46), check_if_Cin(4, 47), check_if_Cin(4, 48),
                      check_if_Cin(4, 49), check_if_Cin(4, 50)], ignore_index=True)
    return data


def check_C5():
    data = pd.concat([check_if_Cin(5, 0), check_if_Cin(5, 1), check_if_Cin(5, 2), check_if_Cin(5, 3),
                      check_if_Cin(5, 4), check_if_Cin(5, 6), check_if_Cin(5, 7), check_if_Cin(5, 8),
                      check_if_Cin(5, 9), check_if_Cin(5, 10), check_if_Cin(5, 11), check_if_Cin(5, 12),
                      check_if_Cin(5, 13), check_if_Cin(5, 14), check_if_Cin(5, 15), check_if_Cin(5, 16),
                      check_if_Cin(5, 17), check_if_Cin(5, 18), check_if_Cin(5, 19), check_if_Cin(5, 20),
                      check_if_Cin(5, 21), check_if_Cin(5, 22), check_if_Cin(5, 23), check_if_Cin(5, 24),
                      check_if_Cin(5, 25), check_if_Cin(5, 26), check_if_Cin(5, 27), check_if_Cin(5, 28),
                      check_if_Cin(5, 29), check_if_Cin(5, 30), check_if_Cin(5, 31), check_if_Cin(5, 32),
                      check_if_Cin(5, 33), check_if_Cin(5, 34), check_if_Cin(5, 35), check_if_Cin(5, 36),
                      check_if_Cin(5, 37), check_if_Cin(5, 38), check_if_Cin(5, 39), check_if_Cin(5, 40),
                      check_if_Cin(5, 41), check_if_Cin(5, 42), check_if_Cin(5, 43), check_if_Cin(5, 44),
                      check_if_Cin(5, 45), check_if_Cin(5, 46), check_if_Cin(5, 47), check_if_Cin(5, 48),
                      check_if_Cin(5, 49), check_if_Cin(5, 50)], ignore_index=True)
    return data


def check_C6():
    data = pd.concat([check_if_Cin(6, 0), check_if_Cin(6, 1), check_if_Cin(6, 2), check_if_Cin(6, 3),
                      check_if_Cin(6, 4), check_if_Cin(6, 5), check_if_Cin(6, 7), check_if_Cin(6, 8),
                      check_if_Cin(6, 9), check_if_Cin(6, 10), check_if_Cin(6, 11), check_if_Cin(6, 12),
                      check_if_Cin(6, 13), check_if_Cin(6, 14), check_if_Cin(6, 15), check_if_Cin(6, 16),
                      check_if_Cin(6, 17), check_if_Cin(6, 18), check_if_Cin(6, 19), check_if_Cin(6, 20),
                      check_if_Cin(6, 21), check_if_Cin(6, 22), check_if_Cin(6, 23), check_if_Cin(6, 24),
                      check_if_Cin(6, 25), check_if_Cin(6, 26), check_if_Cin(6, 27), check_if_Cin(6, 28),
                      check_if_Cin(6, 29), check_if_Cin(6, 30), check_if_Cin(6, 31), check_if_Cin(6, 32),
                      check_if_Cin(6, 33), check_if_Cin(6, 34), check_if_Cin(6, 35), check_if_Cin(6, 36),
                      check_if_Cin(6, 37), check_if_Cin(6, 38), check_if_Cin(6, 39), check_if_Cin(6, 40),
                      check_if_Cin(6, 41), check_if_Cin(6, 42), check_if_Cin(6, 43), check_if_Cin(6, 44),
                      check_if_Cin(6, 45), check_if_Cin(6, 46), check_if_Cin(6, 47), check_if_Cin(6, 48),
                      check_if_Cin(6, 49), check_if_Cin(6, 50)], ignore_index=True)
    return data


def check_C7():
    data = pd.concat([check_if_Cin(7, 0), check_if_Cin(7, 1), check_if_Cin(7, 2), check_if_Cin(7, 3),
                      check_if_Cin(7, 4), check_if_Cin(7, 5), check_if_Cin(7, 6), check_if_Cin(7, 8),
                      check_if_Cin(7, 9), check_if_Cin(7, 10), check_if_Cin(7, 11), check_if_Cin(7, 12),
                      check_if_Cin(7, 13), check_if_Cin(7, 14), check_if_Cin(7, 15), check_if_Cin(7, 16),
                      check_if_Cin(7, 17), check_if_Cin(7, 18), check_if_Cin(7, 19), check_if_Cin(7, 20),
                      check_if_Cin(7, 21), check_if_Cin(7, 22), check_if_Cin(7, 23), check_if_Cin(7, 24),
                      check_if_Cin(7, 25), check_if_Cin(7, 26), check_if_Cin(7, 27), check_if_Cin(7, 28),
                      check_if_Cin(7, 29), check_if_Cin(7, 30), check_if_Cin(7, 31), check_if_Cin(7, 32),
                      check_if_Cin(7, 33), check_if_Cin(7, 34), check_if_Cin(7, 35), check_if_Cin(7, 36),
                      check_if_Cin(7, 37), check_if_Cin(7, 38), check_if_Cin(7, 39), check_if_Cin(7, 40),
                      check_if_Cin(7, 41), check_if_Cin(7, 42), check_if_Cin(7, 43), check_if_Cin(7, 44),
                      check_if_Cin(7, 45), check_if_Cin(7, 46), check_if_Cin(7, 47), check_if_Cin(7, 48),
                      check_if_Cin(7, 49), check_if_Cin(7, 50)], ignore_index=True)
    return data


def check_C8():
    data = pd.concat([check_if_Cin(8, 0), check_if_Cin(8, 1), check_if_Cin(8, 2), check_if_Cin(8, 3),
                      check_if_Cin(8, 4), check_if_Cin(8, 5), check_if_Cin(8, 6), check_if_Cin(8, 7),
                      check_if_Cin(8, 9), check_if_Cin(8, 10), check_if_Cin(8, 11), check_if_Cin(8, 12),
                      check_if_Cin(8, 13), check_if_Cin(8, 14), check_if_Cin(8, 15), check_if_Cin(8, 16),
                      check_if_Cin(8, 17), check_if_Cin(8, 18), check_if_Cin(8, 19), check_if_Cin(8, 20),
                      check_if_Cin(8, 21), check_if_Cin(8, 22), check_if_Cin(8, 23), check_if_Cin(8, 24),
                      check_if_Cin(8, 25), check_if_Cin(8, 26), check_if_Cin(8, 27), check_if_Cin(8, 28),
                      check_if_Cin(8, 29), check_if_Cin(8, 30), check_if_Cin(8, 31), check_if_Cin(8, 32),
                      check_if_Cin(8, 33), check_if_Cin(8, 34), check_if_Cin(8, 35), check_if_Cin(8, 36),
                      check_if_Cin(8, 37), check_if_Cin(8, 38), check_if_Cin(8, 39), check_if_Cin(8, 40),
                      check_if_Cin(8, 41), check_if_Cin(8, 42), check_if_Cin(8, 43), check_if_Cin(8, 44),
                      check_if_Cin(8, 45), check_if_Cin(8, 46), check_if_Cin(8, 47), check_if_Cin(8, 48),
                      check_if_Cin(8, 49), check_if_Cin(8, 50)], ignore_index=True)
    return data


def check_C9():
    data = pd.concat([check_if_Cin(9, 0), check_if_Cin(9, 1), check_if_Cin(9, 2), check_if_Cin(9, 3),
                      check_if_Cin(9, 4), check_if_Cin(9, 5), check_if_Cin(9, 6), check_if_Cin(9, 7),
                      check_if_Cin(9, 8), check_if_Cin(9, 10), check_if_Cin(9, 11), check_if_Cin(9, 12),
                      check_if_Cin(9, 13), check_if_Cin(9, 14), check_if_Cin(9, 15), check_if_Cin(9, 16),
                      check_if_Cin(9, 17), check_if_Cin(9, 18), check_if_Cin(9, 19), check_if_Cin(9, 20),
                      check_if_Cin(9, 21), check_if_Cin(9, 22), check_if_Cin(9, 23), check_if_Cin(9, 24),
                      check_if_Cin(9, 25), check_if_Cin(9, 26), check_if_Cin(9, 27), check_if_Cin(9, 28),
                      check_if_Cin(9, 29), check_if_Cin(9, 30), check_if_Cin(9, 31), check_if_Cin(9, 32),
                      check_if_Cin(9, 33), check_if_Cin(9, 34), check_if_Cin(9, 35), check_if_Cin(9, 36),
                      check_if_Cin(9, 37), check_if_Cin(9, 38), check_if_Cin(9, 39), check_if_Cin(9, 40),
                      check_if_Cin(9, 41), check_if_Cin(9, 42), check_if_Cin(9, 43), check_if_Cin(9, 44),
                      check_if_Cin(9, 45), check_if_Cin(9, 46), check_if_Cin(9, 47), check_if_Cin(9, 48),
                      check_if_Cin(9, 49), check_if_Cin(9, 50)], ignore_index=True)
    return data


def check_C10():
    data = pd.concat([check_if_Cin(10, 0), check_if_Cin(10, 1), check_if_Cin(10, 2), check_if_Cin(10, 3),
                      check_if_Cin(10, 4), check_if_Cin(10, 5), check_if_Cin(10, 6), check_if_Cin(10, 7),
                      check_if_Cin(10, 8), check_if_Cin(10, 9), check_if_Cin(10, 11), check_if_Cin(10, 12),
                      check_if_Cin(10, 13), check_if_Cin(10, 14), check_if_Cin(10, 15), check_if_Cin(10, 16),
                      check_if_Cin(10, 17), check_if_Cin(10, 18), check_if_Cin(10, 19), check_if_Cin(10, 20),
                      check_if_Cin(10, 21), check_if_Cin(10, 22), check_if_Cin(10, 23), check_if_Cin(10, 24),
                      check_if_Cin(10, 25), check_if_Cin(10, 26), check_if_Cin(10, 27), check_if_Cin(10, 28),
                      check_if_Cin(10, 29), check_if_Cin(10, 30), check_if_Cin(10, 31), check_if_Cin(10, 32),
                      check_if_Cin(10, 33), check_if_Cin(10, 34), check_if_Cin(10, 35), check_if_Cin(10, 36),
                      check_if_Cin(10, 37), check_if_Cin(10, 38), check_if_Cin(10, 39), check_if_Cin(10, 40),
                      check_if_Cin(10, 41), check_if_Cin(10, 42), check_if_Cin(10, 43), check_if_Cin(10, 44),
                      check_if_Cin(10, 45), check_if_Cin(10, 46), check_if_Cin(10, 47), check_if_Cin(10, 48),
                      check_if_Cin(10, 49), check_if_Cin(10, 50)], ignore_index=True)
    return data


def check_C11():
    data = pd.concat([check_if_Cin(11, 0), check_if_Cin(11, 1), check_if_Cin(11, 2), check_if_Cin(11, 3),
                      check_if_Cin(11, 4), check_if_Cin(11, 5), check_if_Cin(11, 6), check_if_Cin(11, 7),
                      check_if_Cin(11, 8), check_if_Cin(11, 9), check_if_Cin(11, 10), check_if_Cin(11, 12),
                      check_if_Cin(11, 13), check_if_Cin(11, 14), check_if_Cin(11, 15), check_if_Cin(11, 16),
                      check_if_Cin(11, 17), check_if_Cin(11, 18), check_if_Cin(11, 19), check_if_Cin(11, 20),
                      check_if_Cin(11, 21), check_if_Cin(11, 22), check_if_Cin(11, 23), check_if_Cin(11, 24),
                      check_if_Cin(11, 25), check_if_Cin(11, 26), check_if_Cin(11, 27), check_if_Cin(11, 28),
                      check_if_Cin(11, 29), check_if_Cin(11, 30), check_if_Cin(11, 31), check_if_Cin(11, 32),
                      check_if_Cin(11, 33), check_if_Cin(11, 34), check_if_Cin(11, 35), check_if_Cin(11, 36),
                      check_if_Cin(11, 37), check_if_Cin(11, 38), check_if_Cin(11, 39), check_if_Cin(11, 40),
                      check_if_Cin(11, 41), check_if_Cin(11, 42), check_if_Cin(11, 43), check_if_Cin(11, 44),
                      check_if_Cin(11, 45), check_if_Cin(11, 46), check_if_Cin(11, 47), check_if_Cin(11, 48),
                      check_if_Cin(11, 49), check_if_Cin(11, 50)], ignore_index=True)
    return data


def check_C12():
    data = pd.concat([check_if_Cin(12, 0), check_if_Cin(12, 1), check_if_Cin(12, 2), check_if_Cin(12, 3),
                      check_if_Cin(12, 4), check_if_Cin(12, 5), check_if_Cin(12, 6), check_if_Cin(12, 7),
                      check_if_Cin(12, 8), check_if_Cin(12, 9), check_if_Cin(12, 10), check_if_Cin(12, 11),
                      check_if_Cin(12, 13), check_if_Cin(12, 14), check_if_Cin(12, 15), check_if_Cin(12, 16),
                      check_if_Cin(12, 17), check_if_Cin(12, 18), check_if_Cin(12, 19), check_if_Cin(12, 20),
                      check_if_Cin(12, 21), check_if_Cin(12, 22), check_if_Cin(12, 23), check_if_Cin(12, 24),
                      check_if_Cin(12, 25), check_if_Cin(12, 26), check_if_Cin(12, 27), check_if_Cin(12, 28),
                      check_if_Cin(12, 29), check_if_Cin(12, 30), check_if_Cin(12, 31), check_if_Cin(12, 32),
                      check_if_Cin(12, 33), check_if_Cin(12, 34), check_if_Cin(12, 35), check_if_Cin(12, 36),
                      check_if_Cin(12, 37), check_if_Cin(12, 38), check_if_Cin(12, 39), check_if_Cin(12, 40),
                      check_if_Cin(12, 41), check_if_Cin(12, 42), check_if_Cin(12, 43), check_if_Cin(12, 44),
                      check_if_Cin(12, 45), check_if_Cin(12, 46), check_if_Cin(12, 47), check_if_Cin(12, 48),
                      check_if_Cin(12, 49), check_if_Cin(12, 50)], ignore_index=True)
    return data


def check_C13():
    data = pd.concat([check_if_Cin(13, 0), check_if_Cin(13, 1), check_if_Cin(13, 2), check_if_Cin(13, 3),
                      check_if_Cin(13, 4), check_if_Cin(13, 5), check_if_Cin(13, 6), check_if_Cin(13, 7),
                      check_if_Cin(13, 8), check_if_Cin(13, 9), check_if_Cin(13, 10), check_if_Cin(13, 11),
                      check_if_Cin(13, 12), check_if_Cin(13, 14), check_if_Cin(13, 15), check_if_Cin(13, 16),
                      check_if_Cin(13, 17), check_if_Cin(13, 18), check_if_Cin(13, 19), check_if_Cin(13, 20),
                      check_if_Cin(13, 21), check_if_Cin(13, 22), check_if_Cin(13, 23), check_if_Cin(13, 24),
                      check_if_Cin(13, 25), check_if_Cin(13, 26), check_if_Cin(13, 27), check_if_Cin(13, 28),
                      check_if_Cin(13, 29), check_if_Cin(13, 30), check_if_Cin(13, 31), check_if_Cin(13, 32),
                      check_if_Cin(13, 33), check_if_Cin(13, 34), check_if_Cin(13, 35), check_if_Cin(13, 36),
                      check_if_Cin(13, 37), check_if_Cin(13, 38), check_if_Cin(13, 39), check_if_Cin(13, 40),
                      check_if_Cin(13, 41), check_if_Cin(13, 42), check_if_Cin(13, 43), check_if_Cin(13, 44),
                      check_if_Cin(13, 45), check_if_Cin(13, 46), check_if_Cin(13, 47), check_if_Cin(13, 48),
                      check_if_Cin(13, 49), check_if_Cin(13, 50)], ignore_index=True)
    return data


def check_C14():
    data = pd.concat([check_if_Cin(14, 0), check_if_Cin(14, 1), check_if_Cin(14, 2), check_if_Cin(14, 3),
                      check_if_Cin(14, 4), check_if_Cin(14, 5), check_if_Cin(14, 6), check_if_Cin(14, 7),
                      check_if_Cin(14, 8), check_if_Cin(14, 9), check_if_Cin(14, 10), check_if_Cin(14, 11),
                      check_if_Cin(14, 12), check_if_Cin(14, 13), check_if_Cin(14, 15), check_if_Cin(14, 16),
                      check_if_Cin(14, 17), check_if_Cin(14, 18), check_if_Cin(14, 19), check_if_Cin(14, 20),
                      check_if_Cin(14, 21), check_if_Cin(14, 22), check_if_Cin(14, 23), check_if_Cin(14, 24),
                      check_if_Cin(14, 25), check_if_Cin(14, 26), check_if_Cin(14, 27), check_if_Cin(14, 28),
                      check_if_Cin(14, 29), check_if_Cin(14, 30), check_if_Cin(14, 31), check_if_Cin(14, 32),
                      check_if_Cin(14, 33), check_if_Cin(14, 34), check_if_Cin(14, 35), check_if_Cin(14, 36),
                      check_if_Cin(14, 37), check_if_Cin(14, 38), check_if_Cin(14, 39), check_if_Cin(14, 40),
                      check_if_Cin(14, 41), check_if_Cin(14, 42), check_if_Cin(14, 43), check_if_Cin(14, 44),
                      check_if_Cin(14, 45), check_if_Cin(14, 46), check_if_Cin(14, 47), check_if_Cin(14, 48),
                      check_if_Cin(14, 49), check_if_Cin(14, 50)], ignore_index=True)
    return data


def check_C15():
    data = pd.concat([check_if_Cin(15, 0), check_if_Cin(15, 1), check_if_Cin(15, 2), check_if_Cin(15, 3),
                      check_if_Cin(15, 4), check_if_Cin(15, 5), check_if_Cin(15, 6), check_if_Cin(15, 7),
                      check_if_Cin(15, 8), check_if_Cin(15, 9), check_if_Cin(15, 10), check_if_Cin(15, 11),
                      check_if_Cin(15, 12), check_if_Cin(15, 13), check_if_Cin(15, 14), check_if_Cin(15, 16),
                      check_if_Cin(15, 17), check_if_Cin(15, 18), check_if_Cin(15, 19), check_if_Cin(15, 20),
                      check_if_Cin(15, 21), check_if_Cin(15, 22), check_if_Cin(15, 23), check_if_Cin(15, 24),
                      check_if_Cin(15, 25), check_if_Cin(15, 26), check_if_Cin(15, 27), check_if_Cin(15, 28),
                      check_if_Cin(15, 29), check_if_Cin(15, 30), check_if_Cin(15, 31), check_if_Cin(15, 32),
                      check_if_Cin(15, 33), check_if_Cin(15, 34), check_if_Cin(15, 35), check_if_Cin(15, 36),
                      check_if_Cin(15, 37), check_if_Cin(15, 38), check_if_Cin(15, 39), check_if_Cin(15, 40),
                      check_if_Cin(15, 41), check_if_Cin(15, 42), check_if_Cin(15, 43), check_if_Cin(15, 44),
                      check_if_Cin(15, 45), check_if_Cin(15, 46), check_if_Cin(15, 47), check_if_Cin(15, 48),
                      check_if_Cin(15, 49), check_if_Cin(15, 50)], ignore_index=True)
    return data


def check_C16():
    data = pd.concat([check_if_Cin(16, 0), check_if_Cin(16, 1), check_if_Cin(16, 2), check_if_Cin(16, 3),
                      check_if_Cin(16, 4), check_if_Cin(16, 5), check_if_Cin(16, 6), check_if_Cin(16, 7),
                      check_if_Cin(16, 8), check_if_Cin(16, 9), check_if_Cin(16, 10), check_if_Cin(16, 11),
                      check_if_Cin(16, 12), check_if_Cin(16, 13), check_if_Cin(16, 14), check_if_Cin(16, 15),
                      check_if_Cin(16, 17), check_if_Cin(16, 18), check_if_Cin(16, 19), check_if_Cin(16, 20),
                      check_if_Cin(16, 21), check_if_Cin(16, 22), check_if_Cin(16, 23), check_if_Cin(16, 24),
                      check_if_Cin(16, 25), check_if_Cin(16, 26), check_if_Cin(16, 27), check_if_Cin(16, 28),
                      check_if_Cin(16, 29), check_if_Cin(16, 30), check_if_Cin(16, 31), check_if_Cin(16, 32),
                      check_if_Cin(16, 33), check_if_Cin(16, 34), check_if_Cin(16, 35), check_if_Cin(16, 36),
                      check_if_Cin(16, 37), check_if_Cin(16, 38), check_if_Cin(16, 39), check_if_Cin(16, 40),
                      check_if_Cin(16, 41), check_if_Cin(16, 42), check_if_Cin(16, 43), check_if_Cin(16, 44),
                      check_if_Cin(16, 45), check_if_Cin(16, 46), check_if_Cin(16, 47), check_if_Cin(16, 48),
                      check_if_Cin(16, 49), check_if_Cin(16, 50)], ignore_index=True)
    return data


def check_C17():
    data = pd.concat([check_if_Cin(17, 0), check_if_Cin(17, 1), check_if_Cin(17, 2), check_if_Cin(17, 3),
                      check_if_Cin(17, 4), check_if_Cin(17, 5), check_if_Cin(17, 6), check_if_Cin(17, 7),
                      check_if_Cin(17, 8), check_if_Cin(17, 9), check_if_Cin(17, 10), check_if_Cin(17, 11),
                      check_if_Cin(17, 12), check_if_Cin(17, 13), check_if_Cin(17, 14), check_if_Cin(17, 15),
                      check_if_Cin(17, 16), check_if_Cin(17, 18), check_if_Cin(17, 19), check_if_Cin(17, 20),
                      check_if_Cin(17, 21), check_if_Cin(17, 22), check_if_Cin(17, 23), check_if_Cin(17, 24),
                      check_if_Cin(17, 25), check_if_Cin(17, 26), check_if_Cin(17, 27), check_if_Cin(17, 28),
                      check_if_Cin(17, 29), check_if_Cin(17, 30), check_if_Cin(17, 31), check_if_Cin(17, 32),
                      check_if_Cin(17, 33), check_if_Cin(17, 34), check_if_Cin(17, 35), check_if_Cin(17, 36),
                      check_if_Cin(17, 37), check_if_Cin(17, 38), check_if_Cin(17, 39), check_if_Cin(17, 40),
                      check_if_Cin(17, 41), check_if_Cin(17, 42), check_if_Cin(17, 43), check_if_Cin(17, 44),
                      check_if_Cin(17, 45), check_if_Cin(17, 46), check_if_Cin(17, 47), check_if_Cin(17, 48),
                      check_if_Cin(17, 49), check_if_Cin(17, 50)], ignore_index=True)
    return data


def check_C18():
    data = pd.concat([check_if_Cin(18, 0), check_if_Cin(18, 1), check_if_Cin(18, 2), check_if_Cin(18, 3),
                      check_if_Cin(18, 4), check_if_Cin(18, 5), check_if_Cin(18, 6), check_if_Cin(18, 7),
                      check_if_Cin(18, 8), check_if_Cin(18, 9), check_if_Cin(18, 10), check_if_Cin(18, 11),
                      check_if_Cin(18, 12), check_if_Cin(18, 13), check_if_Cin(18, 14), check_if_Cin(18, 15),
                      check_if_Cin(18, 16), check_if_Cin(18, 17), check_if_Cin(18, 19), check_if_Cin(18, 20),
                      check_if_Cin(18, 21), check_if_Cin(18, 22), check_if_Cin(18, 23), check_if_Cin(18, 24),
                      check_if_Cin(18, 25), check_if_Cin(18, 26), check_if_Cin(18, 27), check_if_Cin(18, 28),
                      check_if_Cin(18, 29), check_if_Cin(18, 30), check_if_Cin(18, 31), check_if_Cin(18, 32),
                      check_if_Cin(18, 33), check_if_Cin(18, 34), check_if_Cin(18, 35), check_if_Cin(18, 36),
                      check_if_Cin(18, 37), check_if_Cin(18, 38), check_if_Cin(18, 39), check_if_Cin(18, 40),
                      check_if_Cin(18, 41), check_if_Cin(18, 42), check_if_Cin(18, 43), check_if_Cin(18, 44),
                      check_if_Cin(18, 45), check_if_Cin(18, 46), check_if_Cin(18, 47), check_if_Cin(18, 48),
                      check_if_Cin(18, 49), check_if_Cin(18, 50)], ignore_index=True)
    return data


def check_C19():
    data = pd.concat([check_if_Cin(19, 0), check_if_Cin(19, 1), check_if_Cin(19, 2), check_if_Cin(19, 3),
                      check_if_Cin(19, 4), check_if_Cin(19, 5), check_if_Cin(19, 6), check_if_Cin(19, 7),
                      check_if_Cin(19, 8), check_if_Cin(19, 9), check_if_Cin(19, 10), check_if_Cin(19, 11),
                      check_if_Cin(19, 12), check_if_Cin(19, 13), check_if_Cin(19, 14), check_if_Cin(19, 15),
                      check_if_Cin(19, 16), check_if_Cin(19, 17), check_if_Cin(19, 18), check_if_Cin(19, 20),
                      check_if_Cin(19, 21), check_if_Cin(19, 22), check_if_Cin(19, 23), check_if_Cin(19, 24),
                      check_if_Cin(19, 25), check_if_Cin(19, 26), check_if_Cin(19, 27), check_if_Cin(19, 28),
                      check_if_Cin(19, 29), check_if_Cin(19, 30), check_if_Cin(19, 31), check_if_Cin(19, 32),
                      check_if_Cin(19, 33), check_if_Cin(19, 34), check_if_Cin(19, 35), check_if_Cin(19, 36),
                      check_if_Cin(19, 37), check_if_Cin(19, 38), check_if_Cin(19, 39), check_if_Cin(19, 40),
                      check_if_Cin(19, 41), check_if_Cin(19, 42), check_if_Cin(19, 43), check_if_Cin(19, 44),
                      check_if_Cin(19, 45), check_if_Cin(19, 46), check_if_Cin(19, 47), check_if_Cin(19, 48),
                      check_if_Cin(19, 49), check_if_Cin(19, 50)], ignore_index=True)
    return data


def check_C20():
    data = pd.concat([check_if_Cin(20, 0), check_if_Cin(20, 1), check_if_Cin(20, 2), check_if_Cin(20, 3),
                      check_if_Cin(20, 4), check_if_Cin(20, 5), check_if_Cin(20, 6), check_if_Cin(20, 7),
                      check_if_Cin(20, 8), check_if_Cin(20, 9), check_if_Cin(20, 10), check_if_Cin(20, 11),
                      check_if_Cin(20, 12), check_if_Cin(20, 13), check_if_Cin(20, 14), check_if_Cin(20, 15),
                      check_if_Cin(20, 16), check_if_Cin(20, 17), check_if_Cin(20, 18), check_if_Cin(20, 19),
                      check_if_Cin(20, 21), check_if_Cin(20, 22), check_if_Cin(20, 23), check_if_Cin(20, 24),
                      check_if_Cin(20, 25), check_if_Cin(20, 26), check_if_Cin(20, 27), check_if_Cin(20, 28),
                      check_if_Cin(20, 29), check_if_Cin(20, 30), check_if_Cin(20, 31), check_if_Cin(20, 32),
                      check_if_Cin(20, 33), check_if_Cin(20, 34), check_if_Cin(20, 35), check_if_Cin(20, 36),
                      check_if_Cin(20, 37), check_if_Cin(20, 38), check_if_Cin(20, 39), check_if_Cin(20, 40),
                      check_if_Cin(20, 41), check_if_Cin(20, 42), check_if_Cin(20, 43), check_if_Cin(20, 44),
                      check_if_Cin(20, 45), check_if_Cin(20, 46), check_if_Cin(20, 47), check_if_Cin(20, 48),
                      check_if_Cin(20, 49), check_if_Cin(20, 50)], ignore_index=True)
    return data


def check_C21():
    data = pd.concat([check_if_Cin(21, 0), check_if_Cin(21, 1), check_if_Cin(21, 2), check_if_Cin(21, 3),
                      check_if_Cin(21, 4), check_if_Cin(21, 5), check_if_Cin(21, 6), check_if_Cin(21, 7),
                      check_if_Cin(21, 8), check_if_Cin(21, 9), check_if_Cin(21, 10), check_if_Cin(21, 11),
                      check_if_Cin(21, 12), check_if_Cin(21, 13), check_if_Cin(21, 14), check_if_Cin(21, 15),
                      check_if_Cin(21, 16), check_if_Cin(21, 17), check_if_Cin(21, 18), check_if_Cin(21, 19),
                      check_if_Cin(21, 20), check_if_Cin(21, 22), check_if_Cin(21, 23), check_if_Cin(21, 24),
                      check_if_Cin(21, 25), check_if_Cin(21, 26), check_if_Cin(21, 27), check_if_Cin(21, 28),
                      check_if_Cin(21, 29), check_if_Cin(21, 30), check_if_Cin(21, 31), check_if_Cin(21, 32),
                      check_if_Cin(21, 33), check_if_Cin(21, 34), check_if_Cin(21, 35), check_if_Cin(21, 36),
                      check_if_Cin(21, 37), check_if_Cin(21, 38), check_if_Cin(21, 39), check_if_Cin(21, 40),
                      check_if_Cin(21, 41), check_if_Cin(21, 42), check_if_Cin(21, 43), check_if_Cin(21, 44),
                      check_if_Cin(21, 45), check_if_Cin(21, 46), check_if_Cin(21, 47), check_if_Cin(21, 48),
                      check_if_Cin(21, 49), check_if_Cin(21, 50)], ignore_index=True)
    return data


def check_C22():
    data = pd.concat([check_if_Cin(22, 0), check_if_Cin(22, 1), check_if_Cin(22, 2), check_if_Cin(22, 3),
                      check_if_Cin(22, 4), check_if_Cin(22, 5), check_if_Cin(22, 6), check_if_Cin(22, 7),
                      check_if_Cin(22, 8), check_if_Cin(22, 9), check_if_Cin(22, 10), check_if_Cin(22, 11),
                      check_if_Cin(22, 12), check_if_Cin(22, 13), check_if_Cin(22, 14), check_if_Cin(22, 15),
                      check_if_Cin(22, 16), check_if_Cin(22, 17), check_if_Cin(22, 18), check_if_Cin(22, 19),
                      check_if_Cin(22, 20), check_if_Cin(22, 21), check_if_Cin(22, 23), check_if_Cin(22, 24),
                      check_if_Cin(22, 25), check_if_Cin(22, 26), check_if_Cin(22, 27), check_if_Cin(22, 28),
                      check_if_Cin(22, 29), check_if_Cin(22, 30), check_if_Cin(22, 31), check_if_Cin(22, 32),
                      check_if_Cin(22, 33), check_if_Cin(22, 34), check_if_Cin(22, 35), check_if_Cin(22, 36),
                      check_if_Cin(22, 37), check_if_Cin(22, 38), check_if_Cin(22, 39), check_if_Cin(22, 40),
                      check_if_Cin(22, 41), check_if_Cin(22, 42), check_if_Cin(22, 43), check_if_Cin(22, 44),
                      check_if_Cin(22, 45), check_if_Cin(22, 46), check_if_Cin(22, 47), check_if_Cin(22, 48),
                      check_if_Cin(22, 49), check_if_Cin(22, 50)], ignore_index=True)
    return data


def check_C23():
    data = pd.concat([check_if_Cin(23, 0), check_if_Cin(23, 1), check_if_Cin(23, 2), check_if_Cin(23, 3),
                      check_if_Cin(23, 4), check_if_Cin(23, 5), check_if_Cin(23, 6), check_if_Cin(23, 7),
                      check_if_Cin(23, 8), check_if_Cin(23, 9), check_if_Cin(23, 10), check_if_Cin(23, 11),
                      check_if_Cin(23, 12), check_if_Cin(23, 13), check_if_Cin(23, 14), check_if_Cin(23, 15),
                      check_if_Cin(23, 16), check_if_Cin(23, 17), check_if_Cin(23, 18), check_if_Cin(23, 19),
                      check_if_Cin(23, 20), check_if_Cin(23, 21), check_if_Cin(23, 22), check_if_Cin(23, 24),
                      check_if_Cin(23, 25), check_if_Cin(23, 26), check_if_Cin(23, 27), check_if_Cin(23, 28),
                      check_if_Cin(23, 29), check_if_Cin(23, 30), check_if_Cin(23, 31), check_if_Cin(23, 32),
                      check_if_Cin(23, 33), check_if_Cin(23, 34), check_if_Cin(23, 35), check_if_Cin(23, 36),
                      check_if_Cin(23, 37), check_if_Cin(23, 38), check_if_Cin(23, 39), check_if_Cin(23, 40),
                      check_if_Cin(23, 41), check_if_Cin(23, 42), check_if_Cin(23, 43), check_if_Cin(23, 44),
                      check_if_Cin(23, 45), check_if_Cin(23, 46), check_if_Cin(23, 47), check_if_Cin(23, 48),
                      check_if_Cin(23, 49), check_if_Cin(23, 50)], ignore_index=True)
    return data


def check_C24():
    data = pd.concat([check_if_Cin(24, 0), check_if_Cin(24, 1), check_if_Cin(24, 2), check_if_Cin(24, 3),
                      check_if_Cin(24, 4), check_if_Cin(24, 5), check_if_Cin(24, 6), check_if_Cin(24, 7),
                      check_if_Cin(24, 8), check_if_Cin(24, 9), check_if_Cin(24, 10), check_if_Cin(24, 11),
                      check_if_Cin(24, 12), check_if_Cin(24, 13), check_if_Cin(24, 14), check_if_Cin(24, 15),
                      check_if_Cin(24, 16), check_if_Cin(24, 17), check_if_Cin(24, 18), check_if_Cin(24, 19),
                      check_if_Cin(24, 20), check_if_Cin(24, 21), check_if_Cin(24, 22), check_if_Cin(24, 23),
                      check_if_Cin(24, 25), check_if_Cin(24, 26), check_if_Cin(24, 27), check_if_Cin(24, 28),
                      check_if_Cin(24, 29), check_if_Cin(24, 30), check_if_Cin(24, 31), check_if_Cin(24, 32),
                      check_if_Cin(24, 33), check_if_Cin(24, 34), check_if_Cin(24, 35), check_if_Cin(24, 36),
                      check_if_Cin(24, 37), check_if_Cin(24, 38), check_if_Cin(24, 39), check_if_Cin(24, 40),
                      check_if_Cin(24, 41), check_if_Cin(24, 42), check_if_Cin(24, 43), check_if_Cin(24, 44),
                      check_if_Cin(24, 45), check_if_Cin(24, 46), check_if_Cin(24, 47), check_if_Cin(24, 48),
                      check_if_Cin(24, 49), check_if_Cin(24, 50)], ignore_index=True)
    return data


def check_C25():
    data = pd.concat([check_if_Cin(25, 0), check_if_Cin(25, 1), check_if_Cin(25, 2), check_if_Cin(25, 3),
                      check_if_Cin(25, 4), check_if_Cin(25, 5), check_if_Cin(25, 6), check_if_Cin(25, 7),
                      check_if_Cin(25, 8), check_if_Cin(25, 9), check_if_Cin(25, 10), check_if_Cin(25, 11),
                      check_if_Cin(25, 12), check_if_Cin(25, 13), check_if_Cin(25, 14), check_if_Cin(25, 15),
                      check_if_Cin(25, 16), check_if_Cin(25, 17), check_if_Cin(25, 18), check_if_Cin(25, 19),
                      check_if_Cin(25, 20), check_if_Cin(25, 21), check_if_Cin(25, 22), check_if_Cin(25, 23),
                      check_if_Cin(25, 24), check_if_Cin(25, 26), check_if_Cin(25, 27), check_if_Cin(25, 28),
                      check_if_Cin(25, 29), check_if_Cin(25, 30), check_if_Cin(25, 31), check_if_Cin(25, 32),
                      check_if_Cin(25, 33), check_if_Cin(25, 34), check_if_Cin(25, 35), check_if_Cin(25, 36),
                      check_if_Cin(25, 37), check_if_Cin(25, 38), check_if_Cin(25, 39), check_if_Cin(25, 40),
                      check_if_Cin(25, 41), check_if_Cin(25, 42), check_if_Cin(25, 43), check_if_Cin(25, 44),
                      check_if_Cin(25, 45), check_if_Cin(25, 46), check_if_Cin(25, 47), check_if_Cin(25, 48),
                      check_if_Cin(25, 49), check_if_Cin(25, 50)], ignore_index=True)
    return data


def check_C26():
    data = pd.concat([check_if_Cin(26, 0), check_if_Cin(26, 1), check_if_Cin(26, 2), check_if_Cin(26, 3),
                      check_if_Cin(26, 4), check_if_Cin(26, 5), check_if_Cin(26, 6), check_if_Cin(26, 7),
                      check_if_Cin(26, 8), check_if_Cin(26, 9), check_if_Cin(26, 10), check_if_Cin(26, 11),
                      check_if_Cin(26, 12), check_if_Cin(26, 13), check_if_Cin(26, 14), check_if_Cin(26, 15),
                      check_if_Cin(26, 16), check_if_Cin(26, 17), check_if_Cin(26, 18), check_if_Cin(26, 19),
                      check_if_Cin(26, 20), check_if_Cin(26, 21), check_if_Cin(26, 22), check_if_Cin(26, 23),
                      check_if_Cin(26, 24), check_if_Cin(26, 25), check_if_Cin(26, 27), check_if_Cin(26, 28),
                      check_if_Cin(26, 29), check_if_Cin(26, 30), check_if_Cin(26, 31), check_if_Cin(26, 32),
                      check_if_Cin(26, 33), check_if_Cin(26, 34), check_if_Cin(26, 35), check_if_Cin(26, 36),
                      check_if_Cin(26, 37), check_if_Cin(26, 38), check_if_Cin(26, 39), check_if_Cin(26, 40),
                      check_if_Cin(26, 41), check_if_Cin(26, 42), check_if_Cin(26, 43), check_if_Cin(26, 44),
                      check_if_Cin(26, 45), check_if_Cin(26, 46), check_if_Cin(26, 47), check_if_Cin(26, 48),
                      check_if_Cin(26, 49), check_if_Cin(26, 50)], ignore_index=True)
    return data


def check_C27():
    data = pd.concat([check_if_Cin(27, 0), check_if_Cin(27, 1), check_if_Cin(27, 2), check_if_Cin(27, 3),
                      check_if_Cin(27, 4), check_if_Cin(27, 5), check_if_Cin(27, 6), check_if_Cin(27, 7),
                      check_if_Cin(27, 8), check_if_Cin(27, 9), check_if_Cin(27, 10), check_if_Cin(27, 11),
                      check_if_Cin(27, 12), check_if_Cin(27, 13), check_if_Cin(27, 14), check_if_Cin(27, 15),
                      check_if_Cin(27, 16), check_if_Cin(27, 17), check_if_Cin(27, 18), check_if_Cin(27, 19),
                      check_if_Cin(27, 20), check_if_Cin(27, 21), check_if_Cin(27, 22), check_if_Cin(27, 23),
                      check_if_Cin(27, 24), check_if_Cin(27, 25), check_if_Cin(27, 26), check_if_Cin(27, 28),
                      check_if_Cin(27, 29), check_if_Cin(27, 30), check_if_Cin(27, 31), check_if_Cin(27, 32),
                      check_if_Cin(27, 33), check_if_Cin(27, 34), check_if_Cin(27, 35), check_if_Cin(27, 36),
                      check_if_Cin(27, 37), check_if_Cin(27, 38), check_if_Cin(27, 39), check_if_Cin(27, 40),
                      check_if_Cin(27, 41), check_if_Cin(27, 42), check_if_Cin(27, 43), check_if_Cin(27, 44),
                      check_if_Cin(27, 45), check_if_Cin(27, 46), check_if_Cin(27, 47), check_if_Cin(27, 48),
                      check_if_Cin(27, 49), check_if_Cin(27, 50)], ignore_index=True)
    return data


def check_C28():
    data = pd.concat([check_if_Cin(28, 0), check_if_Cin(28, 1), check_if_Cin(28, 2), check_if_Cin(28, 3),
                      check_if_Cin(28, 4), check_if_Cin(28, 5), check_if_Cin(28, 6), check_if_Cin(28, 7),
                      check_if_Cin(28, 8), check_if_Cin(28, 9), check_if_Cin(28, 10), check_if_Cin(28, 11),
                      check_if_Cin(28, 12), check_if_Cin(28, 13), check_if_Cin(28, 14), check_if_Cin(28, 15),
                      check_if_Cin(28, 16), check_if_Cin(28, 17), check_if_Cin(28, 18), check_if_Cin(28, 19),
                      check_if_Cin(28, 20), check_if_Cin(28, 21), check_if_Cin(28, 22), check_if_Cin(28, 23),
                      check_if_Cin(28, 24), check_if_Cin(28, 25), check_if_Cin(28, 26), check_if_Cin(28, 27),
                      check_if_Cin(28, 29), check_if_Cin(28, 30), check_if_Cin(28, 31), check_if_Cin(28, 32),
                      check_if_Cin(28, 33), check_if_Cin(28, 34), check_if_Cin(28, 35), check_if_Cin(28, 36),
                      check_if_Cin(28, 37), check_if_Cin(28, 38), check_if_Cin(28, 39), check_if_Cin(28, 40),
                      check_if_Cin(28, 41), check_if_Cin(28, 42), check_if_Cin(28, 43), check_if_Cin(28, 44),
                      check_if_Cin(28, 45), check_if_Cin(28, 46), check_if_Cin(28, 47), check_if_Cin(28, 48),
                      check_if_Cin(28, 49), check_if_Cin(28, 50)], ignore_index=True)
    return data


def check_C29():
    data = pd.concat([check_if_Cin(29, 0), check_if_Cin(29, 1), check_if_Cin(29, 2), check_if_Cin(29, 3),
                      check_if_Cin(29, 4), check_if_Cin(29, 5), check_if_Cin(29, 6), check_if_Cin(29, 7),
                      check_if_Cin(29, 8), check_if_Cin(29, 9), check_if_Cin(29, 10), check_if_Cin(29, 11),
                      check_if_Cin(29, 12), check_if_Cin(29, 13), check_if_Cin(29, 14), check_if_Cin(29, 15),
                      check_if_Cin(29, 16), check_if_Cin(29, 17), check_if_Cin(29, 18), check_if_Cin(29, 19),
                      check_if_Cin(29, 20), check_if_Cin(29, 21), check_if_Cin(29, 22), check_if_Cin(29, 23),
                      check_if_Cin(29, 24), check_if_Cin(29, 25), check_if_Cin(29, 26), check_if_Cin(29, 27),
                      check_if_Cin(29, 28), check_if_Cin(29, 30), check_if_Cin(29, 31), check_if_Cin(29, 32),
                      check_if_Cin(29, 33), check_if_Cin(29, 34), check_if_Cin(29, 35), check_if_Cin(29, 36),
                      check_if_Cin(29, 37), check_if_Cin(29, 38), check_if_Cin(29, 39), check_if_Cin(29, 40),
                      check_if_Cin(29, 41), check_if_Cin(29, 42), check_if_Cin(29, 43), check_if_Cin(29, 44),
                      check_if_Cin(29, 45), check_if_Cin(29, 46), check_if_Cin(29, 47), check_if_Cin(29, 48),
                      check_if_Cin(29, 49), check_if_Cin(29, 50)], ignore_index=True)
    return data


def check_C30():
    data = pd.concat([check_if_Cin(30, 0), check_if_Cin(30, 1), check_if_Cin(30, 2), check_if_Cin(30, 3),
                      check_if_Cin(30, 4), check_if_Cin(30, 5), check_if_Cin(30, 6), check_if_Cin(30, 7),
                      check_if_Cin(30, 8), check_if_Cin(30, 9), check_if_Cin(30, 10), check_if_Cin(30, 11),
                      check_if_Cin(30, 12), check_if_Cin(30, 13), check_if_Cin(30, 14), check_if_Cin(30, 15),
                      check_if_Cin(30, 16), check_if_Cin(30, 17), check_if_Cin(30, 18), check_if_Cin(30, 19),
                      check_if_Cin(30, 20), check_if_Cin(30, 21), check_if_Cin(30, 22), check_if_Cin(30, 23),
                      check_if_Cin(30, 24), check_if_Cin(30, 25), check_if_Cin(30, 26), check_if_Cin(30, 27),
                      check_if_Cin(30, 28), check_if_Cin(30, 29), check_if_Cin(30, 31), check_if_Cin(30, 32),
                      check_if_Cin(30, 33), check_if_Cin(30, 34), check_if_Cin(30, 35), check_if_Cin(30, 36),
                      check_if_Cin(30, 37), check_if_Cin(30, 38), check_if_Cin(30, 39), check_if_Cin(30, 40),
                      check_if_Cin(30, 41), check_if_Cin(30, 42), check_if_Cin(30, 43), check_if_Cin(30, 44),
                      check_if_Cin(30, 45), check_if_Cin(30, 46), check_if_Cin(30, 47), check_if_Cin(30, 48),
                      check_if_Cin(30, 49), check_if_Cin(30, 50)], ignore_index=True)
    return data


def check_C31():
    data = pd.concat([check_if_Cin(31, 0), check_if_Cin(31, 1), check_if_Cin(31, 2), check_if_Cin(31, 3),
                      check_if_Cin(31, 4), check_if_Cin(31, 5), check_if_Cin(31, 6), check_if_Cin(31, 7),
                      check_if_Cin(31, 8), check_if_Cin(31, 9), check_if_Cin(31, 10), check_if_Cin(31, 11),
                      check_if_Cin(31, 12), check_if_Cin(31, 13), check_if_Cin(31, 14), check_if_Cin(31, 15),
                      check_if_Cin(31, 16), check_if_Cin(31, 17), check_if_Cin(31, 18), check_if_Cin(31, 19),
                      check_if_Cin(31, 20), check_if_Cin(31, 21), check_if_Cin(31, 22), check_if_Cin(31, 23),
                      check_if_Cin(31, 24), check_if_Cin(31, 25), check_if_Cin(31, 26), check_if_Cin(31, 27),
                      check_if_Cin(31, 28), check_if_Cin(31, 29), check_if_Cin(31, 30), check_if_Cin(31, 32),
                      check_if_Cin(31, 33), check_if_Cin(31, 34), check_if_Cin(31, 35), check_if_Cin(31, 36),
                      check_if_Cin(31, 37), check_if_Cin(31, 38), check_if_Cin(31, 39), check_if_Cin(31, 40),
                      check_if_Cin(31, 41), check_if_Cin(31, 42), check_if_Cin(31, 43), check_if_Cin(31, 44),
                      check_if_Cin(31, 45), check_if_Cin(31, 46), check_if_Cin(31, 47), check_if_Cin(31, 48),
                      check_if_Cin(31, 49), check_if_Cin(31, 50)], ignore_index=True)
    return data


def check_C32():
    data = pd.concat([check_if_Cin(32, 0), check_if_Cin(32, 1), check_if_Cin(32, 2), check_if_Cin(32, 3),
                      check_if_Cin(32, 4), check_if_Cin(32, 5), check_if_Cin(32, 6), check_if_Cin(32, 7),
                      check_if_Cin(32, 8), check_if_Cin(32, 9), check_if_Cin(32, 10), check_if_Cin(32, 11),
                      check_if_Cin(32, 12), check_if_Cin(32, 13), check_if_Cin(32, 14), check_if_Cin(32, 15),
                      check_if_Cin(32, 16), check_if_Cin(32, 17), check_if_Cin(32, 18), check_if_Cin(32, 19),
                      check_if_Cin(32, 20), check_if_Cin(32, 21), check_if_Cin(32, 22), check_if_Cin(32, 23),
                      check_if_Cin(32, 24), check_if_Cin(32, 25), check_if_Cin(32, 26), check_if_Cin(32, 27),
                      check_if_Cin(32, 28), check_if_Cin(32, 29), check_if_Cin(32, 30), check_if_Cin(32, 31),
                      check_if_Cin(32, 33), check_if_Cin(32, 34), check_if_Cin(32, 35), check_if_Cin(32, 36),
                      check_if_Cin(32, 37), check_if_Cin(32, 38), check_if_Cin(32, 39), check_if_Cin(32, 40),
                      check_if_Cin(32, 41), check_if_Cin(32, 42), check_if_Cin(32, 43), check_if_Cin(32, 44),
                      check_if_Cin(32, 45), check_if_Cin(32, 46), check_if_Cin(32, 47), check_if_Cin(32, 48),
                      check_if_Cin(32, 49), check_if_Cin(32, 50)], ignore_index=True)
    return data


def check_C33():
    data = pd.concat([check_if_Cin(33, 0), check_if_Cin(33, 1), check_if_Cin(33, 2), check_if_Cin(33, 3),
                      check_if_Cin(33, 4), check_if_Cin(33, 5), check_if_Cin(33, 6), check_if_Cin(33, 7),
                      check_if_Cin(33, 8), check_if_Cin(33, 9), check_if_Cin(33, 10), check_if_Cin(33, 11),
                      check_if_Cin(33, 12), check_if_Cin(33, 13), check_if_Cin(33, 14), check_if_Cin(33, 15),
                      check_if_Cin(33, 16), check_if_Cin(33, 17), check_if_Cin(33, 18), check_if_Cin(33, 19),
                      check_if_Cin(33, 20), check_if_Cin(33, 21), check_if_Cin(33, 22), check_if_Cin(33, 23),
                      check_if_Cin(33, 24), check_if_Cin(33, 25), check_if_Cin(33, 26), check_if_Cin(33, 27),
                      check_if_Cin(33, 28), check_if_Cin(33, 29), check_if_Cin(33, 30), check_if_Cin(33, 31),
                      check_if_Cin(33, 32), check_if_Cin(33, 34), check_if_Cin(33, 35), check_if_Cin(33, 36),
                      check_if_Cin(33, 37), check_if_Cin(33, 38), check_if_Cin(33, 39), check_if_Cin(33, 40),
                      check_if_Cin(33, 41), check_if_Cin(33, 42), check_if_Cin(33, 43), check_if_Cin(33, 44),
                      check_if_Cin(33, 45), check_if_Cin(33, 46), check_if_Cin(33, 47), check_if_Cin(33, 48),
                      check_if_Cin(33, 49), check_if_Cin(33, 50)], ignore_index=True)
    return data


def check_C34():
    data = pd.concat([check_if_Cin(34, 0), check_if_Cin(34, 1), check_if_Cin(34, 2), check_if_Cin(34, 3),
                      check_if_Cin(34, 4), check_if_Cin(34, 5), check_if_Cin(34, 6), check_if_Cin(34, 7),
                      check_if_Cin(34, 8), check_if_Cin(34, 9), check_if_Cin(34, 10), check_if_Cin(34, 11),
                      check_if_Cin(34, 12), check_if_Cin(34, 13), check_if_Cin(34, 14), check_if_Cin(34, 15),
                      check_if_Cin(34, 16), check_if_Cin(34, 17), check_if_Cin(34, 18), check_if_Cin(34, 19),
                      check_if_Cin(34, 20), check_if_Cin(34, 21), check_if_Cin(34, 22), check_if_Cin(34, 23),
                      check_if_Cin(34, 24), check_if_Cin(34, 25), check_if_Cin(34, 26), check_if_Cin(34, 27),
                      check_if_Cin(34, 28), check_if_Cin(34, 29), check_if_Cin(34, 30), check_if_Cin(34, 31),
                      check_if_Cin(34, 32), check_if_Cin(34, 33), check_if_Cin(34, 35), check_if_Cin(34, 36),
                      check_if_Cin(34, 37), check_if_Cin(34, 38), check_if_Cin(34, 39), check_if_Cin(34, 40),
                      check_if_Cin(34, 41), check_if_Cin(34, 42), check_if_Cin(34, 43), check_if_Cin(34, 44),
                      check_if_Cin(34, 45), check_if_Cin(34, 46), check_if_Cin(34, 47), check_if_Cin(34, 48),
                      check_if_Cin(34, 49), check_if_Cin(34, 50)], ignore_index=True)
    return data


def check_C35():
    data = pd.concat([check_if_Cin(35, 0), check_if_Cin(35, 1), check_if_Cin(35, 2), check_if_Cin(35, 3),
                      check_if_Cin(35, 4), check_if_Cin(35, 5), check_if_Cin(35, 6), check_if_Cin(35, 7),
                      check_if_Cin(35, 8), check_if_Cin(35, 9), check_if_Cin(35, 10), check_if_Cin(35, 11),
                      check_if_Cin(35, 12), check_if_Cin(35, 13), check_if_Cin(35, 14), check_if_Cin(35, 15),
                      check_if_Cin(35, 16), check_if_Cin(35, 17), check_if_Cin(35, 18), check_if_Cin(35, 19),
                      check_if_Cin(35, 20), check_if_Cin(35, 21), check_if_Cin(35, 22), check_if_Cin(35, 23),
                      check_if_Cin(35, 24), check_if_Cin(35, 25), check_if_Cin(35, 26), check_if_Cin(35, 27),
                      check_if_Cin(35, 28), check_if_Cin(35, 29), check_if_Cin(35, 30), check_if_Cin(35, 31),
                      check_if_Cin(35, 32), check_if_Cin(35, 33), check_if_Cin(35, 34), check_if_Cin(35, 36),
                      check_if_Cin(35, 37), check_if_Cin(35, 38), check_if_Cin(35, 39), check_if_Cin(35, 40),
                      check_if_Cin(35, 41), check_if_Cin(35, 42), check_if_Cin(35, 43), check_if_Cin(35, 44),
                      check_if_Cin(35, 45), check_if_Cin(35, 46), check_if_Cin(35, 47), check_if_Cin(35, 48),
                      check_if_Cin(35, 49), check_if_Cin(35, 50)], ignore_index=True)
    return data


def check_C36():
    data = pd.concat([check_if_Cin(36, 0), check_if_Cin(36, 1), check_if_Cin(36, 2), check_if_Cin(36, 3),
                      check_if_Cin(36, 4), check_if_Cin(36, 5), check_if_Cin(36, 6), check_if_Cin(36, 7),
                      check_if_Cin(36, 8), check_if_Cin(36, 9), check_if_Cin(36, 10), check_if_Cin(36, 11),
                      check_if_Cin(36, 12), check_if_Cin(36, 13), check_if_Cin(36, 14), check_if_Cin(36, 15),
                      check_if_Cin(36, 16), check_if_Cin(36, 17), check_if_Cin(36, 18), check_if_Cin(36, 19),
                      check_if_Cin(36, 20), check_if_Cin(36, 21), check_if_Cin(36, 22), check_if_Cin(36, 23),
                      check_if_Cin(36, 24), check_if_Cin(36, 25), check_if_Cin(36, 26), check_if_Cin(36, 27),
                      check_if_Cin(36, 28), check_if_Cin(36, 29), check_if_Cin(36, 30), check_if_Cin(36, 31),
                      check_if_Cin(36, 32), check_if_Cin(36, 33), check_if_Cin(36, 34), check_if_Cin(36, 35),
                      check_if_Cin(36, 37), check_if_Cin(36, 38), check_if_Cin(36, 39), check_if_Cin(36, 40),
                      check_if_Cin(36, 41), check_if_Cin(36, 42), check_if_Cin(36, 43), check_if_Cin(36, 44),
                      check_if_Cin(36, 45), check_if_Cin(36, 46), check_if_Cin(36, 47), check_if_Cin(36, 48),
                      check_if_Cin(36, 49), check_if_Cin(36, 50)], ignore_index=True)
    return data


def check_C37():
    data = pd.concat([check_if_Cin(37, 0), check_if_Cin(37, 1), check_if_Cin(37, 2), check_if_Cin(37, 3),
                      check_if_Cin(37, 4), check_if_Cin(37, 5), check_if_Cin(37, 6), check_if_Cin(37, 7),
                      check_if_Cin(37, 8), check_if_Cin(37, 9), check_if_Cin(37, 10), check_if_Cin(37, 11),
                      check_if_Cin(37, 12), check_if_Cin(37, 13), check_if_Cin(37, 14), check_if_Cin(37, 15),
                      check_if_Cin(37, 16), check_if_Cin(37, 17), check_if_Cin(37, 18), check_if_Cin(37, 19),
                      check_if_Cin(37, 20), check_if_Cin(37, 21), check_if_Cin(37, 22), check_if_Cin(37, 23),
                      check_if_Cin(37, 24), check_if_Cin(37, 25), check_if_Cin(37, 26), check_if_Cin(37, 27),
                      check_if_Cin(37, 28), check_if_Cin(37, 29), check_if_Cin(37, 30), check_if_Cin(37, 31),
                      check_if_Cin(37, 32), check_if_Cin(37, 33), check_if_Cin(37, 34), check_if_Cin(37, 35),
                      check_if_Cin(37, 36), check_if_Cin(37, 38), check_if_Cin(37, 39), check_if_Cin(37, 40),
                      check_if_Cin(37, 41), check_if_Cin(37, 42), check_if_Cin(37, 43), check_if_Cin(37, 44),
                      check_if_Cin(37, 45), check_if_Cin(37, 46), check_if_Cin(37, 47), check_if_Cin(37, 48),
                      check_if_Cin(37, 49), check_if_Cin(37, 50)], ignore_index=True)
    return data


def check_C38():
    data = pd.concat([check_if_Cin(38, 0), check_if_Cin(38, 1), check_if_Cin(38, 2), check_if_Cin(38, 3),
                      check_if_Cin(38, 4), check_if_Cin(38, 5), check_if_Cin(38, 6), check_if_Cin(38, 7),
                      check_if_Cin(38, 8), check_if_Cin(38, 9), check_if_Cin(38, 10), check_if_Cin(38, 11),
                      check_if_Cin(38, 12), check_if_Cin(38, 13), check_if_Cin(38, 14), check_if_Cin(38, 15),
                      check_if_Cin(38, 16), check_if_Cin(38, 17), check_if_Cin(38, 18), check_if_Cin(38, 19),
                      check_if_Cin(38, 20), check_if_Cin(38, 21), check_if_Cin(38, 22), check_if_Cin(38, 23),
                      check_if_Cin(38, 24), check_if_Cin(38, 25), check_if_Cin(38, 26), check_if_Cin(38, 27),
                      check_if_Cin(38, 28), check_if_Cin(38, 29), check_if_Cin(38, 30), check_if_Cin(38, 31),
                      check_if_Cin(38, 32), check_if_Cin(38, 33), check_if_Cin(38, 34), check_if_Cin(38, 35),
                      check_if_Cin(38, 36), check_if_Cin(38, 37), check_if_Cin(38, 39), check_if_Cin(38, 40),
                      check_if_Cin(38, 41), check_if_Cin(38, 42), check_if_Cin(38, 43), check_if_Cin(38, 44),
                      check_if_Cin(38, 45), check_if_Cin(38, 46), check_if_Cin(38, 47), check_if_Cin(38, 48),
                      check_if_Cin(38, 49), check_if_Cin(38, 50)], ignore_index=True)
    return data


def check_C39():
    data = pd.concat([check_if_Cin(39, 0), check_if_Cin(39, 1), check_if_Cin(39, 2), check_if_Cin(39, 3),
                      check_if_Cin(39, 4), check_if_Cin(39, 5), check_if_Cin(39, 6), check_if_Cin(39, 7),
                      check_if_Cin(39, 8), check_if_Cin(39, 9), check_if_Cin(39, 10), check_if_Cin(39, 11),
                      check_if_Cin(39, 12), check_if_Cin(39, 13), check_if_Cin(39, 14), check_if_Cin(39, 15),
                      check_if_Cin(39, 16), check_if_Cin(39, 17), check_if_Cin(39, 18), check_if_Cin(39, 19),
                      check_if_Cin(39, 20), check_if_Cin(39, 21), check_if_Cin(39, 22), check_if_Cin(39, 23),
                      check_if_Cin(39, 24), check_if_Cin(39, 25), check_if_Cin(39, 26), check_if_Cin(39, 27),
                      check_if_Cin(39, 28), check_if_Cin(39, 29), check_if_Cin(39, 30), check_if_Cin(39, 31),
                      check_if_Cin(39, 32), check_if_Cin(39, 33), check_if_Cin(39, 34), check_if_Cin(39, 35),
                      check_if_Cin(39, 36), check_if_Cin(39, 37), check_if_Cin(39, 38), check_if_Cin(39, 40),
                      check_if_Cin(39, 41), check_if_Cin(39, 42), check_if_Cin(39, 43), check_if_Cin(39, 44),
                      check_if_Cin(39, 45), check_if_Cin(39, 46), check_if_Cin(39, 47), check_if_Cin(39, 48),
                      check_if_Cin(39, 49), check_if_Cin(39, 50)], ignore_index=True)
    return data


def check_C40():
    data = pd.concat([check_if_Cin(40, 0), check_if_Cin(40, 1), check_if_Cin(40, 2), check_if_Cin(40, 3),
                      check_if_Cin(40, 4), check_if_Cin(40, 5), check_if_Cin(40, 6), check_if_Cin(40, 7),
                      check_if_Cin(40, 8), check_if_Cin(40, 9), check_if_Cin(40, 10), check_if_Cin(40, 11),
                      check_if_Cin(40, 12), check_if_Cin(40, 13), check_if_Cin(40, 14), check_if_Cin(40, 15),
                      check_if_Cin(40, 16), check_if_Cin(40, 17), check_if_Cin(40, 18), check_if_Cin(40, 19),
                      check_if_Cin(40, 20), check_if_Cin(40, 21), check_if_Cin(40, 22), check_if_Cin(40, 23),
                      check_if_Cin(40, 24), check_if_Cin(40, 25), check_if_Cin(40, 26), check_if_Cin(40, 27),
                      check_if_Cin(40, 28), check_if_Cin(40, 29), check_if_Cin(40, 30), check_if_Cin(40, 31),
                      check_if_Cin(40, 32), check_if_Cin(40, 33), check_if_Cin(40, 34), check_if_Cin(40, 35),
                      check_if_Cin(40, 36), check_if_Cin(40, 37), check_if_Cin(40, 38), check_if_Cin(40, 39),
                      check_if_Cin(40, 41), check_if_Cin(40, 42), check_if_Cin(40, 43), check_if_Cin(40, 44),
                      check_if_Cin(40, 45), check_if_Cin(40, 46), check_if_Cin(40, 47), check_if_Cin(40, 48),
                      check_if_Cin(40, 49), check_if_Cin(40, 50)], ignore_index=True)
    return data


def check_C41():
    data = pd.concat([check_if_Cin(41, 0), check_if_Cin(41, 1), check_if_Cin(41, 2), check_if_Cin(41, 3),
                      check_if_Cin(41, 4), check_if_Cin(41, 5), check_if_Cin(41, 6), check_if_Cin(41, 7),
                      check_if_Cin(41, 8), check_if_Cin(41, 9), check_if_Cin(41, 10), check_if_Cin(41, 11),
                      check_if_Cin(41, 12), check_if_Cin(41, 13), check_if_Cin(41, 14), check_if_Cin(41, 15),
                      check_if_Cin(41, 16), check_if_Cin(41, 17), check_if_Cin(41, 18), check_if_Cin(41, 19),
                      check_if_Cin(41, 20), check_if_Cin(41, 21), check_if_Cin(41, 22), check_if_Cin(41, 23),
                      check_if_Cin(41, 24), check_if_Cin(41, 25), check_if_Cin(41, 26), check_if_Cin(41, 27),
                      check_if_Cin(41, 28), check_if_Cin(41, 29), check_if_Cin(41, 30), check_if_Cin(41, 31),
                      check_if_Cin(41, 32), check_if_Cin(41, 33), check_if_Cin(41, 34), check_if_Cin(41, 35),
                      check_if_Cin(41, 36), check_if_Cin(41, 37), check_if_Cin(41, 38), check_if_Cin(41, 39),
                      check_if_Cin(41, 40), check_if_Cin(41, 42), check_if_Cin(41, 43), check_if_Cin(41, 44),
                      check_if_Cin(41, 45), check_if_Cin(41, 46), check_if_Cin(41, 47), check_if_Cin(41, 48),
                      check_if_Cin(41, 49), check_if_Cin(41, 50)], ignore_index=True)
    return data


def check_C42():
    data = pd.concat([check_if_Cin(42, 0), check_if_Cin(42, 1), check_if_Cin(42, 2), check_if_Cin(42, 3),
                      check_if_Cin(42, 4), check_if_Cin(42, 5), check_if_Cin(42, 6), check_if_Cin(42, 7),
                      check_if_Cin(42, 8), check_if_Cin(42, 9), check_if_Cin(42, 10), check_if_Cin(42, 11),
                      check_if_Cin(42, 12), check_if_Cin(42, 13), check_if_Cin(42, 14), check_if_Cin(42, 15),
                      check_if_Cin(42, 16), check_if_Cin(42, 17), check_if_Cin(42, 18), check_if_Cin(42, 19),
                      check_if_Cin(42, 20), check_if_Cin(42, 21), check_if_Cin(42, 22), check_if_Cin(42, 23),
                      check_if_Cin(42, 24), check_if_Cin(42, 25), check_if_Cin(42, 26), check_if_Cin(42, 27),
                      check_if_Cin(42, 28), check_if_Cin(42, 29), check_if_Cin(42, 30), check_if_Cin(42, 31),
                      check_if_Cin(42, 32), check_if_Cin(42, 33), check_if_Cin(42, 34), check_if_Cin(42, 35),
                      check_if_Cin(42, 36), check_if_Cin(42, 37), check_if_Cin(42, 38), check_if_Cin(42, 39),
                      check_if_Cin(42, 40), check_if_Cin(42, 41), check_if_Cin(42, 43), check_if_Cin(42, 44),
                      check_if_Cin(42, 45), check_if_Cin(42, 46), check_if_Cin(42, 47), check_if_Cin(42, 48),
                      check_if_Cin(42, 49), check_if_Cin(42, 50)], ignore_index=True)
    return data


def check_C43():
    data = pd.concat([check_if_Cin(43, 0), check_if_Cin(43, 1), check_if_Cin(43, 2), check_if_Cin(43, 3),
                      check_if_Cin(43, 4), check_if_Cin(43, 5), check_if_Cin(43, 6), check_if_Cin(43, 7),
                      check_if_Cin(43, 8), check_if_Cin(43, 9), check_if_Cin(43, 10), check_if_Cin(43, 11),
                      check_if_Cin(43, 12), check_if_Cin(43, 13), check_if_Cin(43, 14), check_if_Cin(43, 15),
                      check_if_Cin(43, 16), check_if_Cin(43, 17), check_if_Cin(43, 18), check_if_Cin(43, 19),
                      check_if_Cin(43, 20), check_if_Cin(43, 21), check_if_Cin(43, 22), check_if_Cin(43, 23),
                      check_if_Cin(43, 24), check_if_Cin(43, 25), check_if_Cin(43, 26), check_if_Cin(43, 27),
                      check_if_Cin(43, 28), check_if_Cin(43, 29), check_if_Cin(43, 30), check_if_Cin(43, 31),
                      check_if_Cin(43, 32), check_if_Cin(43, 33), check_if_Cin(43, 34), check_if_Cin(43, 35),
                      check_if_Cin(43, 36), check_if_Cin(43, 37), check_if_Cin(43, 38), check_if_Cin(43, 39),
                      check_if_Cin(43, 40), check_if_Cin(43, 41), check_if_Cin(43, 42), check_if_Cin(43, 44),
                      check_if_Cin(43, 45), check_if_Cin(43, 46), check_if_Cin(43, 47), check_if_Cin(43, 48),
                      check_if_Cin(43, 49), check_if_Cin(43, 50)], ignore_index=True)
    return data


def check_C44():
    data = pd.concat([check_if_Cin(44, 0), check_if_Cin(44, 1), check_if_Cin(44, 2), check_if_Cin(44, 3),
                      check_if_Cin(44, 4), check_if_Cin(44, 5), check_if_Cin(44, 6), check_if_Cin(44, 7),
                      check_if_Cin(44, 8), check_if_Cin(44, 9), check_if_Cin(44, 10), check_if_Cin(44, 11),
                      check_if_Cin(44, 12), check_if_Cin(44, 13), check_if_Cin(44, 14), check_if_Cin(44, 15),
                      check_if_Cin(44, 16), check_if_Cin(44, 17), check_if_Cin(44, 18), check_if_Cin(44, 19),
                      check_if_Cin(44, 20), check_if_Cin(44, 21), check_if_Cin(44, 22), check_if_Cin(44, 23),
                      check_if_Cin(44, 24), check_if_Cin(44, 25), check_if_Cin(44, 26), check_if_Cin(44, 27),
                      check_if_Cin(44, 28), check_if_Cin(44, 29), check_if_Cin(44, 30), check_if_Cin(44, 31),
                      check_if_Cin(44, 32), check_if_Cin(44, 33), check_if_Cin(44, 34), check_if_Cin(44, 35),
                      check_if_Cin(44, 36), check_if_Cin(44, 37), check_if_Cin(44, 38), check_if_Cin(44, 39),
                      check_if_Cin(44, 40), check_if_Cin(44, 41), check_if_Cin(44, 42), check_if_Cin(44, 43),
                      check_if_Cin(44, 45), check_if_Cin(44, 46), check_if_Cin(44, 47), check_if_Cin(44, 48),
                      check_if_Cin(44, 49), check_if_Cin(44, 50)], ignore_index=True)
    return data


def check_C45():
    data = pd.concat([check_if_Cin(45, 0), check_if_Cin(45, 1), check_if_Cin(45, 2), check_if_Cin(45, 3),
                      check_if_Cin(45, 4), check_if_Cin(45, 5), check_if_Cin(45, 6), check_if_Cin(45, 7),
                      check_if_Cin(45, 8), check_if_Cin(45, 9), check_if_Cin(45, 10), check_if_Cin(45, 11),
                      check_if_Cin(45, 12), check_if_Cin(45, 13), check_if_Cin(45, 14), check_if_Cin(45, 15),
                      check_if_Cin(45, 16), check_if_Cin(45, 17), check_if_Cin(45, 18), check_if_Cin(45, 19),
                      check_if_Cin(45, 20), check_if_Cin(45, 21), check_if_Cin(45, 22), check_if_Cin(45, 23),
                      check_if_Cin(45, 24), check_if_Cin(45, 25), check_if_Cin(45, 26), check_if_Cin(45, 27),
                      check_if_Cin(45, 28), check_if_Cin(45, 29), check_if_Cin(45, 30), check_if_Cin(45, 31),
                      check_if_Cin(45, 32), check_if_Cin(45, 33), check_if_Cin(45, 34), check_if_Cin(45, 35),
                      check_if_Cin(45, 36), check_if_Cin(45, 37), check_if_Cin(45, 38), check_if_Cin(45, 39),
                      check_if_Cin(45, 40), check_if_Cin(45, 41), check_if_Cin(45, 42), check_if_Cin(45, 43),
                      check_if_Cin(45, 44), check_if_Cin(45, 46), check_if_Cin(45, 47), check_if_Cin(45, 48),
                      check_if_Cin(45, 49), check_if_Cin(45, 50)], ignore_index=True)
    return data


def check_C46():
    data = pd.concat([check_if_Cin(46, 0), check_if_Cin(46, 1), check_if_Cin(46, 2), check_if_Cin(46, 3),
                      check_if_Cin(46, 4), check_if_Cin(46, 5), check_if_Cin(46, 6), check_if_Cin(46, 7),
                      check_if_Cin(46, 8), check_if_Cin(46, 9), check_if_Cin(46, 10), check_if_Cin(46, 11),
                      check_if_Cin(46, 12), check_if_Cin(46, 13), check_if_Cin(46, 14), check_if_Cin(46, 15),
                      check_if_Cin(46, 16), check_if_Cin(46, 17), check_if_Cin(46, 18), check_if_Cin(46, 19),
                      check_if_Cin(46, 20), check_if_Cin(46, 21), check_if_Cin(46, 22), check_if_Cin(46, 23),
                      check_if_Cin(46, 24), check_if_Cin(46, 25), check_if_Cin(46, 26), check_if_Cin(46, 27),
                      check_if_Cin(46, 28), check_if_Cin(46, 29), check_if_Cin(46, 30), check_if_Cin(46, 31),
                      check_if_Cin(46, 32), check_if_Cin(46, 33), check_if_Cin(46, 34), check_if_Cin(46, 35),
                      check_if_Cin(46, 36), check_if_Cin(46, 37), check_if_Cin(46, 38), check_if_Cin(46, 39),
                      check_if_Cin(46, 40), check_if_Cin(46, 41), check_if_Cin(46, 42), check_if_Cin(46, 43),
                      check_if_Cin(46, 44), check_if_Cin(46, 45), check_if_Cin(46, 47), check_if_Cin(46, 48),
                      check_if_Cin(46, 49), check_if_Cin(46, 50)], ignore_index=True)
    return data


def check_C47():
    data = pd.concat([check_if_Cin(47, 0), check_if_Cin(47, 1), check_if_Cin(47, 2), check_if_Cin(47, 3),
                      check_if_Cin(47, 4), check_if_Cin(47, 5), check_if_Cin(47, 6), check_if_Cin(47, 7),
                      check_if_Cin(47, 8), check_if_Cin(47, 9), check_if_Cin(47, 10), check_if_Cin(47, 11),
                      check_if_Cin(47, 12), check_if_Cin(47, 13), check_if_Cin(47, 14), check_if_Cin(47, 15),
                      check_if_Cin(47, 16), check_if_Cin(47, 17), check_if_Cin(47, 18), check_if_Cin(47, 19),
                      check_if_Cin(47, 20), check_if_Cin(47, 21), check_if_Cin(47, 22), check_if_Cin(47, 23),
                      check_if_Cin(47, 24), check_if_Cin(47, 25), check_if_Cin(47, 26), check_if_Cin(47, 27),
                      check_if_Cin(47, 28), check_if_Cin(47, 29), check_if_Cin(47, 30), check_if_Cin(47, 31),
                      check_if_Cin(47, 32), check_if_Cin(47, 33), check_if_Cin(47, 34), check_if_Cin(47, 35),
                      check_if_Cin(47, 36), check_if_Cin(47, 37), check_if_Cin(47, 38), check_if_Cin(47, 39),
                      check_if_Cin(47, 40), check_if_Cin(47, 41), check_if_Cin(47, 42), check_if_Cin(47, 43),
                      check_if_Cin(47, 44), check_if_Cin(47, 45), check_if_Cin(47, 46), check_if_Cin(47, 48),
                      check_if_Cin(47, 49), check_if_Cin(47, 50)], ignore_index=True)
    return data


def check_C48():
    data = pd.concat([check_if_Cin(48, 0), check_if_Cin(48, 1), check_if_Cin(48, 2), check_if_Cin(48, 3),
                      check_if_Cin(48, 4), check_if_Cin(48, 5), check_if_Cin(48, 6), check_if_Cin(48, 7),
                      check_if_Cin(48, 8), check_if_Cin(48, 9), check_if_Cin(48, 10), check_if_Cin(48, 11),
                      check_if_Cin(48, 12), check_if_Cin(48, 13), check_if_Cin(48, 14), check_if_Cin(48, 15),
                      check_if_Cin(48, 16), check_if_Cin(48, 17), check_if_Cin(48, 18), check_if_Cin(48, 19),
                      check_if_Cin(48, 20), check_if_Cin(48, 21), check_if_Cin(48, 22), check_if_Cin(48, 23),
                      check_if_Cin(48, 24), check_if_Cin(48, 25), check_if_Cin(48, 26), check_if_Cin(48, 27),
                      check_if_Cin(48, 28), check_if_Cin(48, 29), check_if_Cin(48, 30), check_if_Cin(48, 31),
                      check_if_Cin(48, 32), check_if_Cin(48, 33), check_if_Cin(48, 34), check_if_Cin(48, 35),
                      check_if_Cin(48, 36), check_if_Cin(48, 37), check_if_Cin(48, 38), check_if_Cin(48, 39),
                      check_if_Cin(48, 40), check_if_Cin(48, 41), check_if_Cin(48, 42), check_if_Cin(48, 43),
                      check_if_Cin(48, 44), check_if_Cin(48, 45), check_if_Cin(48, 46), check_if_Cin(48, 47),
                      check_if_Cin(48, 49), check_if_Cin(48, 50)], ignore_index=True)
    return data


def check_C49():
    data = pd.concat([check_if_Cin(49, 0), check_if_Cin(49, 1), check_if_Cin(49, 2), check_if_Cin(49, 3),
                      check_if_Cin(49, 4), check_if_Cin(49, 5), check_if_Cin(49, 6), check_if_Cin(49, 7),
                      check_if_Cin(49, 8), check_if_Cin(49, 9), check_if_Cin(49, 10), check_if_Cin(49, 11),
                      check_if_Cin(49, 12), check_if_Cin(49, 13), check_if_Cin(49, 14), check_if_Cin(49, 15),
                      check_if_Cin(49, 16), check_if_Cin(49, 17), check_if_Cin(49, 18), check_if_Cin(49, 19),
                      check_if_Cin(49, 20), check_if_Cin(49, 21), check_if_Cin(49, 22), check_if_Cin(49, 23),
                      check_if_Cin(49, 24), check_if_Cin(49, 25), check_if_Cin(49, 26), check_if_Cin(49, 27),
                      check_if_Cin(49, 28), check_if_Cin(49, 29), check_if_Cin(49, 30), check_if_Cin(49, 31),
                      check_if_Cin(49, 32), check_if_Cin(49, 33), check_if_Cin(49, 34), check_if_Cin(49, 35),
                      check_if_Cin(49, 36), check_if_Cin(49, 37), check_if_Cin(49, 38), check_if_Cin(49, 39),
                      check_if_Cin(49, 40), check_if_Cin(49, 41), check_if_Cin(49, 42), check_if_Cin(49, 43),
                      check_if_Cin(49, 44), check_if_Cin(49, 45), check_if_Cin(49, 46), check_if_Cin(49, 47),
                      check_if_Cin(49, 48), check_if_Cin(49, 50)], ignore_index=True)
    return data


def check_C50():
    data = pd.concat([check_if_Cin(50, 0), check_if_Cin(50, 1), check_if_Cin(50, 2), check_if_Cin(50, 3),
                      check_if_Cin(50, 4), check_if_Cin(50, 5), check_if_Cin(50, 6), check_if_Cin(50, 7),
                      check_if_Cin(50, 8), check_if_Cin(50, 9), check_if_Cin(50, 10), check_if_Cin(50, 11),
                      check_if_Cin(50, 12), check_if_Cin(50, 13), check_if_Cin(50, 14), check_if_Cin(50, 15),
                      check_if_Cin(50, 16), check_if_Cin(50, 17), check_if_Cin(50, 18), check_if_Cin(50, 19),
                      check_if_Cin(50, 20), check_if_Cin(50, 21), check_if_Cin(50, 22), check_if_Cin(50, 23),
                      check_if_Cin(50, 24), check_if_Cin(50, 25), check_if_Cin(50, 26), check_if_Cin(50, 27),
                      check_if_Cin(50, 28), check_if_Cin(50, 29), check_if_Cin(50, 30), check_if_Cin(50, 31),
                      check_if_Cin(50, 32), check_if_Cin(50, 33), check_if_Cin(50, 34), check_if_Cin(50, 35),
                      check_if_Cin(50, 36), check_if_Cin(50, 37), check_if_Cin(50, 38), check_if_Cin(50, 39),
                      check_if_Cin(50, 40), check_if_Cin(50, 41), check_if_Cin(50, 42), check_if_Cin(50, 43),
                      check_if_Cin(50, 44), check_if_Cin(50, 45), check_if_Cin(50, 46), check_if_Cin(50, 47),
                      check_if_Cin(50, 48), check_if_Cin(50, 49)], ignore_index=True)
    return data


def check():
    data = pd.concat([check_C1(), check_C2(), check_C3(), check_C4(),
                      check_C5(), check_C6(), check_C7(), check_C8(),
                      check_C9(), check_C10(), check_C11(), check_C12(),
                      check_C13(), check_C14(), check_C15(), check_C16(),
                      check_C17(), check_C18(), check_C19(), check_C20(),
                      check_C21(), check_C22(), check_C23(), check_C24(),
                      check_C25(), check_C26(), check_C27(), check_C28(),
                      check_C29(), check_C30(), check_C31(), check_C32(),
                      check_C33(), check_C34(), check_C35(), check_C36(),
                      check_C37(), check_C38(), check_C39(), check_C40(),
                      check_C41(), check_C42(), check_C43(), check_C44(),
                      check_C45(), check_C46(), check_C47(), check_C48(),
                      check_C49(), check_C50()], ignore_index=True)
    return data


def check_C_csv():
    data = check()
    string1 = "/Pycharm/HumanActivityRecognition/check"
    string2 = string1 + "/check_C" + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


check_C_csv()
