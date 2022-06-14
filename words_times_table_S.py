import pandas as pd

from CreateWord import create_word


def words_times_S():
    d0 = create_word(0, 'S')
    d1 = create_word(1, 'S')
    d2 = create_word(2, 'S')
    d3 = create_word(3, 'S')
    d4 = create_word(4, 'S')
    d5 = create_word(5, 'S')
    d6 = create_word(6, 'S')
    d7 = create_word(7, 'S')
    d8 = create_word(8, 'S')
    d9 = create_word(9, 'S')
    d10 = create_word(10, 'S')
    d11 = create_word(11, 'S')
    d12 = create_word(12, 'S')
    d13 = create_word(13, 'S')
    d14 = create_word(14, 'S')
    d15 = create_word(15, 'S')
    d16 = create_word(16, 'S')
    d17 = create_word(17, 'S')
    d18 = create_word(18, 'S')
    d19 = create_word(19, 'S')
    d20 = create_word(20, 'S')
    d21 = create_word(21, 'S')
    d22 = create_word(22, 'S')
    d23 = create_word(23, 'S')
    d24 = create_word(24, 'S')
    d25 = create_word(25, 'S')
    d26 = create_word(26, 'S')
    d27 = create_word(27, 'S')
    d28 = create_word(28, 'S')
    d29 = create_word(29, 'S')
    d30 = create_word(30, 'S')
    d31 = create_word(31, 'S')
    d32 = create_word(32, 'S')
    d33 = create_word(33, 'S')
    d34 = create_word(34, 'S')
    d35 = create_word(35, 'S')
    d36 = create_word(36, 'S')
    d37 = create_word(37, 'S')
    d38 = create_word(38, 'S')
    d39 = create_word(39, 'S')
    d40 = create_word(40, 'S')
    d41 = create_word(41, 'S')
    d42 = create_word(42, 'S')
    d43 = create_word(43, 'S')
    d44 = create_word(44, 'S')
    d45 = create_word(45, 'S')
    d46 = create_word(46, 'S')
    d47 = create_word(47, 'S')
    d48 = create_word(48, 'S')
    d49 = create_word(49, 'S')
    d50 = create_word(50, 'S')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

