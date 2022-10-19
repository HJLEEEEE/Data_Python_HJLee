# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:41:22 2022

@author: Hojoong Lee
"""

import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from db_function import db_connection

conn = db_connection()
temp = pd.read_sql_query('''SELECT AutoPitchType, PitcherThrows, RelSpeed, SpinRate, InducedVertBreak, HorzBreak FROM savant_convert''', conn)
conn.close()

# 우투수 구종 분류(전체)

temp1 = temp[temp.PitcherThrows=='Right'].reset_index(drop=True)

X = temp1.drop(['AutoPitchType','PitcherThrows'], axis=1)
Y = temp1[['AutoPitchType']]
train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size = 0.3, random_state = 42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score # 정확도 함수
from sklearn.metrics import confusion_matrix

clf = RandomForestClassifier(n_estimators=300, max_depth=20,random_state=0)
clf.fit(train_x,train_y)

predict = clf.predict(test_x)
print(accuracy_score(test_y,predict)) # 정확도 85%
cfm = confusion_matrix(test_y, predict)
print(cfm)

# 대분류 후 세부분류(이중분류)

# 속구계열 분류(포심, 싱커)
temp1_Fast = temp1[(temp1.AutoPitchType=='Four-Seam')|(temp1.AutoPitchType=='Sinker')|(temp1.AutoPitchType=='Cutter')]
X = temp1_Fast.drop(['AutoPitchType','PitcherThrows'], axis=1)
Y = temp1_Fast[['AutoPitchType']]
train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size = 0.3, random_state = 42)

clf1 = RandomForestClassifier(n_estimators=300, max_depth=20,random_state=0)
clf1.fit(train_x,train_y)

predict1 = clf1.predict(test_x)
print(accuracy_score(test_y,predict1)) # 정확도 91%

# 혼동 행렬
cfm1 = confusion_matrix(test_y, predict1)
print(cfm1)


# 브레이킹 계열 분류(슬라이더, 커브)
temp1_Break = temp1[(temp1.AutoPitchType=='Slider')|(temp1.AutoPitchType=='Curveball')]
X = temp1_Break.drop(['AutoPitchType','PitcherThrows'], axis=1)
Y = temp1_Break[['AutoPitchType']]
train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size = 0.3, random_state = 42)

clf2 = RandomForestClassifier(n_estimators=300, max_depth=20,random_state=0)
clf2.fit(train_x,train_y)

predict2 = clf2.predict(test_x)
print(accuracy_score(test_y,predict2)) # 정확도 91%

# 혼동 행렬
cfm2 = confusion_matrix(test_y, predict2)
print(cfm2)

# 오프스피드 계열 분류(체인지업, 스플리터)
temp1_Off = temp1[(temp1.AutoPitchType=='Changeup')|(temp1.AutoPitchType=='Splitter')]

X = temp1_Off.drop(['AutoPitchType','PitcherThrows'], axis=1)
Y = temp1_Off[['AutoPitchType']]
train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size = 0.3, random_state = 42)

clf3 = RandomForestClassifier(n_estimators=500, max_depth=30,random_state=0)
clf3.fit(train_x,train_y)

predict3 = clf3.predict(test_x)
print(accuracy_score(test_y,predict3)) # 정확도 88%

# 혼동 행렬
cfm3 = confusion_matrix(test_y, predict3) 
print(cfm3)
