import pandas as pd

from CreateWord import create_word


def words_times_J():
    d0 = create_word(0, 'J')
    d1 = create_word(1, 'J')
    d2 = create_word(2, 'J')
    d3 = create_word(3, 'J')
    d4 = create_word(4, 'J')
    d5 = create_word(5, 'J')
    d6 = create_word(6, 'J')
    d7 = create_word(7, 'J')
    d8 = create_word(8, 'J')
    d9 = create_word(9, 'J')
    d10 = create_word(10, 'J')
    d11 = create_word(11, 'J')
    d12 = create_word(12, 'J')
    d13 = create_word(13, 'J')
    d14 = create_word(14, 'J')
    d15 = create_word(15, 'J')
    d16 = create_word(16, 'J')
    d17 = create_word(17, 'J')
    d18 = create_word(18, 'J')
    d19 = create_word(19, 'J')
    d20 = create_word(20, 'J')
    d21 = create_word(21, 'J')
    d22 = create_word(22, 'J')
    d23 = create_word(23, 'J')
    d24 = create_word(24, 'J')
    d25 = create_word(25, 'J')
    d26 = create_word(26, 'J')
    d27 = create_word(27, 'J')
    d28 = create_word(28, 'J')
    d29 = create_word(29, 'J')
    d30 = create_word(30, 'J')
    d31 = create_word(31, 'J')
    d32 = create_word(32, 'J')
    d33 = create_word(33, 'J')
    d34 = create_word(34, 'J')
    d35 = create_word(35, 'J')
    d36 = create_word(36, 'J')
    d37 = create_word(37, 'J')
    d38 = create_word(38, 'J')
    d39 = create_word(39, 'J')
    d40 = create_word(40, 'J')
    d41 = create_word(41, 'J')
    d42 = create_word(42, 'J')
    d43 = create_word(43, 'J')
    d44 = create_word(44, 'J')
    d45 = create_word(45, 'J')
    d46 = create_word(46, 'J')
    d47 = create_word(47, 'J')
    d48 = create_word(48, 'J')
    d49 = create_word(49, 'J')
    d50 = create_word(50, 'J')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

