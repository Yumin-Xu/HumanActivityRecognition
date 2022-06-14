import os

import numpy as np
import pandas as pd

from CreateWord import create_word


def check_if_Min(x, y):
    d = create_word(x, 'M')['words']
    word_to_keep = np.array(create_word(y, 'M')['words'])
    df = pd.DataFrame(np.array(d[d.isin(word_to_keep)]), columns=['words'])
    return df


def check_M0():
    data = pd.concat([check_if_Min(0, 1), check_if_Min(0, 2), check_if_Min(0, 3), check_if_Min(0, 4),
                      check_if_Min(0, 5), check_if_Min(0, 6), check_if_Min(0, 7), check_if_Min(0, 8),
                      check_if_Min(0, 9), check_if_Min(0, 10), check_if_Min(0, 11), check_if_Min(0, 12),
                      check_if_Min(0, 13), check_if_Min(0, 14), check_if_Min(0, 15), check_if_Min(0, 16),
                      check_if_Min(0, 17), check_if_Min(0, 18), check_if_Min(0, 19), check_if_Min(0, 20),
                      check_if_Min(0, 21), check_if_Min(0, 22), check_if_Min(0, 23), check_if_Min(0, 24),
                      check_if_Min(0, 25), check_if_Min(0, 26), check_if_Min(0, 27), check_if_Min(0, 28),
                      check_if_Min(0, 29), check_if_Min(0, 30), check_if_Min(0, 31), check_if_Min(0, 32),
                      check_if_Min(0, 33), check_if_Min(0, 34), check_if_Min(0, 35), check_if_Min(0, 36),
                      check_if_Min(0, 37), check_if_Min(0, 38), check_if_Min(0, 39), check_if_Min(0, 40),
                      check_if_Min(0, 41), check_if_Min(0, 42), check_if_Min(0, 43), check_if_Min(0, 44),
                      check_if_Min(0, 45), check_if_Min(0, 46), check_if_Min(0, 47), check_if_Min(0, 48),
                      check_if_Min(0, 49), check_if_Min(0, 50)], ignore_index=True)
    return data


def check_M1():
    data = pd.concat([check_if_Min(1, 0), check_if_Min(1, 2), check_if_Min(1, 3), check_if_Min(1, 4),
                      check_if_Min(1, 5), check_if_Min(1, 6), check_if_Min(1, 7), check_if_Min(1, 8),
                      check_if_Min(1, 9), check_if_Min(1, 10), check_if_Min(1, 11), check_if_Min(1, 12),
                      check_if_Min(1, 13), check_if_Min(1, 14), check_if_Min(1, 15), check_if_Min(1, 16),
                      check_if_Min(1, 17), check_if_Min(1, 18), check_if_Min(1, 19), check_if_Min(1, 20),
                      check_if_Min(1, 21), check_if_Min(1, 22), check_if_Min(1, 23), check_if_Min(1, 24),
                      check_if_Min(1, 25), check_if_Min(1, 26), check_if_Min(1, 27), check_if_Min(1, 28),
                      check_if_Min(1, 29), check_if_Min(1, 30), check_if_Min(1, 31), check_if_Min(1, 32),
                      check_if_Min(1, 33), check_if_Min(1, 34), check_if_Min(1, 35), check_if_Min(1, 36),
                      check_if_Min(1, 37), check_if_Min(1, 38), check_if_Min(1, 39), check_if_Min(1, 40),
                      check_if_Min(1, 41), check_if_Min(1, 42), check_if_Min(1, 43), check_if_Min(1, 44),
                      check_if_Min(1, 45), check_if_Min(1, 46), check_if_Min(1, 47), check_if_Min(1, 48),
                      check_if_Min(1, 49), check_if_Min(1, 50)], ignore_index=True)
    return data


def check_M2():
    data = pd.concat([check_if_Min(2, 0), check_if_Min(2, 1), check_if_Min(2, 3), check_if_Min(2, 4),
                      check_if_Min(2, 5), check_if_Min(2, 6), check_if_Min(2, 7), check_if_Min(2, 8),
                      check_if_Min(2, 9), check_if_Min(2, 10), check_if_Min(2, 11), check_if_Min(2, 12),
                      check_if_Min(2, 13), check_if_Min(2, 14), check_if_Min(2, 15), check_if_Min(2, 16),
                      check_if_Min(2, 17), check_if_Min(2, 18), check_if_Min(2, 19), check_if_Min(2, 20),
                      check_if_Min(2, 21), check_if_Min(2, 22), check_if_Min(2, 23), check_if_Min(2, 24),
                      check_if_Min(2, 25), check_if_Min(2, 26), check_if_Min(2, 27), check_if_Min(2, 28),
                      check_if_Min(2, 29), check_if_Min(2, 30), check_if_Min(2, 31), check_if_Min(2, 32),
                      check_if_Min(2, 33), check_if_Min(2, 34), check_if_Min(2, 35), check_if_Min(2, 36),
                      check_if_Min(2, 37), check_if_Min(2, 38), check_if_Min(2, 39), check_if_Min(2, 40),
                      check_if_Min(2, 41), check_if_Min(2, 42), check_if_Min(2, 43), check_if_Min(2, 44),
                      check_if_Min(2, 45), check_if_Min(2, 46), check_if_Min(2, 47), check_if_Min(2, 48),
                      check_if_Min(2, 49), check_if_Min(2, 50)], ignore_index=True)
    return data


def check_M3():
    data = pd.concat([check_if_Min(3, 0), check_if_Min(3, 1), check_if_Min(3, 2), check_if_Min(3, 4),
                      check_if_Min(3, 5), check_if_Min(3, 6), check_if_Min(3, 7), check_if_Min(3, 8),
                      check_if_Min(3, 9), check_if_Min(3, 10), check_if_Min(3, 11), check_if_Min(3, 12),
                      check_if_Min(3, 13), check_if_Min(3, 14), check_if_Min(3, 15), check_if_Min(3, 16),
                      check_if_Min(3, 17), check_if_Min(3, 18), check_if_Min(3, 19), check_if_Min(3, 20),
                      check_if_Min(3, 21), check_if_Min(3, 22), check_if_Min(3, 23), check_if_Min(3, 24),
                      check_if_Min(3, 25), check_if_Min(3, 26), check_if_Min(3, 27), check_if_Min(3, 28),
                      check_if_Min(3, 29), check_if_Min(3, 30), check_if_Min(3, 31), check_if_Min(3, 32),
                      check_if_Min(3, 33), check_if_Min(3, 34), check_if_Min(3, 35), check_if_Min(3, 36),
                      check_if_Min(3, 37), check_if_Min(3, 38), check_if_Min(3, 39), check_if_Min(3, 40),
                      check_if_Min(3, 41), check_if_Min(3, 42), check_if_Min(3, 43), check_if_Min(3, 44),
                      check_if_Min(3, 45), check_if_Min(3, 46), check_if_Min(3, 47), check_if_Min(3, 48),
                      check_if_Min(3, 49), check_if_Min(3, 50)], ignore_index=True)
    return data


def check_M4():
    data = pd.concat([check_if_Min(4, 0), check_if_Min(4, 1), check_if_Min(4, 2), check_if_Min(4, 3),
                      check_if_Min(4, 5), check_if_Min(4, 6), check_if_Min(4, 7), check_if_Min(4, 8),
                      check_if_Min(4, 9), check_if_Min(4, 10), check_if_Min(4, 11), check_if_Min(4, 12),
                      check_if_Min(4, 13), check_if_Min(4, 14), check_if_Min(4, 15), check_if_Min(4, 16),
                      check_if_Min(4, 17), check_if_Min(4, 18), check_if_Min(4, 19), check_if_Min(4, 20),
                      check_if_Min(4, 21), check_if_Min(4, 22), check_if_Min(4, 23), check_if_Min(4, 24),
                      check_if_Min(4, 25), check_if_Min(4, 26), check_if_Min(4, 27), check_if_Min(4, 28),
                      check_if_Min(4, 29), check_if_Min(4, 30), check_if_Min(4, 31), check_if_Min(4, 32),
                      check_if_Min(4, 33), check_if_Min(4, 34), check_if_Min(4, 35), check_if_Min(4, 36),
                      check_if_Min(4, 37), check_if_Min(4, 38), check_if_Min(4, 39), check_if_Min(4, 40),
                      check_if_Min(4, 41), check_if_Min(4, 42), check_if_Min(4, 43), check_if_Min(4, 44),
                      check_if_Min(4, 45), check_if_Min(4, 46), check_if_Min(4, 47), check_if_Min(4, 48),
                      check_if_Min(4, 49), check_if_Min(4, 50)], ignore_index=True)
    return data


def check_M5():
    data = pd.concat([check_if_Min(5, 0), check_if_Min(5, 1), check_if_Min(5, 2), check_if_Min(5, 3),
                      check_if_Min(5, 4), check_if_Min(5, 6), check_if_Min(5, 7), check_if_Min(5, 8),
                      check_if_Min(5, 9), check_if_Min(5, 10), check_if_Min(5, 11), check_if_Min(5, 12),
                      check_if_Min(5, 13), check_if_Min(5, 14), check_if_Min(5, 15), check_if_Min(5, 16),
                      check_if_Min(5, 17), check_if_Min(5, 18), check_if_Min(5, 19), check_if_Min(5, 20),
                      check_if_Min(5, 21), check_if_Min(5, 22), check_if_Min(5, 23), check_if_Min(5, 24),
                      check_if_Min(5, 25), check_if_Min(5, 26), check_if_Min(5, 27), check_if_Min(5, 28),
                      check_if_Min(5, 29), check_if_Min(5, 30), check_if_Min(5, 31), check_if_Min(5, 32),
                      check_if_Min(5, 33), check_if_Min(5, 34), check_if_Min(5, 35), check_if_Min(5, 36),
                      check_if_Min(5, 37), check_if_Min(5, 38), check_if_Min(5, 39), check_if_Min(5, 40),
                      check_if_Min(5, 41), check_if_Min(5, 42), check_if_Min(5, 43), check_if_Min(5, 44),
                      check_if_Min(5, 45), check_if_Min(5, 46), check_if_Min(5, 47), check_if_Min(5, 48),
                      check_if_Min(5, 49), check_if_Min(5, 50)], ignore_index=True)
    return data


