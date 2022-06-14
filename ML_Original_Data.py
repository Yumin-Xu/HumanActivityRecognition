import os
from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree, svm, metrics, linear_model
from sklearn.ensemble import AdaBoostClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.linear_model._sgd_fast import Regression
from sklearn.metrics import roc_curve, auc, plot_confusion_matrix, accuracy_score, confusion_matrix, \
    ConfusionMatrixDisplay, PrecisionRecallDisplay, precision_score, recall_score, precision_recall_curve, \
    classification_report, RocCurveDisplay, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle

import OpenData_phone_accel
import OpenData_phone_gyro
import OpenData_watch_accel
import OpenData_watch_gyro
from TF_IDF import IDF_test, test_no_IDF

# OpenData_phone_accel
d0 = OpenData_phone_accel.csv_new_file(0)
d1 = OpenData_phone_accel.csv_new_file(1)
d2 = OpenData_phone_accel.csv_new_file(2)
d3 = OpenData_phone_accel.csv_new_file(3)
d4 = OpenData_phone_accel.csv_new_file(4)
d5 = OpenData_phone_accel.csv_new_file(5)
d6 = OpenData_phone_accel.csv_new_file(6)
d7 = OpenData_phone_accel.csv_new_file(7)
d8 = OpenData_phone_accel.csv_new_file(8)
d9 = OpenData_phone_accel.csv_new_file(9)
d10 = OpenData_phone_accel.csv_new_file(10)
d11 = OpenData_phone_accel.csv_new_file(11)
d12 = OpenData_phone_accel.csv_new_file(12)
d13 = OpenData_phone_accel.csv_new_file(13)
d14 = OpenData_phone_accel.csv_new_file(14)
d15 = OpenData_phone_accel.csv_new_file(15)
d16 = OpenData_phone_accel.csv_new_file(16)
d17 = OpenData_phone_accel.csv_new_file(17)
d18 = OpenData_phone_accel.csv_new_file(18)
d19 = OpenData_phone_accel.csv_new_file(19)
d20 = OpenData_phone_accel.csv_new_file(20)
d21 = OpenData_phone_accel.csv_new_file(21)
d22 = OpenData_phone_accel.csv_new_file(22)
d23 = OpenData_phone_accel.csv_new_file(23)
d24 = OpenData_phone_accel.csv_new_file(24)
d25 = OpenData_phone_accel.csv_new_file(25)
d26 = OpenData_phone_accel.csv_new_file(26)
d27 = OpenData_phone_accel.csv_new_file(27)
d28 = OpenData_phone_accel.csv_new_file(28)
d29 = OpenData_phone_accel.csv_new_file(29)
d30 = OpenData_phone_accel.csv_new_file(30)
d31 = OpenData_phone_accel.csv_new_file(31)
d32 = OpenData_phone_accel.csv_new_file(32)
d33 = OpenData_phone_accel.csv_new_file(33)
d34 = OpenData_phone_accel.csv_new_file(34)
d35 = OpenData_phone_accel.csv_new_file(35)
d36 = OpenData_phone_accel.csv_new_file(36)
d37 = OpenData_phone_accel.csv_new_file(37)
d38 = OpenData_phone_accel.csv_new_file(38)
d39 = OpenData_phone_accel.csv_new_file(39)
d40 = OpenData_phone_accel.csv_new_file(40)
d41 = OpenData_phone_accel.csv_new_file(41)
d42 = OpenData_phone_accel.csv_new_file(42)
d43 = OpenData_phone_accel.csv_new_file(43)
d44 = OpenData_phone_accel.csv_new_file(44)
d45 = OpenData_phone_accel.csv_new_file(45)
d46 = OpenData_phone_accel.csv_new_file(46)
d47 = OpenData_phone_accel.csv_new_file(47)
d48 = OpenData_phone_accel.csv_new_file(48)
d49 = OpenData_phone_accel.csv_new_file(49)
d50 = OpenData_phone_accel.csv_new_file(50)

df1 = pd.concat([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                 d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                 d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                 d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                 d41, d42, d43, d44, d45, d46, d47, d48, d49, d50], ignore_index=True)

