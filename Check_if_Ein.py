import os

import numpy as np
import pandas as pd

from CreateWord import create_word


def check_if_Ein(x, y):
    d = create_word(x, 'E')['words']
    word_to_keep = np.array(create_word(y, 'E')['words'])
    df = pd.DataFrame(np.array(d[d.isin(word_to_keep)]), columns=['words'])
    return df


def check_E0():
    data = pd.concat([check_if_Ein(0, 1), check_if_Ein(0, 2), check_if_Ein(0, 3), check_if_Ein(0, 4),
                      check_if_Ein(0, 5), check_if_Ein(0, 6), check_if_Ein(0, 7), check_if_Ein(0, 8),
                      check_if_Ein(0, 9), check_if_Ein(0, 10), check_if_Ein(0, 11), check_if_Ein(0, 12),
                      check_if_Ein(0, 13), check_if_Ein(0, 14), check_if_Ein(0, 15), check_if_Ein(0, 16),
                      check_if_Ein(0, 17), check_if_Ein(0, 18), check_if_Ein(0, 19), check_if_Ein(0, 20),
                      check_if_Ein(0, 21), check_if_Ein(0, 22), check_if_Ein(0, 23), check_if_Ein(0, 24),
                      check_if_Ein(0, 25), check_if_Ein(0, 26), check_if_Ein(0, 27), check_if_Ein(0, 28),
                      check_if_Ein(0, 29), check_if_Ein(0, 30), check_if_Ein(0, 31), check_if_Ein(0, 32),
                      check_if_Ein(0, 33), check_if_Ein(0, 34), check_if_Ein(0, 35), check_if_Ein(0, 36),
                      check_if_Ein(0, 37), check_if_Ein(0, 38), check_if_Ein(0, 39), check_if_Ein(0, 40),
                      check_if_Ein(0, 41), check_if_Ein(0, 42), check_if_Ein(0, 43), check_if_Ein(0, 44),
                      check_if_Ein(0, 45), check_if_Ein(0, 46), check_if_Ein(0, 47), check_if_Ein(0, 48),
                      check_if_Ein(0, 49), check_if_Ein(0, 50)], ignore_index=True)
    return data


def check_E1():
    data = pd.concat([check_if_Ein(1, 0), check_if_Ein(1, 2), check_if_Ein(1, 3), check_if_Ein(1, 4),
                      check_if_Ein(1, 5), check_if_Ein(1, 6), check_if_Ein(1, 7), check_if_Ein(1, 8),
                      check_if_Ein(1, 9), check_if_Ein(1, 10), check_if_Ein(1, 11), check_if_Ein(1, 12),
                      check_if_Ein(1, 13), check_if_Ein(1, 14), check_if_Ein(1, 15), check_if_Ein(1, 16),
                      check_if_Ein(1, 17), check_if_Ein(1, 18), check_if_Ein(1, 19), check_if_Ein(1, 20),
                      check_if_Ein(1, 21), check_if_Ein(1, 22), check_if_Ein(1, 23), check_if_Ein(1, 24),
                      check_if_Ein(1, 25), check_if_Ein(1, 26), check_if_Ein(1, 27), check_if_Ein(1, 28),
                      check_if_Ein(1, 29), check_if_Ein(1, 30), check_if_Ein(1, 31), check_if_Ein(1, 32),
                      check_if_Ein(1, 33), check_if_Ein(1, 34), check_if_Ein(1, 35), check_if_Ein(1, 36),
                      check_if_Ein(1, 37), check_if_Ein(1, 38), check_if_Ein(1, 39), check_if_Ein(1, 40),
                      check_if_Ein(1, 41), check_if_Ein(1, 42), check_if_Ein(1, 43), check_if_Ein(1, 44),
                      check_if_Ein(1, 45), check_if_Ein(1, 46), check_if_Ein(1, 47), check_if_Ein(1, 48),
                      check_if_Ein(1, 49), check_if_Ein(1, 50)], ignore_index=True)
    return data


def check_E2():
    data = pd.concat([check_if_Ein(2, 0), check_if_Ein(2, 1), check_if_Ein(2, 3), check_if_Ein(2, 4),
                      check_if_Ein(2, 5), check_if_Ein(2, 6), check_if_Ein(2, 7), check_if_Ein(2, 8),
                      check_if_Ein(2, 9), check_if_Ein(2, 10), check_if_Ein(2, 11), check_if_Ein(2, 12),
                      check_if_Ein(2, 13), check_if_Ein(2, 14), check_if_Ein(2, 15), check_if_Ein(2, 16),
                      check_if_Ein(2, 17), check_if_Ein(2, 18), check_if_Ein(2, 19), check_if_Ein(2, 20),
                      check_if_Ein(2, 21), check_if_Ein(2, 22), check_if_Ein(2, 23), check_if_Ein(2, 24),
                      check_if_Ein(2, 25), check_if_Ein(2, 26), check_if_Ein(2, 27), check_if_Ein(2, 28),
                      check_if_Ein(2, 29), check_if_Ein(2, 30), check_if_Ein(2, 31), check_if_Ein(2, 32),
                      check_if_Ein(2, 33), check_if_Ein(2, 34), check_if_Ein(2, 35), check_if_Ein(2, 36),
                      check_if_Ein(2, 37), check_if_Ein(2, 38), check_if_Ein(2, 39), check_if_Ein(2, 40),
                      check_if_Ein(2, 41), check_if_Ein(2, 42), check_if_Ein(2, 43), check_if_Ein(2, 44),
                      check_if_Ein(2, 45), check_if_Ein(2, 46), check_if_Ein(2, 47), check_if_Ein(2, 48),
                      check_if_Ein(2, 49), check_if_Ein(2, 50)], ignore_index=True)
    return data


def check_E3():
    data = pd.concat([check_if_Ein(3, 0), check_if_Ein(3, 1), check_if_Ein(3, 2), check_if_Ein(3, 4),
                      check_if_Ein(3, 5), check_if_Ein(3, 6), check_if_Ein(3, 7), check_if_Ein(3, 8),
                      check_if_Ein(3, 9), check_if_Ein(3, 10), check_if_Ein(3, 11), check_if_Ein(3, 12),
                      check_if_Ein(3, 13), check_if_Ein(3, 14), check_if_Ein(3, 15), check_if_Ein(3, 16),
                      check_if_Ein(3, 17), check_if_Ein(3, 18), check_if_Ein(3, 19), check_if_Ein(3, 20),
                      check_if_Ein(3, 21), check_if_Ein(3, 22), check_if_Ein(3, 23), check_if_Ein(3, 24),
                      check_if_Ein(3, 25), check_if_Ein(3, 26), check_if_Ein(3, 27), check_if_Ein(3, 28),
                      check_if_Ein(3, 29), check_if_Ein(3, 30), check_if_Ein(3, 31), check_if_Ein(3, 32),
                      check_if_Ein(3, 33), check_if_Ein(3, 34), check_if_Ein(3, 35), check_if_Ein(3, 36),
                      check_if_Ein(3, 37), check_if_Ein(3, 38), check_if_Ein(3, 39), check_if_Ein(3, 40),
                      check_if_Ein(3, 41), check_if_Ein(3, 42), check_if_Ein(3, 43), check_if_Ein(3, 44),
                      check_if_Ein(3, 45), check_if_Ein(3, 46), check_if_Ein(3, 47), check_if_Ein(3, 48),
                      check_if_Ein(3, 49), check_if_Ein(3, 50)], ignore_index=True)
    return data


def check_E4():
    data = pd.concat([check_if_Ein(4, 0), check_if_Ein(4, 1), check_if_Ein(4, 2), check_if_Ein(4, 3),
                      check_if_Ein(4, 5), check_if_Ein(4, 6), check_if_Ein(4, 7), check_if_Ein(4, 8),
                      check_if_Ein(4, 9), check_if_Ein(4, 10), check_if_Ein(4, 11), check_if_Ein(4, 12),
                      check_if_Ein(4, 13), check_if_Ein(4, 14), check_if_Ein(4, 15), check_if_Ein(4, 16),
                      check_if_Ein(4, 17), check_if_Ein(4, 18), check_if_Ein(4, 19), check_if_Ein(4, 20),
                      check_if_Ein(4, 21), check_if_Ein(4, 22), check_if_Ein(4, 23), check_if_Ein(4, 24),
                      check_if_Ein(4, 25), check_if_Ein(4, 26), check_if_Ein(4, 27), check_if_Ein(4, 28),
                      check_if_Ein(4, 29), check_if_Ein(4, 30), check_if_Ein(4, 31), check_if_Ein(4, 32),
                      check_if_Ein(4, 33), check_if_Ein(4, 34), check_if_Ein(4, 35), check_if_Ein(4, 36),
                      check_if_Ein(4, 37), check_if_Ein(4, 38), check_if_Ein(4, 39), check_if_Ein(4, 40),
                      check_if_Ein(4, 41), check_if_Ein(4, 42), check_if_Ein(4, 43), check_if_Ein(4, 44),
                      check_if_Ein(4, 45), check_if_Ein(4, 46), check_if_Ein(4, 47), check_if_Ein(4, 48),
                      check_if_Ein(4, 49), check_if_Ein(4, 50)], ignore_index=True)
    return data


def check_E5():
    data = pd.concat([check_if_Ein(5, 0), check_if_Ein(5, 1), check_if_Ein(5, 2), check_if_Ein(5, 3),
                      check_if_Ein(5, 4), check_if_Ein(5, 6), check_if_Ein(5, 7), check_if_Ein(5, 8),
                      check_if_Ein(5, 9), check_if_Ein(5, 10), check_if_Ein(5, 11), check_if_Ein(5, 12),
                      check_if_Ein(5, 13), check_if_Ein(5, 14), check_if_Ein(5, 15), check_if_Ein(5, 16),
                      check_if_Ein(5, 17), check_if_Ein(5, 18), check_if_Ein(5, 19), check_if_Ein(5, 20),
                      check_if_Ein(5, 21), check_if_Ein(5, 22), check_if_Ein(5, 23), check_if_Ein(5, 24),
                      check_if_Ein(5, 25), check_if_Ein(5, 26), check_if_Ein(5, 27), check_if_Ein(5, 28),
                      check_if_Ein(5, 29), check_if_Ein(5, 30), check_if_Ein(5, 31), check_if_Ein(5, 32),
                      check_if_Ein(5, 33), check_if_Ein(5, 34), check_if_Ein(5, 35), check_if_Ein(5, 36),
                      check_if_Ein(5, 37), check_if_Ein(5, 38), check_if_Ein(5, 39), check_if_Ein(5, 40),
                      check_if_Ein(5, 41), check_if_Ein(5, 42), check_if_Ein(5, 43), check_if_Ein(5, 44),
                      check_if_Ein(5, 45), check_if_Ein(5, 46), check_if_Ein(5, 47), check_if_Ein(5, 48),
                      check_if_Ein(5, 49), check_if_Ein(5, 50)], ignore_index=True)
    return data