def check_M6():
    data = pd.concat([check_if_Min(6, 0), check_if_Min(6, 1), check_if_Min(6, 2), check_if_Min(6, 3),
                      check_if_Min(6, 4), check_if_Min(6, 5), check_if_Min(6, 7), check_if_Min(6, 8),
                      check_if_Min(6, 9), check_if_Min(6, 10), check_if_Min(6, 11), check_if_Min(6, 12),
                      check_if_Min(6, 13), check_if_Min(6, 14), check_if_Min(6, 15), check_if_Min(6, 16),
                      check_if_Min(6, 17), check_if_Min(6, 18), check_if_Min(6, 19), check_if_Min(6, 20),
                      check_if_Min(6, 21), check_if_Min(6, 22), check_if_Min(6, 23), check_if_Min(6, 24),
                      check_if_Min(6, 25), check_if_Min(6, 26), check_if_Min(6, 27), check_if_Min(6, 28),
                      check_if_Min(6, 29), check_if_Min(6, 30), check_if_Min(6, 31), check_if_Min(6, 32),
                      check_if_Min(6, 33), check_if_Min(6, 34), check_if_Min(6, 35), check_if_Min(6, 36),
                      check_if_Min(6, 37), check_if_Min(6, 38), check_if_Min(6, 39), check_if_Min(6, 40),
                      check_if_Min(6, 41), check_if_Min(6, 42), check_if_Min(6, 43), check_if_Min(6, 44),
                      check_if_Min(6, 45), check_if_Min(6, 46), check_if_Min(6, 47), check_if_Min(6, 48),
                      check_if_Min(6, 49), check_if_Min(6, 50)], ignore_index=True)
    return data


def check_M7():
    data = pd.concat([check_if_Min(7, 0), check_if_Min(7, 1), check_if_Min(7, 2), check_if_Min(7, 3),
                      check_if_Min(7, 4), check_if_Min(7, 5), check_if_Min(7, 6), check_if_Min(7, 8),
                      check_if_Min(7, 9), check_if_Min(7, 10), check_if_Min(7, 11), check_if_Min(7, 12),
                      check_if_Min(7, 13), check_if_Min(7, 14), check_if_Min(7, 15), check_if_Min(7, 16),
                      check_if_Min(7, 17), check_if_Min(7, 18), check_if_Min(7, 19), check_if_Min(7, 20),
                      check_if_Min(7, 21), check_if_Min(7, 22), check_if_Min(7, 23), check_if_Min(7, 24),
                      check_if_Min(7, 25), check_if_Min(7, 26), check_if_Min(7, 27), check_if_Min(7, 28),
                      check_if_Min(7, 29), check_if_Min(7, 30), check_if_Min(7, 31), check_if_Min(7, 32),
                      check_if_Min(7, 33), check_if_Min(7, 34), check_if_Min(7, 35), check_if_Min(7, 36),
                      check_if_Min(7, 37), check_if_Min(7, 38), check_if_Min(7, 39), check_if_Min(7, 40),
                      check_if_Min(7, 41), check_if_Min(7, 42), check_if_Min(7, 43), check_if_Min(7, 44),
                      check_if_Min(7, 45), check_if_Min(7, 46), check_if_Min(7, 47), check_if_Min(7, 48),
                      check_if_Min(7, 49), check_if_Min(7, 50)], ignore_index=True)
    return data


def check_M8():
    data = pd.concat([check_if_Min(8, 0), check_if_Min(8, 1), check_if_Min(8, 2), check_if_Min(8, 3),
                      check_if_Min(8, 4), check_if_Min(8, 5), check_if_Min(8, 6), check_if_Min(8, 7),
                      check_if_Min(8, 9), check_if_Min(8, 10), check_if_Min(8, 11), check_if_Min(8, 12),
                      check_if_Min(8, 13), check_if_Min(8, 14), check_if_Min(8, 15), check_if_Min(8, 16),
                      check_if_Min(8, 17), check_if_Min(8, 18), check_if_Min(8, 19), check_if_Min(8, 20),
                      check_if_Min(8, 21), check_if_Min(8, 22), check_if_Min(8, 23), check_if_Min(8, 24),
                      check_if_Min(8, 25), check_if_Min(8, 26), check_if_Min(8, 27), check_if_Min(8, 28),
                      check_if_Min(8, 29), check_if_Min(8, 30), check_if_Min(8, 31), check_if_Min(8, 32),
                      check_if_Min(8, 33), check_if_Min(8, 34), check_if_Min(8, 35), check_if_Min(8, 36),
                      check_if_Min(8, 37), check_if_Min(8, 38), check_if_Min(8, 39), check_if_Min(8, 40),
                      check_if_Min(8, 41), check_if_Min(8, 42), check_if_Min(8, 43), check_if_Min(8, 44),
                      check_if_Min(8, 45), check_if_Min(8, 46), check_if_Min(8, 47), check_if_Min(8, 48),
                      check_if_Min(8, 49), check_if_Min(8, 50)], ignore_index=True)
    return data


def check_M9():
    data = pd.concat([check_if_Min(9, 0), check_if_Min(9, 1), check_if_Min(9, 2), check_if_Min(9, 3),
                      check_if_Min(9, 4), check_if_Min(9, 5), check_if_Min(9, 6), check_if_Min(9, 7),
                      check_if_Min(9, 8), check_if_Min(9, 10), check_if_Min(9, 11), check_if_Min(9, 12),
                      check_if_Min(9, 13), check_if_Min(9, 14), check_if_Min(9, 15), check_if_Min(9, 16),
                      check_if_Min(9, 17), check_if_Min(9, 18), check_if_Min(9, 19), check_if_Min(9, 20),
                      check_if_Min(9, 21), check_if_Min(9, 22), check_if_Min(9, 23), check_if_Min(9, 24),
                      check_if_Min(9, 25), check_if_Min(9, 26), check_if_Min(9, 27), check_if_Min(9, 28),
                      check_if_Min(9, 29), check_if_Min(9, 30), check_if_Min(9, 31), check_if_Min(9, 32),
                      check_if_Min(9, 33), check_if_Min(9, 34), check_if_Min(9, 35), check_if_Min(9, 36),
                      check_if_Min(9, 37), check_if_Min(9, 38), check_if_Min(9, 39), check_if_Min(9, 40),
                      check_if_Min(9, 41), check_if_Min(9, 42), check_if_Min(9, 43), check_if_Min(9, 44),
                      check_if_Min(9, 45), check_if_Min(9, 46), check_if_Min(9, 47), check_if_Min(9, 48),
                      check_if_Min(9, 49), check_if_Min(9, 50)], ignore_index=True)
    return data


def check_M10():
    data = pd.concat([check_if_Min(10, 0), check_if_Min(10, 1), check_if_Min(10, 2), check_if_Min(10, 3),
                      check_if_Min(10, 4), check_if_Min(10, 5), check_if_Min(10, 6), check_if_Min(10, 7),
                      check_if_Min(10, 8), check_if_Min(10, 9), check_if_Min(10, 11), check_if_Min(10, 12),
                      check_if_Min(10, 13), check_if_Min(10, 14), check_if_Min(10, 15), check_if_Min(10, 16),
                      check_if_Min(10, 17), check_if_Min(10, 18), check_if_Min(10, 19), check_if_Min(10, 20),
                      check_if_Min(10, 21), check_if_Min(10, 22), check_if_Min(10, 23), check_if_Min(10, 24),
                      check_if_Min(10, 25), check_if_Min(10, 26), check_if_Min(10, 27), check_if_Min(10, 28),
                      check_if_Min(10, 29), check_if_Min(10, 30), check_if_Min(10, 31), check_if_Min(10, 32),
                      check_if_Min(10, 33), check_if_Min(10, 34), check_if_Min(10, 35), check_if_Min(10, 36),
                      check_if_Min(10, 37), check_if_Min(10, 38), check_if_Min(10, 39), check_if_Min(10, 40),
                      check_if_Min(10, 41), check_if_Min(10, 42), check_if_Min(10, 43), check_if_Min(10, 44),
                      check_if_Min(10, 45), check_if_Min(10, 46), check_if_Min(10, 47), check_if_Min(10, 48),
                      check_if_Min(10, 49), check_if_Min(10, 50)], ignore_index=True)
    return data


def check_M11():
    data = pd.concat([check_if_Min(11, 0), check_if_Min(11, 1), check_if_Min(11, 2), check_if_Min(11, 3),
                      check_if_Min(11, 4), check_if_Min(11, 5), check_if_Min(11, 6), check_if_Min(11, 7),
                      check_if_Min(11, 8), check_if_Min(11, 9), check_if_Min(11, 10), check_if_Min(11, 12),
                      check_if_Min(11, 13), check_if_Min(11, 14), check_if_Min(11, 15), check_if_Min(11, 16),
                      check_if_Min(11, 17), check_if_Min(11, 18), check_if_Min(11, 19), check_if_Min(11, 20),
                      check_if_Min(11, 21), check_if_Min(11, 22), check_if_Min(11, 23), check_if_Min(11, 24),
                      check_if_Min(11, 25), check_if_Min(11, 26), check_if_Min(11, 27), check_if_Min(11, 28),
                      check_if_Min(11, 29), check_if_Min(11, 30), check_if_Min(11, 31), check_if_Min(11, 32),
                      check_if_Min(11, 33), check_if_Min(11, 34), check_if_Min(11, 35), check_if_Min(11, 36),
                      check_if_Min(11, 37), check_if_Min(11, 38), check_if_Min(11, 39), check_if_Min(11, 40),
                      check_if_Min(11, 41), check_if_Min(11, 42), check_if_Min(11, 43), check_if_Min(11, 44),
                      check_if_Min(11, 45), check_if_Min(11, 46), check_if_Min(11, 47), check_if_Min(11, 48),
                      check_if_Min(11, 49), check_if_Min(11, 50)], ignore_index=True)
    return data


def check_M12():
    data = pd.concat([check_if_Min(12, 0), check_if_Min(12, 1), check_if_Min(12, 2), check_if_Min(12, 3),
                      check_if_Min(12, 4), check_if_Min(12, 5), check_if_Min(12, 6), check_if_Min(12, 7),
                      check_if_Min(12, 8), check_if_Min(12, 9), check_if_Min(12, 10), check_if_Min(12, 11),
                      check_if_Min(12, 13), check_if_Min(12, 14), check_if_Min(12, 15), check_if_Min(12, 16),
                      check_if_Min(12, 17), check_if_Min(12, 18), check_if_Min(12, 19), check_if_Min(12, 20),
                      check_if_Min(12, 21), check_if_Min(12, 22), check_if_Min(12, 23), check_if_Min(12, 24),
                      check_if_Min(12, 25), check_if_Min(12, 26), check_if_Min(12, 27), check_if_Min(12, 28),
                      check_if_Min(12, 29), check_if_Min(12, 30), check_if_Min(12, 31), check_if_Min(12, 32),
                      check_if_Min(12, 33), check_if_Min(12, 34), check_if_Min(12, 35), check_if_Min(12, 36),
                      check_if_Min(12, 37), check_if_Min(12, 38), check_if_Min(12, 39), check_if_Min(12, 40),
                      check_if_Min(12, 41), check_if_Min(12, 42), check_if_Min(12, 43), check_if_Min(12, 44),
                      check_if_Min(12, 45), check_if_Min(12, 46), check_if_Min(12, 47), check_if_Min(12, 48),
                      check_if_Min(12, 49), check_if_Min(12, 50)], ignore_index=True)
    return data