# OpenData_phone_gyro
g0 = OpenData_phone_gyro.csv_new_file(0)
g1 = OpenData_phone_gyro.csv_new_file(1)
g2 = OpenData_phone_gyro.csv_new_file(2)
g3 = OpenData_phone_gyro.csv_new_file(3)
g4 = OpenData_phone_gyro.csv_new_file(4)
g5 = OpenData_phone_gyro.csv_new_file(5)
g6 = OpenData_phone_gyro.csv_new_file(6)
g7 = OpenData_phone_gyro.csv_new_file(7)
g8 = OpenData_phone_gyro.csv_new_file(8)
g9 = OpenData_phone_gyro.csv_new_file(9)
g10 = OpenData_phone_gyro.csv_new_file(10)
g11 = OpenData_phone_gyro.csv_new_file(11)
g12 = OpenData_phone_gyro.csv_new_file(12)
g13 = OpenData_phone_gyro.csv_new_file(13)
g14 = OpenData_phone_gyro.csv_new_file(14)
g15 = OpenData_phone_gyro.csv_new_file(15)
g16 = OpenData_phone_gyro.csv_new_file(16)
g17 = OpenData_phone_gyro.csv_new_file(17)
g18 = OpenData_phone_gyro.csv_new_file(18)
g19 = OpenData_phone_gyro.csv_new_file(19)
g20 = OpenData_phone_gyro.csv_new_file(20)
g21 = OpenData_phone_gyro.csv_new_file(21)
g22 = OpenData_phone_gyro.csv_new_file(22)
g23 = OpenData_phone_gyro.csv_new_file(23)
g24 = OpenData_phone_gyro.csv_new_file(24)
g25 = OpenData_phone_gyro.csv_new_file(25)
g26 = OpenData_phone_gyro.csv_new_file(26)
g27 = OpenData_phone_gyro.csv_new_file(27)
g28 = OpenData_phone_gyro.csv_new_file(28)
g29 = OpenData_phone_gyro.csv_new_file(29)
g30 = OpenData_phone_gyro.csv_new_file(30)
g31 = OpenData_phone_gyro.csv_new_file(31)
g32 = OpenData_phone_gyro.csv_new_file(32)
g33 = OpenData_phone_gyro.csv_new_file(33)
g34 = OpenData_phone_gyro.csv_new_file(34)
g35 = OpenData_phone_gyro.csv_new_file(35)
g36 = OpenData_phone_gyro.csv_new_file(36)
g37 = OpenData_phone_gyro.csv_new_file(37)
g38 = OpenData_phone_gyro.csv_new_file(38)
g39 = OpenData_phone_gyro.csv_new_file(39)
g40 = OpenData_phone_gyro.csv_new_file(40)
g41 = OpenData_phone_gyro.csv_new_file(41)
g42 = OpenData_phone_gyro.csv_new_file(42)
g43 = OpenData_phone_gyro.csv_new_file(43)
g44 = OpenData_phone_gyro.csv_new_file(44)
g45 = OpenData_phone_gyro.csv_new_file(45)
g46 = OpenData_phone_gyro.csv_new_file(46)
g47 = OpenData_phone_gyro.csv_new_file(47)
g48 = OpenData_phone_gyro.csv_new_file(48)
g49 = OpenData_phone_gyro.csv_new_file(49)
g50 = OpenData_phone_gyro.csv_new_file(50)

df2 = pd.concat([g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10,
                 g11, g12, g13, g14, g15, g16, g17, g18, g19, g20,
                 g21, g22, g23, g24, g25, g26, g27, g28, g29, g30,
                 g31, g32, g33, g34, g35, g36, g37, g38, g39, g40,
                 g41, g42, g43, g44, g45, g46, g47, g48, g49, g50], ignore_index=True)

