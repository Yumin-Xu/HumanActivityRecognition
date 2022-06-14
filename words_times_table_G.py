import pandas as pd

from CreateWord import create_word


def words_times_G():
    d0 = create_word(0, 'G')
    d1 = create_word(1, 'G')
    d2 = create_word(2, 'G')
    d3 = create_word(3, 'G')
    d4 = create_word(4, 'G')
    d5 = create_word(5, 'G')
    d6 = create_word(6, 'G')
    d7 = create_word(7, 'G')
    d8 = create_word(8, 'G')
    d9 = create_word(9, 'G')
    d10 = create_word(10, 'G')
    d11 = create_word(11, 'G')
    d12 = create_word(12, 'G')
    d13 = create_word(13, 'G')
    d14 = create_word(14, 'G')
    d15 = create_word(15, 'G')
    d16 = create_word(16, 'G')
    d17 = create_word(17, 'G')
    d18 = create_word(18, 'G')
    d19 = create_word(19, 'G')
    d20 = create_word(20, 'G')
    d21 = create_word(21, 'G')
    d22 = create_word(22, 'G')
    d23 = create_word(23, 'G')
    d24 = create_word(24, 'G')
    d25 = create_word(25, 'G')
    d26 = create_word(26, 'G')
    d27 = create_word(27, 'G')
    d28 = create_word(28, 'G')
    d29 = create_word(29, 'G')
    d30 = create_word(30, 'G')
    d31 = create_word(31, 'G')
    d32 = create_word(32, 'G')
    d33 = create_word(33, 'G')
    d34 = create_word(34, 'G')
    d35 = create_word(35, 'G')
    d36 = create_word(36, 'G')
    d37 = create_word(37, 'G')
    d38 = create_word(38, 'G')
    d39 = create_word(39, 'G')
    d40 = create_word(40, 'G')
    d41 = create_word(41, 'G')
    d42 = create_word(42, 'G')
    d43 = create_word(43, 'G')
    d44 = create_word(44, 'G')
    d45 = create_word(45, 'G')
    d46 = create_word(46, 'G')
    d47 = create_word(47, 'G')
    d48 = create_word(48, 'G')
    d49 = create_word(49, 'G')
    d50 = create_word(50, 'G')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