def check_E6():
    data = pd.concat([check_if_Ein(6, 0), check_if_Ein(6, 1), check_if_Ein(6, 2), check_if_Ein(6, 3),
                      check_if_Ein(6, 4), check_if_Ein(6, 5), check_if_Ein(6, 7), check_if_Ein(6, 8),
                      check_if_Ein(6, 9), check_if_Ein(6, 10), check_if_Ein(6, 11), check_if_Ein(6, 12),
                      check_if_Ein(6, 13), check_if_Ein(6, 14), check_if_Ein(6, 15), check_if_Ein(6, 16),
                      check_if_Ein(6, 17), check_if_Ein(6, 18), check_if_Ein(6, 19), check_if_Ein(6, 20),
                      check_if_Ein(6, 21), check_if_Ein(6, 22), check_if_Ein(6, 23), check_if_Ein(6, 24),
                      check_if_Ein(6, 25), check_if_Ein(6, 26), check_if_Ein(6, 27), check_if_Ein(6, 28),
                      check_if_Ein(6, 29), check_if_Ein(6, 30), check_if_Ein(6, 31), check_if_Ein(6, 32),
                      check_if_Ein(6, 33), check_if_Ein(6, 34), check_if_Ein(6, 35), check_if_Ein(6, 36),
                      check_if_Ein(6, 37), check_if_Ein(6, 38), check_if_Ein(6, 39), check_if_Ein(6, 40),
                      check_if_Ein(6, 41), check_if_Ein(6, 42), check_if_Ein(6, 43), check_if_Ein(6, 44),
                      check_if_Ein(6, 45), check_if_Ein(6, 46), check_if_Ein(6, 47), check_if_Ein(6, 48),
                      check_if_Ein(6, 49), check_if_Ein(6, 50)], ignore_index=True)
    return data


def check_E7():
    data = pd.concat([check_if_Ein(7, 0), check_if_Ein(7, 1), check_if_Ein(7, 2), check_if_Ein(7, 3),
                      check_if_Ein(7, 4), check_if_Ein(7, 5), check_if_Ein(7, 6), check_if_Ein(7, 8),
                      check_if_Ein(7, 9), check_if_Ein(7, 10), check_if_Ein(7, 11), check_if_Ein(7, 12),
                      check_if_Ein(7, 13), check_if_Ein(7, 14), check_if_Ein(7, 15), check_if_Ein(7, 16),
                      check_if_Ein(7, 17), check_if_Ein(7, 18), check_if_Ein(7, 19), check_if_Ein(7, 20),
                      check_if_Ein(7, 21), check_if_Ein(7, 22), check_if_Ein(7, 23), check_if_Ein(7, 24),
                      check_if_Ein(7, 25), check_if_Ein(7, 26), check_if_Ein(7, 27), check_if_Ein(7, 28),
                      check_if_Ein(7, 29), check_if_Ein(7, 30), check_if_Ein(7, 31), check_if_Ein(7, 32),
                      check_if_Ein(7, 33), check_if_Ein(7, 34), check_if_Ein(7, 35), check_if_Ein(7, 36),
                      check_if_Ein(7, 37), check_if_Ein(7, 38), check_if_Ein(7, 39), check_if_Ein(7, 40),
                      check_if_Ein(7, 41), check_if_Ein(7, 42), check_if_Ein(7, 43), check_if_Ein(7, 44),
                      check_if_Ein(7, 45), check_if_Ein(7, 46), check_if_Ein(7, 47), check_if_Ein(7, 48),
                      check_if_Ein(7, 49), check_if_Ein(7, 50)], ignore_index=True)
    return data


def check_E8():
    data = pd.concat([check_if_Ein(8, 0), check_if_Ein(8, 1), check_if_Ein(8, 2), check_if_Ein(8, 3),
                      check_if_Ein(8, 4), check_if_Ein(8, 5), check_if_Ein(8, 6), check_if_Ein(8, 7),
                      check_if_Ein(8, 9), check_if_Ein(8, 10), check_if_Ein(8, 11), check_if_Ein(8, 12),
                      check_if_Ein(8, 13), check_if_Ein(8, 14), check_if_Ein(8, 15), check_if_Ein(8, 16),
                      check_if_Ein(8, 17), check_if_Ein(8, 18), check_if_Ein(8, 19), check_if_Ein(8, 20),
                      check_if_Ein(8, 21), check_if_Ein(8, 22), check_if_Ein(8, 23), check_if_Ein(8, 24),
                      check_if_Ein(8, 25), check_if_Ein(8, 26), check_if_Ein(8, 27), check_if_Ein(8, 28),
                      check_if_Ein(8, 29), check_if_Ein(8, 30), check_if_Ein(8, 31), check_if_Ein(8, 32),
                      check_if_Ein(8, 33), check_if_Ein(8, 34), check_if_Ein(8, 35), check_if_Ein(8, 36),
                      check_if_Ein(8, 37), check_if_Ein(8, 38), check_if_Ein(8, 39), check_if_Ein(8, 40),
                      check_if_Ein(8, 41), check_if_Ein(8, 42), check_if_Ein(8, 43), check_if_Ein(8, 44),
                      check_if_Ein(8, 45), check_if_Ein(8, 46), check_if_Ein(8, 47), check_if_Ein(8, 48),
                      check_if_Ein(8, 49), check_if_Ein(8, 50)], ignore_index=True)
    return data


def check_E9():
    data = pd.concat([check_if_Ein(9, 0), check_if_Ein(9, 1), check_if_Ein(9, 2), check_if_Ein(9, 3),
                      check_if_Ein(9, 4), check_if_Ein(9, 5), check_if_Ein(9, 6), check_if_Ein(9, 7),
                      check_if_Ein(9, 8), check_if_Ein(9, 10), check_if_Ein(9, 11), check_if_Ein(9, 12),
                      check_if_Ein(9, 13), check_if_Ein(9, 14), check_if_Ein(9, 15), check_if_Ein(9, 16),
                      check_if_Ein(9, 17), check_if_Ein(9, 18), check_if_Ein(9, 19), check_if_Ein(9, 20),
                      check_if_Ein(9, 21), check_if_Ein(9, 22), check_if_Ein(9, 23), check_if_Ein(9, 24),
                      check_if_Ein(9, 25), check_if_Ein(9, 26), check_if_Ein(9, 27), check_if_Ein(9, 28),
                      check_if_Ein(9, 29), check_if_Ein(9, 30), check_if_Ein(9, 31), check_if_Ein(9, 32),
                      check_if_Ein(9, 33), check_if_Ein(9, 34), check_if_Ein(9, 35), check_if_Ein(9, 36),
                      check_if_Ein(9, 37), check_if_Ein(9, 38), check_if_Ein(9, 39), check_if_Ein(9, 40),
                      check_if_Ein(9, 41), check_if_Ein(9, 42), check_if_Ein(9, 43), check_if_Ein(9, 44),
                      check_if_Ein(9, 45), check_if_Ein(9, 46), check_if_Ein(9, 47), check_if_Ein(9, 48),
                      check_if_Ein(9, 49), check_if_Ein(9, 50)], ignore_index=True)
    return data


def check_E10():
    data = pd.concat([check_if_Ein(10, 0), check_if_Ein(10, 1), check_if_Ein(10, 2), check_if_Ein(10, 3),
                      check_if_Ein(10, 4), check_if_Ein(10, 5), check_if_Ein(10, 6), check_if_Ein(10, 7),
                      check_if_Ein(10, 8), check_if_Ein(10, 9), check_if_Ein(10, 11), check_if_Ein(10, 12),
                      check_if_Ein(10, 13), check_if_Ein(10, 14), check_if_Ein(10, 15), check_if_Ein(10, 16),
                      check_if_Ein(10, 17), check_if_Ein(10, 18), check_if_Ein(10, 19), check_if_Ein(10, 20),
                      check_if_Ein(10, 21), check_if_Ein(10, 22), check_if_Ein(10, 23), check_if_Ein(10, 24),
                      check_if_Ein(10, 25), check_if_Ein(10, 26), check_if_Ein(10, 27), check_if_Ein(10, 28),
                      check_if_Ein(10, 29), check_if_Ein(10, 30), check_if_Ein(10, 31), check_if_Ein(10, 32),
                      check_if_Ein(10, 33), check_if_Ein(10, 34), check_if_Ein(10, 35), check_if_Ein(10, 36),
                      check_if_Ein(10, 37), check_if_Ein(10, 38), check_if_Ein(10, 39), check_if_Ein(10, 40),
                      check_if_Ein(10, 41), check_if_Ein(10, 42), check_if_Ein(10, 43), check_if_Ein(10, 44),
                      check_if_Ein(10, 45), check_if_Ein(10, 46), check_if_Ein(10, 47), check_if_Ein(10, 48),
                      check_if_Ein(10, 49), check_if_Ein(10, 50)], ignore_index=True)
    return data


def check_E11():
    data = pd.concat([check_if_Ein(11, 0), check_if_Ein(11, 1), check_if_Ein(11, 2), check_if_Ein(11, 3),
                      check_if_Ein(11, 4), check_if_Ein(11, 5), check_if_Ein(11, 6), check_if_Ein(11, 7),
                      check_if_Ein(11, 8), check_if_Ein(11, 9), check_if_Ein(11, 10), check_if_Ein(11, 12),
                      check_if_Ein(11, 13), check_if_Ein(11, 14), check_if_Ein(11, 15), check_if_Ein(11, 16),
                      check_if_Ein(11, 17), check_if_Ein(11, 18), check_if_Ein(11, 19), check_if_Ein(11, 20),
                      check_if_Ein(11, 21), check_if_Ein(11, 22), check_if_Ein(11, 23), check_if_Ein(11, 24),
                      check_if_Ein(11, 25), check_if_Ein(11, 26), check_if_Ein(11, 27), check_if_Ein(11, 28),
                      check_if_Ein(11, 29), check_if_Ein(11, 30), check_if_Ein(11, 31), check_if_Ein(11, 32),
                      check_if_Ein(11, 33), check_if_Ein(11, 34), check_if_Ein(11, 35), check_if_Ein(11, 36),
                      check_if_Ein(11, 37), check_if_Ein(11, 38), check_if_Ein(11, 39), check_if_Ein(11, 40),
                      check_if_Ein(11, 41), check_if_Ein(11, 42), check_if_Ein(11, 43), check_if_Ein(11, 44),
                      check_if_Ein(11, 45), check_if_Ein(11, 46), check_if_Ein(11, 47), check_if_Ein(11, 48),
                      check_if_Ein(11, 49), check_if_Ein(11, 50)], ignore_index=True)
    return data


def check_E12():
    data = pd.concat([check_if_Ein(12, 0), check_if_Ein(12, 1), check_if_Ein(12, 2), check_if_Ein(12, 3),
                      check_if_Ein(12, 4), check_if_Ein(12, 5), check_if_Ein(12, 6), check_if_Ein(12, 7),
                      check_if_Ein(12, 8), check_if_Ein(12, 9), check_if_Ein(12, 10), check_if_Ein(12, 11),
                      check_if_Ein(12, 13), check_if_Ein(12, 14), check_if_Ein(12, 15), check_if_Ein(12, 16),
                      check_if_Ein(12, 17), check_if_Ein(12, 18), check_if_Ein(12, 19), check_if_Ein(12, 20),
                      check_if_Ein(12, 21), check_if_Ein(12, 22), check_if_Ein(12, 23), check_if_Ein(12, 24),
                      check_if_Ein(12, 25), check_if_Ein(12, 26), check_if_Ein(12, 27), check_if_Ein(12, 28),
                      check_if_Ein(12, 29), check_if_Ein(12, 30), check_if_Ein(12, 31), check_if_Ein(12, 32),
                      check_if_Ein(12, 33), check_if_Ein(12, 34), check_if_Ein(12, 35), check_if_Ein(12, 36),
                      check_if_Ein(12, 37), check_if_Ein(12, 38), check_if_Ein(12, 39), check_if_Ein(12, 40),
                      check_if_Ein(12, 41), check_if_Ein(12, 42), check_if_Ein(12, 43), check_if_Ein(12, 44),
                      check_if_Ein(12, 45), check_if_Ein(12, 46), check_if_Ein(12, 47), check_if_Ein(12, 48),
                      check_if_Ein(12, 49), check_if_Ein(12, 50)], ignore_index=True)
    return data


