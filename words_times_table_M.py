import pandas as pd

from CreateWord import create_word


def words_times_M():
    d0 = create_word(0, 'M')
    d1 = create_word(1, 'M')
    d2 = create_word(2, 'M')
    d3 = create_word(3, 'M')
    d4 = create_word(4, 'M')
    d5 = create_word(5, 'M')
    d6 = create_word(6, 'M')
    d7 = create_word(7, 'M')
    d8 = create_word(8, 'M')
    d9 = create_word(9, 'M')
    d10 = create_word(10, 'M')
    d11 = create_word(11, 'M')
    d12 = create_word(12, 'M')
    d13 = create_word(13, 'M')
    d14 = create_word(14, 'M')
    d15 = create_word(15, 'M')
    d16 = create_word(16, 'M')
    d17 = create_word(17, 'M')
    d18 = create_word(18, 'M')
    d19 = create_word(19, 'M')
    d20 = create_word(20, 'M')
    d21 = create_word(21, 'M')
    d22 = create_word(22, 'M')
    d23 = create_word(23, 'M')
    d24 = create_word(24, 'M')
    d25 = create_word(25, 'M')
    d26 = create_word(26, 'M')
    d27 = create_word(27, 'M')
    d28 = create_word(28, 'M')
    d29 = create_word(29, 'M')
    d30 = create_word(30, 'M')
    d31 = create_word(31, 'M')
    d32 = create_word(32, 'M')
    d33 = create_word(33, 'M')
    d34 = create_word(34, 'M')
    d35 = create_word(35, 'M')
    d36 = create_word(36, 'M')
    d37 = create_word(37, 'M')
    d38 = create_word(38, 'M')
    d39 = create_word(39, 'M')
    d40 = create_word(40, 'M')
    d41 = create_word(41, 'M')
    d42 = create_word(42, 'M')
    d43 = create_word(43, 'M')
    d44 = create_word(44, 'M')
    d45 = create_word(45, 'M')
    d46 = create_word(46, 'M')
    d47 = create_word(47, 'M')
    d48 = create_word(48, 'M')
    d49 = create_word(49, 'M')
    d50 = create_word(50, 'M')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

