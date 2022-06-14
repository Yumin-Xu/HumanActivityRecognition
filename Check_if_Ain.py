import os

import numpy as np
import pandas as pd

from CreateWord import create_word


def check_if_Ain(x, y):
    d = create_word(x, 'A')['words']
    word_to_keep = np.array(create_word(y, 'A')['words'])
    df = pd.DataFrame(np.array(d[d.isin(word_to_keep)]), columns=['words'])
    return df


def check_A0():
    data = pd.concat([check_if_Ain(0, 1), check_if_Ain(0, 2), check_if_Ain(0, 3), check_if_Ain(0, 4),
                      check_if_Ain(0, 5), check_if_Ain(0, 6), check_if_Ain(0, 7), check_if_Ain(0, 8),
                      check_if_Ain(0, 9), check_if_Ain(0, 10), check_if_Ain(0, 11), check_if_Ain(0, 12),
                      check_if_Ain(0, 13), check_if_Ain(0, 14), check_if_Ain(0, 15), check_if_Ain(0, 16),
                      check_if_Ain(0, 17), check_if_Ain(0, 18), check_if_Ain(0, 19), check_if_Ain(0, 20),
                      check_if_Ain(0, 21), check_if_Ain(0, 22), check_if_Ain(0, 23), check_if_Ain(0, 24),
                      check_if_Ain(0, 25), check_if_Ain(0, 26), check_if_Ain(0, 27), check_if_Ain(0, 28),
                      check_if_Ain(0, 29), check_if_Ain(0, 30), check_if_Ain(0, 31), check_if_Ain(0, 32),
                      check_if_Ain(0, 33), check_if_Ain(0, 34), check_if_Ain(0, 35), check_if_Ain(0, 36),
                      check_if_Ain(0, 37), check_if_Ain(0, 38), check_if_Ain(0, 39), check_if_Ain(0, 40),
                      check_if_Ain(0, 41), check_if_Ain(0, 42), check_if_Ain(0, 43), check_if_Ain(0, 44),
                      check_if_Ain(0, 45), check_if_Ain(0, 46), check_if_Ain(0, 47), check_if_Ain(0, 48),
                      check_if_Ain(0, 49), check_if_Ain(0, 50)], ignore_index=True)
    return data


def check_A1():
    data = pd.concat([check_if_Ain(1, 0), check_if_Ain(1, 2), check_if_Ain(1, 3), check_if_Ain(1, 4),
                      check_if_Ain(1, 5), check_if_Ain(1, 6), check_if_Ain(1, 7), check_if_Ain(1, 8),
                      check_if_Ain(1, 9), check_if_Ain(1, 10), check_if_Ain(1, 11), check_if_Ain(1, 12),
                      check_if_Ain(1, 13), check_if_Ain(1, 14), check_if_Ain(1, 15), check_if_Ain(1, 16),
                      check_if_Ain(1, 17), check_if_Ain(1, 18), check_if_Ain(1, 19), check_if_Ain(1, 20),
                      check_if_Ain(1, 21), check_if_Ain(1, 22), check_if_Ain(1, 23), check_if_Ain(1, 24),
                      check_if_Ain(1, 25), check_if_Ain(1, 26), check_if_Ain(1, 27), check_if_Ain(1, 28),
                      check_if_Ain(1, 29), check_if_Ain(1, 30), check_if_Ain(1, 31), check_if_Ain(1, 32),
                      check_if_Ain(1, 33), check_if_Ain(1, 34), check_if_Ain(1, 35), check_if_Ain(1, 36),
                      check_if_Ain(1, 37), check_if_Ain(1, 38), check_if_Ain(1, 39), check_if_Ain(1, 40),
                      check_if_Ain(1, 41), check_if_Ain(1, 42), check_if_Ain(1, 43), check_if_Ain(1, 44),
                      check_if_Ain(1, 45), check_if_Ain(1, 46), check_if_Ain(1, 47), check_if_Ain(1, 48),
                      check_if_Ain(1, 49), check_if_Ain(1, 50)], ignore_index=True)
    return data


def check_A2():
    data = pd.concat([check_if_Ain(2, 0), check_if_Ain(2, 1), check_if_Ain(2, 3), check_if_Ain(2, 4),
                      check_if_Ain(2, 5), check_if_Ain(2, 6), check_if_Ain(2, 7), check_if_Ain(2, 8),
                      check_if_Ain(2, 9), check_if_Ain(2, 10), check_if_Ain(2, 11), check_if_Ain(2, 12),
                      check_if_Ain(2, 13), check_if_Ain(2, 14), check_if_Ain(2, 15), check_if_Ain(2, 16),
                      check_if_Ain(2, 17), check_if_Ain(2, 18), check_if_Ain(2, 19), check_if_Ain(2, 20),
                      check_if_Ain(2, 21), check_if_Ain(2, 22), check_if_Ain(2, 23), check_if_Ain(2, 24),
                      check_if_Ain(2, 25), check_if_Ain(2, 26), check_if_Ain(2, 27), check_if_Ain(2, 28),
                      check_if_Ain(2, 29), check_if_Ain(2, 30), check_if_Ain(2, 31), check_if_Ain(2, 32),
                      check_if_Ain(2, 33), check_if_Ain(2, 34), check_if_Ain(2, 35), check_if_Ain(2, 36),
                      check_if_Ain(2, 37), check_if_Ain(2, 38), check_if_Ain(2, 39), check_if_Ain(2, 40),
                      check_if_Ain(2, 41), check_if_Ain(2, 42), check_if_Ain(2, 43), check_if_Ain(2, 44),
                      check_if_Ain(2, 45), check_if_Ain(2, 46), check_if_Ain(2, 47), check_if_Ain(2, 48),
                      check_if_Ain(2, 49), check_if_Ain(2, 50)], ignore_index=True)
    return data


def check_A3():
    data = pd.concat([check_if_Ain(3, 0), check_if_Ain(3, 1), check_if_Ain(3, 2), check_if_Ain(3, 4),
                      check_if_Ain(3, 5), check_if_Ain(3, 6), check_if_Ain(3, 7), check_if_Ain(3, 8),
                      check_if_Ain(3, 9), check_if_Ain(3, 10), check_if_Ain(3, 11), check_if_Ain(3, 12),
                      check_if_Ain(3, 13), check_if_Ain(3, 14), check_if_Ain(3, 15), check_if_Ain(3, 16),
                      check_if_Ain(3, 17), check_if_Ain(3, 18), check_if_Ain(3, 19), check_if_Ain(3, 20),
                      check_if_Ain(3, 21), check_if_Ain(3, 22), check_if_Ain(3, 23), check_if_Ain(3, 24),
                      check_if_Ain(3, 25), check_if_Ain(3, 26), check_if_Ain(3, 27), check_if_Ain(3, 28),
                      check_if_Ain(3, 29), check_if_Ain(3, 30), check_if_Ain(3, 31), check_if_Ain(3, 32),
                      check_if_Ain(3, 33), check_if_Ain(3, 34), check_if_Ain(3, 35), check_if_Ain(3, 36),
                      check_if_Ain(3, 37), check_if_Ain(3, 38), check_if_Ain(3, 39), check_if_Ain(3, 40),
                      check_if_Ain(3, 41), check_if_Ain(3, 42), check_if_Ain(3, 43), check_if_Ain(3, 44),
                      check_if_Ain(3, 45), check_if_Ain(3, 46), check_if_Ain(3, 47), check_if_Ain(3, 48),
                      check_if_Ain(3, 49), check_if_Ain(3, 50)], ignore_index=True)
    return data


def check_A4():
    data = pd.concat([check_if_Ain(4, 0), check_if_Ain(4, 1), check_if_Ain(4, 2), check_if_Ain(4, 3),
                      check_if_Ain(4, 5), check_if_Ain(4, 6), check_if_Ain(4, 7), check_if_Ain(4, 8),
                      check_if_Ain(4, 9), check_if_Ain(4, 10), check_if_Ain(4, 11), check_if_Ain(4, 12),
                      check_if_Ain(4, 13), check_if_Ain(4, 14), check_if_Ain(4, 15), check_if_Ain(4, 16),
                      check_if_Ain(4, 17), check_if_Ain(4, 18), check_if_Ain(4, 19), check_if_Ain(4, 20),
                      check_if_Ain(4, 21), check_if_Ain(4, 22), check_if_Ain(4, 23), check_if_Ain(4, 24),
                      check_if_Ain(4, 25), check_if_Ain(4, 26), check_if_Ain(4, 27), check_if_Ain(4, 28),
                      check_if_Ain(4, 29), check_if_Ain(4, 30), check_if_Ain(4, 31), check_if_Ain(4, 32),
                      check_if_Ain(4, 33), check_if_Ain(4, 34), check_if_Ain(4, 35), check_if_Ain(4, 36),
                      check_if_Ain(4, 37), check_if_Ain(4, 38), check_if_Ain(4, 39), check_if_Ain(4, 40),
                      check_if_Ain(4, 41), check_if_Ain(4, 42), check_if_Ain(4, 43), check_if_Ain(4, 44),
                      check_if_Ain(4, 45), check_if_Ain(4, 46), check_if_Ain(4, 47), check_if_Ain(4, 48),
                      check_if_Ain(4, 49), check_if_Ain(4, 50)], ignore_index=True)
    return data


def check_A5():
    data = pd.concat([check_if_Ain(5, 0), check_if_Ain(5, 1), check_if_Ain(5, 2), check_if_Ain(5, 3),
                      check_if_Ain(5, 4), check_if_Ain(5, 6), check_if_Ain(5, 7), check_if_Ain(5, 8),
                      check_if_Ain(5, 9), check_if_Ain(5, 10), check_if_Ain(5, 11), check_if_Ain(5, 12),
                      check_if_Ain(5, 13), check_if_Ain(5, 14), check_if_Ain(5, 15), check_if_Ain(5, 16),
                      check_if_Ain(5, 17), check_if_Ain(5, 18), check_if_Ain(5, 19), check_if_Ain(5, 20),
                      check_if_Ain(5, 21), check_if_Ain(5, 22), check_if_Ain(5, 23), check_if_Ain(5, 24),
                      check_if_Ain(5, 25), check_if_Ain(5, 26), check_if_Ain(5, 27), check_if_Ain(5, 28),
                      check_if_Ain(5, 29), check_if_Ain(5, 30), check_if_Ain(5, 31), check_if_Ain(5, 32),
                      check_if_Ain(5, 33), check_if_Ain(5, 34), check_if_Ain(5, 35), check_if_Ain(5, 36),
                      check_if_Ain(5, 37), check_if_Ain(5, 38), check_if_Ain(5, 39), check_if_Ain(5, 40),
                      check_if_Ain(5, 41), check_if_Ain(5, 42), check_if_Ain(5, 43), check_if_Ain(5, 44),
                      check_if_Ain(5, 45), check_if_Ain(5, 46), check_if_Ain(5, 47), check_if_Ain(5, 48),
                      check_if_Ain(5, 49), check_if_Ain(5, 50)], ignore_index=True)
    return data