def check_E13():
    data = pd.concat([check_if_Ein(13, 0), check_if_Ein(13, 1), check_if_Ein(13, 2), check_if_Ein(13, 3),
                      check_if_Ein(13, 4), check_if_Ein(13, 5), check_if_Ein(13, 6), check_if_Ein(13, 7),
                      check_if_Ein(13, 8), check_if_Ein(13, 9), check_if_Ein(13, 10), check_if_Ein(13, 11),
                      check_if_Ein(13, 12), check_if_Ein(13, 14), check_if_Ein(13, 15), check_if_Ein(13, 16),
                      check_if_Ein(13, 17), check_if_Ein(13, 18), check_if_Ein(13, 19), check_if_Ein(13, 20),
                      check_if_Ein(13, 21), check_if_Ein(13, 22), check_if_Ein(13, 23), check_if_Ein(13, 24),
                      check_if_Ein(13, 25), check_if_Ein(13, 26), check_if_Ein(13, 27), check_if_Ein(13, 28),
                      check_if_Ein(13, 29), check_if_Ein(13, 30), check_if_Ein(13, 31), check_if_Ein(13, 32),
                      check_if_Ein(13, 33), check_if_Ein(13, 34), check_if_Ein(13, 35), check_if_Ein(13, 36),
                      check_if_Ein(13, 37), check_if_Ein(13, 38), check_if_Ein(13, 39), check_if_Ein(13, 40),
                      check_if_Ein(13, 41), check_if_Ein(13, 42), check_if_Ein(13, 43), check_if_Ein(13, 44),
                      check_if_Ein(13, 45), check_if_Ein(13, 46), check_if_Ein(13, 47), check_if_Ein(13, 48),
                      check_if_Ein(13, 49), check_if_Ein(13, 50)], ignore_index=True)
    return data


def check_E14():
    data = pd.concat([check_if_Ein(14, 0), check_if_Ein(14, 1), check_if_Ein(14, 2), check_if_Ein(14, 3),
                      check_if_Ein(14, 4), check_if_Ein(14, 5), check_if_Ein(14, 6), check_if_Ein(14, 7),
                      check_if_Ein(14, 8), check_if_Ein(14, 9), check_if_Ein(14, 10), check_if_Ein(14, 11),
                      check_if_Ein(14, 12), check_if_Ein(14, 13), check_if_Ein(14, 15), check_if_Ein(14, 16),
                      check_if_Ein(14, 17), check_if_Ein(14, 18), check_if_Ein(14, 19), check_if_Ein(14, 20),
                      check_if_Ein(14, 21), check_if_Ein(14, 22), check_if_Ein(14, 23), check_if_Ein(14, 24),
                      check_if_Ein(14, 25), check_if_Ein(14, 26), check_if_Ein(14, 27), check_if_Ein(14, 28),
                      check_if_Ein(14, 29), check_if_Ein(14, 30), check_if_Ein(14, 31), check_if_Ein(14, 32),
                      check_if_Ein(14, 33), check_if_Ein(14, 34), check_if_Ein(14, 35), check_if_Ein(14, 36),
                      check_if_Ein(14, 37), check_if_Ein(14, 38), check_if_Ein(14, 39), check_if_Ein(14, 40),
                      check_if_Ein(14, 41), check_if_Ein(14, 42), check_if_Ein(14, 43), check_if_Ein(14, 44),
                      check_if_Ein(14, 45), check_if_Ein(14, 46), check_if_Ein(14, 47), check_if_Ein(14, 48),
                      check_if_Ein(14, 49), check_if_Ein(14, 50)], ignore_index=True)
    return data


def check_E15():
    data = pd.concat([check_if_Ein(15, 0), check_if_Ein(15, 1), check_if_Ein(15, 2), check_if_Ein(15, 3),
                      check_if_Ein(15, 4), check_if_Ein(15, 5), check_if_Ein(15, 6), check_if_Ein(15, 7),
                      check_if_Ein(15, 8), check_if_Ein(15, 9), check_if_Ein(15, 10), check_if_Ein(15, 11),
                      check_if_Ein(15, 12), check_if_Ein(15, 13), check_if_Ein(15, 14), check_if_Ein(15, 16),
                      check_if_Ein(15, 17), check_if_Ein(15, 18), check_if_Ein(15, 19), check_if_Ein(15, 20),
                      check_if_Ein(15, 21), check_if_Ein(15, 22), check_if_Ein(15, 23), check_if_Ein(15, 24),
                      check_if_Ein(15, 25), check_if_Ein(15, 26), check_if_Ein(15, 27), check_if_Ein(15, 28),
                      check_if_Ein(15, 29), check_if_Ein(15, 30), check_if_Ein(15, 31), check_if_Ein(15, 32),
                      check_if_Ein(15, 33), check_if_Ein(15, 34), check_if_Ein(15, 35), check_if_Ein(15, 36),
                      check_if_Ein(15, 37), check_if_Ein(15, 38), check_if_Ein(15, 39), check_if_Ein(15, 40),
                      check_if_Ein(15, 41), check_if_Ein(15, 42), check_if_Ein(15, 43), check_if_Ein(15, 44),
                      check_if_Ein(15, 45), check_if_Ein(15, 46), check_if_Ein(15, 47), check_if_Ein(15, 48),
                      check_if_Ein(15, 49), check_if_Ein(15, 50)], ignore_index=True)
    return data


def check_E16():
    data = pd.concat([check_if_Ein(16, 0), check_if_Ein(16, 1), check_if_Ein(16, 2), check_if_Ein(16, 3),
                      check_if_Ein(16, 4), check_if_Ein(16, 5), check_if_Ein(16, 6), check_if_Ein(16, 7),
                      check_if_Ein(16, 8), check_if_Ein(16, 9), check_if_Ein(16, 10), check_if_Ein(16, 11),
                      check_if_Ein(16, 12), check_if_Ein(16, 13), check_if_Ein(16, 14), check_if_Ein(16, 15),
                      check_if_Ein(16, 17), check_if_Ein(16, 18), check_if_Ein(16, 19), check_if_Ein(16, 20),
                      check_if_Ein(16, 21), check_if_Ein(16, 22), check_if_Ein(16, 23), check_if_Ein(16, 24),
                      check_if_Ein(16, 25), check_if_Ein(16, 26), check_if_Ein(16, 27), check_if_Ein(16, 28),
                      check_if_Ein(16, 29), check_if_Ein(16, 30), check_if_Ein(16, 31), check_if_Ein(16, 32),
                      check_if_Ein(16, 33), check_if_Ein(16, 34), check_if_Ein(16, 35), check_if_Ein(16, 36),
                      check_if_Ein(16, 37), check_if_Ein(16, 38), check_if_Ein(16, 39), check_if_Ein(16, 40),
                      check_if_Ein(16, 41), check_if_Ein(16, 42), check_if_Ein(16, 43), check_if_Ein(16, 44),
                      check_if_Ein(16, 45), check_if_Ein(16, 46), check_if_Ein(16, 47), check_if_Ein(16, 48),
                      check_if_Ein(16, 49), check_if_Ein(16, 50)], ignore_index=True)
    return data


def check_E17():
    data = pd.concat([check_if_Ein(17, 0), check_if_Ein(17, 1), check_if_Ein(17, 2), check_if_Ein(17, 3),
                      check_if_Ein(17, 4), check_if_Ein(17, 5), check_if_Ein(17, 6), check_if_Ein(17, 7),
                      check_if_Ein(17, 8), check_if_Ein(17, 9), check_if_Ein(17, 10), check_if_Ein(17, 11),
                      check_if_Ein(17, 12), check_if_Ein(17, 13), check_if_Ein(17, 14), check_if_Ein(17, 15),
                      check_if_Ein(17, 16), check_if_Ein(17, 18), check_if_Ein(17, 19), check_if_Ein(17, 20),
                      check_if_Ein(17, 21), check_if_Ein(17, 22), check_if_Ein(17, 23), check_if_Ein(17, 24),
                      check_if_Ein(17, 25), check_if_Ein(17, 26), check_if_Ein(17, 27), check_if_Ein(17, 28),
                      check_if_Ein(17, 29), check_if_Ein(17, 30), check_if_Ein(17, 31), check_if_Ein(17, 32),
                      check_if_Ein(17, 33), check_if_Ein(17, 34), check_if_Ein(17, 35), check_if_Ein(17, 36),
                      check_if_Ein(17, 37), check_if_Ein(17, 38), check_if_Ein(17, 39), check_if_Ein(17, 40),
                      check_if_Ein(17, 41), check_if_Ein(17, 42), check_if_Ein(17, 43), check_if_Ein(17, 44),
                      check_if_Ein(17, 45), check_if_Ein(17, 46), check_if_Ein(17, 47), check_if_Ein(17, 48),
                      check_if_Ein(17, 49), check_if_Ein(17, 50)], ignore_index=True)
    return data


def check_E18():
    data = pd.concat([check_if_Ein(18, 0), check_if_Ein(18, 1), check_if_Ein(18, 2), check_if_Ein(18, 3),
                      check_if_Ein(18, 4), check_if_Ein(18, 5), check_if_Ein(18, 6), check_if_Ein(18, 7),
                      check_if_Ein(18, 8), check_if_Ein(18, 9), check_if_Ein(18, 10), check_if_Ein(18, 11),
                      check_if_Ein(18, 12), check_if_Ein(18, 13), check_if_Ein(18, 14), check_if_Ein(18, 15),
                      check_if_Ein(18, 16), check_if_Ein(18, 17), check_if_Ein(18, 19), check_if_Ein(18, 20),
                      check_if_Ein(18, 21), check_if_Ein(18, 22), check_if_Ein(18, 23), check_if_Ein(18, 24),
                      check_if_Ein(18, 25), check_if_Ein(18, 26), check_if_Ein(18, 27), check_if_Ein(18, 28),
                      check_if_Ein(18, 29), check_if_Ein(18, 30), check_if_Ein(18, 31), check_if_Ein(18, 32),
                      check_if_Ein(18, 33), check_if_Ein(18, 34), check_if_Ein(18, 35), check_if_Ein(18, 36),
                      check_if_Ein(18, 37), check_if_Ein(18, 38), check_if_Ein(18, 39), check_if_Ein(18, 40),
                      check_if_Ein(18, 41), check_if_Ein(18, 42), check_if_Ein(18, 43), check_if_Ein(18, 44),
                      check_if_Ein(18, 45), check_if_Ein(18, 46), check_if_Ein(18, 47), check_if_Ein(18, 48),
                      check_if_Ein(18, 49), check_if_Ein(18, 50)], ignore_index=True)
    return data