# OpenData_watch_accel
x0 = OpenData_watch_accel.csv_new_file(0)
x1 = OpenData_watch_accel.csv_new_file(1)
x2 = OpenData_watch_accel.csv_new_file(2)
x3 = OpenData_watch_accel.csv_new_file(3)
x4 = OpenData_watch_accel.csv_new_file(4)
x5 = OpenData_watch_accel.csv_new_file(5)
x6 = OpenData_watch_accel.csv_new_file(6)
x7 = OpenData_watch_accel.csv_new_file(7)
x8 = OpenData_watch_accel.csv_new_file(8)
x9 = OpenData_watch_accel.csv_new_file(9)
x10 = OpenData_watch_accel.csv_new_file(10)
x11 = OpenData_watch_accel.csv_new_file(11)
x12 = OpenData_watch_accel.csv_new_file(12)
x13 = OpenData_watch_accel.csv_new_file(13)
x14 = OpenData_watch_accel.csv_new_file(14)
x15 = OpenData_watch_accel.csv_new_file(15)
x16 = OpenData_watch_accel.csv_new_file(16)
x17 = OpenData_watch_accel.csv_new_file(17)
x18 = OpenData_watch_accel.csv_new_file(18)
x19 = OpenData_watch_accel.csv_new_file(19)
x20 = OpenData_watch_accel.csv_new_file(20)
x21 = OpenData_watch_accel.csv_new_file(21)
x22 = OpenData_watch_accel.csv_new_file(22)
x23 = OpenData_watch_accel.csv_new_file(23)
x24 = OpenData_watch_accel.csv_new_file(24)
x25 = OpenData_watch_accel.csv_new_file(25)
x26 = OpenData_watch_accel.csv_new_file(26)
x27 = OpenData_watch_accel.csv_new_file(27)
x28 = OpenData_watch_accel.csv_new_file(28)
x29 = OpenData_watch_accel.csv_new_file(29)
x30 = OpenData_watch_accel.csv_new_file(30)
x31 = OpenData_watch_accel.csv_new_file(31)
x32 = OpenData_watch_accel.csv_new_file(32)
x33 = OpenData_watch_accel.csv_new_file(33)
x34 = OpenData_watch_accel.csv_new_file(34)
x35 = OpenData_watch_accel.csv_new_file(35)
x36 = OpenData_watch_accel.csv_new_file(36)
x37 = OpenData_watch_accel.csv_new_file(37)
x38 = OpenData_watch_accel.csv_new_file(38)
x39 = OpenData_watch_accel.csv_new_file(39)
x40 = OpenData_watch_accel.csv_new_file(40)
x41 = OpenData_watch_accel.csv_new_file(41)
x42 = OpenData_watch_accel.csv_new_file(42)
x43 = OpenData_watch_accel.csv_new_file(43)
x44 = OpenData_watch_accel.csv_new_file(44)
x45 = OpenData_watch_accel.csv_new_file(45)
x46 = OpenData_watch_accel.csv_new_file(46)
x47 = OpenData_watch_accel.csv_new_file(47)
x48 = OpenData_watch_accel.csv_new_file(48)
x49 = OpenData_watch_accel.csv_new_file(49)
x50 = OpenData_watch_accel.csv_new_file(50)

df3 = pd.concat([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,
                 x11, x12, x13, x14, x15, x16, x17, x18, x19, x20,
                 x21, x22, x23, x24, x25, x26, x27, x28, x29, x30,
                 x31, x32, x33, x34, x35, x36, x37, x38, x39, x40,
                 x41, x42, x43, x44, x45, x46, x47, x48, x49, x50], ignore_index=True)