def check_M13():
    data = pd.concat([check_if_Min(13, 0), check_if_Min(13, 1), check_if_Min(13, 2), check_if_Min(13, 3),
                      check_if_Min(13, 4), check_if_Min(13, 5), check_if_Min(13, 6), check_if_Min(13, 7),
                      check_if_Min(13, 8), check_if_Min(13, 9), check_if_Min(13, 10), check_if_Min(13, 11),
                      check_if_Min(13, 12), check_if_Min(13, 14), check_if_Min(13, 15), check_if_Min(13, 16),
                      check_if_Min(13, 17), check_if_Min(13, 18), check_if_Min(13, 19), check_if_Min(13, 20),
                      check_if_Min(13, 21), check_if_Min(13, 22), check_if_Min(13, 23), check_if_Min(13, 24),
                      check_if_Min(13, 25), check_if_Min(13, 26), check_if_Min(13, 27), check_if_Min(13, 28),
                      check_if_Min(13, 29), check_if_Min(13, 30), check_if_Min(13, 31), check_if_Min(13, 32),
                      check_if_Min(13, 33), check_if_Min(13, 34), check_if_Min(13, 35), check_if_Min(13, 36),
                      check_if_Min(13, 37), check_if_Min(13, 38), check_if_Min(13, 39), check_if_Min(13, 40),
                      check_if_Min(13, 41), check_if_Min(13, 42), check_if_Min(13, 43), check_if_Min(13, 44),
                      check_if_Min(13, 45), check_if_Min(13, 46), check_if_Min(13, 47), check_if_Min(13, 48),
                      check_if_Min(13, 49), check_if_Min(13, 50)], ignore_index=True)
    return data


def check_M14():
    data = pd.concat([check_if_Min(14, 0), check_if_Min(14, 1), check_if_Min(14, 2), check_if_Min(14, 3),
                      check_if_Min(14, 4), check_if_Min(14, 5), check_if_Min(14, 6), check_if_Min(14, 7),
                      check_if_Min(14, 8), check_if_Min(14, 9), check_if_Min(14, 10), check_if_Min(14, 11),
                      check_if_Min(14, 12), check_if_Min(14, 13), check_if_Min(14, 15), check_if_Min(14, 16),
                      check_if_Min(14, 17), check_if_Min(14, 18), check_if_Min(14, 19), check_if_Min(14, 20),
                      check_if_Min(14, 21), check_if_Min(14, 22), check_if_Min(14, 23), check_if_Min(14, 24),
                      check_if_Min(14, 25), check_if_Min(14, 26), check_if_Min(14, 27), check_if_Min(14, 28),
                      check_if_Min(14, 29), check_if_Min(14, 30), check_if_Min(14, 31), check_if_Min(14, 32),
                      check_if_Min(14, 33), check_if_Min(14, 34), check_if_Min(14, 35), check_if_Min(14, 36),
                      check_if_Min(14, 37), check_if_Min(14, 38), check_if_Min(14, 39), check_if_Min(14, 40),
                      check_if_Min(14, 41), check_if_Min(14, 42), check_if_Min(14, 43), check_if_Min(14, 44),
                      check_if_Min(14, 45), check_if_Min(14, 46), check_if_Min(14, 47), check_if_Min(14, 48),
                      check_if_Min(14, 49), check_if_Min(14, 50)], ignore_index=True)
    return data


def check_M15():
    data = pd.concat([check_if_Min(15, 0), check_if_Min(15, 1), check_if_Min(15, 2), check_if_Min(15, 3),
                      check_if_Min(15, 4), check_if_Min(15, 5), check_if_Min(15, 6), check_if_Min(15, 7),
                      check_if_Min(15, 8), check_if_Min(15, 9), check_if_Min(15, 10), check_if_Min(15, 11),
                      check_if_Min(15, 12), check_if_Min(15, 13), check_if_Min(15, 14), check_if_Min(15, 16),
                      check_if_Min(15, 17), check_if_Min(15, 18), check_if_Min(15, 19), check_if_Min(15, 20),
                      check_if_Min(15, 21), check_if_Min(15, 22), check_if_Min(15, 23), check_if_Min(15, 24),
                      check_if_Min(15, 25), check_if_Min(15, 26), check_if_Min(15, 27), check_if_Min(15, 28),
                      check_if_Min(15, 29), check_if_Min(15, 30), check_if_Min(15, 31), check_if_Min(15, 32),
                      check_if_Min(15, 33), check_if_Min(15, 34), check_if_Min(15, 35), check_if_Min(15, 36),
                      check_if_Min(15, 37), check_if_Min(15, 38), check_if_Min(15, 39), check_if_Min(15, 40),
                      check_if_Min(15, 41), check_if_Min(15, 42), check_if_Min(15, 43), check_if_Min(15, 44),
                      check_if_Min(15, 45), check_if_Min(15, 46), check_if_Min(15, 47), check_if_Min(15, 48),
                      check_if_Min(15, 49), check_if_Min(15, 50)], ignore_index=True)
    return data


def check_M16():
    data = pd.concat([check_if_Min(16, 0), check_if_Min(16, 1), check_if_Min(16, 2), check_if_Min(16, 3),
                      check_if_Min(16, 4), check_if_Min(16, 5), check_if_Min(16, 6), check_if_Min(16, 7),
                      check_if_Min(16, 8), check_if_Min(16, 9), check_if_Min(16, 10), check_if_Min(16, 11),
                      check_if_Min(16, 12), check_if_Min(16, 13), check_if_Min(16, 14), check_if_Min(16, 15),
                      check_if_Min(16, 17), check_if_Min(16, 18), check_if_Min(16, 19), check_if_Min(16, 20),
                      check_if_Min(16, 21), check_if_Min(16, 22), check_if_Min(16, 23), check_if_Min(16, 24),
                      check_if_Min(16, 25), check_if_Min(16, 26), check_if_Min(16, 27), check_if_Min(16, 28),
                      check_if_Min(16, 29), check_if_Min(16, 30), check_if_Min(16, 31), check_if_Min(16, 32),
                      check_if_Min(16, 33), check_if_Min(16, 34), check_if_Min(16, 35), check_if_Min(16, 36),
                      check_if_Min(16, 37), check_if_Min(16, 38), check_if_Min(16, 39), check_if_Min(16, 40),
                      check_if_Min(16, 41), check_if_Min(16, 42), check_if_Min(16, 43), check_if_Min(16, 44),
                      check_if_Min(16, 45), check_if_Min(16, 46), check_if_Min(16, 47), check_if_Min(16, 48),
                      check_if_Min(16, 49), check_if_Min(16, 50)], ignore_index=True)
    return data


def check_M17():
    data = pd.concat([check_if_Min(17, 0), check_if_Min(17, 1), check_if_Min(17, 2), check_if_Min(17, 3),
                      check_if_Min(17, 4), check_if_Min(17, 5), check_if_Min(17, 6), check_if_Min(17, 7),
                      check_if_Min(17, 8), check_if_Min(17, 9), check_if_Min(17, 10), check_if_Min(17, 11),
                      check_if_Min(17, 12), check_if_Min(17, 13), check_if_Min(17, 14), check_if_Min(17, 15),
                      check_if_Min(17, 16), check_if_Min(17, 18), check_if_Min(17, 19), check_if_Min(17, 20),
                      check_if_Min(17, 21), check_if_Min(17, 22), check_if_Min(17, 23), check_if_Min(17, 24),
                      check_if_Min(17, 25), check_if_Min(17, 26), check_if_Min(17, 27), check_if_Min(17, 28),
                      check_if_Min(17, 29), check_if_Min(17, 30), check_if_Min(17, 31), check_if_Min(17, 32),
                      check_if_Min(17, 33), check_if_Min(17, 34), check_if_Min(17, 35), check_if_Min(17, 36),
                      check_if_Min(17, 37), check_if_Min(17, 38), check_if_Min(17, 39), check_if_Min(17, 40),
                      check_if_Min(17, 41), check_if_Min(17, 42), check_if_Min(17, 43), check_if_Min(17, 44),
                      check_if_Min(17, 45), check_if_Min(17, 46), check_if_Min(17, 47), check_if_Min(17, 48),
                      check_if_Min(17, 49), check_if_Min(17, 50)], ignore_index=True)
    return data


def check_M18():
    data = pd.concat([check_if_Min(18, 0), check_if_Min(18, 1), check_if_Min(18, 2), check_if_Min(18, 3),
                      check_if_Min(18, 4), check_if_Min(18, 5), check_if_Min(18, 6), check_if_Min(18, 7),
                      check_if_Min(18, 8), check_if_Min(18, 9), check_if_Min(18, 10), check_if_Min(18, 11),
                      check_if_Min(18, 12), check_if_Min(18, 13), check_if_Min(18, 14), check_if_Min(18, 15),
                      check_if_Min(18, 16), check_if_Min(18, 17), check_if_Min(18, 19), check_if_Min(18, 20),
                      check_if_Min(18, 21), check_if_Min(18, 22), check_if_Min(18, 23), check_if_Min(18, 24),
                      check_if_Min(18, 25), check_if_Min(18, 26), check_if_Min(18, 27), check_if_Min(18, 28),
                      check_if_Min(18, 29), check_if_Min(18, 30), check_if_Min(18, 31), check_if_Min(18, 32),
                      check_if_Min(18, 33), check_if_Min(18, 34), check_if_Min(18, 35), check_if_Min(18, 36),
                      check_if_Min(18, 37), check_if_Min(18, 38), check_if_Min(18, 39), check_if_Min(18, 40),
                      check_if_Min(18, 41), check_if_Min(18, 42), check_if_Min(18, 43), check_if_Min(18, 44),
                      check_if_Min(18, 45), check_if_Min(18, 46), check_if_Min(18, 47), check_if_Min(18, 48),
                      check_if_Min(18, 49), check_if_Min(18, 50)], ignore_index=True)
    return data


