import os

import numpy as np
import pandas as pd

from CreateWord import create_word


def check_if_Din(x, y):
    d = create_word(x, 'D')['words']
    word_to_keep = np.array(create_word(y, 'D')['words'])
    df = pd.DataFrame(np.array(d[d.isin(word_to_keep)]), columns=['words'])
    return df


def check_D0():
    data = pd.concat([check_if_Din(0, 1), check_if_Din(0, 2), check_if_Din(0, 3), check_if_Din(0, 4),
                      check_if_Din(0, 5), check_if_Din(0, 6), check_if_Din(0, 7), check_if_Din(0, 8),
                      check_if_Din(0, 9), check_if_Din(0, 10), check_if_Din(0, 11), check_if_Din(0, 12),
                      check_if_Din(0, 13), check_if_Din(0, 14), check_if_Din(0, 15), check_if_Din(0, 16),
                      check_if_Din(0, 17), check_if_Din(0, 18), check_if_Din(0, 19), check_if_Din(0, 20),
                      check_if_Din(0, 21), check_if_Din(0, 22), check_if_Din(0, 23), check_if_Din(0, 24),
                      check_if_Din(0, 25), check_if_Din(0, 26), check_if_Din(0, 27), check_if_Din(0, 28),
                      check_if_Din(0, 29), check_if_Din(0, 30), check_if_Din(0, 31), check_if_Din(0, 32),
                      check_if_Din(0, 33), check_if_Din(0, 34), check_if_Din(0, 35), check_if_Din(0, 36),
                      check_if_Din(0, 37), check_if_Din(0, 38), check_if_Din(0, 39), check_if_Din(0, 40),
                      check_if_Din(0, 41), check_if_Din(0, 42), check_if_Din(0, 43), check_if_Din(0, 44),
                      check_if_Din(0, 45), check_if_Din(0, 46), check_if_Din(0, 47), check_if_Din(0, 48),
                      check_if_Din(0, 49), check_if_Din(0, 50)], ignore_index=True)
    return data


def check_D1():
    data = pd.concat([check_if_Din(1, 0), check_if_Din(1, 2), check_if_Din(1, 3), check_if_Din(1, 4),
                      check_if_Din(1, 5), check_if_Din(1, 6), check_if_Din(1, 7), check_if_Din(1, 8),
                      check_if_Din(1, 9), check_if_Din(1, 10), check_if_Din(1, 11), check_if_Din(1, 12),
                      check_if_Din(1, 13), check_if_Din(1, 14), check_if_Din(1, 15), check_if_Din(1, 16),
                      check_if_Din(1, 17), check_if_Din(1, 18), check_if_Din(1, 19), check_if_Din(1, 20),
                      check_if_Din(1, 21), check_if_Din(1, 22), check_if_Din(1, 23), check_if_Din(1, 24),
                      check_if_Din(1, 25), check_if_Din(1, 26), check_if_Din(1, 27), check_if_Din(1, 28),
                      check_if_Din(1, 29), check_if_Din(1, 30), check_if_Din(1, 31), check_if_Din(1, 32),
                      check_if_Din(1, 33), check_if_Din(1, 34), check_if_Din(1, 35), check_if_Din(1, 36),
                      check_if_Din(1, 37), check_if_Din(1, 38), check_if_Din(1, 39), check_if_Din(1, 40),
                      check_if_Din(1, 41), check_if_Din(1, 42), check_if_Din(1, 43), check_if_Din(1, 44),
                      check_if_Din(1, 45), check_if_Din(1, 46), check_if_Din(1, 47), check_if_Din(1, 48),
                      check_if_Din(1, 49), check_if_Din(1, 50)], ignore_index=True)
    return data


def check_D2():
    data = pd.concat([check_if_Din(2, 0), check_if_Din(2, 1), check_if_Din(2, 3), check_if_Din(2, 4),
                      check_if_Din(2, 5), check_if_Din(2, 6), check_if_Din(2, 7), check_if_Din(2, 8),
                      check_if_Din(2, 9), check_if_Din(2, 10), check_if_Din(2, 11), check_if_Din(2, 12),
                      check_if_Din(2, 13), check_if_Din(2, 14), check_if_Din(2, 15), check_if_Din(2, 16),
                      check_if_Din(2, 17), check_if_Din(2, 18), check_if_Din(2, 19), check_if_Din(2, 20),
                      check_if_Din(2, 21), check_if_Din(2, 22), check_if_Din(2, 23), check_if_Din(2, 24),
                      check_if_Din(2, 25), check_if_Din(2, 26), check_if_Din(2, 27), check_if_Din(2, 28),
                      check_if_Din(2, 29), check_if_Din(2, 30), check_if_Din(2, 31), check_if_Din(2, 32),
                      check_if_Din(2, 33), check_if_Din(2, 34), check_if_Din(2, 35), check_if_Din(2, 36),
                      check_if_Din(2, 37), check_if_Din(2, 38), check_if_Din(2, 39), check_if_Din(2, 40),
                      check_if_Din(2, 41), check_if_Din(2, 42), check_if_Din(2, 43), check_if_Din(2, 44),
                      check_if_Din(2, 45), check_if_Din(2, 46), check_if_Din(2, 47), check_if_Din(2, 48),
                      check_if_Din(2, 49), check_if_Din(2, 50)], ignore_index=True)
    return data


def check_D3():
    data = pd.concat([check_if_Din(3, 0), check_if_Din(3, 1), check_if_Din(3, 2), check_if_Din(3, 4),
                      check_if_Din(3, 5), check_if_Din(3, 6), check_if_Din(3, 7), check_if_Din(3, 8),
                      check_if_Din(3, 9), check_if_Din(3, 10), check_if_Din(3, 11), check_if_Din(3, 12),
                      check_if_Din(3, 13), check_if_Din(3, 14), check_if_Din(3, 15), check_if_Din(3, 16),
                      check_if_Din(3, 17), check_if_Din(3, 18), check_if_Din(3, 19), check_if_Din(3, 20),
                      check_if_Din(3, 21), check_if_Din(3, 22), check_if_Din(3, 23), check_if_Din(3, 24),
                      check_if_Din(3, 25), check_if_Din(3, 26), check_if_Din(3, 27), check_if_Din(3, 28),
                      check_if_Din(3, 29), check_if_Din(3, 30), check_if_Din(3, 31), check_if_Din(3, 32),
                      check_if_Din(3, 33), check_if_Din(3, 34), check_if_Din(3, 35), check_if_Din(3, 36),
                      check_if_Din(3, 37), check_if_Din(3, 38), check_if_Din(3, 39), check_if_Din(3, 40),
                      check_if_Din(3, 41), check_if_Din(3, 42), check_if_Din(3, 43), check_if_Din(3, 44),
                      check_if_Din(3, 45), check_if_Din(3, 46), check_if_Din(3, 47), check_if_Din(3, 48),
                      check_if_Din(3, 49), check_if_Din(3, 50)], ignore_index=True)
    return data


def check_D4():
    data = pd.concat([check_if_Din(4, 0), check_if_Din(4, 1), check_if_Din(4, 2), check_if_Din(4, 3),
                      check_if_Din(4, 5), check_if_Din(4, 6), check_if_Din(4, 7), check_if_Din(4, 8),
                      check_if_Din(4, 9), check_if_Din(4, 10), check_if_Din(4, 11), check_if_Din(4, 12),
                      check_if_Din(4, 13), check_if_Din(4, 14), check_if_Din(4, 15), check_if_Din(4, 16),
                      check_if_Din(4, 17), check_if_Din(4, 18), check_if_Din(4, 19), check_if_Din(4, 20),
                      check_if_Din(4, 21), check_if_Din(4, 22), check_if_Din(4, 23), check_if_Din(4, 24),
                      check_if_Din(4, 25), check_if_Din(4, 26), check_if_Din(4, 27), check_if_Din(4, 28),
                      check_if_Din(4, 29), check_if_Din(4, 30), check_if_Din(4, 31), check_if_Din(4, 32),
                      check_if_Din(4, 33), check_if_Din(4, 34), check_if_Din(4, 35), check_if_Din(4, 36),
                      check_if_Din(4, 37), check_if_Din(4, 38), check_if_Din(4, 39), check_if_Din(4, 40),
                      check_if_Din(4, 41), check_if_Din(4, 42), check_if_Din(4, 43), check_if_Din(4, 44),
                      check_if_Din(4, 45), check_if_Din(4, 46), check_if_Din(4, 47), check_if_Din(4, 48),
                      check_if_Din(4, 49), check_if_Din(4, 50)], ignore_index=True)
    return data


def check_D5():
    data = pd.concat([check_if_Din(5, 0), check_if_Din(5, 1), check_if_Din(5, 2), check_if_Din(5, 3),
                      check_if_Din(5, 4), check_if_Din(5, 6), check_if_Din(5, 7), check_if_Din(5, 8),
                      check_if_Din(5, 9), check_if_Din(5, 10), check_if_Din(5, 11), check_if_Din(5, 12),
                      check_if_Din(5, 13), check_if_Din(5, 14), check_if_Din(5, 15), check_if_Din(5, 16),
                      check_if_Din(5, 17), check_if_Din(5, 18), check_if_Din(5, 19), check_if_Din(5, 20),
                      check_if_Din(5, 21), check_if_Din(5, 22), check_if_Din(5, 23), check_if_Din(5, 24),
                      check_if_Din(5, 25), check_if_Din(5, 26), check_if_Din(5, 27), check_if_Din(5, 28),
                      check_if_Din(5, 29), check_if_Din(5, 30), check_if_Din(5, 31), check_if_Din(5, 32),
                      check_if_Din(5, 33), check_if_Din(5, 34), check_if_Din(5, 35), check_if_Din(5, 36),
                      check_if_Din(5, 37), check_if_Din(5, 38), check_if_Din(5, 39), check_if_Din(5, 40),
                      check_if_Din(5, 41), check_if_Din(5, 42), check_if_Din(5, 43), check_if_Din(5, 44),
                      check_if_Din(5, 45), check_if_Din(5, 46), check_if_Din(5, 47), check_if_Din(5, 48),
                      check_if_Din(5, 49), check_if_Din(5, 50)], ignore_index=True)
    return data