def check_A6():
    data = pd.concat([check_if_Ain(6, 0), check_if_Ain(6, 1), check_if_Ain(6, 2), check_if_Ain(6, 3),
                      check_if_Ain(6, 4), check_if_Ain(6, 5), check_if_Ain(6, 7), check_if_Ain(6, 8),
                      check_if_Ain(6, 9), check_if_Ain(6, 10), check_if_Ain(6, 11), check_if_Ain(6, 12),
                      check_if_Ain(6, 13), check_if_Ain(6, 14), check_if_Ain(6, 15), check_if_Ain(6, 16),
                      check_if_Ain(6, 17), check_if_Ain(6, 18), check_if_Ain(6, 19), check_if_Ain(6, 20),
                      check_if_Ain(6, 21), check_if_Ain(6, 22), check_if_Ain(6, 23), check_if_Ain(6, 24),
                      check_if_Ain(6, 25), check_if_Ain(6, 26), check_if_Ain(6, 27), check_if_Ain(6, 28),
                      check_if_Ain(6, 29), check_if_Ain(6, 30), check_if_Ain(6, 31), check_if_Ain(6, 32),
                      check_if_Ain(6, 33), check_if_Ain(6, 34), check_if_Ain(6, 35), check_if_Ain(6, 36),
                      check_if_Ain(6, 37), check_if_Ain(6, 38), check_if_Ain(6, 39), check_if_Ain(6, 40),
                      check_if_Ain(6, 41), check_if_Ain(6, 42), check_if_Ain(6, 43), check_if_Ain(6, 44),
                      check_if_Ain(6, 45), check_if_Ain(6, 46), check_if_Ain(6, 47), check_if_Ain(6, 48),
                      check_if_Ain(6, 49), check_if_Ain(6, 50)], ignore_index=True)
    return data


def check_A7():
    data = pd.concat([check_if_Ain(7, 0), check_if_Ain(7, 1), check_if_Ain(7, 2), check_if_Ain(7, 3),
                      check_if_Ain(7, 4), check_if_Ain(7, 5), check_if_Ain(7, 6), check_if_Ain(7, 8),
                      check_if_Ain(7, 9), check_if_Ain(7, 10), check_if_Ain(7, 11), check_if_Ain(7, 12),
                      check_if_Ain(7, 13), check_if_Ain(7, 14), check_if_Ain(7, 15), check_if_Ain(7, 16),
                      check_if_Ain(7, 17), check_if_Ain(7, 18), check_if_Ain(7, 19), check_if_Ain(7, 20),
                      check_if_Ain(7, 21), check_if_Ain(7, 22), check_if_Ain(7, 23), check_if_Ain(7, 24),
                      check_if_Ain(7, 25), check_if_Ain(7, 26), check_if_Ain(7, 27), check_if_Ain(7, 28),
                      check_if_Ain(7, 29), check_if_Ain(7, 30), check_if_Ain(7, 31), check_if_Ain(7, 32),
                      check_if_Ain(7, 33), check_if_Ain(7, 34), check_if_Ain(7, 35), check_if_Ain(7, 36),
                      check_if_Ain(7, 37), check_if_Ain(7, 38), check_if_Ain(7, 39), check_if_Ain(7, 40),
                      check_if_Ain(7, 41), check_if_Ain(7, 42), check_if_Ain(7, 43), check_if_Ain(7, 44),
                      check_if_Ain(7, 45), check_if_Ain(7, 46), check_if_Ain(7, 47), check_if_Ain(7, 48),
                      check_if_Ain(7, 49), check_if_Ain(7, 50)], ignore_index=True)
    return data


def check_A8():
    data = pd.concat([check_if_Ain(8, 0), check_if_Ain(8, 1), check_if_Ain(8, 2), check_if_Ain(8, 3),
                      check_if_Ain(8, 4), check_if_Ain(8, 5), check_if_Ain(8, 6), check_if_Ain(8, 7),
                      check_if_Ain(8, 9), check_if_Ain(8, 10), check_if_Ain(8, 11), check_if_Ain(8, 12),
                      check_if_Ain(8, 13), check_if_Ain(8, 14), check_if_Ain(8, 15), check_if_Ain(8, 16),
                      check_if_Ain(8, 17), check_if_Ain(8, 18), check_if_Ain(8, 19), check_if_Ain(8, 20),
                      check_if_Ain(8, 21), check_if_Ain(8, 22), check_if_Ain(8, 23), check_if_Ain(8, 24),
                      check_if_Ain(8, 25), check_if_Ain(8, 26), check_if_Ain(8, 27), check_if_Ain(8, 28),
                      check_if_Ain(8, 29), check_if_Ain(8, 30), check_if_Ain(8, 31), check_if_Ain(8, 32),
                      check_if_Ain(8, 33), check_if_Ain(8, 34), check_if_Ain(8, 35), check_if_Ain(8, 36),
                      check_if_Ain(8, 37), check_if_Ain(8, 38), check_if_Ain(8, 39), check_if_Ain(8, 40),
                      check_if_Ain(8, 41), check_if_Ain(8, 42), check_if_Ain(8, 43), check_if_Ain(8, 44),
                      check_if_Ain(8, 45), check_if_Ain(8, 46), check_if_Ain(8, 47), check_if_Ain(8, 48),
                      check_if_Ain(8, 49), check_if_Ain(8, 50)], ignore_index=True)
    return data


def check_A9():
    data = pd.concat([check_if_Ain(9, 0), check_if_Ain(9, 1), check_if_Ain(9, 2), check_if_Ain(9, 3),
                      check_if_Ain(9, 4), check_if_Ain(9, 5), check_if_Ain(9, 6), check_if_Ain(9, 7),
                      check_if_Ain(9, 8), check_if_Ain(9, 10), check_if_Ain(9, 11), check_if_Ain(9, 12),
                      check_if_Ain(9, 13), check_if_Ain(9, 14), check_if_Ain(9, 15), check_if_Ain(9, 16),
                      check_if_Ain(9, 17), check_if_Ain(9, 18), check_if_Ain(9, 19), check_if_Ain(9, 20),
                      check_if_Ain(9, 21), check_if_Ain(9, 22), check_if_Ain(9, 23), check_if_Ain(9, 24),
                      check_if_Ain(9, 25), check_if_Ain(9, 26), check_if_Ain(9, 27), check_if_Ain(9, 28),
                      check_if_Ain(9, 29), check_if_Ain(9, 30), check_if_Ain(9, 31), check_if_Ain(9, 32),
                      check_if_Ain(9, 33), check_if_Ain(9, 34), check_if_Ain(9, 35), check_if_Ain(9, 36),
                      check_if_Ain(9, 37), check_if_Ain(9, 38), check_if_Ain(9, 39), check_if_Ain(9, 40),
                      check_if_Ain(9, 41), check_if_Ain(9, 42), check_if_Ain(9, 43), check_if_Ain(9, 44),
                      check_if_Ain(9, 45), check_if_Ain(9, 46), check_if_Ain(9, 47), check_if_Ain(9, 48),
                      check_if_Ain(9, 49), check_if_Ain(9, 50)], ignore_index=True)
    return data


def check_A10():
    data = pd.concat([check_if_Ain(10, 0), check_if_Ain(10, 1), check_if_Ain(10, 2), check_if_Ain(10, 3),
                      check_if_Ain(10, 4), check_if_Ain(10, 5), check_if_Ain(10, 6), check_if_Ain(10, 7),
                      check_if_Ain(10, 8), check_if_Ain(10, 9), check_if_Ain(10, 11), check_if_Ain(10, 12),
                      check_if_Ain(10, 13), check_if_Ain(10, 14), check_if_Ain(10, 15), check_if_Ain(10, 16),
                      check_if_Ain(10, 17), check_if_Ain(10, 18), check_if_Ain(10, 19), check_if_Ain(10, 20),
                      check_if_Ain(10, 21), check_if_Ain(10, 22), check_if_Ain(10, 23), check_if_Ain(10, 24),
                      check_if_Ain(10, 25), check_if_Ain(10, 26), check_if_Ain(10, 27), check_if_Ain(10, 28),
                      check_if_Ain(10, 29), check_if_Ain(10, 30), check_if_Ain(10, 31), check_if_Ain(10, 32),
                      check_if_Ain(10, 33), check_if_Ain(10, 34), check_if_Ain(10, 35), check_if_Ain(10, 36),
                      check_if_Ain(10, 37), check_if_Ain(10, 38), check_if_Ain(10, 39), check_if_Ain(10, 40),
                      check_if_Ain(10, 41), check_if_Ain(10, 42), check_if_Ain(10, 43), check_if_Ain(10, 44),
                      check_if_Ain(10, 45), check_if_Ain(10, 46), check_if_Ain(10, 47), check_if_Ain(10, 48),
                      check_if_Ain(10, 49), check_if_Ain(10, 50)], ignore_index=True)
    return data


def check_A11():
    data = pd.concat([check_if_Ain(11, 0), check_if_Ain(11, 1), check_if_Ain(11, 2), check_if_Ain(11, 3),
                      check_if_Ain(11, 4), check_if_Ain(11, 5), check_if_Ain(11, 6), check_if_Ain(11, 7),
                      check_if_Ain(11, 8), check_if_Ain(11, 9), check_if_Ain(11, 10), check_if_Ain(11, 12),
                      check_if_Ain(11, 13), check_if_Ain(11, 14), check_if_Ain(11, 15), check_if_Ain(11, 16),
                      check_if_Ain(11, 17), check_if_Ain(11, 18), check_if_Ain(11, 19), check_if_Ain(11, 20),
                      check_if_Ain(11, 21), check_if_Ain(11, 22), check_if_Ain(11, 23), check_if_Ain(11, 24),
                      check_if_Ain(11, 25), check_if_Ain(11, 26), check_if_Ain(11, 27), check_if_Ain(11, 28),
                      check_if_Ain(11, 29), check_if_Ain(11, 30), check_if_Ain(11, 31), check_if_Ain(11, 32),
                      check_if_Ain(11, 33), check_if_Ain(11, 34), check_if_Ain(11, 35), check_if_Ain(11, 36),
                      check_if_Ain(11, 37), check_if_Ain(11, 38), check_if_Ain(11, 39), check_if_Ain(11, 40),
                      check_if_Ain(11, 41), check_if_Ain(11, 42), check_if_Ain(11, 43), check_if_Ain(11, 44),
                      check_if_Ain(11, 45), check_if_Ain(11, 46), check_if_Ain(11, 47), check_if_Ain(11, 48),
                      check_if_Ain(11, 49), check_if_Ain(11, 50)], ignore_index=True)
    return data


def check_A12():
    data = pd.concat([check_if_Ain(12, 0), check_if_Ain(12, 1), check_if_Ain(12, 2), check_if_Ain(12, 3),
                      check_if_Ain(12, 4), check_if_Ain(12, 5), check_if_Ain(12, 6), check_if_Ain(12, 7),
                      check_if_Ain(12, 8), check_if_Ain(12, 9), check_if_Ain(12, 10), check_if_Ain(12, 11),
                      check_if_Ain(12, 13), check_if_Ain(12, 14), check_if_Ain(12, 15), check_if_Ain(12, 16),
                      check_if_Ain(12, 17), check_if_Ain(12, 18), check_if_Ain(12, 19), check_if_Ain(12, 20),
                      check_if_Ain(12, 21), check_if_Ain(12, 22), check_if_Ain(12, 23), check_if_Ain(12, 24),
                      check_if_Ain(12, 25), check_if_Ain(12, 26), check_if_Ain(12, 27), check_if_Ain(12, 28),
                      check_if_Ain(12, 29), check_if_Ain(12, 30), check_if_Ain(12, 31), check_if_Ain(12, 32),
                      check_if_Ain(12, 33), check_if_Ain(12, 34), check_if_Ain(12, 35), check_if_Ain(12, 36),
                      check_if_Ain(12, 37), check_if_Ain(12, 38), check_if_Ain(12, 39), check_if_Ain(12, 40),
                      check_if_Ain(12, 41), check_if_Ain(12, 42), check_if_Ain(12, 43), check_if_Ain(12, 44),
                      check_if_Ain(12, 45), check_if_Ain(12, 46), check_if_Ain(12, 47), check_if_Ain(12, 48),
                      check_if_Ain(12, 49), check_if_Ain(12, 50)], ignore_index=True)
    return data


