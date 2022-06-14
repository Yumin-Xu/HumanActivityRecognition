import pandas as pd

from CreateWord import create_word


def words_times_N():
    d0 = create_word(0, 'N')
    d1 = create_word(1, 'N')
    d2 = create_word(2, 'N')
    d3 = create_word(3, 'N')
    d4 = create_word(4, 'N')
    d5 = create_word(5, 'N')
    d6 = create_word(6, 'N')
    d7 = create_word(7, 'N')
    d8 = create_word(8, 'N')
    d9 = create_word(9, 'N')
    d10 = create_word(10, 'N')
    d11 = create_word(11, 'N')
    d12 = create_word(12, 'N')
    d13 = create_word(13, 'N')
    d14 = create_word(14, 'N')
    d15 = create_word(15, 'N')
    d16 = create_word(16, 'N')
    d17 = create_word(17, 'N')
    d18 = create_word(18, 'N')
    d19 = create_word(19, 'N')
    d20 = create_word(20, 'N')
    d21 = create_word(21, 'N')
    d22 = create_word(22, 'N')
    d23 = create_word(23, 'N')
    d24 = create_word(24, 'N')
    d25 = create_word(25, 'N')
    d26 = create_word(26, 'N')
    d27 = create_word(27, 'N')
    d28 = create_word(28, 'N')
    d29 = create_word(29, 'N')
    d30 = create_word(30, 'N')
    d31 = create_word(31, 'N')
    d32 = create_word(32, 'N')
    d33 = create_word(33, 'N')
    d34 = create_word(34, 'N')
    d35 = create_word(35, 'N')
    d36 = create_word(36, 'N')
    d37 = create_word(37, 'N')
    d38 = create_word(38, 'N')
    d39 = create_word(39, 'N')
    d40 = create_word(40, 'N')
    d41 = create_word(41, 'N')
    d42 = create_word(42, 'N')
    d43 = create_word(43, 'N')
    d44 = create_word(44, 'N')
    d45 = create_word(45, 'N')
    d46 = create_word(46, 'N')
    d47 = create_word(47, 'N')
    d48 = create_word(48, 'N')
    d49 = create_word(49, 'N')
    d50 = create_word(50, 'N')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