def check_D6():
    data = pd.concat([check_if_Din(6, 0), check_if_Din(6, 1), check_if_Din(6, 2), check_if_Din(6, 3),
                      check_if_Din(6, 4), check_if_Din(6, 5), check_if_Din(6, 7), check_if_Din(6, 8),
                      check_if_Din(6, 9), check_if_Din(6, 10), check_if_Din(6, 11), check_if_Din(6, 12),
                      check_if_Din(6, 13), check_if_Din(6, 14), check_if_Din(6, 15), check_if_Din(6, 16),
                      check_if_Din(6, 17), check_if_Din(6, 18), check_if_Din(6, 19), check_if_Din(6, 20),
                      check_if_Din(6, 21), check_if_Din(6, 22), check_if_Din(6, 23), check_if_Din(6, 24),
                      check_if_Din(6, 25), check_if_Din(6, 26), check_if_Din(6, 27), check_if_Din(6, 28),
                      check_if_Din(6, 29), check_if_Din(6, 30), check_if_Din(6, 31), check_if_Din(6, 32),
                      check_if_Din(6, 33), check_if_Din(6, 34), check_if_Din(6, 35), check_if_Din(6, 36),
                      check_if_Din(6, 37), check_if_Din(6, 38), check_if_Din(6, 39), check_if_Din(6, 40),
                      check_if_Din(6, 41), check_if_Din(6, 42), check_if_Din(6, 43), check_if_Din(6, 44),
                      check_if_Din(6, 45), check_if_Din(6, 46), check_if_Din(6, 47), check_if_Din(6, 48),
                      check_if_Din(6, 49), check_if_Din(6, 50)], ignore_index=True)
    return data


def check_D7():
    data = pd.concat([check_if_Din(7, 0), check_if_Din(7, 1), check_if_Din(7, 2), check_if_Din(7, 3),
                      check_if_Din(7, 4), check_if_Din(7, 5), check_if_Din(7, 6), check_if_Din(7, 8),
                      check_if_Din(7, 9), check_if_Din(7, 10), check_if_Din(7, 11), check_if_Din(7, 12),
                      check_if_Din(7, 13), check_if_Din(7, 14), check_if_Din(7, 15), check_if_Din(7, 16),
                      check_if_Din(7, 17), check_if_Din(7, 18), check_if_Din(7, 19), check_if_Din(7, 20),
                      check_if_Din(7, 21), check_if_Din(7, 22), check_if_Din(7, 23), check_if_Din(7, 24),
                      check_if_Din(7, 25), check_if_Din(7, 26), check_if_Din(7, 27), check_if_Din(7, 28),
                      check_if_Din(7, 29), check_if_Din(7, 30), check_if_Din(7, 31), check_if_Din(7, 32),
                      check_if_Din(7, 33), check_if_Din(7, 34), check_if_Din(7, 35), check_if_Din(7, 36),
                      check_if_Din(7, 37), check_if_Din(7, 38), check_if_Din(7, 39), check_if_Din(7, 40),
                      check_if_Din(7, 41), check_if_Din(7, 42), check_if_Din(7, 43), check_if_Din(7, 44),
                      check_if_Din(7, 45), check_if_Din(7, 46), check_if_Din(7, 47), check_if_Din(7, 48),
                      check_if_Din(7, 49), check_if_Din(7, 50)], ignore_index=True)
    return data


def check_D8():
    data = pd.concat([check_if_Din(8, 0), check_if_Din(8, 1), check_if_Din(8, 2), check_if_Din(8, 3),
                      check_if_Din(8, 4), check_if_Din(8, 5), check_if_Din(8, 6), check_if_Din(8, 7),
                      check_if_Din(8, 9), check_if_Din(8, 10), check_if_Din(8, 11), check_if_Din(8, 12),
                      check_if_Din(8, 13), check_if_Din(8, 14), check_if_Din(8, 15), check_if_Din(8, 16),
                      check_if_Din(8, 17), check_if_Din(8, 18), check_if_Din(8, 19), check_if_Din(8, 20),
                      check_if_Din(8, 21), check_if_Din(8, 22), check_if_Din(8, 23), check_if_Din(8, 24),
                      check_if_Din(8, 25), check_if_Din(8, 26), check_if_Din(8, 27), check_if_Din(8, 28),
                      check_if_Din(8, 29), check_if_Din(8, 30), check_if_Din(8, 31), check_if_Din(8, 32),
                      check_if_Din(8, 33), check_if_Din(8, 34), check_if_Din(8, 35), check_if_Din(8, 36),
                      check_if_Din(8, 37), check_if_Din(8, 38), check_if_Din(8, 39), check_if_Din(8, 40),
                      check_if_Din(8, 41), check_if_Din(8, 42), check_if_Din(8, 43), check_if_Din(8, 44),
                      check_if_Din(8, 45), check_if_Din(8, 46), check_if_Din(8, 47), check_if_Din(8, 48),
                      check_if_Din(8, 49), check_if_Din(8, 50)], ignore_index=True)
    return data


def check_D9():
    data = pd.concat([check_if_Din(9, 0), check_if_Din(9, 1), check_if_Din(9, 2), check_if_Din(9, 3),
                      check_if_Din(9, 4), check_if_Din(9, 5), check_if_Din(9, 6), check_if_Din(9, 7),
                      check_if_Din(9, 8), check_if_Din(9, 10), check_if_Din(9, 11), check_if_Din(9, 12),
                      check_if_Din(9, 13), check_if_Din(9, 14), check_if_Din(9, 15), check_if_Din(9, 16),
                      check_if_Din(9, 17), check_if_Din(9, 18), check_if_Din(9, 19), check_if_Din(9, 20),
                      check_if_Din(9, 21), check_if_Din(9, 22), check_if_Din(9, 23), check_if_Din(9, 24),
                      check_if_Din(9, 25), check_if_Din(9, 26), check_if_Din(9, 27), check_if_Din(9, 28),
                      check_if_Din(9, 29), check_if_Din(9, 30), check_if_Din(9, 31), check_if_Din(9, 32),
                      check_if_Din(9, 33), check_if_Din(9, 34), check_if_Din(9, 35), check_if_Din(9, 36),
                      check_if_Din(9, 37), check_if_Din(9, 38), check_if_Din(9, 39), check_if_Din(9, 40),
                      check_if_Din(9, 41), check_if_Din(9, 42), check_if_Din(9, 43), check_if_Din(9, 44),
                      check_if_Din(9, 45), check_if_Din(9, 46), check_if_Din(9, 47), check_if_Din(9, 48),
                      check_if_Din(9, 49), check_if_Din(9, 50)], ignore_index=True)
    return data


def check_D10():
    data = pd.concat([check_if_Din(10, 0), check_if_Din(10, 1), check_if_Din(10, 2), check_if_Din(10, 3),
                      check_if_Din(10, 4), check_if_Din(10, 5), check_if_Din(10, 6), check_if_Din(10, 7),
                      check_if_Din(10, 8), check_if_Din(10, 9), check_if_Din(10, 11), check_if_Din(10, 12),
                      check_if_Din(10, 13), check_if_Din(10, 14), check_if_Din(10, 15), check_if_Din(10, 16),
                      check_if_Din(10, 17), check_if_Din(10, 18), check_if_Din(10, 19), check_if_Din(10, 20),
                      check_if_Din(10, 21), check_if_Din(10, 22), check_if_Din(10, 23), check_if_Din(10, 24),
                      check_if_Din(10, 25), check_if_Din(10, 26), check_if_Din(10, 27), check_if_Din(10, 28),
                      check_if_Din(10, 29), check_if_Din(10, 30), check_if_Din(10, 31), check_if_Din(10, 32),
                      check_if_Din(10, 33), check_if_Din(10, 34), check_if_Din(10, 35), check_if_Din(10, 36),
                      check_if_Din(10, 37), check_if_Din(10, 38), check_if_Din(10, 39), check_if_Din(10, 40),
                      check_if_Din(10, 41), check_if_Din(10, 42), check_if_Din(10, 43), check_if_Din(10, 44),
                      check_if_Din(10, 45), check_if_Din(10, 46), check_if_Din(10, 47), check_if_Din(10, 48),
                      check_if_Din(10, 49), check_if_Din(10, 50)], ignore_index=True)
    return data


def check_D11():
    data = pd.concat([check_if_Din(11, 0), check_if_Din(11, 1), check_if_Din(11, 2), check_if_Din(11, 3),
                      check_if_Din(11, 4), check_if_Din(11, 5), check_if_Din(11, 6), check_if_Din(11, 7),
                      check_if_Din(11, 8), check_if_Din(11, 9), check_if_Din(11, 10), check_if_Din(11, 12),
                      check_if_Din(11, 13), check_if_Din(11, 14), check_if_Din(11, 15), check_if_Din(11, 16),
                      check_if_Din(11, 17), check_if_Din(11, 18), check_if_Din(11, 19), check_if_Din(11, 20),
                      check_if_Din(11, 21), check_if_Din(11, 22), check_if_Din(11, 23), check_if_Din(11, 24),
                      check_if_Din(11, 25), check_if_Din(11, 26), check_if_Din(11, 27), check_if_Din(11, 28),
                      check_if_Din(11, 29), check_if_Din(11, 30), check_if_Din(11, 31), check_if_Din(11, 32),
                      check_if_Din(11, 33), check_if_Din(11, 34), check_if_Din(11, 35), check_if_Din(11, 36),
                      check_if_Din(11, 37), check_if_Din(11, 38), check_if_Din(11, 39), check_if_Din(11, 40),
                      check_if_Din(11, 41), check_if_Din(11, 42), check_if_Din(11, 43), check_if_Din(11, 44),
                      check_if_Din(11, 45), check_if_Din(11, 46), check_if_Din(11, 47), check_if_Din(11, 48),
                      check_if_Din(11, 49), check_if_Din(11, 50)], ignore_index=True)
    return data


def check_D12():
    data = pd.concat([check_if_Din(12, 0), check_if_Din(12, 1), check_if_Din(12, 2), check_if_Din(12, 3),
                      check_if_Din(12, 4), check_if_Din(12, 5), check_if_Din(12, 6), check_if_Din(12, 7),
                      check_if_Din(12, 8), check_if_Din(12, 9), check_if_Din(12, 10), check_if_Din(12, 11),
                      check_if_Din(12, 13), check_if_Din(12, 14), check_if_Din(12, 15), check_if_Din(12, 16),
                      check_if_Din(12, 17), check_if_Din(12, 18), check_if_Din(12, 19), check_if_Din(12, 20),
                      check_if_Din(12, 21), check_if_Din(12, 22), check_if_Din(12, 23), check_if_Din(12, 24),
                      check_if_Din(12, 25), check_if_Din(12, 26), check_if_Din(12, 27), check_if_Din(12, 28),
                      check_if_Din(12, 29), check_if_Din(12, 30), check_if_Din(12, 31), check_if_Din(12, 32),
                      check_if_Din(12, 33), check_if_Din(12, 34), check_if_Din(12, 35), check_if_Din(12, 36),
                      check_if_Din(12, 37), check_if_Din(12, 38), check_if_Din(12, 39), check_if_Din(12, 40),
                      check_if_Din(12, 41), check_if_Din(12, 42), check_if_Din(12, 43), check_if_Din(12, 44),
                      check_if_Din(12, 45), check_if_Din(12, 46), check_if_Din(12, 47), check_if_Din(12, 48),
                      check_if_Din(12, 49), check_if_Din(12, 50)], ignore_index=True)
    return data