def check_A13():
    data = pd.concat([check_if_Ain(13, 0), check_if_Ain(13, 1), check_if_Ain(13, 2), check_if_Ain(13, 3),
                      check_if_Ain(13, 4), check_if_Ain(13, 5), check_if_Ain(13, 6), check_if_Ain(13, 7),
                      check_if_Ain(13, 8), check_if_Ain(13, 9), check_if_Ain(13, 10), check_if_Ain(13, 11),
                      check_if_Ain(13, 12), check_if_Ain(13, 14), check_if_Ain(13, 15), check_if_Ain(13, 16),
                      check_if_Ain(13, 17), check_if_Ain(13, 18), check_if_Ain(13, 19), check_if_Ain(13, 20),
                      check_if_Ain(13, 21), check_if_Ain(13, 22), check_if_Ain(13, 23), check_if_Ain(13, 24),
                      check_if_Ain(13, 25), check_if_Ain(13, 26), check_if_Ain(13, 27), check_if_Ain(13, 28),
                      check_if_Ain(13, 29), check_if_Ain(13, 30), check_if_Ain(13, 31), check_if_Ain(13, 32),
                      check_if_Ain(13, 33), check_if_Ain(13, 34), check_if_Ain(13, 35), check_if_Ain(13, 36),
                      check_if_Ain(13, 37), check_if_Ain(13, 38), check_if_Ain(13, 39), check_if_Ain(13, 40),
                      check_if_Ain(13, 41), check_if_Ain(13, 42), check_if_Ain(13, 43), check_if_Ain(13, 44),
                      check_if_Ain(13, 45), check_if_Ain(13, 46), check_if_Ain(13, 47), check_if_Ain(13, 48),
                      check_if_Ain(13, 49), check_if_Ain(13, 50)], ignore_index=True)
    return data


def check_A14():
    data = pd.concat([check_if_Ain(14, 0), check_if_Ain(14, 1), check_if_Ain(14, 2), check_if_Ain(14, 3),
                      check_if_Ain(14, 4), check_if_Ain(14, 5), check_if_Ain(14, 6), check_if_Ain(14, 7),
                      check_if_Ain(14, 8), check_if_Ain(14, 9), check_if_Ain(14, 10), check_if_Ain(14, 11),
                      check_if_Ain(14, 12), check_if_Ain(14, 13), check_if_Ain(14, 15), check_if_Ain(14, 16),
                      check_if_Ain(14, 17), check_if_Ain(14, 18), check_if_Ain(14, 19), check_if_Ain(14, 20),
                      check_if_Ain(14, 21), check_if_Ain(14, 22), check_if_Ain(14, 23), check_if_Ain(14, 24),
                      check_if_Ain(14, 25), check_if_Ain(14, 26), check_if_Ain(14, 27), check_if_Ain(14, 28),
                      check_if_Ain(14, 29), check_if_Ain(14, 30), check_if_Ain(14, 31), check_if_Ain(14, 32),
                      check_if_Ain(14, 33), check_if_Ain(14, 34), check_if_Ain(14, 35), check_if_Ain(14, 36),
                      check_if_Ain(14, 37), check_if_Ain(14, 38), check_if_Ain(14, 39), check_if_Ain(14, 40),
                      check_if_Ain(14, 41), check_if_Ain(14, 42), check_if_Ain(14, 43), check_if_Ain(14, 44),
                      check_if_Ain(14, 45), check_if_Ain(14, 46), check_if_Ain(14, 47), check_if_Ain(14, 48),
                      check_if_Ain(14, 49), check_if_Ain(14, 50)], ignore_index=True)
    return data


def check_A15():
    data = pd.concat([check_if_Ain(15, 0), check_if_Ain(15, 1), check_if_Ain(15, 2), check_if_Ain(15, 3),
                      check_if_Ain(15, 4), check_if_Ain(15, 5), check_if_Ain(15, 6), check_if_Ain(15, 7),
                      check_if_Ain(15, 8), check_if_Ain(15, 9), check_if_Ain(15, 10), check_if_Ain(15, 11),
                      check_if_Ain(15, 12), check_if_Ain(15, 13), check_if_Ain(15, 14), check_if_Ain(15, 16),
                      check_if_Ain(15, 17), check_if_Ain(15, 18), check_if_Ain(15, 19), check_if_Ain(15, 20),
                      check_if_Ain(15, 21), check_if_Ain(15, 22), check_if_Ain(15, 23), check_if_Ain(15, 24),
                      check_if_Ain(15, 25), check_if_Ain(15, 26), check_if_Ain(15, 27), check_if_Ain(15, 28),
                      check_if_Ain(15, 29), check_if_Ain(15, 30), check_if_Ain(15, 31), check_if_Ain(15, 32),
                      check_if_Ain(15, 33), check_if_Ain(15, 34), check_if_Ain(15, 35), check_if_Ain(15, 36),
                      check_if_Ain(15, 37), check_if_Ain(15, 38), check_if_Ain(15, 39), check_if_Ain(15, 40),
                      check_if_Ain(15, 41), check_if_Ain(15, 42), check_if_Ain(15, 43), check_if_Ain(15, 44),
                      check_if_Ain(15, 45), check_if_Ain(15, 46), check_if_Ain(15, 47), check_if_Ain(15, 48),
                      check_if_Ain(15, 49), check_if_Ain(15, 50)], ignore_index=True)
    return data


def check_A16():
    data = pd.concat([check_if_Ain(16, 0), check_if_Ain(16, 1), check_if_Ain(16, 2), check_if_Ain(16, 3),
                      check_if_Ain(16, 4), check_if_Ain(16, 5), check_if_Ain(16, 6), check_if_Ain(16, 7),
                      check_if_Ain(16, 8), check_if_Ain(16, 9), check_if_Ain(16, 10), check_if_Ain(16, 11),
                      check_if_Ain(16, 12), check_if_Ain(16, 13), check_if_Ain(16, 14), check_if_Ain(16, 15),
                      check_if_Ain(16, 17), check_if_Ain(16, 18), check_if_Ain(16, 19), check_if_Ain(16, 20),
                      check_if_Ain(16, 21), check_if_Ain(16, 22), check_if_Ain(16, 23), check_if_Ain(16, 24),
                      check_if_Ain(16, 25), check_if_Ain(16, 26), check_if_Ain(16, 27), check_if_Ain(16, 28),
                      check_if_Ain(16, 29), check_if_Ain(16, 30), check_if_Ain(16, 31), check_if_Ain(16, 32),
                      check_if_Ain(16, 33), check_if_Ain(16, 34), check_if_Ain(16, 35), check_if_Ain(16, 36),
                      check_if_Ain(16, 37), check_if_Ain(16, 38), check_if_Ain(16, 39), check_if_Ain(16, 40),
                      check_if_Ain(16, 41), check_if_Ain(16, 42), check_if_Ain(16, 43), check_if_Ain(16, 44),
                      check_if_Ain(16, 45), check_if_Ain(16, 46), check_if_Ain(16, 47), check_if_Ain(16, 48),
                      check_if_Ain(16, 49), check_if_Ain(16, 50)], ignore_index=True)
    return data


def check_A17():
    data = pd.concat([check_if_Ain(17, 0), check_if_Ain(17, 1), check_if_Ain(17, 2), check_if_Ain(17, 3),
                      check_if_Ain(17, 4), check_if_Ain(17, 5), check_if_Ain(17, 6), check_if_Ain(17, 7),
                      check_if_Ain(17, 8), check_if_Ain(17, 9), check_if_Ain(17, 10), check_if_Ain(17, 11),
                      check_if_Ain(17, 12), check_if_Ain(17, 13), check_if_Ain(17, 14), check_if_Ain(17, 15),
                      check_if_Ain(17, 16), check_if_Ain(17, 18), check_if_Ain(17, 19), check_if_Ain(17, 20),
                      check_if_Ain(17, 21), check_if_Ain(17, 22), check_if_Ain(17, 23), check_if_Ain(17, 24),
                      check_if_Ain(17, 25), check_if_Ain(17, 26), check_if_Ain(17, 27), check_if_Ain(17, 28),
                      check_if_Ain(17, 29), check_if_Ain(17, 30), check_if_Ain(17, 31), check_if_Ain(17, 32),
                      check_if_Ain(17, 33), check_if_Ain(17, 34), check_if_Ain(17, 35), check_if_Ain(17, 36),
                      check_if_Ain(17, 37), check_if_Ain(17, 38), check_if_Ain(17, 39), check_if_Ain(17, 40),
                      check_if_Ain(17, 41), check_if_Ain(17, 42), check_if_Ain(17, 43), check_if_Ain(17, 44),
                      check_if_Ain(17, 45), check_if_Ain(17, 46), check_if_Ain(17, 47), check_if_Ain(17, 48),
                      check_if_Ain(17, 49), check_if_Ain(17, 50)], ignore_index=True)
    return data


def check_A18():
    data = pd.concat([check_if_Ain(18, 0), check_if_Ain(18, 1), check_if_Ain(18, 2), check_if_Ain(18, 3),
                      check_if_Ain(18, 4), check_if_Ain(18, 5), check_if_Ain(18, 6), check_if_Ain(18, 7),
                      check_if_Ain(18, 8), check_if_Ain(18, 9), check_if_Ain(18, 10), check_if_Ain(18, 11),
                      check_if_Ain(18, 12), check_if_Ain(18, 13), check_if_Ain(18, 14), check_if_Ain(18, 15),
                      check_if_Ain(18, 16), check_if_Ain(18, 17), check_if_Ain(18, 19), check_if_Ain(18, 20),
                      check_if_Ain(18, 21), check_if_Ain(18, 22), check_if_Ain(18, 23), check_if_Ain(18, 24),
                      check_if_Ain(18, 25), check_if_Ain(18, 26), check_if_Ain(18, 27), check_if_Ain(18, 28),
                      check_if_Ain(18, 29), check_if_Ain(18, 30), check_if_Ain(18, 31), check_if_Ain(18, 32),
                      check_if_Ain(18, 33), check_if_Ain(18, 34), check_if_Ain(18, 35), check_if_Ain(18, 36),
                      check_if_Ain(18, 37), check_if_Ain(18, 38), check_if_Ain(18, 39), check_if_Ain(18, 40),
                      check_if_Ain(18, 41), check_if_Ain(18, 42), check_if_Ain(18, 43), check_if_Ain(18, 44),
                      check_if_Ain(18, 45), check_if_Ain(18, 46), check_if_Ain(18, 47), check_if_Ain(18, 48),
                      check_if_Ain(18, 49), check_if_Ain(18, 50)], ignore_index=True)
    return data