def check_M19():
    data = pd.concat([check_if_Min(19, 0), check_if_Min(19, 1), check_if_Min(19, 2), check_if_Min(19, 3),
                      check_if_Min(19, 4), check_if_Min(19, 5), check_if_Min(19, 6), check_if_Min(19, 7),
                      check_if_Min(19, 8), check_if_Min(19, 9), check_if_Min(19, 10), check_if_Min(19, 11),
                      check_if_Min(19, 12), check_if_Min(19, 13), check_if_Min(19, 14), check_if_Min(19, 15),
                      check_if_Min(19, 16), check_if_Min(19, 17), check_if_Min(19, 18), check_if_Min(19, 20),
                      check_if_Min(19, 21), check_if_Min(19, 22), check_if_Min(19, 23), check_if_Min(19, 24),
                      check_if_Min(19, 25), check_if_Min(19, 26), check_if_Min(19, 27), check_if_Min(19, 28),
                      check_if_Min(19, 29), check_if_Min(19, 30), check_if_Min(19, 31), check_if_Min(19, 32),
                      check_if_Min(19, 33), check_if_Min(19, 34), check_if_Min(19, 35), check_if_Min(19, 36),
                      check_if_Min(19, 37), check_if_Min(19, 38), check_if_Min(19, 39), check_if_Min(19, 40),
                      check_if_Min(19, 41), check_if_Min(19, 42), check_if_Min(19, 43), check_if_Min(19, 44),
                      check_if_Min(19, 45), check_if_Min(19, 46), check_if_Min(19, 47), check_if_Min(19, 48),
                      check_if_Min(19, 49), check_if_Min(19, 50)], ignore_index=True)
    return data


def check_M20():
    data = pd.concat([check_if_Min(20, 0), check_if_Min(20, 1), check_if_Min(20, 2), check_if_Min(20, 3),
                      check_if_Min(20, 4), check_if_Min(20, 5), check_if_Min(20, 6), check_if_Min(20, 7),
                      check_if_Min(20, 8), check_if_Min(20, 9), check_if_Min(20, 10), check_if_Min(20, 11),
                      check_if_Min(20, 12), check_if_Min(20, 13), check_if_Min(20, 14), check_if_Min(20, 15),
                      check_if_Min(20, 16), check_if_Min(20, 17), check_if_Min(20, 18), check_if_Min(20, 19),
                      check_if_Min(20, 21), check_if_Min(20, 22), check_if_Min(20, 23), check_if_Min(20, 24),
                      check_if_Min(20, 25), check_if_Min(20, 26), check_if_Min(20, 27), check_if_Min(20, 28),
                      check_if_Min(20, 29), check_if_Min(20, 30), check_if_Min(20, 31), check_if_Min(20, 32),
                      check_if_Min(20, 33), check_if_Min(20, 34), check_if_Min(20, 35), check_if_Min(20, 36),
                      check_if_Min(20, 37), check_if_Min(20, 38), check_if_Min(20, 39), check_if_Min(20, 40),
                      check_if_Min(20, 41), check_if_Min(20, 42), check_if_Min(20, 43), check_if_Min(20, 44),
                      check_if_Min(20, 45), check_if_Min(20, 46), check_if_Min(20, 47), check_if_Min(20, 48),
                      check_if_Min(20, 49), check_if_Min(20, 50)], ignore_index=True)
    return data


def check_M21():
    data = pd.concat([check_if_Min(21, 0), check_if_Min(21, 1), check_if_Min(21, 2), check_if_Min(21, 3),
                      check_if_Min(21, 4), check_if_Min(21, 5), check_if_Min(21, 6), check_if_Min(21, 7),
                      check_if_Min(21, 8), check_if_Min(21, 9), check_if_Min(21, 10), check_if_Min(21, 11),
                      check_if_Min(21, 12), check_if_Min(21, 13), check_if_Min(21, 14), check_if_Min(21, 15),
                      check_if_Min(21, 16), check_if_Min(21, 17), check_if_Min(21, 18), check_if_Min(21, 19),
                      check_if_Min(21, 20), check_if_Min(21, 22), check_if_Min(21, 23), check_if_Min(21, 24),
                      check_if_Min(21, 25), check_if_Min(21, 26), check_if_Min(21, 27), check_if_Min(21, 28),
                      check_if_Min(21, 29), check_if_Min(21, 30), check_if_Min(21, 31), check_if_Min(21, 32),
                      check_if_Min(21, 33), check_if_Min(21, 34), check_if_Min(21, 35), check_if_Min(21, 36),
                      check_if_Min(21, 37), check_if_Min(21, 38), check_if_Min(21, 39), check_if_Min(21, 40),
                      check_if_Min(21, 41), check_if_Min(21, 42), check_if_Min(21, 43), check_if_Min(21, 44),
                      check_if_Min(21, 45), check_if_Min(21, 46), check_if_Min(21, 47), check_if_Min(21, 48),
                      check_if_Min(21, 49), check_if_Min(21, 50)], ignore_index=True)
    return data


def check_M22():
    data = pd.concat([check_if_Min(22, 0), check_if_Min(22, 1), check_if_Min(22, 2), check_if_Min(22, 3),
                      check_if_Min(22, 4), check_if_Min(22, 5), check_if_Min(22, 6), check_if_Min(22, 7),
                      check_if_Min(22, 8), check_if_Min(22, 9), check_if_Min(22, 10), check_if_Min(22, 11),
                      check_if_Min(22, 12), check_if_Min(22, 13), check_if_Min(22, 14), check_if_Min(22, 15),
                      check_if_Min(22, 16), check_if_Min(22, 17), check_if_Min(22, 18), check_if_Min(22, 19),
                      check_if_Min(22, 20), check_if_Min(22, 21), check_if_Min(22, 23), check_if_Min(22, 24),
                      check_if_Min(22, 25), check_if_Min(22, 26), check_if_Min(22, 27), check_if_Min(22, 28),
                      check_if_Min(22, 29), check_if_Min(22, 30), check_if_Min(22, 31), check_if_Min(22, 32),
                      check_if_Min(22, 33), check_if_Min(22, 34), check_if_Min(22, 35), check_if_Min(22, 36),
                      check_if_Min(22, 37), check_if_Min(22, 38), check_if_Min(22, 39), check_if_Min(22, 40),
                      check_if_Min(22, 41), check_if_Min(22, 42), check_if_Min(22, 43), check_if_Min(22, 44),
                      check_if_Min(22, 45), check_if_Min(22, 46), check_if_Min(22, 47), check_if_Min(22, 48),
                      check_if_Min(22, 49), check_if_Min(22, 50)], ignore_index=True)
    return data


def check_M23():
    data = pd.concat([check_if_Min(23, 0), check_if_Min(23, 1), check_if_Min(23, 2), check_if_Min(23, 3),
                      check_if_Min(23, 4), check_if_Min(23, 5), check_if_Min(23, 6), check_if_Min(23, 7),
                      check_if_Min(23, 8), check_if_Min(23, 9), check_if_Min(23, 10), check_if_Min(23, 11),
                      check_if_Min(23, 12), check_if_Min(23, 13), check_if_Min(23, 14), check_if_Min(23, 15),
                      check_if_Min(23, 16), check_if_Min(23, 17), check_if_Min(23, 18), check_if_Min(23, 19),
                      check_if_Min(23, 20), check_if_Min(23, 21), check_if_Min(23, 22), check_if_Min(23, 24),
                      check_if_Min(23, 25), check_if_Min(23, 26), check_if_Min(23, 27), check_if_Min(23, 28),
                      check_if_Min(23, 29), check_if_Min(23, 30), check_if_Min(23, 31), check_if_Min(23, 32),
                      check_if_Min(23, 33), check_if_Min(23, 34), check_if_Min(23, 35), check_if_Min(23, 36),
                      check_if_Min(23, 37), check_if_Min(23, 38), check_if_Min(23, 39), check_if_Min(23, 40),
                      check_if_Min(23, 41), check_if_Min(23, 42), check_if_Min(23, 43), check_if_Min(23, 44),
                      check_if_Min(23, 45), check_if_Min(23, 46), check_if_Min(23, 47), check_if_Min(23, 48),
                      check_if_Min(23, 49), check_if_Min(23, 50)], ignore_index=True)
    return data


def check_M24():
    data = pd.concat([check_if_Min(24, 0), check_if_Min(24, 1), check_if_Min(24, 2), check_if_Min(24, 3),
                      check_if_Min(24, 4), check_if_Min(24, 5), check_if_Min(24, 6), check_if_Min(24, 7),
                      check_if_Min(24, 8), check_if_Min(24, 9), check_if_Min(24, 10), check_if_Min(24, 11),
                      check_if_Min(24, 12), check_if_Min(24, 13), check_if_Min(24, 14), check_if_Min(24, 15),
                      check_if_Min(24, 16), check_if_Min(24, 17), check_if_Min(24, 18), check_if_Min(24, 19),
                      check_if_Min(24, 20), check_if_Min(24, 21), check_if_Min(24, 22), check_if_Min(24, 23),
                      check_if_Min(24, 25), check_if_Min(24, 26), check_if_Min(24, 27), check_if_Min(24, 28),
                      check_if_Min(24, 29), check_if_Min(24, 30), check_if_Min(24, 31), check_if_Min(24, 32),
                      check_if_Min(24, 33), check_if_Min(24, 34), check_if_Min(24, 35), check_if_Min(24, 36),
                      check_if_Min(24, 37), check_if_Min(24, 38), check_if_Min(24, 39), check_if_Min(24, 40),
                      check_if_Min(24, 41), check_if_Min(24, 42), check_if_Min(24, 43), check_if_Min(24, 44),
                      check_if_Min(24, 45), check_if_Min(24, 46), check_if_Min(24, 47), check_if_Min(24, 48),
                      check_if_Min(24, 49), check_if_Min(24, 50)], ignore_index=True)
    return data


def check_M25():
    data = pd.concat([check_if_Min(25, 0), check_if_Min(25, 1), check_if_Min(25, 2), check_if_Min(25, 3),
                      check_if_Min(25, 4), check_if_Min(25, 5), check_if_Min(25, 6), check_if_Min(25, 7),
                      check_if_Min(25, 8), check_if_Min(25, 9), check_if_Min(25, 10), check_if_Min(25, 11),
                      check_if_Min(25, 12), check_if_Min(25, 13), check_if_Min(25, 14), check_if_Min(25, 15),
                      check_if_Min(25, 16), check_if_Min(25, 17), check_if_Min(25, 18), check_if_Min(25, 19),
                      check_if_Min(25, 20), check_if_Min(25, 21), check_if_Min(25, 22), check_if_Min(25, 23),
                      check_if_Min(25, 24), check_if_Min(25, 26), check_if_Min(25, 27), check_if_Min(25, 28),
                      check_if_Min(25, 29), check_if_Min(25, 30), check_if_Min(25, 31), check_if_Min(25, 32),
                      check_if_Min(25, 33), check_if_Min(25, 34), check_if_Min(25, 35), check_if_Min(25, 36),
                      check_if_Min(25, 37), check_if_Min(25, 38), check_if_Min(25, 39), check_if_Min(25, 40),
                      check_if_Min(25, 41), check_if_Min(25, 42), check_if_Min(25, 43), check_if_Min(25, 44),
                      check_if_Min(25, 45), check_if_Min(25, 46), check_if_Min(25, 47), check_if_Min(25, 48),
                      check_if_Min(25, 49), check_if_Min(25, 50)], ignore_index=True)
    return data


