import pandas as pd

from CreateWord import create_word


def words_times_O():
    d0 = create_word(0, 'O')
    d1 = create_word(1, 'O')
    d2 = create_word(2, 'O')
    d3 = create_word(3, 'O')
    d4 = create_word(4, 'O')
    d5 = create_word(5, 'O')
    d6 = create_word(6, 'O')
    d7 = create_word(7, 'O')
    d8 = create_word(8, 'O')
    d9 = create_word(9, 'O')
    d10 = create_word(10, 'O')
    d11 = create_word(11, 'O')
    d12 = create_word(12, 'O')
    d13 = create_word(13, 'O')
    d14 = create_word(14, 'O')
    d15 = create_word(15, 'O')
    d16 = create_word(16, 'O')
    d17 = create_word(17, 'O')
    d18 = create_word(18, 'O')
    d19 = create_word(19, 'O')
    d20 = create_word(20, 'O')
    d21 = create_word(21, 'O')
    d22 = create_word(22, 'O')
    d23 = create_word(23, 'O')
    d24 = create_word(24, 'O')
    d25 = create_word(25, 'O')
    d26 = create_word(26, 'O')
    d27 = create_word(27, 'O')
    d28 = create_word(28, 'O')
    d29 = create_word(29, 'O')
    d30 = create_word(30, 'O')
    d31 = create_word(31, 'O')
    d32 = create_word(32, 'O')
    d33 = create_word(33, 'O')
    d34 = create_word(34, 'O')
    d35 = create_word(35, 'O')
    d36 = create_word(36, 'O')
    d37 = create_word(37, 'O')
    d38 = create_word(38, 'O')
    d39 = create_word(39, 'O')
    d40 = create_word(40, 'O')
    d41 = create_word(41, 'O')
    d42 = create_word(42, 'O')
    d43 = create_word(43, 'O')
    d44 = create_word(44, 'O')
    d45 = create_word(45, 'O')
    d46 = create_word(46, 'O')
    d47 = create_word(47, 'O')
    d48 = create_word(48, 'O')
    d49 = create_word(49, 'O')
    d50 = create_word(50, 'O')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    #count = d['words'].value_counts().sort_values()
    #return count
    return d