def check_A19():
    data = pd.concat([check_if_Ain(19, 0), check_if_Ain(19, 1), check_if_Ain(19, 2), check_if_Ain(19, 3),
                      check_if_Ain(19, 4), check_if_Ain(19, 5), check_if_Ain(19, 6), check_if_Ain(19, 7),
                      check_if_Ain(19, 8), check_if_Ain(19, 9), check_if_Ain(19, 10), check_if_Ain(19, 11),
                      check_if_Ain(19, 12), check_if_Ain(19, 13), check_if_Ain(19, 14), check_if_Ain(19, 15),
                      check_if_Ain(19, 16), check_if_Ain(19, 17), check_if_Ain(19, 18), check_if_Ain(19, 20),
                      check_if_Ain(19, 21), check_if_Ain(19, 22), check_if_Ain(19, 23), check_if_Ain(19, 24),
                      check_if_Ain(19, 25), check_if_Ain(19, 26), check_if_Ain(19, 27), check_if_Ain(19, 28),
                      check_if_Ain(19, 29), check_if_Ain(19, 30), check_if_Ain(19, 31), check_if_Ain(19, 32),
                      check_if_Ain(19, 33), check_if_Ain(19, 34), check_if_Ain(19, 35), check_if_Ain(19, 36),
                      check_if_Ain(19, 37), check_if_Ain(19, 38), check_if_Ain(19, 39), check_if_Ain(19, 40),
                      check_if_Ain(19, 41), check_if_Ain(19, 42), check_if_Ain(19, 43), check_if_Ain(19, 44),
                      check_if_Ain(19, 45), check_if_Ain(19, 46), check_if_Ain(19, 47), check_if_Ain(19, 48),
                      check_if_Ain(19, 49), check_if_Ain(19, 50)], ignore_index=True)
    return data


def check_A20():
    data = pd.concat([check_if_Ain(20, 0), check_if_Ain(20, 1), check_if_Ain(20, 2), check_if_Ain(20, 3),
                      check_if_Ain(20, 4), check_if_Ain(20, 5), check_if_Ain(20, 6), check_if_Ain(20, 7),
                      check_if_Ain(20, 8), check_if_Ain(20, 9), check_if_Ain(20, 10), check_if_Ain(20, 11),
                      check_if_Ain(20, 12), check_if_Ain(20, 13), check_if_Ain(20, 14), check_if_Ain(20, 15),
                      check_if_Ain(20, 16), check_if_Ain(20, 17), check_if_Ain(20, 18), check_if_Ain(20, 19),
                      check_if_Ain(20, 21), check_if_Ain(20, 22), check_if_Ain(20, 23), check_if_Ain(20, 24),
                      check_if_Ain(20, 25), check_if_Ain(20, 26), check_if_Ain(20, 27), check_if_Ain(20, 28),
                      check_if_Ain(20, 29), check_if_Ain(20, 30), check_if_Ain(20, 31), check_if_Ain(20, 32),
                      check_if_Ain(20, 33), check_if_Ain(20, 34), check_if_Ain(20, 35), check_if_Ain(20, 36),
                      check_if_Ain(20, 37), check_if_Ain(20, 38), check_if_Ain(20, 39), check_if_Ain(20, 40),
                      check_if_Ain(20, 41), check_if_Ain(20, 42), check_if_Ain(20, 43), check_if_Ain(20, 44),
                      check_if_Ain(20, 45), check_if_Ain(20, 46), check_if_Ain(20, 47), check_if_Ain(20, 48),
                      check_if_Ain(20, 49), check_if_Ain(20, 50)], ignore_index=True)
    return data


def check_A21():
    data = pd.concat([check_if_Ain(21, 0), check_if_Ain(21, 1), check_if_Ain(21, 2), check_if_Ain(21, 3),
                      check_if_Ain(21, 4), check_if_Ain(21, 5), check_if_Ain(21, 6), check_if_Ain(21, 7),
                      check_if_Ain(21, 8), check_if_Ain(21, 9), check_if_Ain(21, 10), check_if_Ain(21, 11),
                      check_if_Ain(21, 12), check_if_Ain(21, 13), check_if_Ain(21, 14), check_if_Ain(21, 15),
                      check_if_Ain(21, 16), check_if_Ain(21, 17), check_if_Ain(21, 18), check_if_Ain(21, 19),
                      check_if_Ain(21, 20), check_if_Ain(21, 22), check_if_Ain(21, 23), check_if_Ain(21, 24),
                      check_if_Ain(21, 25), check_if_Ain(21, 26), check_if_Ain(21, 27), check_if_Ain(21, 28),
                      check_if_Ain(21, 29), check_if_Ain(21, 30), check_if_Ain(21, 31), check_if_Ain(21, 32),
                      check_if_Ain(21, 33), check_if_Ain(21, 34), check_if_Ain(21, 35), check_if_Ain(21, 36),
                      check_if_Ain(21, 37), check_if_Ain(21, 38), check_if_Ain(21, 39), check_if_Ain(21, 40),
                      check_if_Ain(21, 41), check_if_Ain(21, 42), check_if_Ain(21, 43), check_if_Ain(21, 44),
                      check_if_Ain(21, 45), check_if_Ain(21, 46), check_if_Ain(21, 47), check_if_Ain(21, 48),
                      check_if_Ain(21, 49), check_if_Ain(21, 50)], ignore_index=True)
    return data


def check_A22():
    data = pd.concat([check_if_Ain(22, 0), check_if_Ain(22, 1), check_if_Ain(22, 2), check_if_Ain(22, 3),
                      check_if_Ain(22, 4), check_if_Ain(22, 5), check_if_Ain(22, 6), check_if_Ain(22, 7),
                      check_if_Ain(22, 8), check_if_Ain(22, 9), check_if_Ain(22, 10), check_if_Ain(22, 11),
                      check_if_Ain(22, 12), check_if_Ain(22, 13), check_if_Ain(22, 14), check_if_Ain(22, 15),
                      check_if_Ain(22, 16), check_if_Ain(22, 17), check_if_Ain(22, 18), check_if_Ain(22, 19),
                      check_if_Ain(22, 20), check_if_Ain(22, 21), check_if_Ain(22, 23), check_if_Ain(22, 24),
                      check_if_Ain(22, 25), check_if_Ain(22, 26), check_if_Ain(22, 27), check_if_Ain(22, 28),
                      check_if_Ain(22, 29), check_if_Ain(22, 30), check_if_Ain(22, 31), check_if_Ain(22, 32),
                      check_if_Ain(22, 33), check_if_Ain(22, 34), check_if_Ain(22, 35), check_if_Ain(22, 36),
                      check_if_Ain(22, 37), check_if_Ain(22, 38), check_if_Ain(22, 39), check_if_Ain(22, 40),
                      check_if_Ain(22, 41), check_if_Ain(22, 42), check_if_Ain(22, 43), check_if_Ain(22, 44),
                      check_if_Ain(22, 45), check_if_Ain(22, 46), check_if_Ain(22, 47), check_if_Ain(22, 48),
                      check_if_Ain(22, 49), check_if_Ain(22, 50)], ignore_index=True)
    return data


def check_A23():
    data = pd.concat([check_if_Ain(23, 0), check_if_Ain(23, 1), check_if_Ain(23, 2), check_if_Ain(23, 3),
                      check_if_Ain(23, 4), check_if_Ain(23, 5), check_if_Ain(23, 6), check_if_Ain(23, 7),
                      check_if_Ain(23, 8), check_if_Ain(23, 9), check_if_Ain(23, 10), check_if_Ain(23, 11),
                      check_if_Ain(23, 12), check_if_Ain(23, 13), check_if_Ain(23, 14), check_if_Ain(23, 15),
                      check_if_Ain(23, 16), check_if_Ain(23, 17), check_if_Ain(23, 18), check_if_Ain(23, 19),
                      check_if_Ain(23, 20), check_if_Ain(23, 21), check_if_Ain(23, 22), check_if_Ain(23, 24),
                      check_if_Ain(23, 25), check_if_Ain(23, 26), check_if_Ain(23, 27), check_if_Ain(23, 28),
                      check_if_Ain(23, 29), check_if_Ain(23, 30), check_if_Ain(23, 31), check_if_Ain(23, 32),
                      check_if_Ain(23, 33), check_if_Ain(23, 34), check_if_Ain(23, 35), check_if_Ain(23, 36),
                      check_if_Ain(23, 37), check_if_Ain(23, 38), check_if_Ain(23, 39), check_if_Ain(23, 40),
                      check_if_Ain(23, 41), check_if_Ain(23, 42), check_if_Ain(23, 43), check_if_Ain(23, 44),
                      check_if_Ain(23, 45), check_if_Ain(23, 46), check_if_Ain(23, 47), check_if_Ain(23, 48),
                      check_if_Ain(23, 49), check_if_Ain(23, 50)], ignore_index=True)
    return data


def check_A24():
    data = pd.concat([check_if_Ain(24, 0), check_if_Ain(24, 1), check_if_Ain(24, 2), check_if_Ain(24, 3),
                      check_if_Ain(24, 4), check_if_Ain(24, 5), check_if_Ain(24, 6), check_if_Ain(24, 7),
                      check_if_Ain(24, 8), check_if_Ain(24, 9), check_if_Ain(24, 10), check_if_Ain(24, 11),
                      check_if_Ain(24, 12), check_if_Ain(24, 13), check_if_Ain(24, 14), check_if_Ain(24, 15),
                      check_if_Ain(24, 16), check_if_Ain(24, 17), check_if_Ain(24, 18), check_if_Ain(24, 19),
                      check_if_Ain(24, 20), check_if_Ain(24, 21), check_if_Ain(24, 22), check_if_Ain(24, 23),
                      check_if_Ain(24, 25), check_if_Ain(24, 26), check_if_Ain(24, 27), check_if_Ain(24, 28),
                      check_if_Ain(24, 29), check_if_Ain(24, 30), check_if_Ain(24, 31), check_if_Ain(24, 32),
                      check_if_Ain(24, 33), check_if_Ain(24, 34), check_if_Ain(24, 35), check_if_Ain(24, 36),
                      check_if_Ain(24, 37), check_if_Ain(24, 38), check_if_Ain(24, 39), check_if_Ain(24, 40),
                      check_if_Ain(24, 41), check_if_Ain(24, 42), check_if_Ain(24, 43), check_if_Ain(24, 44),
                      check_if_Ain(24, 45), check_if_Ain(24, 46), check_if_Ain(24, 47), check_if_Ain(24, 48),
                      check_if_Ain(24, 49), check_if_Ain(24, 50)], ignore_index=True)
    return data


def check_A25():
    data = pd.concat([check_if_Ain(25, 0), check_if_Ain(25, 1), check_if_Ain(25, 2), check_if_Ain(25, 3),
                      check_if_Ain(25, 4), check_if_Ain(25, 5), check_if_Ain(25, 6), check_if_Ain(25, 7),
                      check_if_Ain(25, 8), check_if_Ain(25, 9), check_if_Ain(25, 10), check_if_Ain(25, 11),
                      check_if_Ain(25, 12), check_if_Ain(25, 13), check_if_Ain(25, 14), check_if_Ain(25, 15),
                      check_if_Ain(25, 16), check_if_Ain(25, 17), check_if_Ain(25, 18), check_if_Ain(25, 19),
                      check_if_Ain(25, 20), check_if_Ain(25, 21), check_if_Ain(25, 22), check_if_Ain(25, 23),
                      check_if_Ain(25, 24), check_if_Ain(25, 26), check_if_Ain(25, 27), check_if_Ain(25, 28),
                      check_if_Ain(25, 29), check_if_Ain(25, 30), check_if_Ain(25, 31), check_if_Ain(25, 32),
                      check_if_Ain(25, 33), check_if_Ain(25, 34), check_if_Ain(25, 35), check_if_Ain(25, 36),
                      check_if_Ain(25, 37), check_if_Ain(25, 38), check_if_Ain(25, 39), check_if_Ain(25, 40),
                      check_if_Ain(25, 41), check_if_Ain(25, 42), check_if_Ain(25, 43), check_if_Ain(25, 44),
                      check_if_Ain(25, 45), check_if_Ain(25, 46), check_if_Ain(25, 47), check_if_Ain(25, 48),
                      check_if_Ain(25, 49), check_if_Ain(25, 50)], ignore_index=True)
    return data