def check_M26():
    data = pd.concat([check_if_Min(26, 0), check_if_Min(26, 1), check_if_Min(26, 2), check_if_Min(26, 3),
                      check_if_Min(26, 4), check_if_Min(26, 5), check_if_Min(26, 6), check_if_Min(26, 7),
                      check_if_Min(26, 8), check_if_Min(26, 9), check_if_Min(26, 10), check_if_Min(26, 11),
                      check_if_Min(26, 12), check_if_Min(26, 13), check_if_Min(26, 14), check_if_Min(26, 15),
                      check_if_Min(26, 16), check_if_Min(26, 17), check_if_Min(26, 18), check_if_Min(26, 19),
                      check_if_Min(26, 20), check_if_Min(26, 21), check_if_Min(26, 22), check_if_Min(26, 23),
                      check_if_Min(26, 24), check_if_Min(26, 25), check_if_Min(26, 27), check_if_Min(26, 28),
                      check_if_Min(26, 29), check_if_Min(26, 30), check_if_Min(26, 31), check_if_Min(26, 32),
                      check_if_Min(26, 33), check_if_Min(26, 34), check_if_Min(26, 35), check_if_Min(26, 36),
                      check_if_Min(26, 37), check_if_Min(26, 38), check_if_Min(26, 39), check_if_Min(26, 40),
                      check_if_Min(26, 41), check_if_Min(26, 42), check_if_Min(26, 43), check_if_Min(26, 44),
                      check_if_Min(26, 45), check_if_Min(26, 46), check_if_Min(26, 47), check_if_Min(26, 48),
                      check_if_Min(26, 49), check_if_Min(26, 50)], ignore_index=True)
    return data


def check_M27():
    data = pd.concat([check_if_Min(27, 0), check_if_Min(27, 1), check_if_Min(27, 2), check_if_Min(27, 3),
                      check_if_Min(27, 4), check_if_Min(27, 5), check_if_Min(27, 6), check_if_Min(27, 7),
                      check_if_Min(27, 8), check_if_Min(27, 9), check_if_Min(27, 10), check_if_Min(27, 11),
                      check_if_Min(27, 12), check_if_Min(27, 13), check_if_Min(27, 14), check_if_Min(27, 15),
                      check_if_Min(27, 16), check_if_Min(27, 17), check_if_Min(27, 18), check_if_Min(27, 19),
                      check_if_Min(27, 20), check_if_Min(27, 21), check_if_Min(27, 22), check_if_Min(27, 23),
                      check_if_Min(27, 24), check_if_Min(27, 25), check_if_Min(27, 26), check_if_Min(27, 28),
                      check_if_Min(27, 29), check_if_Min(27, 30), check_if_Min(27, 31), check_if_Min(27, 32),
                      check_if_Min(27, 33), check_if_Min(27, 34), check_if_Min(27, 35), check_if_Min(27, 36),
                      check_if_Min(27, 37), check_if_Min(27, 38), check_if_Min(27, 39), check_if_Min(27, 40),
                      check_if_Min(27, 41), check_if_Min(27, 42), check_if_Min(27, 43), check_if_Min(27, 44),
                      check_if_Min(27, 45), check_if_Min(27, 46), check_if_Min(27, 47), check_if_Min(27, 48),
                      check_if_Min(27, 49), check_if_Min(27, 50)], ignore_index=True)
    return data


def check_M28():
    data = pd.concat([check_if_Min(28, 0), check_if_Min(28, 1), check_if_Min(28, 2), check_if_Min(28, 3),
                      check_if_Min(28, 4), check_if_Min(28, 5), check_if_Min(28, 6), check_if_Min(28, 7),
                      check_if_Min(28, 8), check_if_Min(28, 9), check_if_Min(28, 10), check_if_Min(28, 11),
                      check_if_Min(28, 12), check_if_Min(28, 13), check_if_Min(28, 14), check_if_Min(28, 15),
                      check_if_Min(28, 16), check_if_Min(28, 17), check_if_Min(28, 18), check_if_Min(28, 19),
                      check_if_Min(28, 20), check_if_Min(28, 21), check_if_Min(28, 22), check_if_Min(28, 23),
                      check_if_Min(28, 24), check_if_Min(28, 25), check_if_Min(28, 26), check_if_Min(28, 27),
                      check_if_Min(28, 29), check_if_Min(28, 30), check_if_Min(28, 31), check_if_Min(28, 32),
                      check_if_Min(28, 33), check_if_Min(28, 34), check_if_Min(28, 35), check_if_Min(28, 36),
                      check_if_Min(28, 37), check_if_Min(28, 38), check_if_Min(28, 39), check_if_Min(28, 40),
                      check_if_Min(28, 41), check_if_Min(28, 42), check_if_Min(28, 43), check_if_Min(28, 44),
                      check_if_Min(28, 45), check_if_Min(28, 46), check_if_Min(28, 47), check_if_Min(28, 48),
                      check_if_Min(28, 49), check_if_Min(28, 50)], ignore_index=True)
    return data


def check_M29():
    data = pd.concat([check_if_Min(29, 0), check_if_Min(29, 1), check_if_Min(29, 2), check_if_Min(29, 3),
                      check_if_Min(29, 4), check_if_Min(29, 5), check_if_Min(29, 6), check_if_Min(29, 7),
                      check_if_Min(29, 8), check_if_Min(29, 9), check_if_Min(29, 10), check_if_Min(29, 11),
                      check_if_Min(29, 12), check_if_Min(29, 13), check_if_Min(29, 14), check_if_Min(29, 15),
                      check_if_Min(29, 16), check_if_Min(29, 17), check_if_Min(29, 18), check_if_Min(29, 19),
                      check_if_Min(29, 20), check_if_Min(29, 21), check_if_Min(29, 22), check_if_Min(29, 23),
                      check_if_Min(29, 24), check_if_Min(29, 25), check_if_Min(29, 26), check_if_Min(29, 27),
                      check_if_Min(29, 28), check_if_Min(29, 30), check_if_Min(29, 31), check_if_Min(29, 32),
                      check_if_Min(29, 33), check_if_Min(29, 34), check_if_Min(29, 35), check_if_Min(29, 36),
                      check_if_Min(29, 37), check_if_Min(29, 38), check_if_Min(29, 39), check_if_Min(29, 40),
                      check_if_Min(29, 41), check_if_Min(29, 42), check_if_Min(29, 43), check_if_Min(29, 44),
                      check_if_Min(29, 45), check_if_Min(29, 46), check_if_Min(29, 47), check_if_Min(29, 48),
                      check_if_Min(29, 49), check_if_Min(29, 50)], ignore_index=True)
    return data


def check_M30():
    data = pd.concat([check_if_Min(30, 0), check_if_Min(30, 1), check_if_Min(30, 2), check_if_Min(30, 3),
                      check_if_Min(30, 4), check_if_Min(30, 5), check_if_Min(30, 6), check_if_Min(30, 7),
                      check_if_Min(30, 8), check_if_Min(30, 9), check_if_Min(30, 10), check_if_Min(30, 11),
                      check_if_Min(30, 12), check_if_Min(30, 13), check_if_Min(30, 14), check_if_Min(30, 15),
                      check_if_Min(30, 16), check_if_Min(30, 17), check_if_Min(30, 18), check_if_Min(30, 19),
                      check_if_Min(30, 20), check_if_Min(30, 21), check_if_Min(30, 22), check_if_Min(30, 23),
                      check_if_Min(30, 24), check_if_Min(30, 25), check_if_Min(30, 26), check_if_Min(30, 27),
                      check_if_Min(30, 28), check_if_Min(30, 29), check_if_Min(30, 31), check_if_Min(30, 32),
                      check_if_Min(30, 33), check_if_Min(30, 34), check_if_Min(30, 35), check_if_Min(30, 36),
                      check_if_Min(30, 37), check_if_Min(30, 38), check_if_Min(30, 39), check_if_Min(30, 40),
                      check_if_Min(30, 41), check_if_Min(30, 42), check_if_Min(30, 43), check_if_Min(30, 44),
                      check_if_Min(30, 45), check_if_Min(30, 46), check_if_Min(30, 47), check_if_Min(30, 48),
                      check_if_Min(30, 49), check_if_Min(30, 50)], ignore_index=True)
    return data


def check_M31():
    data = pd.concat([check_if_Min(31, 0), check_if_Min(31, 1), check_if_Min(31, 2), check_if_Min(31, 3),
                      check_if_Min(31, 4), check_if_Min(31, 5), check_if_Min(31, 6), check_if_Min(31, 7),
                      check_if_Min(31, 8), check_if_Min(31, 9), check_if_Min(31, 10), check_if_Min(31, 11),
                      check_if_Min(31, 12), check_if_Min(31, 13), check_if_Min(31, 14), check_if_Min(31, 15),
                      check_if_Min(31, 16), check_if_Min(31, 17), check_if_Min(31, 18), check_if_Min(31, 19),
                      check_if_Min(31, 20), check_if_Min(31, 21), check_if_Min(31, 22), check_if_Min(31, 23),
                      check_if_Min(31, 24), check_if_Min(31, 25), check_if_Min(31, 26), check_if_Min(31, 27),
                      check_if_Min(31, 28), check_if_Min(31, 29), check_if_Min(31, 30), check_if_Min(31, 32),
                      check_if_Min(31, 33), check_if_Min(31, 34), check_if_Min(31, 35), check_if_Min(31, 36),
                      check_if_Min(31, 37), check_if_Min(31, 38), check_if_Min(31, 39), check_if_Min(31, 40),
                      check_if_Min(31, 41), check_if_Min(31, 42), check_if_Min(31, 43), check_if_Min(31, 44),
                      check_if_Min(31, 45), check_if_Min(31, 46), check_if_Min(31, 47), check_if_Min(31, 48),
                      check_if_Min(31, 49), check_if_Min(31, 50)], ignore_index=True)
    return data