# OpenData_watch_gyro
y0 = OpenData_watch_gyro.csv_new_file(0)
y1 = OpenData_watch_gyro.csv_new_file(1)
y2 = OpenData_watch_gyro.csv_new_file(2)
y3 = OpenData_watch_gyro.csv_new_file(3)
y4 = OpenData_watch_gyro.csv_new_file(4)
y5 = OpenData_watch_gyro.csv_new_file(5)
y6 = OpenData_watch_gyro.csv_new_file(6)
y7 = OpenData_watch_gyro.csv_new_file(7)
y8 = OpenData_watch_gyro.csv_new_file(8)
y9 = OpenData_watch_gyro.csv_new_file(9)
y10 = OpenData_watch_gyro.csv_new_file(10)
y11 = OpenData_watch_gyro.csv_new_file(11)
y12 = OpenData_watch_gyro.csv_new_file(12)
y13 = OpenData_watch_gyro.csv_new_file(13)
y14 = OpenData_watch_gyro.csv_new_file(14)
y15 = OpenData_watch_gyro.csv_new_file(15)
y16 = OpenData_watch_gyro.csv_new_file(16)
y17 = OpenData_watch_gyro.csv_new_file(17)
y18 = OpenData_watch_gyro.csv_new_file(18)
y19 = OpenData_watch_gyro.csv_new_file(19)
y20 = OpenData_watch_gyro.csv_new_file(20)
y21 = OpenData_watch_gyro.csv_new_file(21)
y22 = OpenData_watch_gyro.csv_new_file(22)
y23 = OpenData_watch_gyro.csv_new_file(23)
y24 = OpenData_watch_gyro.csv_new_file(24)
y25 = OpenData_watch_gyro.csv_new_file(25)
y26 = OpenData_watch_gyro.csv_new_file(26)
y27 = OpenData_watch_gyro.csv_new_file(27)
y28 = OpenData_watch_gyro.csv_new_file(28)
y29 = OpenData_watch_gyro.csv_new_file(29)
y30 = OpenData_watch_gyro.csv_new_file(30)
y31 = OpenData_watch_gyro.csv_new_file(31)
y32 = OpenData_watch_gyro.csv_new_file(32)
y33 = OpenData_watch_gyro.csv_new_file(33)
y34 = OpenData_watch_gyro.csv_new_file(34)
y35 = OpenData_watch_gyro.csv_new_file(35)
y36 = OpenData_watch_gyro.csv_new_file(36)
y37 = OpenData_watch_gyro.csv_new_file(37)
y38 = OpenData_watch_gyro.csv_new_file(38)
y39 = OpenData_watch_gyro.csv_new_file(39)
y40 = OpenData_watch_gyro.csv_new_file(40)
y41 = OpenData_watch_gyro.csv_new_file(41)
y42 = OpenData_watch_gyro.csv_new_file(42)
y43 = OpenData_watch_gyro.csv_new_file(43)
y44 = OpenData_watch_gyro.csv_new_file(44)
y45 = OpenData_watch_gyro.csv_new_file(45)
y46 = OpenData_watch_gyro.csv_new_file(46)
y47 = OpenData_watch_gyro.csv_new_file(47)
y48 = OpenData_watch_gyro.csv_new_file(48)
y49 = OpenData_watch_gyro.csv_new_file(49)
y50 = OpenData_watch_gyro.csv_new_file(50)

df4 = pd.concat([y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10,
                 y11, y12, y13, y14, y15, y16, y17, y18, y19, y20,
                 y21, y22, y23, y24, y25, y26, y27, y28, y29, y30,
                 y31, y32, y33, y34, y35, y36, y37, y38, y39, y40,
                 y41, y42, y43, y44, y45, y46, y47, y48, y49, y50], ignore_index=True)

df = pd.concat([df1, df2, df3, df4], ignore_index=True)


def csv_file():
    f1 = pd.read_csv('E:/Pycharm/HumanActivityRecognition/full_data.csv')
    return pd.DataFrame(f1)


full = shuffle(csv_file().sample(10000))
train, test = train_test_split(full, test_size=0.2, shuffle=True)
train_x = np.array(pd.DataFrame(train)[['x', 'y', 'z']])  # .reshape(-1, 1)
train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
test_x = np.array(pd.DataFrame(test)[['x', 'y', 'z']])  # .reshape(-1, 1)
test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

clf1 = KNeighborsClassifier(n_neighbors=7)
clf2 = tree.DecisionTreeClassifier(criterion="entropy")
clf3 = svm.SVC(kernel="rbf", probability=True)
clf4 = LogisticRegression()
clf5 = GaussianNB()
clf6 = AdaBoostClassifier(n_estimators=100, random_state=42)
clf7 = MLPClassifier(random_state=42, max_iter=300)

elf = VotingClassifier(estimators=[('KNN', clf1), ('TD', clf2), ('SVM', clf3), ('LR', clf4),
                                   ('GNB', clf5), ('ADA', clf6), ('MLP', clf7)], voting='soft')

elf.fit(train_x, train_y)
pre = pd.DataFrame(elf.predict(test_x))
re = precision_score(test_y, pre, average='micro')
print(re)
print(classification_report(test_y, pre, target_names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                                       'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S']))

sc = roc_auc_score(test_y, elf.predict_proba(test_x), multi_class='ovr')
print('=====================================================')
print('The ROC-AUC SCORE IS:')
print(sc)
print('=====================================================')

ConfusionMatrixDisplay.from_estimator(elf, test_x, test_y)
plt.show()

csv_file()