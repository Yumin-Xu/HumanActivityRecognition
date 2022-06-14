import pandas as pd

from CreateWord import create_word


def words_times_F():
    d0 = create_word(0, 'F')
    d1 = create_word(1, 'F')
    d2 = create_word(2, 'F')
    d3 = create_word(3, 'F')
    d4 = create_word(4, 'F')
    d5 = create_word(5, 'F')
    d6 = create_word(6, 'F')
    d7 = create_word(7, 'F')
    d8 = create_word(8, 'F')
    d9 = create_word(9, 'F')
    d10 = create_word(10, 'F')
    d11 = create_word(11, 'F')
    d12 = create_word(12, 'F')
    d13 = create_word(13, 'F')
    d14 = create_word(14, 'F')
    d15 = create_word(15, 'F')
    d16 = create_word(16, 'F')
    d17 = create_word(17, 'F')
    d18 = create_word(18, 'F')
    d19 = create_word(19, 'F')
    d20 = create_word(20, 'F')
    d21 = create_word(21, 'F')
    d22 = create_word(22, 'F')
    d23 = create_word(23, 'F')
    d24 = create_word(24, 'F')
    d25 = create_word(25, 'F')
    d26 = create_word(26, 'F')
    d27 = create_word(27, 'F')
    d28 = create_word(28, 'F')
    d29 = create_word(29, 'F')
    d30 = create_word(30, 'F')
    d31 = create_word(31, 'F')
    d32 = create_word(32, 'F')
    d33 = create_word(33, 'F')
    d34 = create_word(34, 'F')
    d35 = create_word(35, 'F')
    d36 = create_word(36, 'F')
    d37 = create_word(37, 'F')
    d38 = create_word(38, 'F')
    d39 = create_word(39, 'F')
    d40 = create_word(40, 'F')
    d41 = create_word(41, 'F')
    d42 = create_word(42, 'F')
    d43 = create_word(43, 'F')
    d44 = create_word(44, 'F')
    d45 = create_word(45, 'F')
    d46 = create_word(46, 'F')
    d47 = create_word(47, 'F')
    d48 = create_word(48, 'F')
    d49 = create_word(49, 'F')
    d50 = create_word(50, 'F')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