def check_A26():
    data = pd.concat([check_if_Ain(26, 0), check_if_Ain(26, 1), check_if_Ain(26, 2), check_if_Ain(26, 3),
                      check_if_Ain(26, 4), check_if_Ain(26, 5), check_if_Ain(26, 6), check_if_Ain(26, 7),
                      check_if_Ain(26, 8), check_if_Ain(26, 9), check_if_Ain(26, 10), check_if_Ain(26, 11),
                      check_if_Ain(26, 12), check_if_Ain(26, 13), check_if_Ain(26, 14), check_if_Ain(26, 15),
                      check_if_Ain(26, 16), check_if_Ain(26, 17), check_if_Ain(26, 18), check_if_Ain(26, 19),
                      check_if_Ain(26, 20), check_if_Ain(26, 21), check_if_Ain(26, 22), check_if_Ain(26, 23),
                      check_if_Ain(26, 24), check_if_Ain(26, 25), check_if_Ain(26, 27), check_if_Ain(26, 28),
                      check_if_Ain(26, 29), check_if_Ain(26, 30), check_if_Ain(26, 31), check_if_Ain(26, 32),
                      check_if_Ain(26, 33), check_if_Ain(26, 34), check_if_Ain(26, 35), check_if_Ain(26, 36),
                      check_if_Ain(26, 37), check_if_Ain(26, 38), check_if_Ain(26, 39), check_if_Ain(26, 40),
                      check_if_Ain(26, 41), check_if_Ain(26, 42), check_if_Ain(26, 43), check_if_Ain(26, 44),
                      check_if_Ain(26, 45), check_if_Ain(26, 46), check_if_Ain(26, 47), check_if_Ain(26, 48),
                      check_if_Ain(26, 49), check_if_Ain(26, 50)], ignore_index=True)
    return data


def check_A27():
    data = pd.concat([check_if_Ain(27, 0), check_if_Ain(27, 1), check_if_Ain(27, 2), check_if_Ain(27, 3),
                      check_if_Ain(27, 4), check_if_Ain(27, 5), check_if_Ain(27, 6), check_if_Ain(27, 7),
                      check_if_Ain(27, 8), check_if_Ain(27, 9), check_if_Ain(27, 10), check_if_Ain(27, 11),
                      check_if_Ain(27, 12), check_if_Ain(27, 13), check_if_Ain(27, 14), check_if_Ain(27, 15),
                      check_if_Ain(27, 16), check_if_Ain(27, 17), check_if_Ain(27, 18), check_if_Ain(27, 19),
                      check_if_Ain(27, 20), check_if_Ain(27, 21), check_if_Ain(27, 22), check_if_Ain(27, 23),
                      check_if_Ain(27, 24), check_if_Ain(27, 25), check_if_Ain(27, 26), check_if_Ain(27, 28),
                      check_if_Ain(27, 29), check_if_Ain(27, 30), check_if_Ain(27, 31), check_if_Ain(27, 32),
                      check_if_Ain(27, 33), check_if_Ain(27, 34), check_if_Ain(27, 35), check_if_Ain(27, 36),
                      check_if_Ain(27, 37), check_if_Ain(27, 38), check_if_Ain(27, 39), check_if_Ain(27, 40),
                      check_if_Ain(27, 41), check_if_Ain(27, 42), check_if_Ain(27, 43), check_if_Ain(27, 44),
                      check_if_Ain(27, 45), check_if_Ain(27, 46), check_if_Ain(27, 47), check_if_Ain(27, 48),
                      check_if_Ain(27, 49), check_if_Ain(27, 50)], ignore_index=True)
    return data


def check_A28():
    data = pd.concat([check_if_Ain(28, 0), check_if_Ain(28, 1), check_if_Ain(28, 2), check_if_Ain(28, 3),
                      check_if_Ain(28, 4), check_if_Ain(28, 5), check_if_Ain(28, 6), check_if_Ain(28, 7),
                      check_if_Ain(28, 8), check_if_Ain(28, 9), check_if_Ain(28, 10), check_if_Ain(28, 11),
                      check_if_Ain(28, 12), check_if_Ain(28, 13), check_if_Ain(28, 14), check_if_Ain(28, 15),
                      check_if_Ain(28, 16), check_if_Ain(28, 17), check_if_Ain(28, 18), check_if_Ain(28, 19),
                      check_if_Ain(28, 20), check_if_Ain(28, 21), check_if_Ain(28, 22), check_if_Ain(28, 23),
                      check_if_Ain(28, 24), check_if_Ain(28, 25), check_if_Ain(28, 26), check_if_Ain(28, 27),
                      check_if_Ain(28, 29), check_if_Ain(28, 30), check_if_Ain(28, 31), check_if_Ain(28, 32),
                      check_if_Ain(28, 33), check_if_Ain(28, 34), check_if_Ain(28, 35), check_if_Ain(28, 36),
                      check_if_Ain(28, 37), check_if_Ain(28, 38), check_if_Ain(28, 39), check_if_Ain(28, 40),
                      check_if_Ain(28, 41), check_if_Ain(28, 42), check_if_Ain(28, 43), check_if_Ain(28, 44),
                      check_if_Ain(28, 45), check_if_Ain(28, 46), check_if_Ain(28, 47), check_if_Ain(28, 48),
                      check_if_Ain(28, 49), check_if_Ain(28, 50)], ignore_index=True)
    return data


def check_A29():
    data = pd.concat([check_if_Ain(29, 0), check_if_Ain(29, 1), check_if_Ain(29, 2), check_if_Ain(29, 3),
                      check_if_Ain(29, 4), check_if_Ain(29, 5), check_if_Ain(29, 6), check_if_Ain(29, 7),
                      check_if_Ain(29, 8), check_if_Ain(29, 9), check_if_Ain(29, 10), check_if_Ain(29, 11),
                      check_if_Ain(29, 12), check_if_Ain(29, 13), check_if_Ain(29, 14), check_if_Ain(29, 15),
                      check_if_Ain(29, 16), check_if_Ain(29, 17), check_if_Ain(29, 18), check_if_Ain(29, 19),
                      check_if_Ain(29, 20), check_if_Ain(29, 21), check_if_Ain(29, 22), check_if_Ain(29, 23),
                      check_if_Ain(29, 24), check_if_Ain(29, 25), check_if_Ain(29, 26), check_if_Ain(29, 27),
                      check_if_Ain(29, 28), check_if_Ain(29, 30), check_if_Ain(29, 31), check_if_Ain(29, 32),
                      check_if_Ain(29, 33), check_if_Ain(29, 34), check_if_Ain(29, 35), check_if_Ain(29, 36),
                      check_if_Ain(29, 37), check_if_Ain(29, 38), check_if_Ain(29, 39), check_if_Ain(29, 40),
                      check_if_Ain(29, 41), check_if_Ain(29, 42), check_if_Ain(29, 43), check_if_Ain(29, 44),
                      check_if_Ain(29, 45), check_if_Ain(29, 46), check_if_Ain(29, 47), check_if_Ain(29, 48),
                      check_if_Ain(29, 49), check_if_Ain(29, 50)], ignore_index=True)
    return data


def check_A30():
    data = pd.concat([check_if_Ain(30, 0), check_if_Ain(30, 1), check_if_Ain(30, 2), check_if_Ain(30, 3),
                      check_if_Ain(30, 4), check_if_Ain(30, 5), check_if_Ain(30, 6), check_if_Ain(30, 7),
                      check_if_Ain(30, 8), check_if_Ain(30, 9), check_if_Ain(30, 10), check_if_Ain(30, 11),
                      check_if_Ain(30, 12), check_if_Ain(30, 13), check_if_Ain(30, 14), check_if_Ain(30, 15),
                      check_if_Ain(30, 16), check_if_Ain(30, 17), check_if_Ain(30, 18), check_if_Ain(30, 19),
                      check_if_Ain(30, 20), check_if_Ain(30, 21), check_if_Ain(30, 22), check_if_Ain(30, 23),
                      check_if_Ain(30, 24), check_if_Ain(30, 25), check_if_Ain(30, 26), check_if_Ain(30, 27),
                      check_if_Ain(30, 28), check_if_Ain(30, 29), check_if_Ain(30, 31), check_if_Ain(30, 32),
                      check_if_Ain(30, 33), check_if_Ain(30, 34), check_if_Ain(30, 35), check_if_Ain(30, 36),
                      check_if_Ain(30, 37), check_if_Ain(30, 38), check_if_Ain(30, 39), check_if_Ain(30, 40),
                      check_if_Ain(30, 41), check_if_Ain(30, 42), check_if_Ain(30, 43), check_if_Ain(30, 44),
                      check_if_Ain(30, 45), check_if_Ain(30, 46), check_if_Ain(30, 47), check_if_Ain(30, 48),
                      check_if_Ain(30, 49), check_if_Ain(30, 50)], ignore_index=True)
    return data


def check_A31():
    data = pd.concat([check_if_Ain(31, 0), check_if_Ain(31, 1), check_if_Ain(31, 2), check_if_Ain(31, 3),
                      check_if_Ain(31, 4), check_if_Ain(31, 5), check_if_Ain(31, 6), check_if_Ain(31, 7),
                      check_if_Ain(31, 8), check_if_Ain(31, 9), check_if_Ain(31, 10), check_if_Ain(31, 11),
                      check_if_Ain(31, 12), check_if_Ain(31, 13), check_if_Ain(31, 14), check_if_Ain(31, 15),
                      check_if_Ain(31, 16), check_if_Ain(31, 17), check_if_Ain(31, 18), check_if_Ain(31, 19),
                      check_if_Ain(31, 20), check_if_Ain(31, 21), check_if_Ain(31, 22), check_if_Ain(31, 23),
                      check_if_Ain(31, 24), check_if_Ain(31, 25), check_if_Ain(31, 26), check_if_Ain(31, 27),
                      check_if_Ain(31, 28), check_if_Ain(31, 29), check_if_Ain(31, 30), check_if_Ain(31, 32),
                      check_if_Ain(31, 33), check_if_Ain(31, 34), check_if_Ain(31, 35), check_if_Ain(31, 36),
                      check_if_Ain(31, 37), check_if_Ain(31, 38), check_if_Ain(31, 39), check_if_Ain(31, 40),
                      check_if_Ain(31, 41), check_if_Ain(31, 42), check_if_Ain(31, 43), check_if_Ain(31, 44),
                      check_if_Ain(31, 45), check_if_Ain(31, 46), check_if_Ain(31, 47), check_if_Ain(31, 48),
                      check_if_Ain(31, 49), check_if_Ain(31, 50)], ignore_index=True)
    return data


