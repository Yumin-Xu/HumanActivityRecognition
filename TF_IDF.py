from collections import Counter

import imblearn as imblearn
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification
from sklearn.utils import shuffle

import OpenCheck
from OpenData_label import csv_label_file

d1 = csv_label_file(0)
d2 = csv_label_file(1)
d3 = csv_label_file(2)
d4 = csv_label_file(3)
d5 = csv_label_file(4)
d6 = csv_label_file(5)
d7 = csv_label_file(6)
d8 = csv_label_file(7)
d9 = csv_label_file(8)
d10 = csv_label_file(9)
d11 = csv_label_file(10)
d12 = csv_label_file(11)
d13 = csv_label_file(12)
d15 = csv_label_file(13)
d16 = csv_label_file(14)
d17 = csv_label_file(15)
d18 = csv_label_file(16)
d19 = csv_label_file(17)

d = pd.concat([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)


# from ML_Data import pre_A

def IDF_test():
    d2['label'] = 1
    df1 = d2
    df1 = df1[df1['words'] > 0]
    df2 = pd.concat([d1, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    sp1 = pd.DataFrame(df2[df2['words'].isin(df1['words'])])
    sp1['label'] = 1
    sp2 = pd.DataFrame(df2[~df2['words'].isin(df1['words'])])  # .sample(1 * len(sp1))
    sp2['label'] = 0
    df2 = pd.concat([sp1, sp2], ignore_index=True)

    test = shuffle(pd.concat([df1, df2]))

    rs = np.array(test['words']).reshape(-1, 1)
    ls = np.array(test['label']).reshape(-1, 1)

    sample = SMOTE()
    test = sample.fit_resample(X=rs, y=ls)
    df = pd.DataFrame({'words': pd.DataFrame(test[0], columns=['words'])['words'],
                       'label': pd.DataFrame(test[1], columns=['label'])['label']})
    df = df.sample(10000)
    return df


print(IDF_test().value_counts())


def test_no_IDF():
    d1['label'] = 1
    test2 = pd.concat([d2.sample(int(len(d1) / 17)), d3.sample(int(len(d1) / 17)), d4.sample(int(len(d1) / 17)),
                       d5.sample(int(len(d1) / 17)), d6.sample(int(len(d1) / 17)), d7.sample(int(len(d1) / 17)),
                       d8.sample(int(len(d1) / 17)), d9.sample(int(len(d1) / 17)), d10.sample(int(len(d1) / 17)),
                       d11.sample(int(len(d1) / 17)), d12.sample(int(len(d1) / 17)), d13.sample(int(len(d1) / 17)),
                       d15.sample(int(len(d1) / 17)), d16.sample(int(len(d1) / 17)), d17.sample(int(len(d1) / 17)),
                       d18.sample(int(len(d1) / 17)), d19.sample(int(len(d1) / 17))], ignore_index=True)
    test2['label'] = 0
    test = shuffle(pd.concat([d1, test2], ignore_index=True))
    return test
