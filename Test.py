from matplotlib import pyplot as plt

import ML_Data
from TF_IDF import tf

dataA = tf(19)
plt.plot(dataA['times'])
plt.show()

for item in range(len(d_x)):
    if d_x[item] > 0:
        d_x[item] = math.log(d_x[item], math.e)
    elif d_x[item] == 0:
        d_x[item] = 0
    elif d_x[item] < 0:
        d_x[item] = math.fabs(math.log(math.fabs(d_x[item]), math.e))
d_x = np.array(d_x)

for item in range(len(d_y)):
    if d_y[item] > 0:
        d_y[item] = math.log(d_y[item], math.e)
    elif d_y[item] == 0:
        d_y[item] = 0
    elif d_y[item] < 0:
        d_y[item] = math.fabs(math.log(math.fabs(d_y[item]), math.e))
d_y = np.array(d_y)

for item in range(len(d_z)):
    if d_z[item] > 0:
        d_z[item] = math.log(d_z[item], math.e)
    elif d_z[item] == 0:
        d_z[item] = 0
    elif d_z[item] < 0:
        d_z[item] = math.fabs(math.log(math.fabs(d_z[item]), math.e))
d_z = np.array(d_z)

if (d1['x'].loc[0] == 0 and d1['y'].loc[0] == 0 and d1['z'].loc[0] == 0 and
        d2['x'].loc[0] == 0 and d2['y'].loc[0] == 0 and d2['z'].loc[0] == 0 and
        d3['x'].loc[0] == 0 and d3['y'].loc[0] == 0 and d3['z'].loc[0] == 0):
    data = pd.DataFrame(data={'words': [0], 'times': [0]})
    data['words'] = data['words'].astype(float)
    data['times'] = data['words'].astype(float)
else:


, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                   d11, d12, d13, d14, d15, d16, d17, d18, d19, d20,
                   d21, d22, d23, d24, d25, d26, d27, d28, d29, d30,
                   d31, d32, d33, d34, d35, d36, d37, d38, d39, d40,
                   d41, d42, d43, d44, d45, d46, d47, d48, d49, d50

# Decision Tree
clf1 = tree.DecisionTreeClassifier(criterion="entropy")
clf1 = clf1.fit(train_x, train_y)
score1 = clf1.score(test_x, test_y)
print(score1)

# K-NN
clf2 = KNeighborsClassifier(n_neighbors=2)
clf2.fit(train_x, train_y)
score2 = clf2.score(train_x, train_y)
print(score2)

# SVM
clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
clf3.fit(train_x, train_y)
score3 = clf3.score(train_x, train_y)
print(score3)


# Bagging
re = [score1, score2, score3]
var = 0
if re[0] > 0.94:
    var += 1
else:
    var += 0
if re[1] > 0.94:
    var += 1
else:
    var += 0
if re[2] > 0.94:
    var += 1
else:
    var += 0
if var > len(re) / 2:
    print('prediction result is', 'A')

for file in range(0, len(ML_Data.train_x)):
    x = x[file]
    y = y[file]
    if 320 <= x <= 548 and 468 <= y <= 653:
        print('Select: LABEL A, B, C')
    if 448 <= x <= 672 and 573 <= y <= 714:
        print('Select: LABEL S, M, O, P')
    if 448 <= x <= 672 and 714 <= y <= 845:
        print('Select: LABEL D, E, F, G, H, I, J, K, L, Q, R')
    else:
        print('USE ALL')


def tf(x):
    data = pd.DataFrame(csv_label_file(x)['times'].value_counts().sort_values())
    # data = pd.DataFrame(x.value_counts().sort_values())
    data = pd.DataFrame({'words': data.index.tolist(),
                         'times': pd.DataFrame(np.sort(np.array(pd.DataFrame(data))))[0]})
    TF_IDF_A = (data['times'] / len(data)) * math.log(50 / (50 + 1))
    data = pd.DataFrame({'words': data.index.tolist(),
                         'times': pd.DataFrame(np.sort(np.array(pd.DataFrame(data))))[0],
                         'TF-IDF_A': TF_IDF_A})
    data = data.sort_values(['times'], ascending=[False])

    return data


for file in range(0, len(pd.DataFrame(d_x))):
    x = d_x['words'].loc[file]
    y = d_x['times'].loc[file]
    if 320 <= x <= 548 and 468 <= y <= 653:
        print(ML_Data.pre_A(x))
        var1 += 1
    if 448 <= x <= 672 and 573 <= y <= 714:
        var2 += 1
    if 448 <= x <= 672 and 714 <= y <= 845:
        var3 += 1
    else:
        expect += 1
print(var1)
print(var2)
print(var3)
print(expect)


re = np.arange(len(ML_Data.d_x))
for x in range(0, len(ML_Data.d_x)):
    re = ML_Data.pre_A(ML_Data.d_x[x])
print(re)

if 448 <= x <= 672 and 573 <= y <= 714:
    var2 += 1
if 448 <= x <= 672 and 714 <= y <= 845:
    var3 += 1
else:
    expect += 1


for file in range(0, len(pd.DataFrame(ML_Data.d))):
    if 320 <= pd.DataFrame(ML_Data.d_x).loc[0][file] <= 548 and 468 <= pd.DataFrame(ML_Data.d_y).loc[0][file] <= 653:
        d = np.array(pd.DataFrame(ML_Data.d_x).loc[0][file]).reshape(-1, 1)
        re = ML_Data.pre_A(d)
        print(re)


###############################################################################