def check_M32():
    data = pd.concat([check_if_Min(32, 0), check_if_Min(32, 1), check_if_Min(32, 2), check_if_Min(32, 3),
                      check_if_Min(32, 4), check_if_Min(32, 5), check_if_Min(32, 6), check_if_Min(32, 7),
                      check_if_Min(32, 8), check_if_Min(32, 9), check_if_Min(32, 10), check_if_Min(32, 11),
                      check_if_Min(32, 12), check_if_Min(32, 13), check_if_Min(32, 14), check_if_Min(32, 15),
                      check_if_Min(32, 16), check_if_Min(32, 17), check_if_Min(32, 18), check_if_Min(32, 19),
                      check_if_Min(32, 20), check_if_Min(32, 21), check_if_Min(32, 22), check_if_Min(32, 23),
                      check_if_Min(32, 24), check_if_Min(32, 25), check_if_Min(32, 26), check_if_Min(32, 27),
                      check_if_Min(32, 28), check_if_Min(32, 29), check_if_Min(32, 30), check_if_Min(32, 31),
                      check_if_Min(32, 33), check_if_Min(32, 34), check_if_Min(32, 35), check_if_Min(32, 36),
                      check_if_Min(32, 37), check_if_Min(32, 38), check_if_Min(32, 39), check_if_Min(32, 40),
                      check_if_Min(32, 41), check_if_Min(32, 42), check_if_Min(32, 43), check_if_Min(32, 44),
                      check_if_Min(32, 45), check_if_Min(32, 46), check_if_Min(32, 47), check_if_Min(32, 48),
                      check_if_Min(32, 49), check_if_Min(32, 50)], ignore_index=True)
    return data


def check_M33():
    data = pd.concat([check_if_Min(33, 0), check_if_Min(33, 1), check_if_Min(33, 2), check_if_Min(33, 3),
                      check_if_Min(33, 4), check_if_Min(33, 5), check_if_Min(33, 6), check_if_Min(33, 7),
                      check_if_Min(33, 8), check_if_Min(33, 9), check_if_Min(33, 10), check_if_Min(33, 11),
                      check_if_Min(33, 12), check_if_Min(33, 13), check_if_Min(33, 14), check_if_Min(33, 15),
                      check_if_Min(33, 16), check_if_Min(33, 17), check_if_Min(33, 18), check_if_Min(33, 19),
                      check_if_Min(33, 20), check_if_Min(33, 21), check_if_Min(33, 22), check_if_Min(33, 23),
                      check_if_Min(33, 24), check_if_Min(33, 25), check_if_Min(33, 26), check_if_Min(33, 27),
                      check_if_Min(33, 28), check_if_Min(33, 29), check_if_Min(33, 30), check_if_Min(33, 31),
                      check_if_Min(33, 32), check_if_Min(33, 34), check_if_Min(33, 35), check_if_Min(33, 36),
                      check_if_Min(33, 37), check_if_Min(33, 38), check_if_Min(33, 39), check_if_Min(33, 40),
                      check_if_Min(33, 41), check_if_Min(33, 42), check_if_Min(33, 43), check_if_Min(33, 44),
                      check_if_Min(33, 45), check_if_Min(33, 46), check_if_Min(33, 47), check_if_Min(33, 48),
                      check_if_Min(33, 49), check_if_Min(33, 50)], ignore_index=True)
    return data


def check_M34():
    data = pd.concat([check_if_Min(34, 0), check_if_Min(34, 1), check_if_Min(34, 2), check_if_Min(34, 3),
                      check_if_Min(34, 4), check_if_Min(34, 5), check_if_Min(34, 6), check_if_Min(34, 7),
                      check_if_Min(34, 8), check_if_Min(34, 9), check_if_Min(34, 10), check_if_Min(34, 11),
                      check_if_Min(34, 12), check_if_Min(34, 13), check_if_Min(34, 14), check_if_Min(34, 15),
                      check_if_Min(34, 16), check_if_Min(34, 17), check_if_Min(34, 18), check_if_Min(34, 19),
                      check_if_Min(34, 20), check_if_Min(34, 21), check_if_Min(34, 22), check_if_Min(34, 23),
                      check_if_Min(34, 24), check_if_Min(34, 25), check_if_Min(34, 26), check_if_Min(34, 27),
                      check_if_Min(34, 28), check_if_Min(34, 29), check_if_Min(34, 30), check_if_Min(34, 31),
                      check_if_Min(34, 32), check_if_Min(34, 33), check_if_Min(34, 35), check_if_Min(34, 36),
                      check_if_Min(34, 37), check_if_Min(34, 38), check_if_Min(34, 39), check_if_Min(34, 40),
                      check_if_Min(34, 41), check_if_Min(34, 42), check_if_Min(34, 43), check_if_Min(34, 44),
                      check_if_Min(34, 45), check_if_Min(34, 46), check_if_Min(34, 47), check_if_Min(34, 48),
                      check_if_Min(34, 49), check_if_Min(34, 50)], ignore_index=True)
    return data


def check_M35():
    data = pd.concat([check_if_Min(35, 0), check_if_Min(35, 1), check_if_Min(35, 2), check_if_Min(35, 3),
                      check_if_Min(35, 4), check_if_Min(35, 5), check_if_Min(35, 6), check_if_Min(35, 7),
                      check_if_Min(35, 8), check_if_Min(35, 9), check_if_Min(35, 10), check_if_Min(35, 11),
                      check_if_Min(35, 12), check_if_Min(35, 13), check_if_Min(35, 14), check_if_Min(35, 15),
                      check_if_Min(35, 16), check_if_Min(35, 17), check_if_Min(35, 18), check_if_Min(35, 19),
                      check_if_Min(35, 20), check_if_Min(35, 21), check_if_Min(35, 22), check_if_Min(35, 23),
                      check_if_Min(35, 24), check_if_Min(35, 25), check_if_Min(35, 26), check_if_Min(35, 27),
                      check_if_Min(35, 28), check_if_Min(35, 29), check_if_Min(35, 30), check_if_Min(35, 31),
                      check_if_Min(35, 32), check_if_Min(35, 33), check_if_Min(35, 34), check_if_Min(35, 36),
                      check_if_Min(35, 37), check_if_Min(35, 38), check_if_Min(35, 39), check_if_Min(35, 40),
                      check_if_Min(35, 41), check_if_Min(35, 42), check_if_Min(35, 43), check_if_Min(35, 44),
                      check_if_Min(35, 45), check_if_Min(35, 46), check_if_Min(35, 47), check_if_Min(35, 48),
                      check_if_Min(35, 49), check_if_Min(35, 50)], ignore_index=True)
    return data


def check_M36():
    data = pd.concat([check_if_Min(36, 0), check_if_Min(36, 1), check_if_Min(36, 2), check_if_Min(36, 3),
                      check_if_Min(36, 4), check_if_Min(36, 5), check_if_Min(36, 6), check_if_Min(36, 7),
                      check_if_Min(36, 8), check_if_Min(36, 9), check_if_Min(36, 10), check_if_Min(36, 11),
                      check_if_Min(36, 12), check_if_Min(36, 13), check_if_Min(36, 14), check_if_Min(36, 15),
                      check_if_Min(36, 16), check_if_Min(36, 17), check_if_Min(36, 18), check_if_Min(36, 19),
                      check_if_Min(36, 20), check_if_Min(36, 21), check_if_Min(36, 22), check_if_Min(36, 23),
                      check_if_Min(36, 24), check_if_Min(36, 25), check_if_Min(36, 26), check_if_Min(36, 27),
                      check_if_Min(36, 28), check_if_Min(36, 29), check_if_Min(36, 30), check_if_Min(36, 31),
                      check_if_Min(36, 32), check_if_Min(36, 33), check_if_Min(36, 34), check_if_Min(36, 35),
                      check_if_Min(36, 37), check_if_Min(36, 38), check_if_Min(36, 39), check_if_Min(36, 40),
                      check_if_Min(36, 41), check_if_Min(36, 42), check_if_Min(36, 43), check_if_Min(36, 44),
                      check_if_Min(36, 45), check_if_Min(36, 46), check_if_Min(36, 47), check_if_Min(36, 48),
                      check_if_Min(36, 49), check_if_Min(36, 50)], ignore_index=True)
    return data


def check_M37():
    data = pd.concat([check_if_Min(37, 0), check_if_Min(37, 1), check_if_Min(37, 2), check_if_Min(37, 3),
                      check_if_Min(37, 4), check_if_Min(37, 5), check_if_Min(37, 6), check_if_Min(37, 7),
                      check_if_Min(37, 8), check_if_Min(37, 9), check_if_Min(37, 10), check_if_Min(37, 11),
                      check_if_Min(37, 12), check_if_Min(37, 13), check_if_Min(37, 14), check_if_Min(37, 15),
                      check_if_Min(37, 16), check_if_Min(37, 17), check_if_Min(37, 18), check_if_Min(37, 19),
                      check_if_Min(37, 20), check_if_Min(37, 21), check_if_Min(37, 22), check_if_Min(37, 23),
                      check_if_Min(37, 24), check_if_Min(37, 25), check_if_Min(37, 26), check_if_Min(37, 27),
                      check_if_Min(37, 28), check_if_Min(37, 29), check_if_Min(37, 30), check_if_Min(37, 31),
                      check_if_Min(37, 32), check_if_Min(37, 33), check_if_Min(37, 34), check_if_Min(37, 35),
                      check_if_Min(37, 36), check_if_Min(37, 38), check_if_Min(37, 39), check_if_Min(37, 40),
                      check_if_Min(37, 41), check_if_Min(37, 42), check_if_Min(37, 43), check_if_Min(37, 44),
                      check_if_Min(37, 45), check_if_Min(37, 46), check_if_Min(37, 47), check_if_Min(37, 48),
                      check_if_Min(37, 49), check_if_Min(37, 50)], ignore_index=True)
    return data


def check_M38():
    data = pd.concat([check_if_Min(38, 0), check_if_Min(38, 1), check_if_Min(38, 2), check_if_Min(38, 3),
                      check_if_Min(38, 4), check_if_Min(38, 5), check_if_Min(38, 6), check_if_Min(38, 7),
                      check_if_Min(38, 8), check_if_Min(38, 9), check_if_Min(38, 10), check_if_Min(38, 11),
                      check_if_Min(38, 12), check_if_Min(38, 13), check_if_Min(38, 14), check_if_Min(38, 15),
                      check_if_Min(38, 16), check_if_Min(38, 17), check_if_Min(38, 18), check_if_Min(38, 19),
                      check_if_Min(38, 20), check_if_Min(38, 21), check_if_Min(38, 22), check_if_Min(38, 23),
                      check_if_Min(38, 24), check_if_Min(38, 25), check_if_Min(38, 26), check_if_Min(38, 27),
                      check_if_Min(38, 28), check_if_Min(38, 29), check_if_Min(38, 30), check_if_Min(38, 31),
                      check_if_Min(38, 32), check_if_Min(38, 33), check_if_Min(38, 34), check_if_Min(38, 35),
                      check_if_Min(38, 36), check_if_Min(38, 37), check_if_Min(38, 39), check_if_Min(38, 40),
                      check_if_Min(38, 41), check_if_Min(38, 42), check_if_Min(38, 43), check_if_Min(38, 44),
                      check_if_Min(38, 45), check_if_Min(38, 46), check_if_Min(38, 47), check_if_Min(38, 48),
                      check_if_Min(38, 49), check_if_Min(38, 50)], ignore_index=True)
    return data