def check_D13():
    data = pd.concat([check_if_Din(13, 0), check_if_Din(13, 1), check_if_Din(13, 2), check_if_Din(13, 3),
                      check_if_Din(13, 4), check_if_Din(13, 5), check_if_Din(13, 6), check_if_Din(13, 7),
                      check_if_Din(13, 8), check_if_Din(13, 9), check_if_Din(13, 10), check_if_Din(13, 11),
                      check_if_Din(13, 12), check_if_Din(13, 14), check_if_Din(13, 15), check_if_Din(13, 16),
                      check_if_Din(13, 17), check_if_Din(13, 18), check_if_Din(13, 19), check_if_Din(13, 20),
                      check_if_Din(13, 21), check_if_Din(13, 22), check_if_Din(13, 23), check_if_Din(13, 24),
                      check_if_Din(13, 25), check_if_Din(13, 26), check_if_Din(13, 27), check_if_Din(13, 28),
                      check_if_Din(13, 29), check_if_Din(13, 30), check_if_Din(13, 31), check_if_Din(13, 32),
                      check_if_Din(13, 33), check_if_Din(13, 34), check_if_Din(13, 35), check_if_Din(13, 36),
                      check_if_Din(13, 37), check_if_Din(13, 38), check_if_Din(13, 39), check_if_Din(13, 40),
                      check_if_Din(13, 41), check_if_Din(13, 42), check_if_Din(13, 43), check_if_Din(13, 44),
                      check_if_Din(13, 45), check_if_Din(13, 46), check_if_Din(13, 47), check_if_Din(13, 48),
                      check_if_Din(13, 49), check_if_Din(13, 50)], ignore_index=True)
    return data


def check_D14():
    data = pd.concat([check_if_Din(14, 0), check_if_Din(14, 1), check_if_Din(14, 2), check_if_Din(14, 3),
                      check_if_Din(14, 4), check_if_Din(14, 5), check_if_Din(14, 6), check_if_Din(14, 7),
                      check_if_Din(14, 8), check_if_Din(14, 9), check_if_Din(14, 10), check_if_Din(14, 11),
                      check_if_Din(14, 12), check_if_Din(14, 13), check_if_Din(14, 15), check_if_Din(14, 16),
                      check_if_Din(14, 17), check_if_Din(14, 18), check_if_Din(14, 19), check_if_Din(14, 20),
                      check_if_Din(14, 21), check_if_Din(14, 22), check_if_Din(14, 23), check_if_Din(14, 24),
                      check_if_Din(14, 25), check_if_Din(14, 26), check_if_Din(14, 27), check_if_Din(14, 28),
                      check_if_Din(14, 29), check_if_Din(14, 30), check_if_Din(14, 31), check_if_Din(14, 32),
                      check_if_Din(14, 33), check_if_Din(14, 34), check_if_Din(14, 35), check_if_Din(14, 36),
                      check_if_Din(14, 37), check_if_Din(14, 38), check_if_Din(14, 39), check_if_Din(14, 40),
                      check_if_Din(14, 41), check_if_Din(14, 42), check_if_Din(14, 43), check_if_Din(14, 44),
                      check_if_Din(14, 45), check_if_Din(14, 46), check_if_Din(14, 47), check_if_Din(14, 48),
                      check_if_Din(14, 49), check_if_Din(14, 50)], ignore_index=True)
    return data


def check_D15():
    data = pd.concat([check_if_Din(15, 0), check_if_Din(15, 1), check_if_Din(15, 2), check_if_Din(15, 3),
                      check_if_Din(15, 4), check_if_Din(15, 5), check_if_Din(15, 6), check_if_Din(15, 7),
                      check_if_Din(15, 8), check_if_Din(15, 9), check_if_Din(15, 10), check_if_Din(15, 11),
                      check_if_Din(15, 12), check_if_Din(15, 13), check_if_Din(15, 14), check_if_Din(15, 16),
                      check_if_Din(15, 17), check_if_Din(15, 18), check_if_Din(15, 19), check_if_Din(15, 20),
                      check_if_Din(15, 21), check_if_Din(15, 22), check_if_Din(15, 23), check_if_Din(15, 24),
                      check_if_Din(15, 25), check_if_Din(15, 26), check_if_Din(15, 27), check_if_Din(15, 28),
                      check_if_Din(15, 29), check_if_Din(15, 30), check_if_Din(15, 31), check_if_Din(15, 32),
                      check_if_Din(15, 33), check_if_Din(15, 34), check_if_Din(15, 35), check_if_Din(15, 36),
                      check_if_Din(15, 37), check_if_Din(15, 38), check_if_Din(15, 39), check_if_Din(15, 40),
                      check_if_Din(15, 41), check_if_Din(15, 42), check_if_Din(15, 43), check_if_Din(15, 44),
                      check_if_Din(15, 45), check_if_Din(15, 46), check_if_Din(15, 47), check_if_Din(15, 48),
                      check_if_Din(15, 49), check_if_Din(15, 50)], ignore_index=True)
    return data


def check_D16():
    data = pd.concat([check_if_Din(16, 0), check_if_Din(16, 1), check_if_Din(16, 2), check_if_Din(16, 3),
                      check_if_Din(16, 4), check_if_Din(16, 5), check_if_Din(16, 6), check_if_Din(16, 7),
                      check_if_Din(16, 8), check_if_Din(16, 9), check_if_Din(16, 10), check_if_Din(16, 11),
                      check_if_Din(16, 12), check_if_Din(16, 13), check_if_Din(16, 14), check_if_Din(16, 15),
                      check_if_Din(16, 17), check_if_Din(16, 18), check_if_Din(16, 19), check_if_Din(16, 20),
                      check_if_Din(16, 21), check_if_Din(16, 22), check_if_Din(16, 23), check_if_Din(16, 24),
                      check_if_Din(16, 25), check_if_Din(16, 26), check_if_Din(16, 27), check_if_Din(16, 28),
                      check_if_Din(16, 29), check_if_Din(16, 30), check_if_Din(16, 31), check_if_Din(16, 32),
                      check_if_Din(16, 33), check_if_Din(16, 34), check_if_Din(16, 35), check_if_Din(16, 36),
                      check_if_Din(16, 37), check_if_Din(16, 38), check_if_Din(16, 39), check_if_Din(16, 40),
                      check_if_Din(16, 41), check_if_Din(16, 42), check_if_Din(16, 43), check_if_Din(16, 44),
                      check_if_Din(16, 45), check_if_Din(16, 46), check_if_Din(16, 47), check_if_Din(16, 48),
                      check_if_Din(16, 49), check_if_Din(16, 50)], ignore_index=True)
    return data


def check_D17():
    data = pd.concat([check_if_Din(17, 0), check_if_Din(17, 1), check_if_Din(17, 2), check_if_Din(17, 3),
                      check_if_Din(17, 4), check_if_Din(17, 5), check_if_Din(17, 6), check_if_Din(17, 7),
                      check_if_Din(17, 8), check_if_Din(17, 9), check_if_Din(17, 10), check_if_Din(17, 11),
                      check_if_Din(17, 12), check_if_Din(17, 13), check_if_Din(17, 14), check_if_Din(17, 15),
                      check_if_Din(17, 16), check_if_Din(17, 18), check_if_Din(17, 19), check_if_Din(17, 20),
                      check_if_Din(17, 21), check_if_Din(17, 22), check_if_Din(17, 23), check_if_Din(17, 24),
                      check_if_Din(17, 25), check_if_Din(17, 26), check_if_Din(17, 27), check_if_Din(17, 28),
                      check_if_Din(17, 29), check_if_Din(17, 30), check_if_Din(17, 31), check_if_Din(17, 32),
                      check_if_Din(17, 33), check_if_Din(17, 34), check_if_Din(17, 35), check_if_Din(17, 36),
                      check_if_Din(17, 37), check_if_Din(17, 38), check_if_Din(17, 39), check_if_Din(17, 40),
                      check_if_Din(17, 41), check_if_Din(17, 42), check_if_Din(17, 43), check_if_Din(17, 44),
                      check_if_Din(17, 45), check_if_Din(17, 46), check_if_Din(17, 47), check_if_Din(17, 48),
                      check_if_Din(17, 49), check_if_Din(17, 50)], ignore_index=True)
    return data


def check_D18():
    data = pd.concat([check_if_Din(18, 0), check_if_Din(18, 1), check_if_Din(18, 2), check_if_Din(18, 3),
                      check_if_Din(18, 4), check_if_Din(18, 5), check_if_Din(18, 6), check_if_Din(18, 7),
                      check_if_Din(18, 8), check_if_Din(18, 9), check_if_Din(18, 10), check_if_Din(18, 11),
                      check_if_Din(18, 12), check_if_Din(18, 13), check_if_Din(18, 14), check_if_Din(18, 15),
                      check_if_Din(18, 16), check_if_Din(18, 17), check_if_Din(18, 19), check_if_Din(18, 20),
                      check_if_Din(18, 21), check_if_Din(18, 22), check_if_Din(18, 23), check_if_Din(18, 24),
                      check_if_Din(18, 25), check_if_Din(18, 26), check_if_Din(18, 27), check_if_Din(18, 28),
                      check_if_Din(18, 29), check_if_Din(18, 30), check_if_Din(18, 31), check_if_Din(18, 32),
                      check_if_Din(18, 33), check_if_Din(18, 34), check_if_Din(18, 35), check_if_Din(18, 36),
                      check_if_Din(18, 37), check_if_Din(18, 38), check_if_Din(18, 39), check_if_Din(18, 40),
                      check_if_Din(18, 41), check_if_Din(18, 42), check_if_Din(18, 43), check_if_Din(18, 44),
                      check_if_Din(18, 45), check_if_Din(18, 46), check_if_Din(18, 47), check_if_Din(18, 48),
                      check_if_Din(18, 49), check_if_Din(18, 50)], ignore_index=True)
    return data