def check_E19():
    data = pd.concat([check_if_Ein(19, 0), check_if_Ein(19, 1), check_if_Ein(19, 2), check_if_Ein(19, 3),
                      check_if_Ein(19, 4), check_if_Ein(19, 5), check_if_Ein(19, 6), check_if_Ein(19, 7),
                      check_if_Ein(19, 8), check_if_Ein(19, 9), check_if_Ein(19, 10), check_if_Ein(19, 11),
                      check_if_Ein(19, 12), check_if_Ein(19, 13), check_if_Ein(19, 14), check_if_Ein(19, 15),
                      check_if_Ein(19, 16), check_if_Ein(19, 17), check_if_Ein(19, 18), check_if_Ein(19, 20),
                      check_if_Ein(19, 21), check_if_Ein(19, 22), check_if_Ein(19, 23), check_if_Ein(19, 24),
                      check_if_Ein(19, 25), check_if_Ein(19, 26), check_if_Ein(19, 27), check_if_Ein(19, 28),
                      check_if_Ein(19, 29), check_if_Ein(19, 30), check_if_Ein(19, 31), check_if_Ein(19, 32),
                      check_if_Ein(19, 33), check_if_Ein(19, 34), check_if_Ein(19, 35), check_if_Ein(19, 36),
                      check_if_Ein(19, 37), check_if_Ein(19, 38), check_if_Ein(19, 39), check_if_Ein(19, 40),
                      check_if_Ein(19, 41), check_if_Ein(19, 42), check_if_Ein(19, 43), check_if_Ein(19, 44),
                      check_if_Ein(19, 45), check_if_Ein(19, 46), check_if_Ein(19, 47), check_if_Ein(19, 48),
                      check_if_Ein(19, 49), check_if_Ein(19, 50)], ignore_index=True)
    return data


def check_E20():
    data = pd.concat([check_if_Ein(20, 0), check_if_Ein(20, 1), check_if_Ein(20, 2), check_if_Ein(20, 3),
                      check_if_Ein(20, 4), check_if_Ein(20, 5), check_if_Ein(20, 6), check_if_Ein(20, 7),
                      check_if_Ein(20, 8), check_if_Ein(20, 9), check_if_Ein(20, 10), check_if_Ein(20, 11),
                      check_if_Ein(20, 12), check_if_Ein(20, 13), check_if_Ein(20, 14), check_if_Ein(20, 15),
                      check_if_Ein(20, 16), check_if_Ein(20, 17), check_if_Ein(20, 18), check_if_Ein(20, 19),
                      check_if_Ein(20, 21), check_if_Ein(20, 22), check_if_Ein(20, 23), check_if_Ein(20, 24),
                      check_if_Ein(20, 25), check_if_Ein(20, 26), check_if_Ein(20, 27), check_if_Ein(20, 28),
                      check_if_Ein(20, 29), check_if_Ein(20, 30), check_if_Ein(20, 31), check_if_Ein(20, 32),
                      check_if_Ein(20, 33), check_if_Ein(20, 34), check_if_Ein(20, 35), check_if_Ein(20, 36),
                      check_if_Ein(20, 37), check_if_Ein(20, 38), check_if_Ein(20, 39), check_if_Ein(20, 40),
                      check_if_Ein(20, 41), check_if_Ein(20, 42), check_if_Ein(20, 43), check_if_Ein(20, 44),
                      check_if_Ein(20, 45), check_if_Ein(20, 46), check_if_Ein(20, 47), check_if_Ein(20, 48),
                      check_if_Ein(20, 49), check_if_Ein(20, 50)], ignore_index=True)
    return data


def check_E21():
    data = pd.concat([check_if_Ein(21, 0), check_if_Ein(21, 1), check_if_Ein(21, 2), check_if_Ein(21, 3),
                      check_if_Ein(21, 4), check_if_Ein(21, 5), check_if_Ein(21, 6), check_if_Ein(21, 7),
                      check_if_Ein(21, 8), check_if_Ein(21, 9), check_if_Ein(21, 10), check_if_Ein(21, 11),
                      check_if_Ein(21, 12), check_if_Ein(21, 13), check_if_Ein(21, 14), check_if_Ein(21, 15),
                      check_if_Ein(21, 16), check_if_Ein(21, 17), check_if_Ein(21, 18), check_if_Ein(21, 19),
                      check_if_Ein(21, 20), check_if_Ein(21, 22), check_if_Ein(21, 23), check_if_Ein(21, 24),
                      check_if_Ein(21, 25), check_if_Ein(21, 26), check_if_Ein(21, 27), check_if_Ein(21, 28),
                      check_if_Ein(21, 29), check_if_Ein(21, 30), check_if_Ein(21, 31), check_if_Ein(21, 32),
                      check_if_Ein(21, 33), check_if_Ein(21, 34), check_if_Ein(21, 35), check_if_Ein(21, 36),
                      check_if_Ein(21, 37), check_if_Ein(21, 38), check_if_Ein(21, 39), check_if_Ein(21, 40),
                      check_if_Ein(21, 41), check_if_Ein(21, 42), check_if_Ein(21, 43), check_if_Ein(21, 44),
                      check_if_Ein(21, 45), check_if_Ein(21, 46), check_if_Ein(21, 47), check_if_Ein(21, 48),
                      check_if_Ein(21, 49), check_if_Ein(21, 50)], ignore_index=True)
    return data


def check_E22():
    data = pd.concat([check_if_Ein(22, 0), check_if_Ein(22, 1), check_if_Ein(22, 2), check_if_Ein(22, 3),
                      check_if_Ein(22, 4), check_if_Ein(22, 5), check_if_Ein(22, 6), check_if_Ein(22, 7),
                      check_if_Ein(22, 8), check_if_Ein(22, 9), check_if_Ein(22, 10), check_if_Ein(22, 11),
                      check_if_Ein(22, 12), check_if_Ein(22, 13), check_if_Ein(22, 14), check_if_Ein(22, 15),
                      check_if_Ein(22, 16), check_if_Ein(22, 17), check_if_Ein(22, 18), check_if_Ein(22, 19),
                      check_if_Ein(22, 20), check_if_Ein(22, 21), check_if_Ein(22, 23), check_if_Ein(22, 24),
                      check_if_Ein(22, 25), check_if_Ein(22, 26), check_if_Ein(22, 27), check_if_Ein(22, 28),
                      check_if_Ein(22, 29), check_if_Ein(22, 30), check_if_Ein(22, 31), check_if_Ein(22, 32),
                      check_if_Ein(22, 33), check_if_Ein(22, 34), check_if_Ein(22, 35), check_if_Ein(22, 36),
                      check_if_Ein(22, 37), check_if_Ein(22, 38), check_if_Ein(22, 39), check_if_Ein(22, 40),
                      check_if_Ein(22, 41), check_if_Ein(22, 42), check_if_Ein(22, 43), check_if_Ein(22, 44),
                      check_if_Ein(22, 45), check_if_Ein(22, 46), check_if_Ein(22, 47), check_if_Ein(22, 48),
                      check_if_Ein(22, 49), check_if_Ein(22, 50)], ignore_index=True)
    return data


def check_E23():
    data = pd.concat([check_if_Ein(23, 0), check_if_Ein(23, 1), check_if_Ein(23, 2), check_if_Ein(23, 3),
                      check_if_Ein(23, 4), check_if_Ein(23, 5), check_if_Ein(23, 6), check_if_Ein(23, 7),
                      check_if_Ein(23, 8), check_if_Ein(23, 9), check_if_Ein(23, 10), check_if_Ein(23, 11),
                      check_if_Ein(23, 12), check_if_Ein(23, 13), check_if_Ein(23, 14), check_if_Ein(23, 15),
                      check_if_Ein(23, 16), check_if_Ein(23, 17), check_if_Ein(23, 18), check_if_Ein(23, 19),
                      check_if_Ein(23, 20), check_if_Ein(23, 21), check_if_Ein(23, 22), check_if_Ein(23, 24),
                      check_if_Ein(23, 25), check_if_Ein(23, 26), check_if_Ein(23, 27), check_if_Ein(23, 28),
                      check_if_Ein(23, 29), check_if_Ein(23, 30), check_if_Ein(23, 31), check_if_Ein(23, 32),
                      check_if_Ein(23, 33), check_if_Ein(23, 34), check_if_Ein(23, 35), check_if_Ein(23, 36),
                      check_if_Ein(23, 37), check_if_Ein(23, 38), check_if_Ein(23, 39), check_if_Ein(23, 40),
                      check_if_Ein(23, 41), check_if_Ein(23, 42), check_if_Ein(23, 43), check_if_Ein(23, 44),
                      check_if_Ein(23, 45), check_if_Ein(23, 46), check_if_Ein(23, 47), check_if_Ein(23, 48),
                      check_if_Ein(23, 49), check_if_Ein(23, 50)], ignore_index=True)
    return data


def check_E24():
    data = pd.concat([check_if_Ein(24, 0), check_if_Ein(24, 1), check_if_Ein(24, 2), check_if_Ein(24, 3),
                      check_if_Ein(24, 4), check_if_Ein(24, 5), check_if_Ein(24, 6), check_if_Ein(24, 7),
                      check_if_Ein(24, 8), check_if_Ein(24, 9), check_if_Ein(24, 10), check_if_Ein(24, 11),
                      check_if_Ein(24, 12), check_if_Ein(24, 13), check_if_Ein(24, 14), check_if_Ein(24, 15),
                      check_if_Ein(24, 16), check_if_Ein(24, 17), check_if_Ein(24, 18), check_if_Ein(24, 19),
                      check_if_Ein(24, 20), check_if_Ein(24, 21), check_if_Ein(24, 22), check_if_Ein(24, 23),
                      check_if_Ein(24, 25), check_if_Ein(24, 26), check_if_Ein(24, 27), check_if_Ein(24, 28),
                      check_if_Ein(24, 29), check_if_Ein(24, 30), check_if_Ein(24, 31), check_if_Ein(24, 32),
                      check_if_Ein(24, 33), check_if_Ein(24, 34), check_if_Ein(24, 35), check_if_Ein(24, 36),
                      check_if_Ein(24, 37), check_if_Ein(24, 38), check_if_Ein(24, 39), check_if_Ein(24, 40),
                      check_if_Ein(24, 41), check_if_Ein(24, 42), check_if_Ein(24, 43), check_if_Ein(24, 44),
                      check_if_Ein(24, 45), check_if_Ein(24, 46), check_if_Ein(24, 47), check_if_Ein(24, 48),
                      check_if_Ein(24, 49), check_if_Ein(24, 50)], ignore_index=True)
    return data


def check_E25():
    data = pd.concat([check_if_Ein(25, 0), check_if_Ein(25, 1), check_if_Ein(25, 2), check_if_Ein(25, 3),
                      check_if_Ein(25, 4), check_if_Ein(25, 5), check_if_Ein(25, 6), check_if_Ein(25, 7),
                      check_if_Ein(25, 8), check_if_Ein(25, 9), check_if_Ein(25, 10), check_if_Ein(25, 11),
                      check_if_Ein(25, 12), check_if_Ein(25, 13), check_if_Ein(25, 14), check_if_Ein(25, 15),
                      check_if_Ein(25, 16), check_if_Ein(25, 17), check_if_Ein(25, 18), check_if_Ein(25, 19),
                      check_if_Ein(25, 20), check_if_Ein(25, 21), check_if_Ein(25, 22), check_if_Ein(25, 23),
                      check_if_Ein(25, 24), check_if_Ein(25, 26), check_if_Ein(25, 27), check_if_Ein(25, 28),
                      check_if_Ein(25, 29), check_if_Ein(25, 30), check_if_Ein(25, 31), check_if_Ein(25, 32),
                      check_if_Ein(25, 33), check_if_Ein(25, 34), check_if_Ein(25, 35), check_if_Ein(25, 36),
                      check_if_Ein(25, 37), check_if_Ein(25, 38), check_if_Ein(25, 39), check_if_Ein(25, 40),
                      check_if_Ein(25, 41), check_if_Ein(25, 42), check_if_Ein(25, 43), check_if_Ein(25, 44),
                      check_if_Ein(25, 45), check_if_Ein(25, 46), check_if_Ein(25, 47), check_if_Ein(25, 48),
                      check_if_Ein(25, 49), check_if_Ein(25, 50)], ignore_index=True)
    return data