def check_M39():
    data = pd.concat([check_if_Min(39, 0), check_if_Min(39, 1), check_if_Min(39, 2), check_if_Min(39, 3),
                      check_if_Min(39, 4), check_if_Min(39, 5), check_if_Min(39, 6), check_if_Min(39, 7),
                      check_if_Min(39, 8), check_if_Min(39, 9), check_if_Min(39, 10), check_if_Min(39, 11),
                      check_if_Min(39, 12), check_if_Min(39, 13), check_if_Min(39, 14), check_if_Min(39, 15),
                      check_if_Min(39, 16), check_if_Min(39, 17), check_if_Min(39, 18), check_if_Min(39, 19),
                      check_if_Min(39, 20), check_if_Min(39, 21), check_if_Min(39, 22), check_if_Min(39, 23),
                      check_if_Min(39, 24), check_if_Min(39, 25), check_if_Min(39, 26), check_if_Min(39, 27),
                      check_if_Min(39, 28), check_if_Min(39, 29), check_if_Min(39, 30), check_if_Min(39, 31),
                      check_if_Min(39, 32), check_if_Min(39, 33), check_if_Min(39, 34), check_if_Min(39, 35),
                      check_if_Min(39, 36), check_if_Min(39, 37), check_if_Min(39, 38), check_if_Min(39, 40),
                      check_if_Min(39, 41), check_if_Min(39, 42), check_if_Min(39, 43), check_if_Min(39, 44),
                      check_if_Min(39, 45), check_if_Min(39, 46), check_if_Min(39, 47), check_if_Min(39, 48),
                      check_if_Min(39, 49), check_if_Min(39, 50)], ignore_index=True)
    return data


def check_M40():
    data = pd.concat([check_if_Min(40, 0), check_if_Min(40, 1), check_if_Min(40, 2), check_if_Min(40, 3),
                      check_if_Min(40, 4), check_if_Min(40, 5), check_if_Min(40, 6), check_if_Min(40, 7),
                      check_if_Min(40, 8), check_if_Min(40, 9), check_if_Min(40, 10), check_if_Min(40, 11),
                      check_if_Min(40, 12), check_if_Min(40, 13), check_if_Min(40, 14), check_if_Min(40, 15),
                      check_if_Min(40, 16), check_if_Min(40, 17), check_if_Min(40, 18), check_if_Min(40, 19),
                      check_if_Min(40, 20), check_if_Min(40, 21), check_if_Min(40, 22), check_if_Min(40, 23),
                      check_if_Min(40, 24), check_if_Min(40, 25), check_if_Min(40, 26), check_if_Min(40, 27),
                      check_if_Min(40, 28), check_if_Min(40, 29), check_if_Min(40, 30), check_if_Min(40, 31),
                      check_if_Min(40, 32), check_if_Min(40, 33), check_if_Min(40, 34), check_if_Min(40, 35),
                      check_if_Min(40, 36), check_if_Min(40, 37), check_if_Min(40, 38), check_if_Min(40, 39),
                      check_if_Min(40, 41), check_if_Min(40, 42), check_if_Min(40, 43), check_if_Min(40, 44),
                      check_if_Min(40, 45), check_if_Min(40, 46), check_if_Min(40, 47), check_if_Min(40, 48),
                      check_if_Min(40, 49), check_if_Min(40, 50)], ignore_index=True)
    return data


def check_M41():
    data = pd.concat([check_if_Min(41, 0), check_if_Min(41, 1), check_if_Min(41, 2), check_if_Min(41, 3),
                      check_if_Min(41, 4), check_if_Min(41, 5), check_if_Min(41, 6), check_if_Min(41, 7),
                      check_if_Min(41, 8), check_if_Min(41, 9), check_if_Min(41, 10), check_if_Min(41, 11),
                      check_if_Min(41, 12), check_if_Min(41, 13), check_if_Min(41, 14), check_if_Min(41, 15),
                      check_if_Min(41, 16), check_if_Min(41, 17), check_if_Min(41, 18), check_if_Min(41, 19),
                      check_if_Min(41, 20), check_if_Min(41, 21), check_if_Min(41, 22), check_if_Min(41, 23),
                      check_if_Min(41, 24), check_if_Min(41, 25), check_if_Min(41, 26), check_if_Min(41, 27),
                      check_if_Min(41, 28), check_if_Min(41, 29), check_if_Min(41, 30), check_if_Min(41, 31),
                      check_if_Min(41, 32), check_if_Min(41, 33), check_if_Min(41, 34), check_if_Min(41, 35),
                      check_if_Min(41, 36), check_if_Min(41, 37), check_if_Min(41, 38), check_if_Min(41, 39),
                      check_if_Min(41, 40), check_if_Min(41, 42), check_if_Min(41, 43), check_if_Min(41, 44),
                      check_if_Min(41, 45), check_if_Min(41, 46), check_if_Min(41, 47), check_if_Min(41, 48),
                      check_if_Min(41, 49), check_if_Min(41, 50)], ignore_index=True)
    return data


def check_M42():
    data = pd.concat([check_if_Min(42, 0), check_if_Min(42, 1), check_if_Min(42, 2), check_if_Min(42, 3),
                      check_if_Min(42, 4), check_if_Min(42, 5), check_if_Min(42, 6), check_if_Min(42, 7),
                      check_if_Min(42, 8), check_if_Min(42, 9), check_if_Min(42, 10), check_if_Min(42, 11),
                      check_if_Min(42, 12), check_if_Min(42, 13), check_if_Min(42, 14), check_if_Min(42, 15),
                      check_if_Min(42, 16), check_if_Min(42, 17), check_if_Min(42, 18), check_if_Min(42, 19),
                      check_if_Min(42, 20), check_if_Min(42, 21), check_if_Min(42, 22), check_if_Min(42, 23),
                      check_if_Min(42, 24), check_if_Min(42, 25), check_if_Min(42, 26), check_if_Min(42, 27),
                      check_if_Min(42, 28), check_if_Min(42, 29), check_if_Min(42, 30), check_if_Min(42, 31),
                      check_if_Min(42, 32), check_if_Min(42, 33), check_if_Min(42, 34), check_if_Min(42, 35),
                      check_if_Min(42, 36), check_if_Min(42, 37), check_if_Min(42, 38), check_if_Min(42, 39),
                      check_if_Min(42, 40), check_if_Min(42, 41), check_if_Min(42, 43), check_if_Min(42, 44),
                      check_if_Min(42, 45), check_if_Min(42, 46), check_if_Min(42, 47), check_if_Min(42, 48),
                      check_if_Min(42, 49), check_if_Min(42, 50)], ignore_index=True)
    return data


def check_M43():
    data = pd.concat([check_if_Min(43, 0), check_if_Min(43, 1), check_if_Min(43, 2), check_if_Min(43, 3),
                      check_if_Min(43, 4), check_if_Min(43, 5), check_if_Min(43, 6), check_if_Min(43, 7),
                      check_if_Min(43, 8), check_if_Min(43, 9), check_if_Min(43, 10), check_if_Min(43, 11),
                      check_if_Min(43, 12), check_if_Min(43, 13), check_if_Min(43, 14), check_if_Min(43, 15),
                      check_if_Min(43, 16), check_if_Min(43, 17), check_if_Min(43, 18), check_if_Min(43, 19),
                      check_if_Min(43, 20), check_if_Min(43, 21), check_if_Min(43, 22), check_if_Min(43, 23),
                      check_if_Min(43, 24), check_if_Min(43, 25), check_if_Min(43, 26), check_if_Min(43, 27),
                      check_if_Min(43, 28), check_if_Min(43, 29), check_if_Min(43, 30), check_if_Min(43, 31),
                      check_if_Min(43, 32), check_if_Min(43, 33), check_if_Min(43, 34), check_if_Min(43, 35),
                      check_if_Min(43, 36), check_if_Min(43, 37), check_if_Min(43, 38), check_if_Min(43, 39),
                      check_if_Min(43, 40), check_if_Min(43, 41), check_if_Min(43, 42), check_if_Min(43, 44),
                      check_if_Min(43, 45), check_if_Min(43, 46), check_if_Min(43, 47), check_if_Min(43, 48),
                      check_if_Min(43, 49), check_if_Min(43, 50)], ignore_index=True)
    return data


def check_M44():
    data = pd.concat([check_if_Min(44, 0), check_if_Min(44, 1), check_if_Min(44, 2), check_if_Min(44, 3),
                      check_if_Min(44, 4), check_if_Min(44, 5), check_if_Min(44, 6), check_if_Min(44, 7),
                      check_if_Min(44, 8), check_if_Min(44, 9), check_if_Min(44, 10), check_if_Min(44, 11),
                      check_if_Min(44, 12), check_if_Min(44, 13), check_if_Min(44, 14), check_if_Min(44, 15),
                      check_if_Min(44, 16), check_if_Min(44, 17), check_if_Min(44, 18), check_if_Min(44, 19),
                      check_if_Min(44, 20), check_if_Min(44, 21), check_if_Min(44, 22), check_if_Min(44, 23),
                      check_if_Min(44, 24), check_if_Min(44, 25), check_if_Min(44, 26), check_if_Min(44, 27),
                      check_if_Min(44, 28), check_if_Min(44, 29), check_if_Min(44, 30), check_if_Min(44, 31),
                      check_if_Min(44, 32), check_if_Min(44, 33), check_if_Min(44, 34), check_if_Min(44, 35),
                      check_if_Min(44, 36), check_if_Min(44, 37), check_if_Min(44, 38), check_if_Min(44, 39),
                      check_if_Min(44, 40), check_if_Min(44, 41), check_if_Min(44, 42), check_if_Min(44, 43),
                      check_if_Min(44, 45), check_if_Min(44, 46), check_if_Min(44, 47), check_if_Min(44, 48),
                      check_if_Min(44, 49), check_if_Min(44, 50)], ignore_index=True)
    return data


