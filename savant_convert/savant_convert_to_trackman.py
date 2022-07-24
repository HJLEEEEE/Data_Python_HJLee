# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:46:25 2022

Savant data convert to Trackman Style

@author: Hojoong Lee
"""

# 데이터 불러오기 및 merge
import pandas as pd
import numpy as np
import os

path = "./data/"
file_list = os.listdir(path)
df = pd.DataFrame()

for i in file_list: 
    temp = pd.read_csv(f'{path}{i}')
    df = df.append(temp)