def check_A32():
    data = pd.concat([check_if_Ain(32, 0), check_if_Ain(32, 1), check_if_Ain(32, 2), check_if_Ain(32, 3),
                      check_if_Ain(32, 4), check_if_Ain(32, 5), check_if_Ain(32, 6), check_if_Ain(32, 7),
                      check_if_Ain(32, 8), check_if_Ain(32, 9), check_if_Ain(32, 10), check_if_Ain(32, 11),
                      check_if_Ain(32, 12), check_if_Ain(32, 13), check_if_Ain(32, 14), check_if_Ain(32, 15),
                      check_if_Ain(32, 16), check_if_Ain(32, 17), check_if_Ain(32, 18), check_if_Ain(32, 19),
                      check_if_Ain(32, 20), check_if_Ain(32, 21), check_if_Ain(32, 22), check_if_Ain(32, 23),
                      check_if_Ain(32, 24), check_if_Ain(32, 25), check_if_Ain(32, 26), check_if_Ain(32, 27),
                      check_if_Ain(32, 28), check_if_Ain(32, 29), check_if_Ain(32, 30), check_if_Ain(32, 31),
                      check_if_Ain(32, 33), check_if_Ain(32, 34), check_if_Ain(32, 35), check_if_Ain(32, 36),
                      check_if_Ain(32, 37), check_if_Ain(32, 38), check_if_Ain(32, 39), check_if_Ain(32, 40),
                      check_if_Ain(32, 41), check_if_Ain(32, 42), check_if_Ain(32, 43), check_if_Ain(32, 44),
                      check_if_Ain(32, 45), check_if_Ain(32, 46), check_if_Ain(32, 47), check_if_Ain(32, 48),
                      check_if_Ain(32, 49), check_if_Ain(32, 50)], ignore_index=True)
    return data


def check_A33():
    data = pd.concat([check_if_Ain(33, 0), check_if_Ain(33, 1), check_if_Ain(33, 2), check_if_Ain(33, 3),
                      check_if_Ain(33, 4), check_if_Ain(33, 5), check_if_Ain(33, 6), check_if_Ain(33, 7),
                      check_if_Ain(33, 8), check_if_Ain(33, 9), check_if_Ain(33, 10), check_if_Ain(33, 11),
                      check_if_Ain(33, 12), check_if_Ain(33, 13), check_if_Ain(33, 14), check_if_Ain(33, 15),
                      check_if_Ain(33, 16), check_if_Ain(33, 17), check_if_Ain(33, 18), check_if_Ain(33, 19),
                      check_if_Ain(33, 20), check_if_Ain(33, 21), check_if_Ain(33, 22), check_if_Ain(33, 23),
                      check_if_Ain(33, 24), check_if_Ain(33, 25), check_if_Ain(33, 26), check_if_Ain(33, 27),
                      check_if_Ain(33, 28), check_if_Ain(33, 29), check_if_Ain(33, 30), check_if_Ain(33, 31),
                      check_if_Ain(33, 32), check_if_Ain(33, 34), check_if_Ain(33, 35), check_if_Ain(33, 36),
                      check_if_Ain(33, 37), check_if_Ain(33, 38), check_if_Ain(33, 39), check_if_Ain(33, 40),
                      check_if_Ain(33, 41), check_if_Ain(33, 42), check_if_Ain(33, 43), check_if_Ain(33, 44),
                      check_if_Ain(33, 45), check_if_Ain(33, 46), check_if_Ain(33, 47), check_if_Ain(33, 48),
                      check_if_Ain(33, 49), check_if_Ain(33, 50)], ignore_index=True)
    return data


def check_A34():
    data = pd.concat([check_if_Ain(34, 0), check_if_Ain(34, 1), check_if_Ain(34, 2), check_if_Ain(34, 3),
                      check_if_Ain(34, 4), check_if_Ain(34, 5), check_if_Ain(34, 6), check_if_Ain(34, 7),
                      check_if_Ain(34, 8), check_if_Ain(34, 9), check_if_Ain(34, 10), check_if_Ain(34, 11),
                      check_if_Ain(34, 12), check_if_Ain(34, 13), check_if_Ain(34, 14), check_if_Ain(34, 15),
                      check_if_Ain(34, 16), check_if_Ain(34, 17), check_if_Ain(34, 18), check_if_Ain(34, 19),
                      check_if_Ain(34, 20), check_if_Ain(34, 21), check_if_Ain(34, 22), check_if_Ain(34, 23),
                      check_if_Ain(34, 24), check_if_Ain(34, 25), check_if_Ain(34, 26), check_if_Ain(34, 27),
                      check_if_Ain(34, 28), check_if_Ain(34, 29), check_if_Ain(34, 30), check_if_Ain(34, 31),
                      check_if_Ain(34, 32), check_if_Ain(34, 33), check_if_Ain(34, 35), check_if_Ain(34, 36),
                      check_if_Ain(34, 37), check_if_Ain(34, 38), check_if_Ain(34, 39), check_if_Ain(34, 40),
                      check_if_Ain(34, 41), check_if_Ain(34, 42), check_if_Ain(34, 43), check_if_Ain(34, 44),
                      check_if_Ain(34, 45), check_if_Ain(34, 46), check_if_Ain(34, 47), check_if_Ain(34, 48),
                      check_if_Ain(34, 49), check_if_Ain(34, 50)], ignore_index=True)
    return data


def check_A35():
    data = pd.concat([check_if_Ain(35, 0), check_if_Ain(35, 1), check_if_Ain(35, 2), check_if_Ain(35, 3),
                      check_if_Ain(35, 4), check_if_Ain(35, 5), check_if_Ain(35, 6), check_if_Ain(35, 7),
                      check_if_Ain(35, 8), check_if_Ain(35, 9), check_if_Ain(35, 10), check_if_Ain(35, 11),
                      check_if_Ain(35, 12), check_if_Ain(35, 13), check_if_Ain(35, 14), check_if_Ain(35, 15),
                      check_if_Ain(35, 16), check_if_Ain(35, 17), check_if_Ain(35, 18), check_if_Ain(35, 19),
                      check_if_Ain(35, 20), check_if_Ain(35, 21), check_if_Ain(35, 22), check_if_Ain(35, 23),
                      check_if_Ain(35, 24), check_if_Ain(35, 25), check_if_Ain(35, 26), check_if_Ain(35, 27),
                      check_if_Ain(35, 28), check_if_Ain(35, 29), check_if_Ain(35, 30), check_if_Ain(35, 31),
                      check_if_Ain(35, 32), check_if_Ain(35, 33), check_if_Ain(35, 34), check_if_Ain(35, 36),
                      check_if_Ain(35, 37), check_if_Ain(35, 38), check_if_Ain(35, 39), check_if_Ain(35, 40),
                      check_if_Ain(35, 41), check_if_Ain(35, 42), check_if_Ain(35, 43), check_if_Ain(35, 44),
                      check_if_Ain(35, 45), check_if_Ain(35, 46), check_if_Ain(35, 47), check_if_Ain(35, 48),
                      check_if_Ain(35, 49), check_if_Ain(35, 50)], ignore_index=True)
    return data


def check_A36():
    data = pd.concat([check_if_Ain(36, 0), check_if_Ain(36, 1), check_if_Ain(36, 2), check_if_Ain(36, 3),
                      check_if_Ain(36, 4), check_if_Ain(36, 5), check_if_Ain(36, 6), check_if_Ain(36, 7),
                      check_if_Ain(36, 8), check_if_Ain(36, 9), check_if_Ain(36, 10), check_if_Ain(36, 11),
                      check_if_Ain(36, 12), check_if_Ain(36, 13), check_if_Ain(36, 14), check_if_Ain(36, 15),
                      check_if_Ain(36, 16), check_if_Ain(36, 17), check_if_Ain(36, 18), check_if_Ain(36, 19),
                      check_if_Ain(36, 20), check_if_Ain(36, 21), check_if_Ain(36, 22), check_if_Ain(36, 23),
                      check_if_Ain(36, 24), check_if_Ain(36, 25), check_if_Ain(36, 26), check_if_Ain(36, 27),
                      check_if_Ain(36, 28), check_if_Ain(36, 29), check_if_Ain(36, 30), check_if_Ain(36, 31),
                      check_if_Ain(36, 32), check_if_Ain(36, 33), check_if_Ain(36, 34), check_if_Ain(36, 35),
                      check_if_Ain(36, 37), check_if_Ain(36, 38), check_if_Ain(36, 39), check_if_Ain(36, 40),
                      check_if_Ain(36, 41), check_if_Ain(36, 42), check_if_Ain(36, 43), check_if_Ain(36, 44),
                      check_if_Ain(36, 45), check_if_Ain(36, 46), check_if_Ain(36, 47), check_if_Ain(36, 48),
                      check_if_Ain(36, 49), check_if_Ain(36, 50)], ignore_index=True)
    return data


def check_A37():
    data = pd.concat([check_if_Ain(37, 0), check_if_Ain(37, 1), check_if_Ain(37, 2), check_if_Ain(37, 3),
                      check_if_Ain(37, 4), check_if_Ain(37, 5), check_if_Ain(37, 6), check_if_Ain(37, 7),
                      check_if_Ain(37, 8), check_if_Ain(37, 9), check_if_Ain(37, 10), check_if_Ain(37, 11),
                      check_if_Ain(37, 12), check_if_Ain(37, 13), check_if_Ain(37, 14), check_if_Ain(37, 15),
                      check_if_Ain(37, 16), check_if_Ain(37, 17), check_if_Ain(37, 18), check_if_Ain(37, 19),
                      check_if_Ain(37, 20), check_if_Ain(37, 21), check_if_Ain(37, 22), check_if_Ain(37, 23),
                      check_if_Ain(37, 24), check_if_Ain(37, 25), check_if_Ain(37, 26), check_if_Ain(37, 27),
                      check_if_Ain(37, 28), check_if_Ain(37, 29), check_if_Ain(37, 30), check_if_Ain(37, 31),
                      check_if_Ain(37, 32), check_if_Ain(37, 33), check_if_Ain(37, 34), check_if_Ain(37, 35),
                      check_if_Ain(37, 36), check_if_Ain(37, 38), check_if_Ain(37, 39), check_if_Ain(37, 40),
                      check_if_Ain(37, 41), check_if_Ain(37, 42), check_if_Ain(37, 43), check_if_Ain(37, 44),
                      check_if_Ain(37, 45), check_if_Ain(37, 46), check_if_Ain(37, 47), check_if_Ain(37, 48),
                      check_if_Ain(37, 49), check_if_Ain(37, 50)], ignore_index=True)
    return data


def check_A38():
    data = pd.concat([check_if_Ain(38, 0), check_if_Ain(38, 1), check_if_Ain(38, 2), check_if_Ain(38, 3),
                      check_if_Ain(38, 4), check_if_Ain(38, 5), check_if_Ain(38, 6), check_if_Ain(38, 7),
                      check_if_Ain(38, 8), check_if_Ain(38, 9), check_if_Ain(38, 10), check_if_Ain(38, 11),
                      check_if_Ain(38, 12), check_if_Ain(38, 13), check_if_Ain(38, 14), check_if_Ain(38, 15),
                      check_if_Ain(38, 16), check_if_Ain(38, 17), check_if_Ain(38, 18), check_if_Ain(38, 19),
                      check_if_Ain(38, 20), check_if_Ain(38, 21), check_if_Ain(38, 22), check_if_Ain(38, 23),
                      check_if_Ain(38, 24), check_if_Ain(38, 25), check_if_Ain(38, 26), check_if_Ain(38, 27),
                      check_if_Ain(38, 28), check_if_Ain(38, 29), check_if_Ain(38, 30), check_if_Ain(38, 31),
                      check_if_Ain(38, 32), check_if_Ain(38, 33), check_if_Ain(38, 34), check_if_Ain(38, 35),
                      check_if_Ain(38, 36), check_if_Ain(38, 37), check_if_Ain(38, 39), check_if_Ain(38, 40),
                      check_if_Ain(38, 41), check_if_Ain(38, 42), check_if_Ain(38, 43), check_if_Ain(38, 44),
                      check_if_Ain(38, 45), check_if_Ain(38, 46), check_if_Ain(38, 47), check_if_Ain(38, 48),
                      check_if_Ain(38, 49), check_if_Ain(38, 50)], ignore_index=True)
    return data


