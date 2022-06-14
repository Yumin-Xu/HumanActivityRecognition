import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from matplotlib import pyplot as plt
from sklearn import tree, svm
from sklearn.ensemble import AdaBoostClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, classification_report, RocCurveDisplay, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
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


def pre_IDF(x):
    # label A
    data = pd.DataFrame(
        OpenCheck.csv_check(x)).value_counts().reset_index(
        name='times')[
        pd.DataFrame(
            OpenCheck.csv_check(x)).value_counts().reset_index(
            name='times')['words'] != 0][pd.DataFrame(OpenCheck.csv_check(x)).value_counts().reset_index(
        name='times')[
                                             pd.DataFrame(
                                                 OpenCheck.csv_check(x)).value_counts().reset_index(
                                                 name='times')['words'] != 0]['times'] >= 20]
    data = pd.DataFrame(data['words'])

    df1 = pd.DataFrame(
        pd.DataFrame(
            d['words'], columns=['words'])['words'].isin(data['words'])[
            pd.DataFrame(
                d['words'], columns=['words'])['words'].isin(data['words'])].index,
        columns=['words'])
    df1['label'] = 1

    df2 = pd.concat([d1, d2, d3, d4, d5, d6, d7, d8, d10, d11, d12, d15, d16, d17, d18, d19],
                    ignore_index=True)
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

    print(df)

    train, test = train_test_split(df, test_size=0.2, shuffle=True)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(-1, 1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()

    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(-1, 1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    clf1 = KNeighborsClassifier(n_neighbors=7)
    clf2 = tree.DecisionTreeClassifier(criterion="entropy")
    clf3 = svm.SVC(kernel="rbf", probability=True, class_weight={0: 0.01, 1: 1.0})
    clf4 = LogisticRegression(class_weight={0: 0.01, 1: 1.0})
    clf5 = GaussianNB()
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=42)
    clf7 = MLPClassifier(random_state=42, max_iter=300)

    elf = VotingClassifier(
        estimators=[('KNN', clf1), ('TD', clf2), ('SVM', clf3), ('LR', clf4),
                    ('GNB', clf5), ('ADA', clf6), ('MLP', clf7)],
        voting='soft')

    elf.fit(train_x, train_y)
    pre = pd.DataFrame(elf.predict(test_x))
    re = precision_score(test_y, pre, labels='1')
    print(re)

    sc = classification_report(test_y, pre)
    print(sc)

    RocCurveDisplay.from_estimator(elf, test_x, test_y, pos_label=1)
    plt.show()

    ConfusionMatrixDisplay.from_estimator(elf, test_x, test_y)
    plt.show()


pre_IDF(6)


def pre_no_IDF():
    df1 = d13
    df1['label'] = 1

    df2 = pd.concat([d1, d2, d3, d4, d5, d6, d7, d8, d10, d11, d12, d15, d16, d17, d18, d19],
                    ignore_index=True)
    df2['label'] = 0

    test = shuffle(pd.concat([df1, df2]))

    rs = np.array(test['words']).reshape(-1, 1)
    ls = np.array(test['label']).reshape(-1, 1)

    sample = SMOTE()
    test = sample.fit_resample(X=rs, y=ls)
    df = pd.DataFrame({'words': pd.DataFrame(test[0], columns=['words'])['words'],
                       'label': pd.DataFrame(test[1], columns=['label'])['label']})

    df = df.sample(10000)

    train, test = train_test_split(df, test_size=0.2, shuffle=True)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(-1, 1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()

    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(-1, 1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    clf1 = KNeighborsClassifier(n_neighbors=7)
    clf2 = tree.DecisionTreeClassifier(criterion="entropy")
    clf3 = svm.SVC(kernel="rbf", probability=True, class_weight={0: 0.01, 1: 1.0})
    clf4 = LogisticRegression(class_weight={0: 0.01, 1: 1.0})
    clf5 = GaussianNB()
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=42)
    clf7 = MLPClassifier(random_state=42, max_iter=300)

    elf = VotingClassifier(
        estimators=[('KNN', clf1), ('TD', clf2), ('SVM', clf3), ('LR', clf4),
                    ('GNB', clf5), ('ADA', clf6), ('MLP', clf7)],
        voting='soft')

    elf.fit(train_x, train_y)
    pre = pd.DataFrame(elf.predict(test_x))
    re = precision_score(test_y, pre, labels='1')
    print(re)

    sc = classification_report(test_y, pre)
    print(sc)

    RocCurveDisplay.from_estimator(elf, test_x, test_y, pos_label=1)
    plt.show()

    ConfusionMatrixDisplay.from_estimator(elf, test_x, test_y)
    plt.show()


pre_no_IDF()


def pre_IDF_clf(x):
    # label A
    data = pd.DataFrame(
        OpenCheck.csv_check(x)).value_counts().reset_index(
        name='times')[
        pd.DataFrame(
            OpenCheck.csv_check(x)).value_counts().reset_index(
            name='times')['words'] != 0][pd.DataFrame(OpenCheck.csv_check(x)).value_counts().reset_index(
        name='times')[
                                             pd.DataFrame(
                                                 OpenCheck.csv_check(x)).value_counts().reset_index(
                                                 name='times')['words'] != 0]['times'] >= 20]
    data = pd.DataFrame(data['words'])

    df1 = pd.DataFrame(
        pd.DataFrame(
            d['words'], columns=['words'])['words'].isin(data['words'])[
            pd.DataFrame(
                d['words'], columns=['words'])['words'].isin(data['words'])].index,
        columns=['words'])
    df1['label'] = 1

    df2 = pd.concat([d1, d2, d3, d4, d5, d6, d7, d8, d10, d11, d12, d15, d16, d17, d18, d19],
                    ignore_index=True)
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

    train, test = train_test_split(df, test_size=0.2, shuffle=True)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(-1, 1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()

    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(-1, 1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # clf1 = KNeighborsClassifier(n_neighbors=7)
    # clf2 = tree.DecisionTreeClassifier(criterion="entropy")
    # clf3 = svm.SVC(kernel="rbf", probability=True, class_weight={0: 0.01, 1: 1.0})
    # clf4 = LogisticRegression(class_weight={0: 0.01, 1: 1.0})
    # clf5 = GaussianNB()
    # clf6 = AdaBoostClassifier(n_estimators=100, random_state=42)
    clf7 = MLPClassifier(random_state=42, max_iter=300)

    # elf = VotingClassifier(
    #    estimators=[('KNN', clf1), ('TD', clf2), ('SVM', clf3), ('LR', clf4),
    #                ('GNB', clf5), ('ADA', clf6), ('MLP', clf7)],
    #    voting='soft')

    clf7.fit(train_x, train_y)
    pre = pd.DataFrame(clf7.predict(test_x))
    re = precision_score(test_y, pre, labels='1')
    print(re)

    sc = classification_report(test_y, pre)
    print(sc)

    RocCurveDisplay.from_estimator(clf7, test_x, test_y, pos_label=1)
    plt.show()

    ConfusionMatrixDisplay.from_estimator(clf7, test_x, test_y)
    plt.show()


pre_IDF_clf(6)


def pre_no_IDF_clf():
    # label A
    df1 = d13
    df1['label'] = 1

    df2 = pd.concat([d1, d2, d3, d4, d5, d6, d7, d8, d10, d11, d12, d15, d16, d17, d18, d19],
                    ignore_index=True)
    df2['label'] = 0

    test = shuffle(pd.concat([df1, df2]))

    rs = np.array(test['words']).reshape(-1, 1)
    ls = np.array(test['label']).reshape(-1, 1)

    sample = SMOTE()
    test = sample.fit_resample(X=rs, y=ls)
    df = pd.DataFrame({'words': pd.DataFrame(test[0], columns=['words'])['words'],
                       'label': pd.DataFrame(test[1], columns=['label'])['label']})

    df = df.sample(10000)

    train, test = train_test_split(df, test_size=0.2, shuffle=True)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(-1, 1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()

    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(-1, 1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # clf1 = KNeighborsClassifier(n_neighbors=7)
    # clf2 = tree.DecisionTreeClassifier(criterion="entropy")
    # clf3 = svm.SVC(kernel="rbf", probability=True, class_weight={0: 0.01, 1: 1.0})
    # clf4 = LogisticRegression(class_weight={0: 0.01, 1: 1.0})
    # clf5 = GaussianNB()
    # clf6 = AdaBoostClassifier(n_estimators=100, random_state=42)
    clf7 = MLPClassifier(random_state=42, max_iter=300)

    # elf = VotingClassifier(
    #    estimators=[('KNN', clf1), ('TD', clf2), ('SVM', clf3), ('LR', clf4),
    #                ('GNB', clf5), ('ADA', clf6), ('MLP', clf7)],
    #   voting='soft')

    clf7.fit(train_x, train_y)
    pre = pd.DataFrame(clf7.predict(test_x))
    re = precision_score(test_y, pre, labels='1')
    print(re)

    sc = classification_report(test_y, pre)
    print(sc)

    RocCurveDisplay.from_estimator(clf7, test_x, test_y, pos_label=1)
    plt.show()

    ConfusionMatrixDisplay.from_estimator(clf7, test_x, test_y)
    plt.show()


pre_no_IDF_clf()
