import pandas as pd

from CreateWord import create_word


def words_times_P():
    d0 = create_word(0, 'P')
    d1 = create_word(1, 'P')
    d2 = create_word(2, 'P')
    d3 = create_word(3, 'P')
    d4 = create_word(4, 'P')
    d5 = create_word(5, 'P')
    d6 = create_word(6, 'P')
    d7 = create_word(7, 'P')
    d8 = create_word(8, 'P')
    d9 = create_word(9, 'P')
    d10 = create_word(10, 'P')
    d11 = create_word(11, 'P')
    d12 = create_word(12, 'P')
    d13 = create_word(13, 'P')
    d14 = create_word(14, 'P')
    d15 = create_word(15, 'P')
    d16 = create_word(16, 'P')
    d17 = create_word(17, 'P')
    d18 = create_word(18, 'P')
    d19 = create_word(19, 'P')
    d20 = create_word(20, 'P')
    d21 = create_word(21, 'P')
    d22 = create_word(22, 'P')
    d23 = create_word(23, 'P')
    d24 = create_word(24, 'P')
    d25 = create_word(25, 'P')
    d26 = create_word(26, 'P')
    d27 = create_word(27, 'P')
    d28 = create_word(28, 'P')
    d29 = create_word(29, 'P')
    d30 = create_word(30, 'P')
    d31 = create_word(31, 'P')
    d32 = create_word(32, 'P')
    d33 = create_word(33, 'P')
    d34 = create_word(34, 'P')
    d35 = create_word(35, 'P')
    d36 = create_word(36, 'P')
    d37 = create_word(37, 'P')
    d38 = create_word(38, 'P')
    d39 = create_word(39, 'P')
    d40 = create_word(40, 'P')
    d41 = create_word(41, 'P')
    d42 = create_word(42, 'P')
    d43 = create_word(43, 'P')
    d44 = create_word(44, 'P')
    d45 = create_word(45, 'P')
    d46 = create_word(46, 'P')
    d47 = create_word(47, 'P')
    d48 = create_word(48, 'P')
    d49 = create_word(49, 'P')
    d50 = create_word(50, 'P')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

