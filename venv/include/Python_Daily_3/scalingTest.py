# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :scalingTest.py
# Location:/Home/PycharmProjects/..

import numpy as np
from sklearn import preprocessing


if __name__ == '__main__':
    data = np.array([[3, -1.5, 2, -5.4], [0, 4, -0.3, 2.1], [1, 3.3, -1.9, -4.3]])
    data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
    # After scaling
    data_scaled = data_scaler.fit_transform(data)
    print('Min max scaled data:', '\n', data_scaled)