def check_M45():
    data = pd.concat([check_if_Min(45, 0), check_if_Min(45, 1), check_if_Min(45, 2), check_if_Min(45, 3),
                      check_if_Min(45, 4), check_if_Min(45, 5), check_if_Min(45, 6), check_if_Min(45, 7),
                      check_if_Min(45, 8), check_if_Min(45, 9), check_if_Min(45, 10), check_if_Min(45, 11),
                      check_if_Min(45, 12), check_if_Min(45, 13), check_if_Min(45, 14), check_if_Min(45, 15),
                      check_if_Min(45, 16), check_if_Min(45, 17), check_if_Min(45, 18), check_if_Min(45, 19),
                      check_if_Min(45, 20), check_if_Min(45, 21), check_if_Min(45, 22), check_if_Min(45, 23),
                      check_if_Min(45, 24), check_if_Min(45, 25), check_if_Min(45, 26), check_if_Min(45, 27),
                      check_if_Min(45, 28), check_if_Min(45, 29), check_if_Min(45, 30), check_if_Min(45, 31),
                      check_if_Min(45, 32), check_if_Min(45, 33), check_if_Min(45, 34), check_if_Min(45, 35),
                      check_if_Min(45, 36), check_if_Min(45, 37), check_if_Min(45, 38), check_if_Min(45, 39),
                      check_if_Min(45, 40), check_if_Min(45, 41), check_if_Min(45, 42), check_if_Min(45, 43),
                      check_if_Min(45, 44), check_if_Min(45, 46), check_if_Min(45, 47), check_if_Min(45, 48),
                      check_if_Min(45, 49), check_if_Min(45, 50)], ignore_index=True)
    return data


def check_M46():
    data = pd.concat([check_if_Min(46, 0), check_if_Min(46, 1), check_if_Min(46, 2), check_if_Min(46, 3),
                      check_if_Min(46, 4), check_if_Min(46, 5), check_if_Min(46, 6), check_if_Min(46, 7),
                      check_if_Min(46, 8), check_if_Min(46, 9), check_if_Min(46, 10), check_if_Min(46, 11),
                      check_if_Min(46, 12), check_if_Min(46, 13), check_if_Min(46, 14), check_if_Min(46, 15),
                      check_if_Min(46, 16), check_if_Min(46, 17), check_if_Min(46, 18), check_if_Min(46, 19),
                      check_if_Min(46, 20), check_if_Min(46, 21), check_if_Min(46, 22), check_if_Min(46, 23),
                      check_if_Min(46, 24), check_if_Min(46, 25), check_if_Min(46, 26), check_if_Min(46, 27),
                      check_if_Min(46, 28), check_if_Min(46, 29), check_if_Min(46, 30), check_if_Min(46, 31),
                      check_if_Min(46, 32), check_if_Min(46, 33), check_if_Min(46, 34), check_if_Min(46, 35),
                      check_if_Min(46, 36), check_if_Min(46, 37), check_if_Min(46, 38), check_if_Min(46, 39),
                      check_if_Min(46, 40), check_if_Min(46, 41), check_if_Min(46, 42), check_if_Min(46, 43),
                      check_if_Min(46, 44), check_if_Min(46, 45), check_if_Min(46, 47), check_if_Min(46, 48),
                      check_if_Min(46, 49), check_if_Min(46, 50)], ignore_index=True)
    return data


def check_M47():
    data = pd.concat([check_if_Min(47, 0), check_if_Min(47, 1), check_if_Min(47, 2), check_if_Min(47, 3),
                      check_if_Min(47, 4), check_if_Min(47, 5), check_if_Min(47, 6), check_if_Min(47, 7),
                      check_if_Min(47, 8), check_if_Min(47, 9), check_if_Min(47, 10), check_if_Min(47, 11),
                      check_if_Min(47, 12), check_if_Min(47, 13), check_if_Min(47, 14), check_if_Min(47, 15),
                      check_if_Min(47, 16), check_if_Min(47, 17), check_if_Min(47, 18), check_if_Min(47, 19),
                      check_if_Min(47, 20), check_if_Min(47, 21), check_if_Min(47, 22), check_if_Min(47, 23),
                      check_if_Min(47, 24), check_if_Min(47, 25), check_if_Min(47, 26), check_if_Min(47, 27),
                      check_if_Min(47, 28), check_if_Min(47, 29), check_if_Min(47, 30), check_if_Min(47, 31),
                      check_if_Min(47, 32), check_if_Min(47, 33), check_if_Min(47, 34), check_if_Min(47, 35),
                      check_if_Min(47, 36), check_if_Min(47, 37), check_if_Min(47, 38), check_if_Min(47, 39),
                      check_if_Min(47, 40), check_if_Min(47, 41), check_if_Min(47, 42), check_if_Min(47, 43),
                      check_if_Min(47, 44), check_if_Min(47, 45), check_if_Min(47, 46), check_if_Min(47, 48),
                      check_if_Min(47, 49), check_if_Min(47, 50)], ignore_index=True)
    return data


def check_M48():
    data = pd.concat([check_if_Min(48, 0), check_if_Min(48, 1), check_if_Min(48, 2), check_if_Min(48, 3),
                      check_if_Min(48, 4), check_if_Min(48, 5), check_if_Min(48, 6), check_if_Min(48, 7),
                      check_if_Min(48, 8), check_if_Min(48, 9), check_if_Min(48, 10), check_if_Min(48, 11),
                      check_if_Min(48, 12), check_if_Min(48, 13), check_if_Min(48, 14), check_if_Min(48, 15),
                      check_if_Min(48, 16), check_if_Min(48, 17), check_if_Min(48, 18), check_if_Min(48, 19),
                      check_if_Min(48, 20), check_if_Min(48, 21), check_if_Min(48, 22), check_if_Min(48, 23),
                      check_if_Min(48, 24), check_if_Min(48, 25), check_if_Min(48, 26), check_if_Min(48, 27),
                      check_if_Min(48, 28), check_if_Min(48, 29), check_if_Min(48, 30), check_if_Min(48, 31),
                      check_if_Min(48, 32), check_if_Min(48, 33), check_if_Min(48, 34), check_if_Min(48, 35),
                      check_if_Min(48, 36), check_if_Min(48, 37), check_if_Min(48, 38), check_if_Min(48, 39),
                      check_if_Min(48, 40), check_if_Min(48, 41), check_if_Min(48, 42), check_if_Min(48, 43),
                      check_if_Min(48, 44), check_if_Min(48, 45), check_if_Min(48, 46), check_if_Min(48, 47),
                      check_if_Min(48, 49), check_if_Min(48, 50)], ignore_index=True)
    return data


def check_M49():
    data = pd.concat([check_if_Min(49, 0), check_if_Min(49, 1), check_if_Min(49, 2), check_if_Min(49, 3),
                      check_if_Min(49, 4), check_if_Min(49, 5), check_if_Min(49, 6), check_if_Min(49, 7),
                      check_if_Min(49, 8), check_if_Min(49, 9), check_if_Min(49, 10), check_if_Min(49, 11),
                      check_if_Min(49, 12), check_if_Min(49, 13), check_if_Min(49, 14), check_if_Min(49, 15),
                      check_if_Min(49, 16), check_if_Min(49, 17), check_if_Min(49, 18), check_if_Min(49, 19),
                      check_if_Min(49, 20), check_if_Min(49, 21), check_if_Min(49, 22), check_if_Min(49, 23),
                      check_if_Min(49, 24), check_if_Min(49, 25), check_if_Min(49, 26), check_if_Min(49, 27),
                      check_if_Min(49, 28), check_if_Min(49, 29), check_if_Min(49, 30), check_if_Min(49, 31),
                      check_if_Min(49, 32), check_if_Min(49, 33), check_if_Min(49, 34), check_if_Min(49, 35),
                      check_if_Min(49, 36), check_if_Min(49, 37), check_if_Min(49, 38), check_if_Min(49, 39),
                      check_if_Min(49, 40), check_if_Min(49, 41), check_if_Min(49, 42), check_if_Min(49, 43),
                      check_if_Min(49, 44), check_if_Min(49, 45), check_if_Min(49, 46), check_if_Min(49, 47),
                      check_if_Min(49, 48), check_if_Min(49, 50)], ignore_index=True)
    return data


def check_M50():
    data = pd.concat([check_if_Min(50, 0), check_if_Min(50, 1), check_if_Min(50, 2), check_if_Min(50, 3),
                      check_if_Min(50, 4), check_if_Min(50, 5), check_if_Min(50, 6), check_if_Min(50, 7),
                      check_if_Min(50, 8), check_if_Min(50, 9), check_if_Min(50, 10), check_if_Min(50, 11),
                      check_if_Min(50, 12), check_if_Min(50, 13), check_if_Min(50, 14), check_if_Min(50, 15),
                      check_if_Min(50, 16), check_if_Min(50, 17), check_if_Min(50, 18), check_if_Min(50, 19),
                      check_if_Min(50, 20), check_if_Min(50, 21), check_if_Min(50, 22), check_if_Min(50, 23),
                      check_if_Min(50, 24), check_if_Min(50, 25), check_if_Min(50, 26), check_if_Min(50, 27),
                      check_if_Min(50, 28), check_if_Min(50, 29), check_if_Min(50, 30), check_if_Min(50, 31),
                      check_if_Min(50, 32), check_if_Min(50, 33), check_if_Min(50, 34), check_if_Min(50, 35),
                      check_if_Min(50, 36), check_if_Min(50, 37), check_if_Min(50, 38), check_if_Min(50, 39),
                      check_if_Min(50, 40), check_if_Min(50, 41), check_if_Min(50, 42), check_if_Min(50, 43),
                      check_if_Min(50, 44), check_if_Min(50, 45), check_if_Min(50, 46), check_if_Min(50, 47),
                      check_if_Min(50, 48), check_if_Min(50, 49)], ignore_index=True)
    return data


def check():
    data = pd.concat([check_M1(), check_M2(), check_M3(), check_M4(),
                      check_M5(), check_M6(), check_M7(), check_M8(),
                      check_M9(), check_M10(), check_M11(), check_M12(),
                      check_M13(), check_M14(), check_M15(), check_M16(),
                      check_M17(), check_M18(), check_M19(), check_M20(),
                      check_M21(), check_M22(), check_M23(), check_M24(),
                      check_M25(), check_M26(), check_M27(), check_M28(),
                      check_M29(), check_M30(), check_M31(), check_M32(),
                      check_M33(), check_M34(), check_M35(), check_M36(),
                      check_M37(), check_M38(), check_M39(), check_M40(),
                      check_M41(), check_M42(), check_M43(), check_M44(),
                      check_M45(), check_M46(), check_M47(), check_M48(),
                      check_M49(), check_M50()], ignore_index=True)
    return data


def check_M_csv():
    data = check()
    string1 = "/Pycharm/HumanActivityRecognition/check"
    string2 = string1 + "/check_M" + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


check_M_csv()


