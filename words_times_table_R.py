import pandas as pd

from CreateWord import create_word


def words_times_R():
    d0 = create_word(0, 'R')
    d1 = create_word(1, 'R')
    d2 = create_word(2, 'R')
    d3 = create_word(3, 'R')
    d4 = create_word(4, 'R')
    d5 = create_word(5, 'R')
    d6 = create_word(6, 'R')
    d7 = create_word(7, 'R')
    d8 = create_word(8, 'R')
    d9 = create_word(9, 'R')
    d10 = create_word(10, 'R')
    d11 = create_word(11, 'R')
    d12 = create_word(12, 'R')
    d13 = create_word(13, 'R')
    d14 = create_word(14, 'R')
    d15 = create_word(15, 'R')
    d16 = create_word(16, 'R')
    d17 = create_word(17, 'R')
    d18 = create_word(18, 'R')
    d19 = create_word(19, 'R')
    d20 = create_word(20, 'R')
    d21 = create_word(21, 'R')
    d22 = create_word(22, 'R')
    d23 = create_word(23, 'R')
    d24 = create_word(24, 'R')
    d25 = create_word(25, 'R')
    d26 = create_word(26, 'R')
    d27 = create_word(27, 'R')
    d28 = create_word(28, 'R')
    d29 = create_word(29, 'R')
    d30 = create_word(30, 'R')
    d31 = create_word(31, 'R')
    d32 = create_word(32, 'R')
    d33 = create_word(33, 'R')
    d34 = create_word(34, 'R')
    d35 = create_word(35, 'R')
    d36 = create_word(36, 'R')
    d37 = create_word(37, 'R')
    d38 = create_word(38, 'R')
    d39 = create_word(39, 'R')
    d40 = create_word(40, 'R')
    d41 = create_word(41, 'R')
    d42 = create_word(42, 'R')
    d43 = create_word(43, 'R')
    d44 = create_word(44, 'R')
    d45 = create_word(45, 'R')
    d46 = create_word(46, 'R')
    d47 = create_word(47, 'R')
    d48 = create_word(48, 'R')
    d49 = create_word(49, 'R')
    d50 = create_word(50, 'R')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

