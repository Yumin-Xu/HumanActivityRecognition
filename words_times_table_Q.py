import pandas as pd

from CreateWord import create_word


def words_times_Q():
    d0 = create_word(0, 'Q')
    d1 = create_word(1, 'Q')
    d2 = create_word(2, 'Q')
    d3 = create_word(3, 'Q')
    d4 = create_word(4, 'Q')
    d5 = create_word(5, 'Q')
    d6 = create_word(6, 'Q')
    d7 = create_word(7, 'Q')
    d8 = create_word(8, 'Q')
    d9 = create_word(9, 'Q')
    d10 = create_word(10, 'Q')
    d11 = create_word(11, 'Q')
    d12 = create_word(12, 'Q')
    d13 = create_word(13, 'Q')
    d14 = create_word(14, 'Q')
    d15 = create_word(15, 'Q')
    d16 = create_word(16, 'Q')
    d17 = create_word(17, 'Q')
    d18 = create_word(18, 'Q')
    d19 = create_word(19, 'Q')
    d20 = create_word(20, 'Q')
    d21 = create_word(21, 'Q')
    d22 = create_word(22, 'Q')
    d23 = create_word(23, 'Q')
    d24 = create_word(24, 'Q')
    d25 = create_word(25, 'Q')
    d26 = create_word(26, 'Q')
    d27 = create_word(27, 'Q')
    d28 = create_word(28, 'Q')
    d29 = create_word(29, 'Q')
    d30 = create_word(30, 'Q')
    d31 = create_word(31, 'Q')
    d32 = create_word(32, 'Q')
    d33 = create_word(33, 'Q')
    d34 = create_word(34, 'Q')
    d35 = create_word(35, 'Q')
    d36 = create_word(36, 'Q')
    d37 = create_word(37, 'Q')
    d38 = create_word(38, 'Q')
    d39 = create_word(39, 'Q')
    d40 = create_word(40, 'Q')
    d41 = create_word(41, 'Q')
    d42 = create_word(42, 'Q')
    d43 = create_word(43, 'Q')
    d44 = create_word(44, 'Q')
    d45 = create_word(45, 'Q')
    d46 = create_word(46, 'Q')
    d47 = create_word(47, 'Q')
    d48 = create_word(48, 'Q')
    d49 = create_word(49, 'Q')
    d50 = create_word(50, 'Q')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