def check_D19():
    data = pd.concat([check_if_Din(19, 0), check_if_Din(19, 1), check_if_Din(19, 2), check_if_Din(19, 3),
                      check_if_Din(19, 4), check_if_Din(19, 5), check_if_Din(19, 6), check_if_Din(19, 7),
                      check_if_Din(19, 8), check_if_Din(19, 9), check_if_Din(19, 10), check_if_Din(19, 11),
                      check_if_Din(19, 12), check_if_Din(19, 13), check_if_Din(19, 14), check_if_Din(19, 15),
                      check_if_Din(19, 16), check_if_Din(19, 17), check_if_Din(19, 18), check_if_Din(19, 20),
                      check_if_Din(19, 21), check_if_Din(19, 22), check_if_Din(19, 23), check_if_Din(19, 24),
                      check_if_Din(19, 25), check_if_Din(19, 26), check_if_Din(19, 27), check_if_Din(19, 28),
                      check_if_Din(19, 29), check_if_Din(19, 30), check_if_Din(19, 31), check_if_Din(19, 32),
                      check_if_Din(19, 33), check_if_Din(19, 34), check_if_Din(19, 35), check_if_Din(19, 36),
                      check_if_Din(19, 37), check_if_Din(19, 38), check_if_Din(19, 39), check_if_Din(19, 40),
                      check_if_Din(19, 41), check_if_Din(19, 42), check_if_Din(19, 43), check_if_Din(19, 44),
                      check_if_Din(19, 45), check_if_Din(19, 46), check_if_Din(19, 47), check_if_Din(19, 48),
                      check_if_Din(19, 49), check_if_Din(19, 50)], ignore_index=True)
    return data


def check_D20():
    data = pd.concat([check_if_Din(20, 0), check_if_Din(20, 1), check_if_Din(20, 2), check_if_Din(20, 3),
                      check_if_Din(20, 4), check_if_Din(20, 5), check_if_Din(20, 6), check_if_Din(20, 7),
                      check_if_Din(20, 8), check_if_Din(20, 9), check_if_Din(20, 10), check_if_Din(20, 11),
                      check_if_Din(20, 12), check_if_Din(20, 13), check_if_Din(20, 14), check_if_Din(20, 15),
                      check_if_Din(20, 16), check_if_Din(20, 17), check_if_Din(20, 18), check_if_Din(20, 19),
                      check_if_Din(20, 21), check_if_Din(20, 22), check_if_Din(20, 23), check_if_Din(20, 24),
                      check_if_Din(20, 25), check_if_Din(20, 26), check_if_Din(20, 27), check_if_Din(20, 28),
                      check_if_Din(20, 29), check_if_Din(20, 30), check_if_Din(20, 31), check_if_Din(20, 32),
                      check_if_Din(20, 33), check_if_Din(20, 34), check_if_Din(20, 35), check_if_Din(20, 36),
                      check_if_Din(20, 37), check_if_Din(20, 38), check_if_Din(20, 39), check_if_Din(20, 40),
                      check_if_Din(20, 41), check_if_Din(20, 42), check_if_Din(20, 43), check_if_Din(20, 44),
                      check_if_Din(20, 45), check_if_Din(20, 46), check_if_Din(20, 47), check_if_Din(20, 48),
                      check_if_Din(20, 49), check_if_Din(20, 50)], ignore_index=True)
    return data


def check_D21():
    data = pd.concat([check_if_Din(21, 0), check_if_Din(21, 1), check_if_Din(21, 2), check_if_Din(21, 3),
                      check_if_Din(21, 4), check_if_Din(21, 5), check_if_Din(21, 6), check_if_Din(21, 7),
                      check_if_Din(21, 8), check_if_Din(21, 9), check_if_Din(21, 10), check_if_Din(21, 11),
                      check_if_Din(21, 12), check_if_Din(21, 13), check_if_Din(21, 14), check_if_Din(21, 15),
                      check_if_Din(21, 16), check_if_Din(21, 17), check_if_Din(21, 18), check_if_Din(21, 19),
                      check_if_Din(21, 20), check_if_Din(21, 22), check_if_Din(21, 23), check_if_Din(21, 24),
                      check_if_Din(21, 25), check_if_Din(21, 26), check_if_Din(21, 27), check_if_Din(21, 28),
                      check_if_Din(21, 29), check_if_Din(21, 30), check_if_Din(21, 31), check_if_Din(21, 32),
                      check_if_Din(21, 33), check_if_Din(21, 34), check_if_Din(21, 35), check_if_Din(21, 36),
                      check_if_Din(21, 37), check_if_Din(21, 38), check_if_Din(21, 39), check_if_Din(21, 40),
                      check_if_Din(21, 41), check_if_Din(21, 42), check_if_Din(21, 43), check_if_Din(21, 44),
                      check_if_Din(21, 45), check_if_Din(21, 46), check_if_Din(21, 47), check_if_Din(21, 48),
                      check_if_Din(21, 49), check_if_Din(21, 50)], ignore_index=True)
    return data


def check_D22():
    data = pd.concat([check_if_Din(22, 0), check_if_Din(22, 1), check_if_Din(22, 2), check_if_Din(22, 3),
                      check_if_Din(22, 4), check_if_Din(22, 5), check_if_Din(22, 6), check_if_Din(22, 7),
                      check_if_Din(22, 8), check_if_Din(22, 9), check_if_Din(22, 10), check_if_Din(22, 11),
                      check_if_Din(22, 12), check_if_Din(22, 13), check_if_Din(22, 14), check_if_Din(22, 15),
                      check_if_Din(22, 16), check_if_Din(22, 17), check_if_Din(22, 18), check_if_Din(22, 19),
                      check_if_Din(22, 20), check_if_Din(22, 21), check_if_Din(22, 23), check_if_Din(22, 24),
                      check_if_Din(22, 25), check_if_Din(22, 26), check_if_Din(22, 27), check_if_Din(22, 28),
                      check_if_Din(22, 29), check_if_Din(22, 30), check_if_Din(22, 31), check_if_Din(22, 32),
                      check_if_Din(22, 33), check_if_Din(22, 34), check_if_Din(22, 35), check_if_Din(22, 36),
                      check_if_Din(22, 37), check_if_Din(22, 38), check_if_Din(22, 39), check_if_Din(22, 40),
                      check_if_Din(22, 41), check_if_Din(22, 42), check_if_Din(22, 43), check_if_Din(22, 44),
                      check_if_Din(22, 45), check_if_Din(22, 46), check_if_Din(22, 47), check_if_Din(22, 48),
                      check_if_Din(22, 49), check_if_Din(22, 50)], ignore_index=True)
    return data


def check_D23():
    data = pd.concat([check_if_Din(23, 0), check_if_Din(23, 1), check_if_Din(23, 2), check_if_Din(23, 3),
                      check_if_Din(23, 4), check_if_Din(23, 5), check_if_Din(23, 6), check_if_Din(23, 7),
                      check_if_Din(23, 8), check_if_Din(23, 9), check_if_Din(23, 10), check_if_Din(23, 11),
                      check_if_Din(23, 12), check_if_Din(23, 13), check_if_Din(23, 14), check_if_Din(23, 15),
                      check_if_Din(23, 16), check_if_Din(23, 17), check_if_Din(23, 18), check_if_Din(23, 19),
                      check_if_Din(23, 20), check_if_Din(23, 21), check_if_Din(23, 22), check_if_Din(23, 24),
                      check_if_Din(23, 25), check_if_Din(23, 26), check_if_Din(23, 27), check_if_Din(23, 28),
                      check_if_Din(23, 29), check_if_Din(23, 30), check_if_Din(23, 31), check_if_Din(23, 32),
                      check_if_Din(23, 33), check_if_Din(23, 34), check_if_Din(23, 35), check_if_Din(23, 36),
                      check_if_Din(23, 37), check_if_Din(23, 38), check_if_Din(23, 39), check_if_Din(23, 40),
                      check_if_Din(23, 41), check_if_Din(23, 42), check_if_Din(23, 43), check_if_Din(23, 44),
                      check_if_Din(23, 45), check_if_Din(23, 46), check_if_Din(23, 47), check_if_Din(23, 48),
                      check_if_Din(23, 49), check_if_Din(23, 50)], ignore_index=True)
    return data


def check_D24():
    data = pd.concat([check_if_Din(24, 0), check_if_Din(24, 1), check_if_Din(24, 2), check_if_Din(24, 3),
                      check_if_Din(24, 4), check_if_Din(24, 5), check_if_Din(24, 6), check_if_Din(24, 7),
                      check_if_Din(24, 8), check_if_Din(24, 9), check_if_Din(24, 10), check_if_Din(24, 11),
                      check_if_Din(24, 12), check_if_Din(24, 13), check_if_Din(24, 14), check_if_Din(24, 15),
                      check_if_Din(24, 16), check_if_Din(24, 17), check_if_Din(24, 18), check_if_Din(24, 19),
                      check_if_Din(24, 20), check_if_Din(24, 21), check_if_Din(24, 22), check_if_Din(24, 23),
                      check_if_Din(24, 25), check_if_Din(24, 26), check_if_Din(24, 27), check_if_Din(24, 28),
                      check_if_Din(24, 29), check_if_Din(24, 30), check_if_Din(24, 31), check_if_Din(24, 32),
                      check_if_Din(24, 33), check_if_Din(24, 34), check_if_Din(24, 35), check_if_Din(24, 36),
                      check_if_Din(24, 37), check_if_Din(24, 38), check_if_Din(24, 39), check_if_Din(24, 40),
                      check_if_Din(24, 41), check_if_Din(24, 42), check_if_Din(24, 43), check_if_Din(24, 44),
                      check_if_Din(24, 45), check_if_Din(24, 46), check_if_Din(24, 47), check_if_Din(24, 48),
                      check_if_Din(24, 49), check_if_Din(24, 50)], ignore_index=True)
    return data


def check_D25():
    data = pd.concat([check_if_Din(25, 0), check_if_Din(25, 1), check_if_Din(25, 2), check_if_Din(25, 3),
                      check_if_Din(25, 4), check_if_Din(25, 5), check_if_Din(25, 6), check_if_Din(25, 7),
                      check_if_Din(25, 8), check_if_Din(25, 9), check_if_Din(25, 10), check_if_Din(25, 11),
                      check_if_Din(25, 12), check_if_Din(25, 13), check_if_Din(25, 14), check_if_Din(25, 15),
                      check_if_Din(25, 16), check_if_Din(25, 17), check_if_Din(25, 18), check_if_Din(25, 19),
                      check_if_Din(25, 20), check_if_Din(25, 21), check_if_Din(25, 22), check_if_Din(25, 23),
                      check_if_Din(25, 24), check_if_Din(25, 26), check_if_Din(25, 27), check_if_Din(25, 28),
                      check_if_Din(25, 29), check_if_Din(25, 30), check_if_Din(25, 31), check_if_Din(25, 32),
                      check_if_Din(25, 33), check_if_Din(25, 34), check_if_Din(25, 35), check_if_Din(25, 36),
                      check_if_Din(25, 37), check_if_Din(25, 38), check_if_Din(25, 39), check_if_Din(25, 40),
                      check_if_Din(25, 41), check_if_Din(25, 42), check_if_Din(25, 43), check_if_Din(25, 44),
                      check_if_Din(25, 45), check_if_Din(25, 46), check_if_Din(25, 47), check_if_Din(25, 48),
                      check_if_Din(25, 49), check_if_Din(25, 50)], ignore_index=True)
    return data