def check_E26():
    data = pd.concat([check_if_Ein(26, 0), check_if_Ein(26, 1), check_if_Ein(26, 2), check_if_Ein(26, 3),
                      check_if_Ein(26, 4), check_if_Ein(26, 5), check_if_Ein(26, 6), check_if_Ein(26, 7),
                      check_if_Ein(26, 8), check_if_Ein(26, 9), check_if_Ein(26, 10), check_if_Ein(26, 11),
                      check_if_Ein(26, 12), check_if_Ein(26, 13), check_if_Ein(26, 14), check_if_Ein(26, 15),
                      check_if_Ein(26, 16), check_if_Ein(26, 17), check_if_Ein(26, 18), check_if_Ein(26, 19),
                      check_if_Ein(26, 20), check_if_Ein(26, 21), check_if_Ein(26, 22), check_if_Ein(26, 23),
                      check_if_Ein(26, 24), check_if_Ein(26, 25), check_if_Ein(26, 27), check_if_Ein(26, 28),
                      check_if_Ein(26, 29), check_if_Ein(26, 30), check_if_Ein(26, 31), check_if_Ein(26, 32),
                      check_if_Ein(26, 33), check_if_Ein(26, 34), check_if_Ein(26, 35), check_if_Ein(26, 36),
                      check_if_Ein(26, 37), check_if_Ein(26, 38), check_if_Ein(26, 39), check_if_Ein(26, 40),
                      check_if_Ein(26, 41), check_if_Ein(26, 42), check_if_Ein(26, 43), check_if_Ein(26, 44),
                      check_if_Ein(26, 45), check_if_Ein(26, 46), check_if_Ein(26, 47), check_if_Ein(26, 48),
                      check_if_Ein(26, 49), check_if_Ein(26, 50)], ignore_index=True)
    return data


def check_E27():
    data = pd.concat([check_if_Ein(27, 0), check_if_Ein(27, 1), check_if_Ein(27, 2), check_if_Ein(27, 3),
                      check_if_Ein(27, 4), check_if_Ein(27, 5), check_if_Ein(27, 6), check_if_Ein(27, 7),
                      check_if_Ein(27, 8), check_if_Ein(27, 9), check_if_Ein(27, 10), check_if_Ein(27, 11),
                      check_if_Ein(27, 12), check_if_Ein(27, 13), check_if_Ein(27, 14), check_if_Ein(27, 15),
                      check_if_Ein(27, 16), check_if_Ein(27, 17), check_if_Ein(27, 18), check_if_Ein(27, 19),
                      check_if_Ein(27, 20), check_if_Ein(27, 21), check_if_Ein(27, 22), check_if_Ein(27, 23),
                      check_if_Ein(27, 24), check_if_Ein(27, 25), check_if_Ein(27, 26), check_if_Ein(27, 28),
                      check_if_Ein(27, 29), check_if_Ein(27, 30), check_if_Ein(27, 31), check_if_Ein(27, 32),
                      check_if_Ein(27, 33), check_if_Ein(27, 34), check_if_Ein(27, 35), check_if_Ein(27, 36),
                      check_if_Ein(27, 37), check_if_Ein(27, 38), check_if_Ein(27, 39), check_if_Ein(27, 40),
                      check_if_Ein(27, 41), check_if_Ein(27, 42), check_if_Ein(27, 43), check_if_Ein(27, 44),
                      check_if_Ein(27, 45), check_if_Ein(27, 46), check_if_Ein(27, 47), check_if_Ein(27, 48),
                      check_if_Ein(27, 49), check_if_Ein(27, 50)], ignore_index=True)
    return data


def check_E28():
    data = pd.concat([check_if_Ein(28, 0), check_if_Ein(28, 1), check_if_Ein(28, 2), check_if_Ein(28, 3),
                      check_if_Ein(28, 4), check_if_Ein(28, 5), check_if_Ein(28, 6), check_if_Ein(28, 7),
                      check_if_Ein(28, 8), check_if_Ein(28, 9), check_if_Ein(28, 10), check_if_Ein(28, 11),
                      check_if_Ein(28, 12), check_if_Ein(28, 13), check_if_Ein(28, 14), check_if_Ein(28, 15),
                      check_if_Ein(28, 16), check_if_Ein(28, 17), check_if_Ein(28, 18), check_if_Ein(28, 19),
                      check_if_Ein(28, 20), check_if_Ein(28, 21), check_if_Ein(28, 22), check_if_Ein(28, 23),
                      check_if_Ein(28, 24), check_if_Ein(28, 25), check_if_Ein(28, 26), check_if_Ein(28, 27),
                      check_if_Ein(28, 29), check_if_Ein(28, 30), check_if_Ein(28, 31), check_if_Ein(28, 32),
                      check_if_Ein(28, 33), check_if_Ein(28, 34), check_if_Ein(28, 35), check_if_Ein(28, 36),
                      check_if_Ein(28, 37), check_if_Ein(28, 38), check_if_Ein(28, 39), check_if_Ein(28, 40),
                      check_if_Ein(28, 41), check_if_Ein(28, 42), check_if_Ein(28, 43), check_if_Ein(28, 44),
                      check_if_Ein(28, 45), check_if_Ein(28, 46), check_if_Ein(28, 47), check_if_Ein(28, 48),
                      check_if_Ein(28, 49), check_if_Ein(28, 50)], ignore_index=True)
    return data


def check_E29():
    data = pd.concat([check_if_Ein(29, 0), check_if_Ein(29, 1), check_if_Ein(29, 2), check_if_Ein(29, 3),
                      check_if_Ein(29, 4), check_if_Ein(29, 5), check_if_Ein(29, 6), check_if_Ein(29, 7),
                      check_if_Ein(29, 8), check_if_Ein(29, 9), check_if_Ein(29, 10), check_if_Ein(29, 11),
                      check_if_Ein(29, 12), check_if_Ein(29, 13), check_if_Ein(29, 14), check_if_Ein(29, 15),
                      check_if_Ein(29, 16), check_if_Ein(29, 17), check_if_Ein(29, 18), check_if_Ein(29, 19),
                      check_if_Ein(29, 20), check_if_Ein(29, 21), check_if_Ein(29, 22), check_if_Ein(29, 23),
                      check_if_Ein(29, 24), check_if_Ein(29, 25), check_if_Ein(29, 26), check_if_Ein(29, 27),
                      check_if_Ein(29, 28), check_if_Ein(29, 30), check_if_Ein(29, 31), check_if_Ein(29, 32),
                      check_if_Ein(29, 33), check_if_Ein(29, 34), check_if_Ein(29, 35), check_if_Ein(29, 36),
                      check_if_Ein(29, 37), check_if_Ein(29, 38), check_if_Ein(29, 39), check_if_Ein(29, 40),
                      check_if_Ein(29, 41), check_if_Ein(29, 42), check_if_Ein(29, 43), check_if_Ein(29, 44),
                      check_if_Ein(29, 45), check_if_Ein(29, 46), check_if_Ein(29, 47), check_if_Ein(29, 48),
                      check_if_Ein(29, 49), check_if_Ein(29, 50)], ignore_index=True)
    return data


def check_E30():
    data = pd.concat([check_if_Ein(30, 0), check_if_Ein(30, 1), check_if_Ein(30, 2), check_if_Ein(30, 3),
                      check_if_Ein(30, 4), check_if_Ein(30, 5), check_if_Ein(30, 6), check_if_Ein(30, 7),
                      check_if_Ein(30, 8), check_if_Ein(30, 9), check_if_Ein(30, 10), check_if_Ein(30, 11),
                      check_if_Ein(30, 12), check_if_Ein(30, 13), check_if_Ein(30, 14), check_if_Ein(30, 15),
                      check_if_Ein(30, 16), check_if_Ein(30, 17), check_if_Ein(30, 18), check_if_Ein(30, 19),
                      check_if_Ein(30, 20), check_if_Ein(30, 21), check_if_Ein(30, 22), check_if_Ein(30, 23),
                      check_if_Ein(30, 24), check_if_Ein(30, 25), check_if_Ein(30, 26), check_if_Ein(30, 27),
                      check_if_Ein(30, 28), check_if_Ein(30, 29), check_if_Ein(30, 31), check_if_Ein(30, 32),
                      check_if_Ein(30, 33), check_if_Ein(30, 34), check_if_Ein(30, 35), check_if_Ein(30, 36),
                      check_if_Ein(30, 37), check_if_Ein(30, 38), check_if_Ein(30, 39), check_if_Ein(30, 40),
                      check_if_Ein(30, 41), check_if_Ein(30, 42), check_if_Ein(30, 43), check_if_Ein(30, 44),
                      check_if_Ein(30, 45), check_if_Ein(30, 46), check_if_Ein(30, 47), check_if_Ein(30, 48),
                      check_if_Ein(30, 49), check_if_Ein(30, 50)], ignore_index=True)
    return data


def check_E31():
    data = pd.concat([check_if_Ein(31, 0), check_if_Ein(31, 1), check_if_Ein(31, 2), check_if_Ein(31, 3),
                      check_if_Ein(31, 4), check_if_Ein(31, 5), check_if_Ein(31, 6), check_if_Ein(31, 7),
                      check_if_Ein(31, 8), check_if_Ein(31, 9), check_if_Ein(31, 10), check_if_Ein(31, 11),
                      check_if_Ein(31, 12), check_if_Ein(31, 13), check_if_Ein(31, 14), check_if_Ein(31, 15),
                      check_if_Ein(31, 16), check_if_Ein(31, 17), check_if_Ein(31, 18), check_if_Ein(31, 19),
                      check_if_Ein(31, 20), check_if_Ein(31, 21), check_if_Ein(31, 22), check_if_Ein(31, 23),
                      check_if_Ein(31, 24), check_if_Ein(31, 25), check_if_Ein(31, 26), check_if_Ein(31, 27),
                      check_if_Ein(31, 28), check_if_Ein(31, 29), check_if_Ein(31, 30), check_if_Ein(31, 32),
                      check_if_Ein(31, 33), check_if_Ein(31, 34), check_if_Ein(31, 35), check_if_Ein(31, 36),
                      check_if_Ein(31, 37), check_if_Ein(31, 38), check_if_Ein(31, 39), check_if_Ein(31, 40),
                      check_if_Ein(31, 41), check_if_Ein(31, 42), check_if_Ein(31, 43), check_if_Ein(31, 44),
                      check_if_Ein(31, 45), check_if_Ein(31, 46), check_if_Ein(31, 47), check_if_Ein(31, 48),
                      check_if_Ein(31, 49), check_if_Ein(31, 50)], ignore_index=True)
    return data


