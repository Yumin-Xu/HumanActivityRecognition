import pandas as pd

from CreateWord import create_word


def words_times_I():
    d0 = create_word(0, 'I')
    d1 = create_word(1, 'I')
    d2 = create_word(2, 'I')
    d3 = create_word(3, 'I')
    d4 = create_word(4, 'I')
    d5 = create_word(5, 'I')
    d6 = create_word(6, 'I')
    d7 = create_word(7, 'I')
    d8 = create_word(8, 'I')
    d9 = create_word(9, 'I')
    d10 = create_word(10, 'I')
    d11 = create_word(11, 'I')
    d12 = create_word(12, 'I')
    d13 = create_word(13, 'I')
    d14 = create_word(14, 'I')
    d15 = create_word(15, 'I')
    d16 = create_word(16, 'I')
    d17 = create_word(17, 'I')
    d18 = create_word(18, 'I')
    d19 = create_word(19, 'I')
    d20 = create_word(20, 'I')
    d21 = create_word(21, 'I')
    d22 = create_word(22, 'I')
    d23 = create_word(23, 'I')
    d24 = create_word(24, 'I')
    d25 = create_word(25, 'I')
    d26 = create_word(26, 'I')
    d27 = create_word(27, 'I')
    d28 = create_word(28, 'I')
    d29 = create_word(29, 'I')
    d30 = create_word(30, 'I')
    d31 = create_word(31, 'I')
    d32 = create_word(32, 'I')
    d33 = create_word(33, 'I')
    d34 = create_word(34, 'I')
    d35 = create_word(35, 'I')
    d36 = create_word(36, 'I')
    d37 = create_word(37, 'I')
    d38 = create_word(38, 'I')
    d39 = create_word(39, 'I')
    d40 = create_word(40, 'I')
    d41 = create_word(41, 'I')
    d42 = create_word(42, 'I')
    d43 = create_word(43, 'I')
    d44 = create_word(44, 'I')
    d45 = create_word(45, 'I')
    d46 = create_word(46, 'I')
    d47 = create_word(47, 'I')
    d48 = create_word(48, 'I')
    d49 = create_word(49, 'I')
    d50 = create_word(50, 'I')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