def check_D26():
    data = pd.concat([check_if_Din(26, 0), check_if_Din(26, 1), check_if_Din(26, 2), check_if_Din(26, 3),
                      check_if_Din(26, 4), check_if_Din(26, 5), check_if_Din(26, 6), check_if_Din(26, 7),
                      check_if_Din(26, 8), check_if_Din(26, 9), check_if_Din(26, 10), check_if_Din(26, 11),
                      check_if_Din(26, 12), check_if_Din(26, 13), check_if_Din(26, 14), check_if_Din(26, 15),
                      check_if_Din(26, 16), check_if_Din(26, 17), check_if_Din(26, 18), check_if_Din(26, 19),
                      check_if_Din(26, 20), check_if_Din(26, 21), check_if_Din(26, 22), check_if_Din(26, 23),
                      check_if_Din(26, 24), check_if_Din(26, 25), check_if_Din(26, 27), check_if_Din(26, 28),
                      check_if_Din(26, 29), check_if_Din(26, 30), check_if_Din(26, 31), check_if_Din(26, 32),
                      check_if_Din(26, 33), check_if_Din(26, 34), check_if_Din(26, 35), check_if_Din(26, 36),
                      check_if_Din(26, 37), check_if_Din(26, 38), check_if_Din(26, 39), check_if_Din(26, 40),
                      check_if_Din(26, 41), check_if_Din(26, 42), check_if_Din(26, 43), check_if_Din(26, 44),
                      check_if_Din(26, 45), check_if_Din(26, 46), check_if_Din(26, 47), check_if_Din(26, 48),
                      check_if_Din(26, 49), check_if_Din(26, 50)], ignore_index=True)
    return data


def check_D27():
    data = pd.concat([check_if_Din(27, 0), check_if_Din(27, 1), check_if_Din(27, 2), check_if_Din(27, 3),
                      check_if_Din(27, 4), check_if_Din(27, 5), check_if_Din(27, 6), check_if_Din(27, 7),
                      check_if_Din(27, 8), check_if_Din(27, 9), check_if_Din(27, 10), check_if_Din(27, 11),
                      check_if_Din(27, 12), check_if_Din(27, 13), check_if_Din(27, 14), check_if_Din(27, 15),
                      check_if_Din(27, 16), check_if_Din(27, 17), check_if_Din(27, 18), check_if_Din(27, 19),
                      check_if_Din(27, 20), check_if_Din(27, 21), check_if_Din(27, 22), check_if_Din(27, 23),
                      check_if_Din(27, 24), check_if_Din(27, 25), check_if_Din(27, 26), check_if_Din(27, 28),
                      check_if_Din(27, 29), check_if_Din(27, 30), check_if_Din(27, 31), check_if_Din(27, 32),
                      check_if_Din(27, 33), check_if_Din(27, 34), check_if_Din(27, 35), check_if_Din(27, 36),
                      check_if_Din(27, 37), check_if_Din(27, 38), check_if_Din(27, 39), check_if_Din(27, 40),
                      check_if_Din(27, 41), check_if_Din(27, 42), check_if_Din(27, 43), check_if_Din(27, 44),
                      check_if_Din(27, 45), check_if_Din(27, 46), check_if_Din(27, 47), check_if_Din(27, 48),
                      check_if_Din(27, 49), check_if_Din(27, 50)], ignore_index=True)
    return data


def check_D28():
    data = pd.concat([check_if_Din(28, 0), check_if_Din(28, 1), check_if_Din(28, 2), check_if_Din(28, 3),
                      check_if_Din(28, 4), check_if_Din(28, 5), check_if_Din(28, 6), check_if_Din(28, 7),
                      check_if_Din(28, 8), check_if_Din(28, 9), check_if_Din(28, 10), check_if_Din(28, 11),
                      check_if_Din(28, 12), check_if_Din(28, 13), check_if_Din(28, 14), check_if_Din(28, 15),
                      check_if_Din(28, 16), check_if_Din(28, 17), check_if_Din(28, 18), check_if_Din(28, 19),
                      check_if_Din(28, 20), check_if_Din(28, 21), check_if_Din(28, 22), check_if_Din(28, 23),
                      check_if_Din(28, 24), check_if_Din(28, 25), check_if_Din(28, 26), check_if_Din(28, 27),
                      check_if_Din(28, 29), check_if_Din(28, 30), check_if_Din(28, 31), check_if_Din(28, 32),
                      check_if_Din(28, 33), check_if_Din(28, 34), check_if_Din(28, 35), check_if_Din(28, 36),
                      check_if_Din(28, 37), check_if_Din(28, 38), check_if_Din(28, 39), check_if_Din(28, 40),
                      check_if_Din(28, 41), check_if_Din(28, 42), check_if_Din(28, 43), check_if_Din(28, 44),
                      check_if_Din(28, 45), check_if_Din(28, 46), check_if_Din(28, 47), check_if_Din(28, 48),
                      check_if_Din(28, 49), check_if_Din(28, 50)], ignore_index=True)
    return data


def check_D29():
    data = pd.concat([check_if_Din(29, 0), check_if_Din(29, 1), check_if_Din(29, 2), check_if_Din(29, 3),
                      check_if_Din(29, 4), check_if_Din(29, 5), check_if_Din(29, 6), check_if_Din(29, 7),
                      check_if_Din(29, 8), check_if_Din(29, 9), check_if_Din(29, 10), check_if_Din(29, 11),
                      check_if_Din(29, 12), check_if_Din(29, 13), check_if_Din(29, 14), check_if_Din(29, 15),
                      check_if_Din(29, 16), check_if_Din(29, 17), check_if_Din(29, 18), check_if_Din(29, 19),
                      check_if_Din(29, 20), check_if_Din(29, 21), check_if_Din(29, 22), check_if_Din(29, 23),
                      check_if_Din(29, 24), check_if_Din(29, 25), check_if_Din(29, 26), check_if_Din(29, 27),
                      check_if_Din(29, 28), check_if_Din(29, 30), check_if_Din(29, 31), check_if_Din(29, 32),
                      check_if_Din(29, 33), check_if_Din(29, 34), check_if_Din(29, 35), check_if_Din(29, 36),
                      check_if_Din(29, 37), check_if_Din(29, 38), check_if_Din(29, 39), check_if_Din(29, 40),
                      check_if_Din(29, 41), check_if_Din(29, 42), check_if_Din(29, 43), check_if_Din(29, 44),
                      check_if_Din(29, 45), check_if_Din(29, 46), check_if_Din(29, 47), check_if_Din(29, 48),
                      check_if_Din(29, 49), check_if_Din(29, 50)], ignore_index=True)
    return data


def check_D30():
    data = pd.concat([check_if_Din(30, 0), check_if_Din(30, 1), check_if_Din(30, 2), check_if_Din(30, 3),
                      check_if_Din(30, 4), check_if_Din(30, 5), check_if_Din(30, 6), check_if_Din(30, 7),
                      check_if_Din(30, 8), check_if_Din(30, 9), check_if_Din(30, 10), check_if_Din(30, 11),
                      check_if_Din(30, 12), check_if_Din(30, 13), check_if_Din(30, 14), check_if_Din(30, 15),
                      check_if_Din(30, 16), check_if_Din(30, 17), check_if_Din(30, 18), check_if_Din(30, 19),
                      check_if_Din(30, 20), check_if_Din(30, 21), check_if_Din(30, 22), check_if_Din(30, 23),
                      check_if_Din(30, 24), check_if_Din(30, 25), check_if_Din(30, 26), check_if_Din(30, 27),
                      check_if_Din(30, 28), check_if_Din(30, 29), check_if_Din(30, 31), check_if_Din(30, 32),
                      check_if_Din(30, 33), check_if_Din(30, 34), check_if_Din(30, 35), check_if_Din(30, 36),
                      check_if_Din(30, 37), check_if_Din(30, 38), check_if_Din(30, 39), check_if_Din(30, 40),
                      check_if_Din(30, 41), check_if_Din(30, 42), check_if_Din(30, 43), check_if_Din(30, 44),
                      check_if_Din(30, 45), check_if_Din(30, 46), check_if_Din(30, 47), check_if_Din(30, 48),
                      check_if_Din(30, 49), check_if_Din(30, 50)], ignore_index=True)
    return data


def check_D31():
    data = pd.concat([check_if_Din(31, 0), check_if_Din(31, 1), check_if_Din(31, 2), check_if_Din(31, 3),
                      check_if_Din(31, 4), check_if_Din(31, 5), check_if_Din(31, 6), check_if_Din(31, 7),
                      check_if_Din(31, 8), check_if_Din(31, 9), check_if_Din(31, 10), check_if_Din(31, 11),
                      check_if_Din(31, 12), check_if_Din(31, 13), check_if_Din(31, 14), check_if_Din(31, 15),
                      check_if_Din(31, 16), check_if_Din(31, 17), check_if_Din(31, 18), check_if_Din(31, 19),
                      check_if_Din(31, 20), check_if_Din(31, 21), check_if_Din(31, 22), check_if_Din(31, 23),
                      check_if_Din(31, 24), check_if_Din(31, 25), check_if_Din(31, 26), check_if_Din(31, 27),
                      check_if_Din(31, 28), check_if_Din(31, 29), check_if_Din(31, 30), check_if_Din(31, 32),
                      check_if_Din(31, 33), check_if_Din(31, 34), check_if_Din(31, 35), check_if_Din(31, 36),
                      check_if_Din(31, 37), check_if_Din(31, 38), check_if_Din(31, 39), check_if_Din(31, 40),
                      check_if_Din(31, 41), check_if_Din(31, 42), check_if_Din(31, 43), check_if_Din(31, 44),
                      check_if_Din(31, 45), check_if_Din(31, 46), check_if_Din(31, 47), check_if_Din(31, 48),
                      check_if_Din(31, 49), check_if_Din(31, 50)], ignore_index=True)
    return data