# K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =',score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)

    print('Prediction for Label A: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_B():
    # label B
    d_A = d.head(len(d2))
    d_A_other = pd.concat([d1, d3, d4, d5, d6, d7, d8, d9, d10,
                           d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label B: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_C():
    # label C
    d_A = d.head(len(d3))
    d_A_other = pd.concat([d1, d2, d4, d5, d6, d7, d8, d9, d10,
                           d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label C: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_D():
    # label D
    d_A = d.head(len(d4))
    d_A_other = pd.concat([d1, d2, d3, d5, d6, d7, d8, d9, d10,
                           d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label D: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_E():
    # label E
    d_A = d.head(len(d5))
    d_A_other = pd.concat([d1, d2, d3, d4, d6, d7, d8, d9, d10,
                           d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label E: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_F():
    # label F
    d_A = d.head(len(d6))
    d_A_other = pd.concat([d1, d2, d3, d4, d5, d7, d8, d9, d10,
                           d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label F: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_G():
    # label G
    d_A = d.head(len(d7))
    d_A_other = pd.concat([d1, d2, d3, d4, d5, d6, d8, d9, d10,
                           d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label G: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_H():
    # label H
    d_A = d.head(len(d8))
    d_A_other = pd.concat([d1, d2, d3, d4, d5, d6, d7, d9, d10,
                           d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label H: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_I():
    # label I
    d_A = d.head(len(d9))
    d_A_other = pd.concat([d1, d2, d3, d4, d5, d6, d7, d8, d10,
                           d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label I: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_J():
    # label J
    d_A = d.head(len(d10))
    d_A_other = pd.concat([d1, d2, d3, d4, d5, d6, d7, d8, d9,
                           d11, d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label J: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_K():
    # label K
    d_A = d.head(len(d11))
    d_A_other = pd.concat([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                           d12, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label K: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_L():
    # label L
    d_A = d.head(len(d12))
    d_A_other = pd.concat([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
                           d11, d13, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label L: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_M():
    # label M
    d_A = d.head(len(d13))
    d_A_other = pd.concat([d1, d2, d4, d5, d6, d7, d8, d9, d10,
                           d11, d12, d15, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label M: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_O():
    # label O
    d_A = d.head(len(d15))
    d_A_other = pd.concat([d2, d3, d4, d5, d6, d7, d8, d9, d10,
                           d11, d12, d13, d16, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label O: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_P():
    # label P
    d_A = d.head(len(d16))
    d_A_other = pd.concat([d1, d3, d4, d5, d6, d7, d8, d9, d10,
                           d11, d12, d13, d15, d17, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label P: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_Q():
    # label Q
    d_A = d.head(len(d17))
    d_A_other = pd.concat([d1, d2, d4, d5, d6, d7, d8, d9, d10,
                           d11, d12, d13, d15, d16, d18, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label Q: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_R():
    # label R
    d_A = d.head(len(d18))
    d_A_other = pd.concat([d2, d3, d4, d5, d6, d7, d8, d9, d10,
                           d11, d12, d13, d15, d16, d17, d19], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()

    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label R: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


def pre_S():
    # label S
    d_A = d.head(len(d19))
    d_A_other = pd.concat([d1, d3, d4, d5, d6, d7, d8, d9, d10,
                           d11, d12, d13, d15, d16, d17, d18], ignore_index=True)
    A = pd.DataFrame({'label': 1, 'words': d_A['words'], 'times': d_A['times']})
    A_other = pd.DataFrame({'label': 0, 'words': d_A_other['words'], 'times': d_A_other['times']})
    A_label = pd.concat([A, A_other], ignore_index=True)

    labelA = pd.DataFrame(A_label)

    train, test = train_test_split(labelA, test_size=0.2)

    train_x = np.array(pd.DataFrame(train)[['words']]).reshape(len(train), -1)
    train_y = np.array(pd.DataFrame(train)[['label']]).ravel()
    test_x = np.array(pd.DataFrame(test)[['words']]).reshape(len(test), -1)
    test_y = np.array(pd.DataFrame(test)[['label']]).ravel()
    # Decision Tree
    clf1 = tree.DecisionTreeClassifier(criterion="entropy")
    clf1 = clf1.fit(train_x, train_y)
    score1 = clf1.score(test_x, test_y)
    print('Decision Tree =', score1)

    # K-NN
    clf2 = KNeighborsClassifier(n_neighbors=2)
    clf2.fit(train_x, train_y)
    score2 = clf2.score(test_x, test_y)
    print('K-NN =', score2)

    # SVM
    clf3 = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovo')
    clf3.fit(train_x, train_y)
    score3 = clf3.score(test_x, test_y)
    print('SVM =', score3)

    # Logistic Regression
    clf4 = LogisticRegression(random_state=0)
    clf4.fit(train_x, train_y)
    score4 = clf4.score(test_x, test_y)
    print('Logistic Regression =', score4)

    # Bayes
    clf5 = GaussianNB()
    clf5.fit(train_x, train_y)
    score5 = clf5.score(test_x, test_y)
    print('Bayes =', score5)

    # Adaboost
    clf6 = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf6.fit(train_x, train_y)
    score6 = clf6.score(test_x, test_y)
    print('Adaboost =', score6)

    # CNN
    clf7 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(5, 2), random_state=1)
    clf7.fit(train_x, train_y)
    score7 = clf7.score(test_x, test_y)
    print('CNN =', score7)
    print('Prediction for Label S: ', (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7)


pre_A()
print('====================================')
pre_B()
print('====================================')
pre_C()
print('====================================')
pre_D()
print('====================================')
pre_E()
print('====================================')
pre_F()
print('====================================')
pre_G()
print('====================================')
pre_H()
print('====================================')
pre_I()
print('====================================')
pre_J()
print('====================================')
pre_K()
print('====================================')
pre_L()
print('====================================')
pre_M()
print('====================================')
pre_O()
print('====================================')
pre_P()
print('====================================')
pre_Q()
print('====================================')
pre_R()
print('====================================')
pre_S()

