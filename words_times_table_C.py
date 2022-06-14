import pandas as pd

from CreateWord import create_word


def words_times_C():
    d0 = create_word(0, 'C')
    d1 = create_word(1, 'C')
    d2 = create_word(2, 'C')
    d3 = create_word(3, 'C')
    d4 = create_word(4, 'C')
    d5 = create_word(5, 'C')
    d6 = create_word(6, 'C')
    d7 = create_word(7, 'C')
    d8 = create_word(8, 'C')
    d9 = create_word(9, 'C')
    d10 = create_word(10, 'C')
    d11 = create_word(11, 'C')
    d12 = create_word(12, 'C')
    d13 = create_word(13, 'C')
    d14 = create_word(14, 'C')
    d15 = create_word(15, 'C')
    d16 = create_word(16, 'C')
    d17 = create_word(17, 'C')
    d18 = create_word(18, 'C')
    d19 = create_word(19, 'C')
    d20 = create_word(20, 'C')
    d21 = create_word(21, 'C')
    d22 = create_word(22, 'C')
    d23 = create_word(23, 'C')
    d24 = create_word(24, 'C')
    d25 = create_word(25, 'C')
    d26 = create_word(26, 'C')
    d27 = create_word(27, 'C')
    d28 = create_word(28, 'C')
    d29 = create_word(29, 'C')
    d30 = create_word(30, 'C')
    d31 = create_word(31, 'C')
    d32 = create_word(32, 'C')
    d33 = create_word(33, 'C')
    d34 = create_word(34, 'C')
    d35 = create_word(35, 'C')
    d36 = create_word(36, 'C')
    d37 = create_word(37, 'C')
    d38 = create_word(38, 'C')
    d39 = create_word(39, 'C')
    d40 = create_word(40, 'C')
    d41 = create_word(41, 'C')
    d42 = create_word(42, 'C')
    d43 = create_word(43, 'C')
    d44 = create_word(44, 'C')
    d45 = create_word(45, 'C')
    d46 = create_word(46, 'C')
    d47 = create_word(47, 'C')
    d48 = create_word(48, 'C')
    d49 = create_word(49, 'C')
    d50 = create_word(50, 'C')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

