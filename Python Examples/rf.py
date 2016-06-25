# !usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

__author__ = 'David Ji'

'''Random Forest Example'''


def main():
    # Load data
    # iris是一个数据集字典, 有如下key:
    # 'target_names', iris类别名称: 'setosa' 'versicolor' 'virginica'
    # 'data', iris的特征数据
    # 'target', iris的类别数据
    # 'DESCR', 数据集描述
    # 'feature_names', 特征名称: 'sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'
    iris = load_iris()

    # iris['data']是一个150*4 numpy多维数组, 是iris的特征数据
    X = iris['data']

    # iris['target']是一个150*1 numpy数组, 是iris的类别数据, 与iris['data']一一对应
    y = iris['target']

    # 划分训练集, 测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=None, train_size=0.6)

    # 初始化分类器
    clf = RandomForestClassifier(
        n_estimators=20, criterion='entropy', max_features='auto',
        max_depth=None, bootstrap='True', n_jobs=-1)

    # 训练分类器
    clf.fit(X_train, y_train)

    # 测试分类器
    preds = clf.predict(X_test)

    # 输出测试报告
    tab = pd.crosstab(
        y_test, preds, rownames=['actual'], colnames=['predictions'])
    report = classification_report(y_test, preds)
    print(tab)
    print(report)

    # predictions   0   1   2
    # actual
    # 0            21   0   0
    # 1             0  19   1
    # 2             0   0  19
    #              precision    recall  f1-score   support

    #           0       1.00      1.00      1.00        21
    #           1       1.00      0.95      0.97        20
    #           2       0.95      1.00      0.97        19

    # avg / total       0.98      0.98      0.98        60


if __name__ == '__main__':
    main()
