# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import warnings
import numpy as np
import cv2 as cv
import hmmlearn.hmm as hl
warnings.filterwarnings(
    'ignore', category=DeprecationWarning)
np.seterr(all='ignore')


def search_objects(directory):
    directory = os.path.normpath(directory)
    if not os.path.isdir(directory):
        raise IOError("The directory '" + directory +
                      "' doesn't exist!")
    objects = {}
    for curdir, subdirs, files in os.walk(directory):
        for jpeg in (file for file
                     in files if file.endswith('.jpg')):
            path = os.path.join(curdir, jpeg)
            label = path.split(os.path.sep)[-2]
            if label not in objects:
                objects[label] = []
            objects[label].append(path)
    return objects


train_objects = search_objects(
    'D:/fruits/')
print(train_objects)
train_x, train_y = [], []
for label, filenames in train_objects.items():
    descs = np.array([])
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        h, w = gray.shape[:2]
        f = 200 / min(h, w)
        gray = cv.resize(gray, None, fx=f, fy=f)
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(gray)
        _, desc = sift.compute(gray, keypoints)
        desc = np.mean(desc, axis=0)
        train_x.append(desc)
        train_y.append(label)

import sklearn.preprocessing as sp
train_x = np.array(train_x)
encoder = sp.LabelEncoder()
train_y = encoder.fit_transform(train_y)

import sklearn.svm as svm
model = svm.SVC(kernel='poly', degree=2)
model.fit(train_x, train_y)

pred_train_y = model.predict(train_x)
import sklearn.metrics as sm
print(sm.classification_report(train_y, pred_train_y))

