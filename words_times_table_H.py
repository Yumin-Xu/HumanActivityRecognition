import pandas as pd

from CreateWord import create_word


def words_times_H():
    d0 = create_word(0, 'H')
    d1 = create_word(1, 'H')
    d2 = create_word(2, 'H')
    d3 = create_word(3, 'H')
    d4 = create_word(4, 'H')
    d5 = create_word(5, 'H')
    d6 = create_word(6, 'H')
    d7 = create_word(7, 'H')
    d8 = create_word(8, 'H')
    d9 = create_word(9, 'H')
    d10 = create_word(10, 'H')
    d11 = create_word(11, 'H')
    d12 = create_word(12, 'H')
    d13 = create_word(13, 'H')
    d14 = create_word(14, 'H')
    d15 = create_word(15, 'H')
    d16 = create_word(16, 'H')
    d17 = create_word(17, 'H')
    d18 = create_word(18, 'H')
    d19 = create_word(19, 'H')
    d20 = create_word(20, 'H')
    d21 = create_word(21, 'H')
    d22 = create_word(22, 'H')
    d23 = create_word(23, 'H')
    d24 = create_word(24, 'H')
    d25 = create_word(25, 'H')
    d26 = create_word(26, 'H')
    d27 = create_word(27, 'H')
    d28 = create_word(28, 'H')
    d29 = create_word(29, 'H')
    d30 = create_word(30, 'H')
    d31 = create_word(31, 'H')
    d32 = create_word(32, 'H')
    d33 = create_word(33, 'H')
    d34 = create_word(34, 'H')
    d35 = create_word(35, 'H')
    d36 = create_word(36, 'H')
    d37 = create_word(37, 'H')
    d38 = create_word(38, 'H')
    d39 = create_word(39, 'H')
    d40 = create_word(40, 'H')
    d41 = create_word(41, 'H')
    d42 = create_word(42, 'H')
    d43 = create_word(43, 'H')
    d44 = create_word(44, 'H')
    d45 = create_word(45, 'H')
    d46 = create_word(46, 'H')
    d47 = create_word(47, 'H')
    d48 = create_word(48, 'H')
    d49 = create_word(49, 'H')
    d50 = create_word(50, 'H')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