def check_A39():
    data = pd.concat([check_if_Ain(39, 0), check_if_Ain(39, 1), check_if_Ain(39, 2), check_if_Ain(39, 3),
                      check_if_Ain(39, 4), check_if_Ain(39, 5), check_if_Ain(39, 6), check_if_Ain(39, 7),
                      check_if_Ain(39, 8), check_if_Ain(39, 9), check_if_Ain(39, 10), check_if_Ain(39, 11),
                      check_if_Ain(39, 12), check_if_Ain(39, 13), check_if_Ain(39, 14), check_if_Ain(39, 15),
                      check_if_Ain(39, 16), check_if_Ain(39, 17), check_if_Ain(39, 18), check_if_Ain(39, 19),
                      check_if_Ain(39, 20), check_if_Ain(39, 21), check_if_Ain(39, 22), check_if_Ain(39, 23),
                      check_if_Ain(39, 24), check_if_Ain(39, 25), check_if_Ain(39, 26), check_if_Ain(39, 27),
                      check_if_Ain(39, 28), check_if_Ain(39, 29), check_if_Ain(39, 30), check_if_Ain(39, 31),
                      check_if_Ain(39, 32), check_if_Ain(39, 33), check_if_Ain(39, 34), check_if_Ain(39, 35),
                      check_if_Ain(39, 36), check_if_Ain(39, 37), check_if_Ain(39, 38), check_if_Ain(39, 40),
                      check_if_Ain(39, 41), check_if_Ain(39, 42), check_if_Ain(39, 43), check_if_Ain(39, 44),
                      check_if_Ain(39, 45), check_if_Ain(39, 46), check_if_Ain(39, 47), check_if_Ain(39, 48),
                      check_if_Ain(39, 49), check_if_Ain(39, 50)], ignore_index=True)
    return data


def check_A40():
    data = pd.concat([check_if_Ain(40, 0), check_if_Ain(40, 1), check_if_Ain(40, 2), check_if_Ain(40, 3),
                      check_if_Ain(40, 4), check_if_Ain(40, 5), check_if_Ain(40, 6), check_if_Ain(40, 7),
                      check_if_Ain(40, 8), check_if_Ain(40, 9), check_if_Ain(40, 10), check_if_Ain(40, 11),
                      check_if_Ain(40, 12), check_if_Ain(40, 13), check_if_Ain(40, 14), check_if_Ain(40, 15),
                      check_if_Ain(40, 16), check_if_Ain(40, 17), check_if_Ain(40, 18), check_if_Ain(40, 19),
                      check_if_Ain(40, 20), check_if_Ain(40, 21), check_if_Ain(40, 22), check_if_Ain(40, 23),
                      check_if_Ain(40, 24), check_if_Ain(40, 25), check_if_Ain(40, 26), check_if_Ain(40, 27),
                      check_if_Ain(40, 28), check_if_Ain(40, 29), check_if_Ain(40, 30), check_if_Ain(40, 31),
                      check_if_Ain(40, 32), check_if_Ain(40, 33), check_if_Ain(40, 34), check_if_Ain(40, 35),
                      check_if_Ain(40, 36), check_if_Ain(40, 37), check_if_Ain(40, 38), check_if_Ain(40, 39),
                      check_if_Ain(40, 41), check_if_Ain(40, 42), check_if_Ain(40, 43), check_if_Ain(40, 44),
                      check_if_Ain(40, 45), check_if_Ain(40, 46), check_if_Ain(40, 47), check_if_Ain(40, 48),
                      check_if_Ain(40, 49), check_if_Ain(40, 50)], ignore_index=True)
    return data


def check_A41():
    data = pd.concat([check_if_Ain(41, 0), check_if_Ain(41, 1), check_if_Ain(41, 2), check_if_Ain(41, 3),
                      check_if_Ain(41, 4), check_if_Ain(41, 5), check_if_Ain(41, 6), check_if_Ain(41, 7),
                      check_if_Ain(41, 8), check_if_Ain(41, 9), check_if_Ain(41, 10), check_if_Ain(41, 11),
                      check_if_Ain(41, 12), check_if_Ain(41, 13), check_if_Ain(41, 14), check_if_Ain(41, 15),
                      check_if_Ain(41, 16), check_if_Ain(41, 17), check_if_Ain(41, 18), check_if_Ain(41, 19),
                      check_if_Ain(41, 20), check_if_Ain(41, 21), check_if_Ain(41, 22), check_if_Ain(41, 23),
                      check_if_Ain(41, 24), check_if_Ain(41, 25), check_if_Ain(41, 26), check_if_Ain(41, 27),
                      check_if_Ain(41, 28), check_if_Ain(41, 29), check_if_Ain(41, 30), check_if_Ain(41, 31),
                      check_if_Ain(41, 32), check_if_Ain(41, 33), check_if_Ain(41, 34), check_if_Ain(41, 35),
                      check_if_Ain(41, 36), check_if_Ain(41, 37), check_if_Ain(41, 38), check_if_Ain(41, 39),
                      check_if_Ain(41, 40), check_if_Ain(41, 42), check_if_Ain(41, 43), check_if_Ain(41, 44),
                      check_if_Ain(41, 45), check_if_Ain(41, 46), check_if_Ain(41, 47), check_if_Ain(41, 48),
                      check_if_Ain(41, 49), check_if_Ain(41, 50)], ignore_index=True)
    return data


def check_A42():
    data = pd.concat([check_if_Ain(42, 0), check_if_Ain(42, 1), check_if_Ain(42, 2), check_if_Ain(42, 3),
                      check_if_Ain(42, 4), check_if_Ain(42, 5), check_if_Ain(42, 6), check_if_Ain(42, 7),
                      check_if_Ain(42, 8), check_if_Ain(42, 9), check_if_Ain(42, 10), check_if_Ain(42, 11),
                      check_if_Ain(42, 12), check_if_Ain(42, 13), check_if_Ain(42, 14), check_if_Ain(42, 15),
                      check_if_Ain(42, 16), check_if_Ain(42, 17), check_if_Ain(42, 18), check_if_Ain(42, 19),
                      check_if_Ain(42, 20), check_if_Ain(42, 21), check_if_Ain(42, 22), check_if_Ain(42, 23),
                      check_if_Ain(42, 24), check_if_Ain(42, 25), check_if_Ain(42, 26), check_if_Ain(42, 27),
                      check_if_Ain(42, 28), check_if_Ain(42, 29), check_if_Ain(42, 30), check_if_Ain(42, 31),
                      check_if_Ain(42, 32), check_if_Ain(42, 33), check_if_Ain(42, 34), check_if_Ain(42, 35),
                      check_if_Ain(42, 36), check_if_Ain(42, 37), check_if_Ain(42, 38), check_if_Ain(42, 39),
                      check_if_Ain(42, 40), check_if_Ain(42, 41), check_if_Ain(42, 43), check_if_Ain(42, 44),
                      check_if_Ain(42, 45), check_if_Ain(42, 46), check_if_Ain(42, 47), check_if_Ain(42, 48),
                      check_if_Ain(42, 49), check_if_Ain(42, 50)], ignore_index=True)
    return data


def check_A43():
    data = pd.concat([check_if_Ain(43, 0), check_if_Ain(43, 1), check_if_Ain(43, 2), check_if_Ain(43, 3),
                      check_if_Ain(43, 4), check_if_Ain(43, 5), check_if_Ain(43, 6), check_if_Ain(43, 7),
                      check_if_Ain(43, 8), check_if_Ain(43, 9), check_if_Ain(43, 10), check_if_Ain(43, 11),
                      check_if_Ain(43, 12), check_if_Ain(43, 13), check_if_Ain(43, 14), check_if_Ain(43, 15),
                      check_if_Ain(43, 16), check_if_Ain(43, 17), check_if_Ain(43, 18), check_if_Ain(43, 19),
                      check_if_Ain(43, 20), check_if_Ain(43, 21), check_if_Ain(43, 22), check_if_Ain(43, 23),
                      check_if_Ain(43, 24), check_if_Ain(43, 25), check_if_Ain(43, 26), check_if_Ain(43, 27),
                      check_if_Ain(43, 28), check_if_Ain(43, 29), check_if_Ain(43, 30), check_if_Ain(43, 31),
                      check_if_Ain(43, 32), check_if_Ain(43, 33), check_if_Ain(43, 34), check_if_Ain(43, 35),
                      check_if_Ain(43, 36), check_if_Ain(43, 37), check_if_Ain(43, 38), check_if_Ain(43, 39),
                      check_if_Ain(43, 40), check_if_Ain(43, 41), check_if_Ain(43, 42), check_if_Ain(43, 44),
                      check_if_Ain(43, 45), check_if_Ain(43, 46), check_if_Ain(43, 47), check_if_Ain(43, 48),
                      check_if_Ain(43, 49), check_if_Ain(43, 50)], ignore_index=True)
    return data


def check_A44():
    data = pd.concat([check_if_Ain(44, 0), check_if_Ain(44, 1), check_if_Ain(44, 2), check_if_Ain(44, 3),
                      check_if_Ain(44, 4), check_if_Ain(44, 5), check_if_Ain(44, 6), check_if_Ain(44, 7),
                      check_if_Ain(44, 8), check_if_Ain(44, 9), check_if_Ain(44, 10), check_if_Ain(44, 11),
                      check_if_Ain(44, 12), check_if_Ain(44, 13), check_if_Ain(44, 14), check_if_Ain(44, 15),
                      check_if_Ain(44, 16), check_if_Ain(44, 17), check_if_Ain(44, 18), check_if_Ain(44, 19),
                      check_if_Ain(44, 20), check_if_Ain(44, 21), check_if_Ain(44, 22), check_if_Ain(44, 23),
                      check_if_Ain(44, 24), check_if_Ain(44, 25), check_if_Ain(44, 26), check_if_Ain(44, 27),
                      check_if_Ain(44, 28), check_if_Ain(44, 29), check_if_Ain(44, 30), check_if_Ain(44, 31),
                      check_if_Ain(44, 32), check_if_Ain(44, 33), check_if_Ain(44, 34), check_if_Ain(44, 35),
                      check_if_Ain(44, 36), check_if_Ain(44, 37), check_if_Ain(44, 38), check_if_Ain(44, 39),
                      check_if_Ain(44, 40), check_if_Ain(44, 41), check_if_Ain(44, 42), check_if_Ain(44, 43),
                      check_if_Ain(44, 45), check_if_Ain(44, 46), check_if_Ain(44, 47), check_if_Ain(44, 48),
                      check_if_Ain(44, 49), check_if_Ain(44, 50)], ignore_index=True)
    return data