def check_E32():
    data = pd.concat([check_if_Ein(32, 0), check_if_Ein(32, 1), check_if_Ein(32, 2), check_if_Ein(32, 3),
                      check_if_Ein(32, 4), check_if_Ein(32, 5), check_if_Ein(32, 6), check_if_Ein(32, 7),
                      check_if_Ein(32, 8), check_if_Ein(32, 9), check_if_Ein(32, 10), check_if_Ein(32, 11),
                      check_if_Ein(32, 12), check_if_Ein(32, 13), check_if_Ein(32, 14), check_if_Ein(32, 15),
                      check_if_Ein(32, 16), check_if_Ein(32, 17), check_if_Ein(32, 18), check_if_Ein(32, 19),
                      check_if_Ein(32, 20), check_if_Ein(32, 21), check_if_Ein(32, 22), check_if_Ein(32, 23),
                      check_if_Ein(32, 24), check_if_Ein(32, 25), check_if_Ein(32, 26), check_if_Ein(32, 27),
                      check_if_Ein(32, 28), check_if_Ein(32, 29), check_if_Ein(32, 30), check_if_Ein(32, 31),
                      check_if_Ein(32, 33), check_if_Ein(32, 34), check_if_Ein(32, 35), check_if_Ein(32, 36),
                      check_if_Ein(32, 37), check_if_Ein(32, 38), check_if_Ein(32, 39), check_if_Ein(32, 40),
                      check_if_Ein(32, 41), check_if_Ein(32, 42), check_if_Ein(32, 43), check_if_Ein(32, 44),
                      check_if_Ein(32, 45), check_if_Ein(32, 46), check_if_Ein(32, 47), check_if_Ein(32, 48),
                      check_if_Ein(32, 49), check_if_Ein(32, 50)], ignore_index=True)
    return data


def check_E33():
    data = pd.concat([check_if_Ein(33, 0), check_if_Ein(33, 1), check_if_Ein(33, 2), check_if_Ein(33, 3),
                      check_if_Ein(33, 4), check_if_Ein(33, 5), check_if_Ein(33, 6), check_if_Ein(33, 7),
                      check_if_Ein(33, 8), check_if_Ein(33, 9), check_if_Ein(33, 10), check_if_Ein(33, 11),
                      check_if_Ein(33, 12), check_if_Ein(33, 13), check_if_Ein(33, 14), check_if_Ein(33, 15),
                      check_if_Ein(33, 16), check_if_Ein(33, 17), check_if_Ein(33, 18), check_if_Ein(33, 19),
                      check_if_Ein(33, 20), check_if_Ein(33, 21), check_if_Ein(33, 22), check_if_Ein(33, 23),
                      check_if_Ein(33, 24), check_if_Ein(33, 25), check_if_Ein(33, 26), check_if_Ein(33, 27),
                      check_if_Ein(33, 28), check_if_Ein(33, 29), check_if_Ein(33, 30), check_if_Ein(33, 31),
                      check_if_Ein(33, 32), check_if_Ein(33, 34), check_if_Ein(33, 35), check_if_Ein(33, 36),
                      check_if_Ein(33, 37), check_if_Ein(33, 38), check_if_Ein(33, 39), check_if_Ein(33, 40),
                      check_if_Ein(33, 41), check_if_Ein(33, 42), check_if_Ein(33, 43), check_if_Ein(33, 44),
                      check_if_Ein(33, 45), check_if_Ein(33, 46), check_if_Ein(33, 47), check_if_Ein(33, 48),
                      check_if_Ein(33, 49), check_if_Ein(33, 50)], ignore_index=True)
    return data


def check_E34():
    data = pd.concat([check_if_Ein(34, 0), check_if_Ein(34, 1), check_if_Ein(34, 2), check_if_Ein(34, 3),
                      check_if_Ein(34, 4), check_if_Ein(34, 5), check_if_Ein(34, 6), check_if_Ein(34, 7),
                      check_if_Ein(34, 8), check_if_Ein(34, 9), check_if_Ein(34, 10), check_if_Ein(34, 11),
                      check_if_Ein(34, 12), check_if_Ein(34, 13), check_if_Ein(34, 14), check_if_Ein(34, 15),
                      check_if_Ein(34, 16), check_if_Ein(34, 17), check_if_Ein(34, 18), check_if_Ein(34, 19),
                      check_if_Ein(34, 20), check_if_Ein(34, 21), check_if_Ein(34, 22), check_if_Ein(34, 23),
                      check_if_Ein(34, 24), check_if_Ein(34, 25), check_if_Ein(34, 26), check_if_Ein(34, 27),
                      check_if_Ein(34, 28), check_if_Ein(34, 29), check_if_Ein(34, 30), check_if_Ein(34, 31),
                      check_if_Ein(34, 32), check_if_Ein(34, 33), check_if_Ein(34, 35), check_if_Ein(34, 36),
                      check_if_Ein(34, 37), check_if_Ein(34, 38), check_if_Ein(34, 39), check_if_Ein(34, 40),
                      check_if_Ein(34, 41), check_if_Ein(34, 42), check_if_Ein(34, 43), check_if_Ein(34, 44),
                      check_if_Ein(34, 45), check_if_Ein(34, 46), check_if_Ein(34, 47), check_if_Ein(34, 48),
                      check_if_Ein(34, 49), check_if_Ein(34, 50)], ignore_index=True)
    return data


def check_E35():
    data = pd.concat([check_if_Ein(35, 0), check_if_Ein(35, 1), check_if_Ein(35, 2), check_if_Ein(35, 3),
                      check_if_Ein(35, 4), check_if_Ein(35, 5), check_if_Ein(35, 6), check_if_Ein(35, 7),
                      check_if_Ein(35, 8), check_if_Ein(35, 9), check_if_Ein(35, 10), check_if_Ein(35, 11),
                      check_if_Ein(35, 12), check_if_Ein(35, 13), check_if_Ein(35, 14), check_if_Ein(35, 15),
                      check_if_Ein(35, 16), check_if_Ein(35, 17), check_if_Ein(35, 18), check_if_Ein(35, 19),
                      check_if_Ein(35, 20), check_if_Ein(35, 21), check_if_Ein(35, 22), check_if_Ein(35, 23),
                      check_if_Ein(35, 24), check_if_Ein(35, 25), check_if_Ein(35, 26), check_if_Ein(35, 27),
                      check_if_Ein(35, 28), check_if_Ein(35, 29), check_if_Ein(35, 30), check_if_Ein(35, 31),
                      check_if_Ein(35, 32), check_if_Ein(35, 33), check_if_Ein(35, 34), check_if_Ein(35, 36),
                      check_if_Ein(35, 37), check_if_Ein(35, 38), check_if_Ein(35, 39), check_if_Ein(35, 40),
                      check_if_Ein(35, 41), check_if_Ein(35, 42), check_if_Ein(35, 43), check_if_Ein(35, 44),
                      check_if_Ein(35, 45), check_if_Ein(35, 46), check_if_Ein(35, 47), check_if_Ein(35, 48),
                      check_if_Ein(35, 49), check_if_Ein(35, 50)], ignore_index=True)
    return data


def check_E36():
    data = pd.concat([check_if_Ein(36, 0), check_if_Ein(36, 1), check_if_Ein(36, 2), check_if_Ein(36, 3),
                      check_if_Ein(36, 4), check_if_Ein(36, 5), check_if_Ein(36, 6), check_if_Ein(36, 7),
                      check_if_Ein(36, 8), check_if_Ein(36, 9), check_if_Ein(36, 10), check_if_Ein(36, 11),
                      check_if_Ein(36, 12), check_if_Ein(36, 13), check_if_Ein(36, 14), check_if_Ein(36, 15),
                      check_if_Ein(36, 16), check_if_Ein(36, 17), check_if_Ein(36, 18), check_if_Ein(36, 19),
                      check_if_Ein(36, 20), check_if_Ein(36, 21), check_if_Ein(36, 22), check_if_Ein(36, 23),
                      check_if_Ein(36, 24), check_if_Ein(36, 25), check_if_Ein(36, 26), check_if_Ein(36, 27),
                      check_if_Ein(36, 28), check_if_Ein(36, 29), check_if_Ein(36, 30), check_if_Ein(36, 31),
                      check_if_Ein(36, 32), check_if_Ein(36, 33), check_if_Ein(36, 34), check_if_Ein(36, 35),
                      check_if_Ein(36, 37), check_if_Ein(36, 38), check_if_Ein(36, 39), check_if_Ein(36, 40),
                      check_if_Ein(36, 41), check_if_Ein(36, 42), check_if_Ein(36, 43), check_if_Ein(36, 44),
                      check_if_Ein(36, 45), check_if_Ein(36, 46), check_if_Ein(36, 47), check_if_Ein(36, 48),
                      check_if_Ein(36, 49), check_if_Ein(36, 50)], ignore_index=True)
    return data


def check_E37():
    data = pd.concat([check_if_Ein(37, 0), check_if_Ein(37, 1), check_if_Ein(37, 2), check_if_Ein(37, 3),
                      check_if_Ein(37, 4), check_if_Ein(37, 5), check_if_Ein(37, 6), check_if_Ein(37, 7),
                      check_if_Ein(37, 8), check_if_Ein(37, 9), check_if_Ein(37, 10), check_if_Ein(37, 11),
                      check_if_Ein(37, 12), check_if_Ein(37, 13), check_if_Ein(37, 14), check_if_Ein(37, 15),
                      check_if_Ein(37, 16), check_if_Ein(37, 17), check_if_Ein(37, 18), check_if_Ein(37, 19),
                      check_if_Ein(37, 20), check_if_Ein(37, 21), check_if_Ein(37, 22), check_if_Ein(37, 23),
                      check_if_Ein(37, 24), check_if_Ein(37, 25), check_if_Ein(37, 26), check_if_Ein(37, 27),
                      check_if_Ein(37, 28), check_if_Ein(37, 29), check_if_Ein(37, 30), check_if_Ein(37, 31),
                      check_if_Ein(37, 32), check_if_Ein(37, 33), check_if_Ein(37, 34), check_if_Ein(37, 35),
                      check_if_Ein(37, 36), check_if_Ein(37, 38), check_if_Ein(37, 39), check_if_Ein(37, 40),
                      check_if_Ein(37, 41), check_if_Ein(37, 42), check_if_Ein(37, 43), check_if_Ein(37, 44),
                      check_if_Ein(37, 45), check_if_Ein(37, 46), check_if_Ein(37, 47), check_if_Ein(37, 48),
                      check_if_Ein(37, 49), check_if_Ein(37, 50)], ignore_index=True)
    return data


def check_E38():
    data = pd.concat([check_if_Ein(38, 0), check_if_Ein(38, 1), check_if_Ein(38, 2), check_if_Ein(38, 3),
                      check_if_Ein(38, 4), check_if_Ein(38, 5), check_if_Ein(38, 6), check_if_Ein(38, 7),
                      check_if_Ein(38, 8), check_if_Ein(38, 9), check_if_Ein(38, 10), check_if_Ein(38, 11),
                      check_if_Ein(38, 12), check_if_Ein(38, 13), check_if_Ein(38, 14), check_if_Ein(38, 15),
                      check_if_Ein(38, 16), check_if_Ein(38, 17), check_if_Ein(38, 18), check_if_Ein(38, 19),
                      check_if_Ein(38, 20), check_if_Ein(38, 21), check_if_Ein(38, 22), check_if_Ein(38, 23),
                      check_if_Ein(38, 24), check_if_Ein(38, 25), check_if_Ein(38, 26), check_if_Ein(38, 27),
                      check_if_Ein(38, 28), check_if_Ein(38, 29), check_if_Ein(38, 30), check_if_Ein(38, 31),
                      check_if_Ein(38, 32), check_if_Ein(38, 33), check_if_Ein(38, 34), check_if_Ein(38, 35),
                      check_if_Ein(38, 36), check_if_Ein(38, 37), check_if_Ein(38, 39), check_if_Ein(38, 40),
                      check_if_Ein(38, 41), check_if_Ein(38, 42), check_if_Ein(38, 43), check_if_Ein(38, 44),
                      check_if_Ein(38, 45), check_if_Ein(38, 46), check_if_Ein(38, 47), check_if_Ein(38, 48),
                      check_if_Ein(38, 49), check_if_Ein(38, 50)], ignore_index=True)
    return data


