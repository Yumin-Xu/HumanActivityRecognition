import numpy as np
import pandas as pd

from CreateWord import create_word


def words_times_A():
    d0 = create_word(0, 'A')
    d1 = create_word(1, 'A')
    d2 = create_word(2, 'A')
    d3 = create_word(3, 'A')
    d4 = create_word(4, 'A')
    d5 = create_word(5, 'A')
    d6 = create_word(6, 'A')
    d7 = create_word(7, 'A')
    d8 = create_word(8, 'A')
    d9 = create_word(9, 'A')
    d10 = create_word(10, 'A')
    d11 = create_word(11, 'A')
    d12 = create_word(12, 'A')
    d13 = create_word(13, 'A')
    d14 = create_word(14, 'A')
    d15 = create_word(15, 'A')
    d16 = create_word(16, 'A')
    d17 = create_word(17, 'A')
    d18 = create_word(18, 'A')
    d19 = create_word(19, 'A')
    d20 = create_word(20, 'A')
    d21 = create_word(21, 'A')
    d22 = create_word(22, 'A')
    d23 = create_word(23, 'A')
    d24 = create_word(24, 'A')
    d25 = create_word(25, 'A')
    d26 = create_word(26, 'A')
    d27 = create_word(27, 'A')
    d28 = create_word(28, 'A')
    d29 = create_word(29, 'A')
    d30 = create_word(30, 'A')
    d31 = create_word(31, 'A')
    d32 = create_word(32, 'A')
    d33 = create_word(33, 'A')
    d34 = create_word(34, 'A')
    d35 = create_word(35, 'A')
    d36 = create_word(36, 'A')
    d37 = create_word(37, 'A')
    d38 = create_word(38, 'A')
    d39 = create_word(39, 'A')
    d40 = create_word(40, 'A')
    d41 = create_word(41, 'A')
    d42 = create_word(42, 'A')
    d43 = create_word(43, 'A')
    d44 = create_word(44, 'A')
    d45 = create_word(45, 'A')
    d46 = create_word(46, 'A')
    d47 = create_word(47, 'A')
    d48 = create_word(48, 'A')
    d49 = create_word(49, 'A')
    d50 = create_word(50, 'A')

    d = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)
    # count = d['words'].value_counts().sort_values()
    # return count
    return d


print(words_times_A())
