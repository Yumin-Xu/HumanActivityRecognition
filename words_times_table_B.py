import pandas as pd

from CreateWord import create_word


def words_times_B():
    d0 = create_word(0, 'B')
    d1 = create_word(1, 'B')
    d2 = create_word(2, 'B')
    d3 = create_word(3, 'B')
    d4 = create_word(4, 'B')
    d5 = create_word(5, 'B')
    d6 = create_word(6, 'B')
    d7 = create_word(7, 'B')
    d8 = create_word(8, 'B')
    d9 = create_word(9, 'B')
    d10 = create_word(10, 'B')
    d11 = create_word(11, 'B')
    d12 = create_word(12, 'B')
    d13 = create_word(13, 'B')
    d14 = create_word(14, 'B')
    d15 = create_word(15, 'B')
    d16 = create_word(16, 'B')
    d17 = create_word(17, 'B')
    d18 = create_word(18, 'B')
    d19 = create_word(19, 'B')
    d20 = create_word(20, 'B')
    d21 = create_word(21, 'B')
    d22 = create_word(22, 'B')
    d23 = create_word(23, 'B')
    d24 = create_word(24, 'B')
    d25 = create_word(25, 'B')
    d26 = create_word(26, 'B')
    d27 = create_word(27, 'B')
    d28 = create_word(28, 'B')
    d29 = create_word(29, 'B')
    d30 = create_word(30, 'B')
    d31 = create_word(31, 'B')
    d32 = create_word(32, 'B')
    d33 = create_word(33, 'B')
    d34 = create_word(34, 'B')
    d35 = create_word(35, 'B')
    d36 = create_word(36, 'B')
    d37 = create_word(37, 'B')
    d38 = create_word(38, 'B')
    d39 = create_word(39, 'B')
    d40 = create_word(40, 'B')
    d41 = create_word(41, 'B')
    d42 = create_word(42, 'B')
    d43 = create_word(43, 'B')
    d44 = create_word(44, 'B')
    d45 = create_word(45, 'B')
    d46 = create_word(46, 'B')
    d47 = create_word(47, 'B')
    d48 = create_word(48, 'B')
    d49 = create_word(49, 'B')
    d50 = create_word(50, 'B')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