def check_D32():
    data = pd.concat([check_if_Din(32, 0), check_if_Din(32, 1), check_if_Din(32, 2), check_if_Din(32, 3),
                      check_if_Din(32, 4), check_if_Din(32, 5), check_if_Din(32, 6), check_if_Din(32, 7),
                      check_if_Din(32, 8), check_if_Din(32, 9), check_if_Din(32, 10), check_if_Din(32, 11),
                      check_if_Din(32, 12), check_if_Din(32, 13), check_if_Din(32, 14), check_if_Din(32, 15),
                      check_if_Din(32, 16), check_if_Din(32, 17), check_if_Din(32, 18), check_if_Din(32, 19),
                      check_if_Din(32, 20), check_if_Din(32, 21), check_if_Din(32, 22), check_if_Din(32, 23),
                      check_if_Din(32, 24), check_if_Din(32, 25), check_if_Din(32, 26), check_if_Din(32, 27),
                      check_if_Din(32, 28), check_if_Din(32, 29), check_if_Din(32, 30), check_if_Din(32, 31),
                      check_if_Din(32, 33), check_if_Din(32, 34), check_if_Din(32, 35), check_if_Din(32, 36),
                      check_if_Din(32, 37), check_if_Din(32, 38), check_if_Din(32, 39), check_if_Din(32, 40),
                      check_if_Din(32, 41), check_if_Din(32, 42), check_if_Din(32, 43), check_if_Din(32, 44),
                      check_if_Din(32, 45), check_if_Din(32, 46), check_if_Din(32, 47), check_if_Din(32, 48),
                      check_if_Din(32, 49), check_if_Din(32, 50)], ignore_index=True)
    return data


def check_D33():
    data = pd.concat([check_if_Din(33, 0), check_if_Din(33, 1), check_if_Din(33, 2), check_if_Din(33, 3),
                      check_if_Din(33, 4), check_if_Din(33, 5), check_if_Din(33, 6), check_if_Din(33, 7),
                      check_if_Din(33, 8), check_if_Din(33, 9), check_if_Din(33, 10), check_if_Din(33, 11),
                      check_if_Din(33, 12), check_if_Din(33, 13), check_if_Din(33, 14), check_if_Din(33, 15),
                      check_if_Din(33, 16), check_if_Din(33, 17), check_if_Din(33, 18), check_if_Din(33, 19),
                      check_if_Din(33, 20), check_if_Din(33, 21), check_if_Din(33, 22), check_if_Din(33, 23),
                      check_if_Din(33, 24), check_if_Din(33, 25), check_if_Din(33, 26), check_if_Din(33, 27),
                      check_if_Din(33, 28), check_if_Din(33, 29), check_if_Din(33, 30), check_if_Din(33, 31),
                      check_if_Din(33, 32), check_if_Din(33, 34), check_if_Din(33, 35), check_if_Din(33, 36),
                      check_if_Din(33, 37), check_if_Din(33, 38), check_if_Din(33, 39), check_if_Din(33, 40),
                      check_if_Din(33, 41), check_if_Din(33, 42), check_if_Din(33, 43), check_if_Din(33, 44),
                      check_if_Din(33, 45), check_if_Din(33, 46), check_if_Din(33, 47), check_if_Din(33, 48),
                      check_if_Din(33, 49), check_if_Din(33, 50)], ignore_index=True)
    return data


def check_D34():
    data = pd.concat([check_if_Din(34, 0), check_if_Din(34, 1), check_if_Din(34, 2), check_if_Din(34, 3),
                      check_if_Din(34, 4), check_if_Din(34, 5), check_if_Din(34, 6), check_if_Din(34, 7),
                      check_if_Din(34, 8), check_if_Din(34, 9), check_if_Din(34, 10), check_if_Din(34, 11),
                      check_if_Din(34, 12), check_if_Din(34, 13), check_if_Din(34, 14), check_if_Din(34, 15),
                      check_if_Din(34, 16), check_if_Din(34, 17), check_if_Din(34, 18), check_if_Din(34, 19),
                      check_if_Din(34, 20), check_if_Din(34, 21), check_if_Din(34, 22), check_if_Din(34, 23),
                      check_if_Din(34, 24), check_if_Din(34, 25), check_if_Din(34, 26), check_if_Din(34, 27),
                      check_if_Din(34, 28), check_if_Din(34, 29), check_if_Din(34, 30), check_if_Din(34, 31),
                      check_if_Din(34, 32), check_if_Din(34, 33), check_if_Din(34, 35), check_if_Din(34, 36),
                      check_if_Din(34, 37), check_if_Din(34, 38), check_if_Din(34, 39), check_if_Din(34, 40),
                      check_if_Din(34, 41), check_if_Din(34, 42), check_if_Din(34, 43), check_if_Din(34, 44),
                      check_if_Din(34, 45), check_if_Din(34, 46), check_if_Din(34, 47), check_if_Din(34, 48),
                      check_if_Din(34, 49), check_if_Din(34, 50)], ignore_index=True)
    return data


def check_D35():
    data = pd.concat([check_if_Din(35, 0), check_if_Din(35, 1), check_if_Din(35, 2), check_if_Din(35, 3),
                      check_if_Din(35, 4), check_if_Din(35, 5), check_if_Din(35, 6), check_if_Din(35, 7),
                      check_if_Din(35, 8), check_if_Din(35, 9), check_if_Din(35, 10), check_if_Din(35, 11),
                      check_if_Din(35, 12), check_if_Din(35, 13), check_if_Din(35, 14), check_if_Din(35, 15),
                      check_if_Din(35, 16), check_if_Din(35, 17), check_if_Din(35, 18), check_if_Din(35, 19),
                      check_if_Din(35, 20), check_if_Din(35, 21), check_if_Din(35, 22), check_if_Din(35, 23),
                      check_if_Din(35, 24), check_if_Din(35, 25), check_if_Din(35, 26), check_if_Din(35, 27),
                      check_if_Din(35, 28), check_if_Din(35, 29), check_if_Din(35, 30), check_if_Din(35, 31),
                      check_if_Din(35, 32), check_if_Din(35, 33), check_if_Din(35, 34), check_if_Din(35, 36),
                      check_if_Din(35, 37), check_if_Din(35, 38), check_if_Din(35, 39), check_if_Din(35, 40),
                      check_if_Din(35, 41), check_if_Din(35, 42), check_if_Din(35, 43), check_if_Din(35, 44),
                      check_if_Din(35, 45), check_if_Din(35, 46), check_if_Din(35, 47), check_if_Din(35, 48),
                      check_if_Din(35, 49), check_if_Din(35, 50)], ignore_index=True)
    return data


def check_D36():
    data = pd.concat([check_if_Din(36, 0), check_if_Din(36, 1), check_if_Din(36, 2), check_if_Din(36, 3),
                      check_if_Din(36, 4), check_if_Din(36, 5), check_if_Din(36, 6), check_if_Din(36, 7),
                      check_if_Din(36, 8), check_if_Din(36, 9), check_if_Din(36, 10), check_if_Din(36, 11),
                      check_if_Din(36, 12), check_if_Din(36, 13), check_if_Din(36, 14), check_if_Din(36, 15),
                      check_if_Din(36, 16), check_if_Din(36, 17), check_if_Din(36, 18), check_if_Din(36, 19),
                      check_if_Din(36, 20), check_if_Din(36, 21), check_if_Din(36, 22), check_if_Din(36, 23),
                      check_if_Din(36, 24), check_if_Din(36, 25), check_if_Din(36, 26), check_if_Din(36, 27),
                      check_if_Din(36, 28), check_if_Din(36, 29), check_if_Din(36, 30), check_if_Din(36, 31),
                      check_if_Din(36, 32), check_if_Din(36, 33), check_if_Din(36, 34), check_if_Din(36, 35),
                      check_if_Din(36, 37), check_if_Din(36, 38), check_if_Din(36, 39), check_if_Din(36, 40),
                      check_if_Din(36, 41), check_if_Din(36, 42), check_if_Din(36, 43), check_if_Din(36, 44),
                      check_if_Din(36, 45), check_if_Din(36, 46), check_if_Din(36, 47), check_if_Din(36, 48),
                      check_if_Din(36, 49), check_if_Din(36, 50)], ignore_index=True)
    return data


def check_D37():
    data = pd.concat([check_if_Din(37, 0), check_if_Din(37, 1), check_if_Din(37, 2), check_if_Din(37, 3),
                      check_if_Din(37, 4), check_if_Din(37, 5), check_if_Din(37, 6), check_if_Din(37, 7),
                      check_if_Din(37, 8), check_if_Din(37, 9), check_if_Din(37, 10), check_if_Din(37, 11),
                      check_if_Din(37, 12), check_if_Din(37, 13), check_if_Din(37, 14), check_if_Din(37, 15),
                      check_if_Din(37, 16), check_if_Din(37, 17), check_if_Din(37, 18), check_if_Din(37, 19),
                      check_if_Din(37, 20), check_if_Din(37, 21), check_if_Din(37, 22), check_if_Din(37, 23),
                      check_if_Din(37, 24), check_if_Din(37, 25), check_if_Din(37, 26), check_if_Din(37, 27),
                      check_if_Din(37, 28), check_if_Din(37, 29), check_if_Din(37, 30), check_if_Din(37, 31),
                      check_if_Din(37, 32), check_if_Din(37, 33), check_if_Din(37, 34), check_if_Din(37, 35),
                      check_if_Din(37, 36), check_if_Din(37, 38), check_if_Din(37, 39), check_if_Din(37, 40),
                      check_if_Din(37, 41), check_if_Din(37, 42), check_if_Din(37, 43), check_if_Din(37, 44),
                      check_if_Din(37, 45), check_if_Din(37, 46), check_if_Din(37, 47), check_if_Din(37, 48),
                      check_if_Din(37, 49), check_if_Din(37, 50)], ignore_index=True)
    return data


def check_D38():
    data = pd.concat([check_if_Din(38, 0), check_if_Din(38, 1), check_if_Din(38, 2), check_if_Din(38, 3),
                      check_if_Din(38, 4), check_if_Din(38, 5), check_if_Din(38, 6), check_if_Din(38, 7),
                      check_if_Din(38, 8), check_if_Din(38, 9), check_if_Din(38, 10), check_if_Din(38, 11),
                      check_if_Din(38, 12), check_if_Din(38, 13), check_if_Din(38, 14), check_if_Din(38, 15),
                      check_if_Din(38, 16), check_if_Din(38, 17), check_if_Din(38, 18), check_if_Din(38, 19),
                      check_if_Din(38, 20), check_if_Din(38, 21), check_if_Din(38, 22), check_if_Din(38, 23),
                      check_if_Din(38, 24), check_if_Din(38, 25), check_if_Din(38, 26), check_if_Din(38, 27),
                      check_if_Din(38, 28), check_if_Din(38, 29), check_if_Din(38, 30), check_if_Din(38, 31),
                      check_if_Din(38, 32), check_if_Din(38, 33), check_if_Din(38, 34), check_if_Din(38, 35),
                      check_if_Din(38, 36), check_if_Din(38, 37), check_if_Din(38, 39), check_if_Din(38, 40),
                      check_if_Din(38, 41), check_if_Din(38, 42), check_if_Din(38, 43), check_if_Din(38, 44),
                      check_if_Din(38, 45), check_if_Din(38, 46), check_if_Din(38, 47), check_if_Din(38, 48),
                      check_if_Din(38, 49), check_if_Din(38, 50)], ignore_index=True)
    return data