def check_A45():
    data = pd.concat([check_if_Ain(45, 0), check_if_Ain(45, 1), check_if_Ain(45, 2), check_if_Ain(45, 3),
                      check_if_Ain(45, 4), check_if_Ain(45, 5), check_if_Ain(45, 6), check_if_Ain(45, 7),
                      check_if_Ain(45, 8), check_if_Ain(45, 9), check_if_Ain(45, 10), check_if_Ain(45, 11),
                      check_if_Ain(45, 12), check_if_Ain(45, 13), check_if_Ain(45, 14), check_if_Ain(45, 15),
                      check_if_Ain(45, 16), check_if_Ain(45, 17), check_if_Ain(45, 18), check_if_Ain(45, 19),
                      check_if_Ain(45, 20), check_if_Ain(45, 21), check_if_Ain(45, 22), check_if_Ain(45, 23),
                      check_if_Ain(45, 24), check_if_Ain(45, 25), check_if_Ain(45, 26), check_if_Ain(45, 27),
                      check_if_Ain(45, 28), check_if_Ain(45, 29), check_if_Ain(45, 30), check_if_Ain(45, 31),
                      check_if_Ain(45, 32), check_if_Ain(45, 33), check_if_Ain(45, 34), check_if_Ain(45, 35),
                      check_if_Ain(45, 36), check_if_Ain(45, 37), check_if_Ain(45, 38), check_if_Ain(45, 39),
                      check_if_Ain(45, 40), check_if_Ain(45, 41), check_if_Ain(45, 42), check_if_Ain(45, 43),
                      check_if_Ain(45, 44), check_if_Ain(45, 46), check_if_Ain(45, 47), check_if_Ain(45, 48),
                      check_if_Ain(45, 49), check_if_Ain(45, 50)], ignore_index=True)
    return data


def check_A46():
    data = pd.concat([check_if_Ain(46, 0), check_if_Ain(46, 1), check_if_Ain(46, 2), check_if_Ain(46, 3),
                      check_if_Ain(46, 4), check_if_Ain(46, 5), check_if_Ain(46, 6), check_if_Ain(46, 7),
                      check_if_Ain(46, 8), check_if_Ain(46, 9), check_if_Ain(46, 10), check_if_Ain(46, 11),
                      check_if_Ain(46, 12), check_if_Ain(46, 13), check_if_Ain(46, 14), check_if_Ain(46, 15),
                      check_if_Ain(46, 16), check_if_Ain(46, 17), check_if_Ain(46, 18), check_if_Ain(46, 19),
                      check_if_Ain(46, 20), check_if_Ain(46, 21), check_if_Ain(46, 22), check_if_Ain(46, 23),
                      check_if_Ain(46, 24), check_if_Ain(46, 25), check_if_Ain(46, 26), check_if_Ain(46, 27),
                      check_if_Ain(46, 28), check_if_Ain(46, 29), check_if_Ain(46, 30), check_if_Ain(46, 31),
                      check_if_Ain(46, 32), check_if_Ain(46, 33), check_if_Ain(46, 34), check_if_Ain(46, 35),
                      check_if_Ain(46, 36), check_if_Ain(46, 37), check_if_Ain(46, 38), check_if_Ain(46, 39),
                      check_if_Ain(46, 40), check_if_Ain(46, 41), check_if_Ain(46, 42), check_if_Ain(46, 43),
                      check_if_Ain(46, 44), check_if_Ain(46, 45), check_if_Ain(46, 47), check_if_Ain(46, 48),
                      check_if_Ain(46, 49), check_if_Ain(46, 50)], ignore_index=True)
    return data


def check_A47():
    data = pd.concat([check_if_Ain(47, 0), check_if_Ain(47, 1), check_if_Ain(47, 2), check_if_Ain(47, 3),
                      check_if_Ain(47, 4), check_if_Ain(47, 5), check_if_Ain(47, 6), check_if_Ain(47, 7),
                      check_if_Ain(47, 8), check_if_Ain(47, 9), check_if_Ain(47, 10), check_if_Ain(47, 11),
                      check_if_Ain(47, 12), check_if_Ain(47, 13), check_if_Ain(47, 14), check_if_Ain(47, 15),
                      check_if_Ain(47, 16), check_if_Ain(47, 17), check_if_Ain(47, 18), check_if_Ain(47, 19),
                      check_if_Ain(47, 20), check_if_Ain(47, 21), check_if_Ain(47, 22), check_if_Ain(47, 23),
                      check_if_Ain(47, 24), check_if_Ain(47, 25), check_if_Ain(47, 26), check_if_Ain(47, 27),
                      check_if_Ain(47, 28), check_if_Ain(47, 29), check_if_Ain(47, 30), check_if_Ain(47, 31),
                      check_if_Ain(47, 32), check_if_Ain(47, 33), check_if_Ain(47, 34), check_if_Ain(47, 35),
                      check_if_Ain(47, 36), check_if_Ain(47, 37), check_if_Ain(47, 38), check_if_Ain(47, 39),
                      check_if_Ain(47, 40), check_if_Ain(47, 41), check_if_Ain(47, 42), check_if_Ain(47, 43),
                      check_if_Ain(47, 44), check_if_Ain(47, 45), check_if_Ain(47, 46), check_if_Ain(47, 48),
                      check_if_Ain(47, 49), check_if_Ain(47, 50)], ignore_index=True)
    return data


def check_A48():
    data = pd.concat([check_if_Ain(48, 0), check_if_Ain(48, 1), check_if_Ain(48, 2), check_if_Ain(48, 3),
                      check_if_Ain(48, 4), check_if_Ain(48, 5), check_if_Ain(48, 6), check_if_Ain(48, 7),
                      check_if_Ain(48, 8), check_if_Ain(48, 9), check_if_Ain(48, 10), check_if_Ain(48, 11),
                      check_if_Ain(48, 12), check_if_Ain(48, 13), check_if_Ain(48, 14), check_if_Ain(48, 15),
                      check_if_Ain(48, 16), check_if_Ain(48, 17), check_if_Ain(48, 18), check_if_Ain(48, 19),
                      check_if_Ain(48, 20), check_if_Ain(48, 21), check_if_Ain(48, 22), check_if_Ain(48, 23),
                      check_if_Ain(48, 24), check_if_Ain(48, 25), check_if_Ain(48, 26), check_if_Ain(48, 27),
                      check_if_Ain(48, 28), check_if_Ain(48, 29), check_if_Ain(48, 30), check_if_Ain(48, 31),
                      check_if_Ain(48, 32), check_if_Ain(48, 33), check_if_Ain(48, 34), check_if_Ain(48, 35),
                      check_if_Ain(48, 36), check_if_Ain(48, 37), check_if_Ain(48, 38), check_if_Ain(48, 39),
                      check_if_Ain(48, 40), check_if_Ain(48, 41), check_if_Ain(48, 42), check_if_Ain(48, 43),
                      check_if_Ain(48, 44), check_if_Ain(48, 45), check_if_Ain(48, 46), check_if_Ain(48, 47),
                      check_if_Ain(48, 49), check_if_Ain(48, 50)], ignore_index=True)
    return data


def check_A49():
    data = pd.concat([check_if_Ain(49, 0), check_if_Ain(49, 1), check_if_Ain(49, 2), check_if_Ain(49, 3),
                      check_if_Ain(49, 4), check_if_Ain(49, 5), check_if_Ain(49, 6), check_if_Ain(49, 7),
                      check_if_Ain(49, 8), check_if_Ain(49, 9), check_if_Ain(49, 10), check_if_Ain(49, 11),
                      check_if_Ain(49, 12), check_if_Ain(49, 13), check_if_Ain(49, 14), check_if_Ain(49, 15),
                      check_if_Ain(49, 16), check_if_Ain(49, 17), check_if_Ain(49, 18), check_if_Ain(49, 19),
                      check_if_Ain(49, 20), check_if_Ain(49, 21), check_if_Ain(49, 22), check_if_Ain(49, 23),
                      check_if_Ain(49, 24), check_if_Ain(49, 25), check_if_Ain(49, 26), check_if_Ain(49, 27),
                      check_if_Ain(49, 28), check_if_Ain(49, 29), check_if_Ain(49, 30), check_if_Ain(49, 31),
                      check_if_Ain(49, 32), check_if_Ain(49, 33), check_if_Ain(49, 34), check_if_Ain(49, 35),
                      check_if_Ain(49, 36), check_if_Ain(49, 37), check_if_Ain(49, 38), check_if_Ain(49, 39),
                      check_if_Ain(49, 40), check_if_Ain(49, 41), check_if_Ain(49, 42), check_if_Ain(49, 43),
                      check_if_Ain(49, 44), check_if_Ain(49, 45), check_if_Ain(49, 46), check_if_Ain(49, 47),
                      check_if_Ain(49, 48), check_if_Ain(49, 50)], ignore_index=True)
    return data


def check_A50():
    data = pd.concat([check_if_Ain(50, 0), check_if_Ain(50, 1), check_if_Ain(50, 2), check_if_Ain(50, 3),
                      check_if_Ain(50, 4), check_if_Ain(50, 5), check_if_Ain(50, 6), check_if_Ain(50, 7),
                      check_if_Ain(50, 8), check_if_Ain(50, 9), check_if_Ain(50, 10), check_if_Ain(50, 11),
                      check_if_Ain(50, 12), check_if_Ain(50, 13), check_if_Ain(50, 14), check_if_Ain(50, 15),
                      check_if_Ain(50, 16), check_if_Ain(50, 17), check_if_Ain(50, 18), check_if_Ain(50, 19),
                      check_if_Ain(50, 20), check_if_Ain(50, 21), check_if_Ain(50, 22), check_if_Ain(50, 23),
                      check_if_Ain(50, 24), check_if_Ain(50, 25), check_if_Ain(50, 26), check_if_Ain(50, 27),
                      check_if_Ain(50, 28), check_if_Ain(50, 29), check_if_Ain(50, 30), check_if_Ain(50, 31),
                      check_if_Ain(50, 32), check_if_Ain(50, 33), check_if_Ain(50, 34), check_if_Ain(50, 35),
                      check_if_Ain(50, 36), check_if_Ain(50, 37), check_if_Ain(50, 38), check_if_Ain(50, 39),
                      check_if_Ain(50, 40), check_if_Ain(50, 41), check_if_Ain(50, 42), check_if_Ain(50, 43),
                      check_if_Ain(50, 44), check_if_Ain(50, 45), check_if_Ain(50, 46), check_if_Ain(50, 47),
                      check_if_Ain(50, 48), check_if_Ain(50, 49)], ignore_index=True)
    return data


def check():
    data = pd.concat([check_A1(), check_A2(), check_A3(), check_A4(),
                      check_A5(), check_A6(), check_A7(), check_A8(),
                      check_A9(), check_A10(), check_A11(), check_A12(),
                      check_A13(), check_A14(), check_A15(), check_A16(),
                      check_A17(), check_A18(), check_A19(), check_A20(),
                      check_A21(), check_A22(), check_A23(), check_A24(),
                      check_A25(), check_A26(), check_A27(), check_A28(),
                      check_A29(), check_A30(), check_A31(), check_A32(),
                      check_A33(), check_A34(), check_A35(), check_A36(),
                      check_A37(), check_A38(), check_A39(), check_A40(),
                      check_A41(), check_A42(), check_A43(), check_A44(),
                      check_A45(), check_A46(), check_A47(), check_A48(),
                      check_A49(), check_A50()], ignore_index=True)
    return data


def check_A_csv():
    data = check()
    string1 = "/Pycharm/HumanActivityRecognition/check"
    string2 = string1 + "/check_A" + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


check_A_csv()
