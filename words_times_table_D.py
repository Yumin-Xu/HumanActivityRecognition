import pandas as pd

from CreateWord import create_word


def words_times_D():
    d0 = create_word(0, 'D')
    d1 = create_word(1, 'D')
    d2 = create_word(2, 'D')
    d3 = create_word(3, 'D')
    d4 = create_word(4, 'D')
    d5 = create_word(5, 'D')
    d6 = create_word(6, 'D')
    d7 = create_word(7, 'D')
    d8 = create_word(8, 'D')
    d9 = create_word(9, 'D')
    d10 = create_word(10, 'D')
    d11 = create_word(11, 'D')
    d12 = create_word(12, 'D')
    d13 = create_word(13, 'D')
    d14 = create_word(14, 'D')
    d15 = create_word(15, 'D')
    d16 = create_word(16, 'D')
    d17 = create_word(17, 'D')
    d18 = create_word(18, 'D')
    d19 = create_word(19, 'D')
    d20 = create_word(20, 'D')
    d21 = create_word(21, 'D')
    d22 = create_word(22, 'D')
    d23 = create_word(23, 'D')
    d24 = create_word(24, 'D')
    d25 = create_word(25, 'D')
    d26 = create_word(26, 'D')
    d27 = create_word(27, 'D')
    d28 = create_word(28, 'D')
    d29 = create_word(29, 'D')
    d30 = create_word(30, 'D')
    d31 = create_word(31, 'D')
    d32 = create_word(32, 'D')
    d33 = create_word(33, 'D')
    d34 = create_word(34, 'D')
    d35 = create_word(35, 'D')
    d36 = create_word(36, 'D')
    d37 = create_word(37, 'D')
    d38 = create_word(38, 'D')
    d39 = create_word(39, 'D')
    d40 = create_word(40, 'D')
    d41 = create_word(41, 'D')
    d42 = create_word(42, 'D')
    d43 = create_word(43, 'D')
    d44 = create_word(44, 'D')
    d45 = create_word(45, 'D')
    d46 = create_word(46, 'D')
    d47 = create_word(47, 'D')
    d48 = create_word(48, 'D')
    d49 = create_word(49, 'D')
    d50 = create_word(50, 'D')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