def check_E39():
    data = pd.concat([check_if_Ein(39, 0), check_if_Ein(39, 1), check_if_Ein(39, 2), check_if_Ein(39, 3),
                      check_if_Ein(39, 4), check_if_Ein(39, 5), check_if_Ein(39, 6), check_if_Ein(39, 7),
                      check_if_Ein(39, 8), check_if_Ein(39, 9), check_if_Ein(39, 10), check_if_Ein(39, 11),
                      check_if_Ein(39, 12), check_if_Ein(39, 13), check_if_Ein(39, 14), check_if_Ein(39, 15),
                      check_if_Ein(39, 16), check_if_Ein(39, 17), check_if_Ein(39, 18), check_if_Ein(39, 19),
                      check_if_Ein(39, 20), check_if_Ein(39, 21), check_if_Ein(39, 22), check_if_Ein(39, 23),
                      check_if_Ein(39, 24), check_if_Ein(39, 25), check_if_Ein(39, 26), check_if_Ein(39, 27),
                      check_if_Ein(39, 28), check_if_Ein(39, 29), check_if_Ein(39, 30), check_if_Ein(39, 31),
                      check_if_Ein(39, 32), check_if_Ein(39, 33), check_if_Ein(39, 34), check_if_Ein(39, 35),
                      check_if_Ein(39, 36), check_if_Ein(39, 37), check_if_Ein(39, 38), check_if_Ein(39, 40),
                      check_if_Ein(39, 41), check_if_Ein(39, 42), check_if_Ein(39, 43), check_if_Ein(39, 44),
                      check_if_Ein(39, 45), check_if_Ein(39, 46), check_if_Ein(39, 47), check_if_Ein(39, 48),
                      check_if_Ein(39, 49), check_if_Ein(39, 50)], ignore_index=True)
    return data


def check_E40():
    data = pd.concat([check_if_Ein(40, 0), check_if_Ein(40, 1), check_if_Ein(40, 2), check_if_Ein(40, 3),
                      check_if_Ein(40, 4), check_if_Ein(40, 5), check_if_Ein(40, 6), check_if_Ein(40, 7),
                      check_if_Ein(40, 8), check_if_Ein(40, 9), check_if_Ein(40, 10), check_if_Ein(40, 11),
                      check_if_Ein(40, 12), check_if_Ein(40, 13), check_if_Ein(40, 14), check_if_Ein(40, 15),
                      check_if_Ein(40, 16), check_if_Ein(40, 17), check_if_Ein(40, 18), check_if_Ein(40, 19),
                      check_if_Ein(40, 20), check_if_Ein(40, 21), check_if_Ein(40, 22), check_if_Ein(40, 23),
                      check_if_Ein(40, 24), check_if_Ein(40, 25), check_if_Ein(40, 26), check_if_Ein(40, 27),
                      check_if_Ein(40, 28), check_if_Ein(40, 29), check_if_Ein(40, 30), check_if_Ein(40, 31),
                      check_if_Ein(40, 32), check_if_Ein(40, 33), check_if_Ein(40, 34), check_if_Ein(40, 35),
                      check_if_Ein(40, 36), check_if_Ein(40, 37), check_if_Ein(40, 38), check_if_Ein(40, 39),
                      check_if_Ein(40, 41), check_if_Ein(40, 42), check_if_Ein(40, 43), check_if_Ein(40, 44),
                      check_if_Ein(40, 45), check_if_Ein(40, 46), check_if_Ein(40, 47), check_if_Ein(40, 48),
                      check_if_Ein(40, 49), check_if_Ein(40, 50)], ignore_index=True)
    return data


def check_E41():
    data = pd.concat([check_if_Ein(41, 0), check_if_Ein(41, 1), check_if_Ein(41, 2), check_if_Ein(41, 3),
                      check_if_Ein(41, 4), check_if_Ein(41, 5), check_if_Ein(41, 6), check_if_Ein(41, 7),
                      check_if_Ein(41, 8), check_if_Ein(41, 9), check_if_Ein(41, 10), check_if_Ein(41, 11),
                      check_if_Ein(41, 12), check_if_Ein(41, 13), check_if_Ein(41, 14), check_if_Ein(41, 15),
                      check_if_Ein(41, 16), check_if_Ein(41, 17), check_if_Ein(41, 18), check_if_Ein(41, 19),
                      check_if_Ein(41, 20), check_if_Ein(41, 21), check_if_Ein(41, 22), check_if_Ein(41, 23),
                      check_if_Ein(41, 24), check_if_Ein(41, 25), check_if_Ein(41, 26), check_if_Ein(41, 27),
                      check_if_Ein(41, 28), check_if_Ein(41, 29), check_if_Ein(41, 30), check_if_Ein(41, 31),
                      check_if_Ein(41, 32), check_if_Ein(41, 33), check_if_Ein(41, 34), check_if_Ein(41, 35),
                      check_if_Ein(41, 36), check_if_Ein(41, 37), check_if_Ein(41, 38), check_if_Ein(41, 39),
                      check_if_Ein(41, 40), check_if_Ein(41, 42), check_if_Ein(41, 43), check_if_Ein(41, 44),
                      check_if_Ein(41, 45), check_if_Ein(41, 46), check_if_Ein(41, 47), check_if_Ein(41, 48),
                      check_if_Ein(41, 49), check_if_Ein(41, 50)], ignore_index=True)
    return data


def check_E42():
    data = pd.concat([check_if_Ein(42, 0), check_if_Ein(42, 1), check_if_Ein(42, 2), check_if_Ein(42, 3),
                      check_if_Ein(42, 4), check_if_Ein(42, 5), check_if_Ein(42, 6), check_if_Ein(42, 7),
                      check_if_Ein(42, 8), check_if_Ein(42, 9), check_if_Ein(42, 10), check_if_Ein(42, 11),
                      check_if_Ein(42, 12), check_if_Ein(42, 13), check_if_Ein(42, 14), check_if_Ein(42, 15),
                      check_if_Ein(42, 16), check_if_Ein(42, 17), check_if_Ein(42, 18), check_if_Ein(42, 19),
                      check_if_Ein(42, 20), check_if_Ein(42, 21), check_if_Ein(42, 22), check_if_Ein(42, 23),
                      check_if_Ein(42, 24), check_if_Ein(42, 25), check_if_Ein(42, 26), check_if_Ein(42, 27),
                      check_if_Ein(42, 28), check_if_Ein(42, 29), check_if_Ein(42, 30), check_if_Ein(42, 31),
                      check_if_Ein(42, 32), check_if_Ein(42, 33), check_if_Ein(42, 34), check_if_Ein(42, 35),
                      check_if_Ein(42, 36), check_if_Ein(42, 37), check_if_Ein(42, 38), check_if_Ein(42, 39),
                      check_if_Ein(42, 40), check_if_Ein(42, 41), check_if_Ein(42, 43), check_if_Ein(42, 44),
                      check_if_Ein(42, 45), check_if_Ein(42, 46), check_if_Ein(42, 47), check_if_Ein(42, 48),
                      check_if_Ein(42, 49), check_if_Ein(42, 50)], ignore_index=True)
    return data


def check_E43():
    data = pd.concat([check_if_Ein(43, 0), check_if_Ein(43, 1), check_if_Ein(43, 2), check_if_Ein(43, 3),
                      check_if_Ein(43, 4), check_if_Ein(43, 5), check_if_Ein(43, 6), check_if_Ein(43, 7),
                      check_if_Ein(43, 8), check_if_Ein(43, 9), check_if_Ein(43, 10), check_if_Ein(43, 11),
                      check_if_Ein(43, 12), check_if_Ein(43, 13), check_if_Ein(43, 14), check_if_Ein(43, 15),
                      check_if_Ein(43, 16), check_if_Ein(43, 17), check_if_Ein(43, 18), check_if_Ein(43, 19),
                      check_if_Ein(43, 20), check_if_Ein(43, 21), check_if_Ein(43, 22), check_if_Ein(43, 23),
                      check_if_Ein(43, 24), check_if_Ein(43, 25), check_if_Ein(43, 26), check_if_Ein(43, 27),
                      check_if_Ein(43, 28), check_if_Ein(43, 29), check_if_Ein(43, 30), check_if_Ein(43, 31),
                      check_if_Ein(43, 32), check_if_Ein(43, 33), check_if_Ein(43, 34), check_if_Ein(43, 35),
                      check_if_Ein(43, 36), check_if_Ein(43, 37), check_if_Ein(43, 38), check_if_Ein(43, 39),
                      check_if_Ein(43, 40), check_if_Ein(43, 41), check_if_Ein(43, 42), check_if_Ein(43, 44),
                      check_if_Ein(43, 45), check_if_Ein(43, 46), check_if_Ein(43, 47), check_if_Ein(43, 48),
                      check_if_Ein(43, 49), check_if_Ein(43, 50)], ignore_index=True)
    return data


def check_E44():
    data = pd.concat([check_if_Ein(44, 0), check_if_Ein(44, 1), check_if_Ein(44, 2), check_if_Ein(44, 3),
                      check_if_Ein(44, 4), check_if_Ein(44, 5), check_if_Ein(44, 6), check_if_Ein(44, 7),
                      check_if_Ein(44, 8), check_if_Ein(44, 9), check_if_Ein(44, 10), check_if_Ein(44, 11),
                      check_if_Ein(44, 12), check_if_Ein(44, 13), check_if_Ein(44, 14), check_if_Ein(44, 15),
                      check_if_Ein(44, 16), check_if_Ein(44, 17), check_if_Ein(44, 18), check_if_Ein(44, 19),
                      check_if_Ein(44, 20), check_if_Ein(44, 21), check_if_Ein(44, 22), check_if_Ein(44, 23),
                      check_if_Ein(44, 24), check_if_Ein(44, 25), check_if_Ein(44, 26), check_if_Ein(44, 27),
                      check_if_Ein(44, 28), check_if_Ein(44, 29), check_if_Ein(44, 30), check_if_Ein(44, 31),
                      check_if_Ein(44, 32), check_if_Ein(44, 33), check_if_Ein(44, 34), check_if_Ein(44, 35),
                      check_if_Ein(44, 36), check_if_Ein(44, 37), check_if_Ein(44, 38), check_if_Ein(44, 39),
                      check_if_Ein(44, 40), check_if_Ein(44, 41), check_if_Ein(44, 42), check_if_Ein(44, 43),
                      check_if_Ein(44, 45), check_if_Ein(44, 46), check_if_Ein(44, 47), check_if_Ein(44, 48),
                      check_if_Ein(44, 49), check_if_Ein(44, 50)], ignore_index=True)
    return data


