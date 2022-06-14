import pandas as pd

from CreateWord import create_word


def words_times_E():
    d0 = create_word(0, 'E')
    d1 = create_word(1, 'E')
    d2 = create_word(2, 'E')
    d3 = create_word(3, 'E')
    d4 = create_word(4, 'E')
    d5 = create_word(5, 'E')
    d6 = create_word(6, 'E')
    d7 = create_word(7, 'E')
    d8 = create_word(8, 'E')
    d9 = create_word(9, 'E')
    d10 = create_word(10, 'E')
    d11 = create_word(11, 'E')
    d12 = create_word(12, 'E')
    d13 = create_word(13, 'E')
    d14 = create_word(14, 'E')
    d15 = create_word(15, 'E')
    d16 = create_word(16, 'E')
    d17 = create_word(17, 'E')
    d18 = create_word(18, 'E')
    d19 = create_word(19, 'E')
    d20 = create_word(20, 'E')
    d21 = create_word(21, 'E')
    d22 = create_word(22, 'E')
    d23 = create_word(23, 'E')
    d24 = create_word(24, 'E')
    d25 = create_word(25, 'E')
    d26 = create_word(26, 'E')
    d27 = create_word(27, 'E')
    d28 = create_word(28, 'E')
    d29 = create_word(29, 'E')
    d30 = create_word(30, 'E')
    d31 = create_word(31, 'E')
    d32 = create_word(32, 'E')
    d33 = create_word(33, 'E')
    d34 = create_word(34, 'E')
    d35 = create_word(35, 'E')
    d36 = create_word(36, 'E')
    d37 = create_word(37, 'E')
    d38 = create_word(38, 'E')
    d39 = create_word(39, 'E')
    d40 = create_word(40, 'E')
    d41 = create_word(41, 'E')
    d42 = create_word(42, 'E')
    d43 = create_word(43, 'E')
    d44 = create_word(44, 'E')
    d45 = create_word(45, 'E')
    d46 = create_word(46, 'E')
    d47 = create_word(47, 'E')
    d48 = create_word(48, 'E')
    d49 = create_word(49, 'E')
    d50 = create_word(50, 'E')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

