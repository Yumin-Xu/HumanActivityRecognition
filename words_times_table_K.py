import pandas as pd

from CreateWord import create_word


def words_times_K():
    d0 = create_word(0, 'K')
    d1 = create_word(1, 'K')
    d2 = create_word(2, 'K')
    d3 = create_word(3, 'K')
    d4 = create_word(4, 'K')
    d5 = create_word(5, 'K')
    d6 = create_word(6, 'K')
    d7 = create_word(7, 'K')
    d8 = create_word(8, 'K')
    d9 = create_word(9, 'K')
    d10 = create_word(10, 'K')
    d11 = create_word(11, 'K')
    d12 = create_word(12, 'K')
    d13 = create_word(13, 'K')
    d14 = create_word(14, 'K')
    d15 = create_word(15, 'K')
    d16 = create_word(16, 'K')
    d17 = create_word(17, 'K')
    d18 = create_word(18, 'K')
    d19 = create_word(19, 'K')
    d20 = create_word(20, 'K')
    d21 = create_word(21, 'K')
    d22 = create_word(22, 'K')
    d23 = create_word(23, 'K')
    d24 = create_word(24, 'K')
    d25 = create_word(25, 'K')
    d26 = create_word(26, 'K')
    d27 = create_word(27, 'K')
    d28 = create_word(28, 'K')
    d29 = create_word(29, 'K')
    d30 = create_word(30, 'K')
    d31 = create_word(31, 'K')
    d32 = create_word(32, 'K')
    d33 = create_word(33, 'K')
    d34 = create_word(34, 'K')
    d35 = create_word(35, 'K')
    d36 = create_word(36, 'K')
    d37 = create_word(37, 'K')
    d38 = create_word(38, 'K')
    d39 = create_word(39, 'K')
    d40 = create_word(40, 'K')
    d41 = create_word(41, 'K')
    d42 = create_word(42, 'K')
    d43 = create_word(43, 'K')
    d44 = create_word(44, 'K')
    d45 = create_word(45, 'K')
    d46 = create_word(46, 'K')
    d47 = create_word(47, 'K')
    d48 = create_word(48, 'K')
    d49 = create_word(49, 'K')
    d50 = create_word(50, 'K')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