def check_E45():
    data = pd.concat([check_if_Ein(45, 0), check_if_Ein(45, 1), check_if_Ein(45, 2), check_if_Ein(45, 3),
                      check_if_Ein(45, 4), check_if_Ein(45, 5), check_if_Ein(45, 6), check_if_Ein(45, 7),
                      check_if_Ein(45, 8), check_if_Ein(45, 9), check_if_Ein(45, 10), check_if_Ein(45, 11),
                      check_if_Ein(45, 12), check_if_Ein(45, 13), check_if_Ein(45, 14), check_if_Ein(45, 15),
                      check_if_Ein(45, 16), check_if_Ein(45, 17), check_if_Ein(45, 18), check_if_Ein(45, 19),
                      check_if_Ein(45, 20), check_if_Ein(45, 21), check_if_Ein(45, 22), check_if_Ein(45, 23),
                      check_if_Ein(45, 24), check_if_Ein(45, 25), check_if_Ein(45, 26), check_if_Ein(45, 27),
                      check_if_Ein(45, 28), check_if_Ein(45, 29), check_if_Ein(45, 30), check_if_Ein(45, 31),
                      check_if_Ein(45, 32), check_if_Ein(45, 33), check_if_Ein(45, 34), check_if_Ein(45, 35),
                      check_if_Ein(45, 36), check_if_Ein(45, 37), check_if_Ein(45, 38), check_if_Ein(45, 39),
                      check_if_Ein(45, 40), check_if_Ein(45, 41), check_if_Ein(45, 42), check_if_Ein(45, 43),
                      check_if_Ein(45, 44), check_if_Ein(45, 46), check_if_Ein(45, 47), check_if_Ein(45, 48),
                      check_if_Ein(45, 49), check_if_Ein(45, 50)], ignore_index=True)
    return data


def check_E46():
    data = pd.concat([check_if_Ein(46, 0), check_if_Ein(46, 1), check_if_Ein(46, 2), check_if_Ein(46, 3),
                      check_if_Ein(46, 4), check_if_Ein(46, 5), check_if_Ein(46, 6), check_if_Ein(46, 7),
                      check_if_Ein(46, 8), check_if_Ein(46, 9), check_if_Ein(46, 10), check_if_Ein(46, 11),
                      check_if_Ein(46, 12), check_if_Ein(46, 13), check_if_Ein(46, 14), check_if_Ein(46, 15),
                      check_if_Ein(46, 16), check_if_Ein(46, 17), check_if_Ein(46, 18), check_if_Ein(46, 19),
                      check_if_Ein(46, 20), check_if_Ein(46, 21), check_if_Ein(46, 22), check_if_Ein(46, 23),
                      check_if_Ein(46, 24), check_if_Ein(46, 25), check_if_Ein(46, 26), check_if_Ein(46, 27),
                      check_if_Ein(46, 28), check_if_Ein(46, 29), check_if_Ein(46, 30), check_if_Ein(46, 31),
                      check_if_Ein(46, 32), check_if_Ein(46, 33), check_if_Ein(46, 34), check_if_Ein(46, 35),
                      check_if_Ein(46, 36), check_if_Ein(46, 37), check_if_Ein(46, 38), check_if_Ein(46, 39),
                      check_if_Ein(46, 40), check_if_Ein(46, 41), check_if_Ein(46, 42), check_if_Ein(46, 43),
                      check_if_Ein(46, 44), check_if_Ein(46, 45), check_if_Ein(46, 47), check_if_Ein(46, 48),
                      check_if_Ein(46, 49), check_if_Ein(46, 50)], ignore_index=True)
    return data


def check_E47():
    data = pd.concat([check_if_Ein(47, 0), check_if_Ein(47, 1), check_if_Ein(47, 2), check_if_Ein(47, 3),
                      check_if_Ein(47, 4), check_if_Ein(47, 5), check_if_Ein(47, 6), check_if_Ein(47, 7),
                      check_if_Ein(47, 8), check_if_Ein(47, 9), check_if_Ein(47, 10), check_if_Ein(47, 11),
                      check_if_Ein(47, 12), check_if_Ein(47, 13), check_if_Ein(47, 14), check_if_Ein(47, 15),
                      check_if_Ein(47, 16), check_if_Ein(47, 17), check_if_Ein(47, 18), check_if_Ein(47, 19),
                      check_if_Ein(47, 20), check_if_Ein(47, 21), check_if_Ein(47, 22), check_if_Ein(47, 23),
                      check_if_Ein(47, 24), check_if_Ein(47, 25), check_if_Ein(47, 26), check_if_Ein(47, 27),
                      check_if_Ein(47, 28), check_if_Ein(47, 29), check_if_Ein(47, 30), check_if_Ein(47, 31),
                      check_if_Ein(47, 32), check_if_Ein(47, 33), check_if_Ein(47, 34), check_if_Ein(47, 35),
                      check_if_Ein(47, 36), check_if_Ein(47, 37), check_if_Ein(47, 38), check_if_Ein(47, 39),
                      check_if_Ein(47, 40), check_if_Ein(47, 41), check_if_Ein(47, 42), check_if_Ein(47, 43),
                      check_if_Ein(47, 44), check_if_Ein(47, 45), check_if_Ein(47, 46), check_if_Ein(47, 48),
                      check_if_Ein(47, 49), check_if_Ein(47, 50)], ignore_index=True)
    return data


def check_E48():
    data = pd.concat([check_if_Ein(48, 0), check_if_Ein(48, 1), check_if_Ein(48, 2), check_if_Ein(48, 3),
                      check_if_Ein(48, 4), check_if_Ein(48, 5), check_if_Ein(48, 6), check_if_Ein(48, 7),
                      check_if_Ein(48, 8), check_if_Ein(48, 9), check_if_Ein(48, 10), check_if_Ein(48, 11),
                      check_if_Ein(48, 12), check_if_Ein(48, 13), check_if_Ein(48, 14), check_if_Ein(48, 15),
                      check_if_Ein(48, 16), check_if_Ein(48, 17), check_if_Ein(48, 18), check_if_Ein(48, 19),
                      check_if_Ein(48, 20), check_if_Ein(48, 21), check_if_Ein(48, 22), check_if_Ein(48, 23),
                      check_if_Ein(48, 24), check_if_Ein(48, 25), check_if_Ein(48, 26), check_if_Ein(48, 27),
                      check_if_Ein(48, 28), check_if_Ein(48, 29), check_if_Ein(48, 30), check_if_Ein(48, 31),
                      check_if_Ein(48, 32), check_if_Ein(48, 33), check_if_Ein(48, 34), check_if_Ein(48, 35),
                      check_if_Ein(48, 36), check_if_Ein(48, 37), check_if_Ein(48, 38), check_if_Ein(48, 39),
                      check_if_Ein(48, 40), check_if_Ein(48, 41), check_if_Ein(48, 42), check_if_Ein(48, 43),
                      check_if_Ein(48, 44), check_if_Ein(48, 45), check_if_Ein(48, 46), check_if_Ein(48, 47),
                      check_if_Ein(48, 49), check_if_Ein(48, 50)], ignore_index=True)
    return data


def check_E49():
    data = pd.concat([check_if_Ein(49, 0), check_if_Ein(49, 1), check_if_Ein(49, 2), check_if_Ein(49, 3),
                      check_if_Ein(49, 4), check_if_Ein(49, 5), check_if_Ein(49, 6), check_if_Ein(49, 7),
                      check_if_Ein(49, 8), check_if_Ein(49, 9), check_if_Ein(49, 10), check_if_Ein(49, 11),
                      check_if_Ein(49, 12), check_if_Ein(49, 13), check_if_Ein(49, 14), check_if_Ein(49, 15),
                      check_if_Ein(49, 16), check_if_Ein(49, 17), check_if_Ein(49, 18), check_if_Ein(49, 19),
                      check_if_Ein(49, 20), check_if_Ein(49, 21), check_if_Ein(49, 22), check_if_Ein(49, 23),
                      check_if_Ein(49, 24), check_if_Ein(49, 25), check_if_Ein(49, 26), check_if_Ein(49, 27),
                      check_if_Ein(49, 28), check_if_Ein(49, 29), check_if_Ein(49, 30), check_if_Ein(49, 31),
                      check_if_Ein(49, 32), check_if_Ein(49, 33), check_if_Ein(49, 34), check_if_Ein(49, 35),
                      check_if_Ein(49, 36), check_if_Ein(49, 37), check_if_Ein(49, 38), check_if_Ein(49, 39),
                      check_if_Ein(49, 40), check_if_Ein(49, 41), check_if_Ein(49, 42), check_if_Ein(49, 43),
                      check_if_Ein(49, 44), check_if_Ein(49, 45), check_if_Ein(49, 46), check_if_Ein(49, 47),
                      check_if_Ein(49, 48), check_if_Ein(49, 50)], ignore_index=True)
    return data


def check_E50():
    data = pd.concat([check_if_Ein(50, 0), check_if_Ein(50, 1), check_if_Ein(50, 2), check_if_Ein(50, 3),
                      check_if_Ein(50, 4), check_if_Ein(50, 5), check_if_Ein(50, 6), check_if_Ein(50, 7),
                      check_if_Ein(50, 8), check_if_Ein(50, 9), check_if_Ein(50, 10), check_if_Ein(50, 11),
                      check_if_Ein(50, 12), check_if_Ein(50, 13), check_if_Ein(50, 14), check_if_Ein(50, 15),
                      check_if_Ein(50, 16), check_if_Ein(50, 17), check_if_Ein(50, 18), check_if_Ein(50, 19),
                      check_if_Ein(50, 20), check_if_Ein(50, 21), check_if_Ein(50, 22), check_if_Ein(50, 23),
                      check_if_Ein(50, 24), check_if_Ein(50, 25), check_if_Ein(50, 26), check_if_Ein(50, 27),
                      check_if_Ein(50, 28), check_if_Ein(50, 29), check_if_Ein(50, 30), check_if_Ein(50, 31),
                      check_if_Ein(50, 32), check_if_Ein(50, 33), check_if_Ein(50, 34), check_if_Ein(50, 35),
                      check_if_Ein(50, 36), check_if_Ein(50, 37), check_if_Ein(50, 38), check_if_Ein(50, 39),
                      check_if_Ein(50, 40), check_if_Ein(50, 41), check_if_Ein(50, 42), check_if_Ein(50, 43),
                      check_if_Ein(50, 44), check_if_Ein(50, 45), check_if_Ein(50, 46), check_if_Ein(50, 47),
                      check_if_Ein(50, 48), check_if_Ein(50, 49)], ignore_index=True)
    return data


def check():
    data = pd.concat([check_E1(), check_E2(), check_E3(), check_E4(),
                      check_E5(), check_E6(), check_E7(), check_E8(),
                      check_E9(), check_E10(), check_E11(), check_E12(),
                      check_E13(), check_E14(), check_E15(), check_E16(),
                      check_E17(), check_E18(), check_E19(), check_E20(),
                      check_E21(), check_E22(), check_E23(), check_E24(),
                      check_E25(), check_E26(), check_E27(), check_E28(),
                      check_E29(), check_E30(), check_E31(), check_E32(),
                      check_E33(), check_E34(), check_E35(), check_E36(),
                      check_E37(), check_E38(), check_E39(), check_E40(),
                      check_E41(), check_E42(), check_E43(), check_E44(),
                      check_E45(), check_E46(), check_E47(), check_E48(),
                      check_E49(), check_E50()], ignore_index=True)
    return data


def check_E_csv():
    data = check()
    string1 = "/Pycharm/HumanActivityRecognition/check"
    string2 = string1 + "/check_E" + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


check_E_csv()