def check_D39():
    data = pd.concat([check_if_Din(39, 0), check_if_Din(39, 1), check_if_Din(39, 2), check_if_Din(39, 3),
                      check_if_Din(39, 4), check_if_Din(39, 5), check_if_Din(39, 6), check_if_Din(39, 7),
                      check_if_Din(39, 8), check_if_Din(39, 9), check_if_Din(39, 10), check_if_Din(39, 11),
                      check_if_Din(39, 12), check_if_Din(39, 13), check_if_Din(39, 14), check_if_Din(39, 15),
                      check_if_Din(39, 16), check_if_Din(39, 17), check_if_Din(39, 18), check_if_Din(39, 19),
                      check_if_Din(39, 20), check_if_Din(39, 21), check_if_Din(39, 22), check_if_Din(39, 23),
                      check_if_Din(39, 24), check_if_Din(39, 25), check_if_Din(39, 26), check_if_Din(39, 27),
                      check_if_Din(39, 28), check_if_Din(39, 29), check_if_Din(39, 30), check_if_Din(39, 31),
                      check_if_Din(39, 32), check_if_Din(39, 33), check_if_Din(39, 34), check_if_Din(39, 35),
                      check_if_Din(39, 36), check_if_Din(39, 37), check_if_Din(39, 38), check_if_Din(39, 40),
                      check_if_Din(39, 41), check_if_Din(39, 42), check_if_Din(39, 43), check_if_Din(39, 44),
                      check_if_Din(39, 45), check_if_Din(39, 46), check_if_Din(39, 47), check_if_Din(39, 48),
                      check_if_Din(39, 49), check_if_Din(39, 50)], ignore_index=True)
    return data


def check_D40():
    data = pd.concat([check_if_Din(40, 0), check_if_Din(40, 1), check_if_Din(40, 2), check_if_Din(40, 3),
                      check_if_Din(40, 4), check_if_Din(40, 5), check_if_Din(40, 6), check_if_Din(40, 7),
                      check_if_Din(40, 8), check_if_Din(40, 9), check_if_Din(40, 10), check_if_Din(40, 11),
                      check_if_Din(40, 12), check_if_Din(40, 13), check_if_Din(40, 14), check_if_Din(40, 15),
                      check_if_Din(40, 16), check_if_Din(40, 17), check_if_Din(40, 18), check_if_Din(40, 19),
                      check_if_Din(40, 20), check_if_Din(40, 21), check_if_Din(40, 22), check_if_Din(40, 23),
                      check_if_Din(40, 24), check_if_Din(40, 25), check_if_Din(40, 26), check_if_Din(40, 27),
                      check_if_Din(40, 28), check_if_Din(40, 29), check_if_Din(40, 30), check_if_Din(40, 31),
                      check_if_Din(40, 32), check_if_Din(40, 33), check_if_Din(40, 34), check_if_Din(40, 35),
                      check_if_Din(40, 36), check_if_Din(40, 37), check_if_Din(40, 38), check_if_Din(40, 39),
                      check_if_Din(40, 41), check_if_Din(40, 42), check_if_Din(40, 43), check_if_Din(40, 44),
                      check_if_Din(40, 45), check_if_Din(40, 46), check_if_Din(40, 47), check_if_Din(40, 48),
                      check_if_Din(40, 49), check_if_Din(40, 50)], ignore_index=True)
    return data


def check_D41():
    data = pd.concat([check_if_Din(41, 0), check_if_Din(41, 1), check_if_Din(41, 2), check_if_Din(41, 3),
                      check_if_Din(41, 4), check_if_Din(41, 5), check_if_Din(41, 6), check_if_Din(41, 7),
                      check_if_Din(41, 8), check_if_Din(41, 9), check_if_Din(41, 10), check_if_Din(41, 11),
                      check_if_Din(41, 12), check_if_Din(41, 13), check_if_Din(41, 14), check_if_Din(41, 15),
                      check_if_Din(41, 16), check_if_Din(41, 17), check_if_Din(41, 18), check_if_Din(41, 19),
                      check_if_Din(41, 20), check_if_Din(41, 21), check_if_Din(41, 22), check_if_Din(41, 23),
                      check_if_Din(41, 24), check_if_Din(41, 25), check_if_Din(41, 26), check_if_Din(41, 27),
                      check_if_Din(41, 28), check_if_Din(41, 29), check_if_Din(41, 30), check_if_Din(41, 31),
                      check_if_Din(41, 32), check_if_Din(41, 33), check_if_Din(41, 34), check_if_Din(41, 35),
                      check_if_Din(41, 36), check_if_Din(41, 37), check_if_Din(41, 38), check_if_Din(41, 39),
                      check_if_Din(41, 40), check_if_Din(41, 42), check_if_Din(41, 43), check_if_Din(41, 44),
                      check_if_Din(41, 45), check_if_Din(41, 46), check_if_Din(41, 47), check_if_Din(41, 48),
                      check_if_Din(41, 49), check_if_Din(41, 50)], ignore_index=True)
    return data


def check_D42():
    data = pd.concat([check_if_Din(42, 0), check_if_Din(42, 1), check_if_Din(42, 2), check_if_Din(42, 3),
                      check_if_Din(42, 4), check_if_Din(42, 5), check_if_Din(42, 6), check_if_Din(42, 7),
                      check_if_Din(42, 8), check_if_Din(42, 9), check_if_Din(42, 10), check_if_Din(42, 11),
                      check_if_Din(42, 12), check_if_Din(42, 13), check_if_Din(42, 14), check_if_Din(42, 15),
                      check_if_Din(42, 16), check_if_Din(42, 17), check_if_Din(42, 18), check_if_Din(42, 19),
                      check_if_Din(42, 20), check_if_Din(42, 21), check_if_Din(42, 22), check_if_Din(42, 23),
                      check_if_Din(42, 24), check_if_Din(42, 25), check_if_Din(42, 26), check_if_Din(42, 27),
                      check_if_Din(42, 28), check_if_Din(42, 29), check_if_Din(42, 30), check_if_Din(42, 31),
                      check_if_Din(42, 32), check_if_Din(42, 33), check_if_Din(42, 34), check_if_Din(42, 35),
                      check_if_Din(42, 36), check_if_Din(42, 37), check_if_Din(42, 38), check_if_Din(42, 39),
                      check_if_Din(42, 40), check_if_Din(42, 41), check_if_Din(42, 43), check_if_Din(42, 44),
                      check_if_Din(42, 45), check_if_Din(42, 46), check_if_Din(42, 47), check_if_Din(42, 48),
                      check_if_Din(42, 49), check_if_Din(42, 50)], ignore_index=True)
    return data


def check_D43():
    data = pd.concat([check_if_Din(43, 0), check_if_Din(43, 1), check_if_Din(43, 2), check_if_Din(43, 3),
                      check_if_Din(43, 4), check_if_Din(43, 5), check_if_Din(43, 6), check_if_Din(43, 7),
                      check_if_Din(43, 8), check_if_Din(43, 9), check_if_Din(43, 10), check_if_Din(43, 11),
                      check_if_Din(43, 12), check_if_Din(43, 13), check_if_Din(43, 14), check_if_Din(43, 15),
                      check_if_Din(43, 16), check_if_Din(43, 17), check_if_Din(43, 18), check_if_Din(43, 19),
                      check_if_Din(43, 20), check_if_Din(43, 21), check_if_Din(43, 22), check_if_Din(43, 23),
                      check_if_Din(43, 24), check_if_Din(43, 25), check_if_Din(43, 26), check_if_Din(43, 27),
                      check_if_Din(43, 28), check_if_Din(43, 29), check_if_Din(43, 30), check_if_Din(43, 31),
                      check_if_Din(43, 32), check_if_Din(43, 33), check_if_Din(43, 34), check_if_Din(43, 35),
                      check_if_Din(43, 36), check_if_Din(43, 37), check_if_Din(43, 38), check_if_Din(43, 39),
                      check_if_Din(43, 40), check_if_Din(43, 41), check_if_Din(43, 42), check_if_Din(43, 44),
                      check_if_Din(43, 45), check_if_Din(43, 46), check_if_Din(43, 47), check_if_Din(43, 48),
                      check_if_Din(43, 49), check_if_Din(43, 50)], ignore_index=True)
    return data


def check_D44():
    data = pd.concat([check_if_Din(44, 0), check_if_Din(44, 1), check_if_Din(44, 2), check_if_Din(44, 3),
                      check_if_Din(44, 4), check_if_Din(44, 5), check_if_Din(44, 6), check_if_Din(44, 7),
                      check_if_Din(44, 8), check_if_Din(44, 9), check_if_Din(44, 10), check_if_Din(44, 11),
                      check_if_Din(44, 12), check_if_Din(44, 13), check_if_Din(44, 14), check_if_Din(44, 15),
                      check_if_Din(44, 16), check_if_Din(44, 17), check_if_Din(44, 18), check_if_Din(44, 19),
                      check_if_Din(44, 20), check_if_Din(44, 21), check_if_Din(44, 22), check_if_Din(44, 23),
                      check_if_Din(44, 24), check_if_Din(44, 25), check_if_Din(44, 26), check_if_Din(44, 27),
                      check_if_Din(44, 28), check_if_Din(44, 29), check_if_Din(44, 30), check_if_Din(44, 31),
                      check_if_Din(44, 32), check_if_Din(44, 33), check_if_Din(44, 34), check_if_Din(44, 35),
                      check_if_Din(44, 36), check_if_Din(44, 37), check_if_Din(44, 38), check_if_Din(44, 39),
                      check_if_Din(44, 40), check_if_Din(44, 41), check_if_Din(44, 42), check_if_Din(44, 43),
                      check_if_Din(44, 45), check_if_Din(44, 46), check_if_Din(44, 47), check_if_Din(44, 48),
                      check_if_Din(44, 49), check_if_Din(44, 50)], ignore_index=True)
    return data


def check_D45():
    data = pd.concat([check_if_Din(45, 0), check_if_Din(45, 1), check_if_Din(45, 2), check_if_Din(45, 3),
                      check_if_Din(45, 4), check_if_Din(45, 5), check_if_Din(45, 6), check_if_Din(45, 7),
                      check_if_Din(45, 8), check_if_Din(45, 9), check_if_Din(45, 10), check_if_Din(45, 11),
                      check_if_Din(45, 12), check_if_Din(45, 13), check_if_Din(45, 14), check_if_Din(45, 15),
                      check_if_Din(45, 16), check_if_Din(45, 17), check_if_Din(45, 18), check_if_Din(45, 19),
                      check_if_Din(45, 20), check_if_Din(45, 21), check_if_Din(45, 22), check_if_Din(45, 23),
                      check_if_Din(45, 24), check_if_Din(45, 25), check_if_Din(45, 26), check_if_Din(45, 27),
                      check_if_Din(45, 28), check_if_Din(45, 29), check_if_Din(45, 30), check_if_Din(45, 31),
                      check_if_Din(45, 32), check_if_Din(45, 33), check_if_Din(45, 34), check_if_Din(45, 35),
                      check_if_Din(45, 36), check_if_Din(45, 37), check_if_Din(45, 38), check_if_Din(45, 39),
                      check_if_Din(45, 40), check_if_Din(45, 41), check_if_Din(45, 42), check_if_Din(45, 43),
                      check_if_Din(45, 44), check_if_Din(45, 46), check_if_Din(45, 47), check_if_Din(45, 48),
                      check_if_Din(45, 49), check_if_Din(45, 50)], ignore_index=True)
    return data


def check_D46():
    data = pd.concat([check_if_Din(46, 0), check_if_Din(46, 1), check_if_Din(46, 2), check_if_Din(46, 3),
                      check_if_Din(46, 4), check_if_Din(46, 5), check_if_Din(46, 6), check_if_Din(46, 7),
                      check_if_Din(46, 8), check_if_Din(46, 9), check_if_Din(46, 10), check_if_Din(46, 11),
                      check_if_Din(46, 12), check_if_Din(46, 13), check_if_Din(46, 14), check_if_Din(46, 15),
                      check_if_Din(46, 16), check_if_Din(46, 17), check_if_Din(46, 18), check_if_Din(46, 19),
                      check_if_Din(46, 20), check_if_Din(46, 21), check_if_Din(46, 22), check_if_Din(46, 23),
                      check_if_Din(46, 24), check_if_Din(46, 25), check_if_Din(46, 26), check_if_Din(46, 27),
                      check_if_Din(46, 28), check_if_Din(46, 29), check_if_Din(46, 30), check_if_Din(46, 31),
                      check_if_Din(46, 32), check_if_Din(46, 33), check_if_Din(46, 34), check_if_Din(46, 35),
                      check_if_Din(46, 36), check_if_Din(46, 37), check_if_Din(46, 38), check_if_Din(46, 39),
                      check_if_Din(46, 40), check_if_Din(46, 41), check_if_Din(46, 42), check_if_Din(46, 43),
                      check_if_Din(46, 44), check_if_Din(46, 45), check_if_Din(46, 47), check_if_Din(46, 48),
                      check_if_Din(46, 49), check_if_Din(46, 50)], ignore_index=True)
    return data


def check_D47():
    data = pd.concat([check_if_Din(47, 0), check_if_Din(47, 1), check_if_Din(47, 2), check_if_Din(47, 3),
                      check_if_Din(47, 4), check_if_Din(47, 5), check_if_Din(47, 6), check_if_Din(47, 7),
                      check_if_Din(47, 8), check_if_Din(47, 9), check_if_Din(47, 10), check_if_Din(47, 11),
                      check_if_Din(47, 12), check_if_Din(47, 13), check_if_Din(47, 14), check_if_Din(47, 15),
                      check_if_Din(47, 16), check_if_Din(47, 17), check_if_Din(47, 18), check_if_Din(47, 19),
                      check_if_Din(47, 20), check_if_Din(47, 21), check_if_Din(47, 22), check_if_Din(47, 23),
                      check_if_Din(47, 24), check_if_Din(47, 25), check_if_Din(47, 26), check_if_Din(47, 27),
                      check_if_Din(47, 28), check_if_Din(47, 29), check_if_Din(47, 30), check_if_Din(47, 31),
                      check_if_Din(47, 32), check_if_Din(47, 33), check_if_Din(47, 34), check_if_Din(47, 35),
                      check_if_Din(47, 36), check_if_Din(47, 37), check_if_Din(47, 38), check_if_Din(47, 39),
                      check_if_Din(47, 40), check_if_Din(47, 41), check_if_Din(47, 42), check_if_Din(47, 43),
                      check_if_Din(47, 44), check_if_Din(47, 45), check_if_Din(47, 46), check_if_Din(47, 48),
                      check_if_Din(47, 49), check_if_Din(47, 50)], ignore_index=True)
    return data


def check_D48():
    data = pd.concat([check_if_Din(48, 0), check_if_Din(48, 1), check_if_Din(48, 2), check_if_Din(48, 3),
                      check_if_Din(48, 4), check_if_Din(48, 5), check_if_Din(48, 6), check_if_Din(48, 7),
                      check_if_Din(48, 8), check_if_Din(48, 9), check_if_Din(48, 10), check_if_Din(48, 11),
                      check_if_Din(48, 12), check_if_Din(48, 13), check_if_Din(48, 14), check_if_Din(48, 15),
                      check_if_Din(48, 16), check_if_Din(48, 17), check_if_Din(48, 18), check_if_Din(48, 19),
                      check_if_Din(48, 20), check_if_Din(48, 21), check_if_Din(48, 22), check_if_Din(48, 23),
                      check_if_Din(48, 24), check_if_Din(48, 25), check_if_Din(48, 26), check_if_Din(48, 27),
                      check_if_Din(48, 28), check_if_Din(48, 29), check_if_Din(48, 30), check_if_Din(48, 31),
                      check_if_Din(48, 32), check_if_Din(48, 33), check_if_Din(48, 34), check_if_Din(48, 35),
                      check_if_Din(48, 36), check_if_Din(48, 37), check_if_Din(48, 38), check_if_Din(48, 39),
                      check_if_Din(48, 40), check_if_Din(48, 41), check_if_Din(48, 42), check_if_Din(48, 43),
                      check_if_Din(48, 44), check_if_Din(48, 45), check_if_Din(48, 46), check_if_Din(48, 47),
                      check_if_Din(48, 49), check_if_Din(48, 50)], ignore_index=True)
    return data


def check_D49():
    data = pd.concat([check_if_Din(49, 0), check_if_Din(49, 1), check_if_Din(49, 2), check_if_Din(49, 3),
                      check_if_Din(49, 4), check_if_Din(49, 5), check_if_Din(49, 6), check_if_Din(49, 7),
                      check_if_Din(49, 8), check_if_Din(49, 9), check_if_Din(49, 10), check_if_Din(49, 11),
                      check_if_Din(49, 12), check_if_Din(49, 13), check_if_Din(49, 14), check_if_Din(49, 15),
                      check_if_Din(49, 16), check_if_Din(49, 17), check_if_Din(49, 18), check_if_Din(49, 19),
                      check_if_Din(49, 20), check_if_Din(49, 21), check_if_Din(49, 22), check_if_Din(49, 23),
                      check_if_Din(49, 24), check_if_Din(49, 25), check_if_Din(49, 26), check_if_Din(49, 27),
                      check_if_Din(49, 28), check_if_Din(49, 29), check_if_Din(49, 30), check_if_Din(49, 31),
                      check_if_Din(49, 32), check_if_Din(49, 33), check_if_Din(49, 34), check_if_Din(49, 35),
                      check_if_Din(49, 36), check_if_Din(49, 37), check_if_Din(49, 38), check_if_Din(49, 39),
                      check_if_Din(49, 40), check_if_Din(49, 41), check_if_Din(49, 42), check_if_Din(49, 43),
                      check_if_Din(49, 44), check_if_Din(49, 45), check_if_Din(49, 46), check_if_Din(49, 47),
                      check_if_Din(49, 48), check_if_Din(49, 50)], ignore_index=True)
    return data


def check_D50():
    data = pd.concat([check_if_Din(50, 0), check_if_Din(50, 1), check_if_Din(50, 2), check_if_Din(50, 3),
                      check_if_Din(50, 4), check_if_Din(50, 5), check_if_Din(50, 6), check_if_Din(50, 7),
                      check_if_Din(50, 8), check_if_Din(50, 9), check_if_Din(50, 10), check_if_Din(50, 11),
                      check_if_Din(50, 12), check_if_Din(50, 13), check_if_Din(50, 14), check_if_Din(50, 15),
                      check_if_Din(50, 16), check_if_Din(50, 17), check_if_Din(50, 18), check_if_Din(50, 19),
                      check_if_Din(50, 20), check_if_Din(50, 21), check_if_Din(50, 22), check_if_Din(50, 23),
                      check_if_Din(50, 24), check_if_Din(50, 25), check_if_Din(50, 26), check_if_Din(50, 27),
                      check_if_Din(50, 28), check_if_Din(50, 29), check_if_Din(50, 30), check_if_Din(50, 31),
                      check_if_Din(50, 32), check_if_Din(50, 33), check_if_Din(50, 34), check_if_Din(50, 35),
                      check_if_Din(50, 36), check_if_Din(50, 37), check_if_Din(50, 38), check_if_Din(50, 39),
                      check_if_Din(50, 40), check_if_Din(50, 41), check_if_Din(50, 42), check_if_Din(50, 43),
                      check_if_Din(50, 44), check_if_Din(50, 45), check_if_Din(50, 46), check_if_Din(50, 47),
                      check_if_Din(50, 48), check_if_Din(50, 49)], ignore_index=True)
    return data


def check():
    data = pd.concat([check_D1(), check_D2(), check_D3(), check_D4(),
                      check_D5(), check_D6(), check_D7(), check_D8(),
                      check_D9(), check_D10(), check_D11(), check_D12(),
                      check_D13(), check_D14(), check_D15(), check_D16(),
                      check_D17(), check_D18(), check_D19(), check_D20(),
                      check_D21(), check_D22(), check_D23(), check_D24(),
                      check_D25(), check_D26(), check_D27(), check_D28(),
                      check_D29(), check_D30(), check_D31(), check_D32(),
                      check_D33(), check_D34(), check_D35(), check_D36(),
                      check_D37(), check_D38(), check_D39(), check_D40(),
                      check_D41(), check_D42(), check_D43(), check_D44(),
                      check_D45(), check_D46(), check_D47(), check_D48(),
                      check_D49(), check_D50()], ignore_index=True)
    return data


def check_D_csv():
    data = check()
    string1 = "/Pycharm/HumanActivityRecognition/check"
    string2 = string1 + "/check_D" + ".csv"
    print(string2)
    os.makedirs(string1, exist_ok=True)
    data.to_csv(string2)


check_D_csv()
