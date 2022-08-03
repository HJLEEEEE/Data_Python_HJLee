# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:15:44 2022

@author: Hojoong Lee
"""

# 투수 구종별 기본 데이터 집계
def pitcher_summary(pid):
    from db_function import db_connection
    import pandas as pd
    
    conn = db_connection()
    
    temp = pd.read_sql_query(f'''SELECT * FROM savant_convert WHERE PitcherId = {pid}''', conn)
    conn.close()
    
    a = temp.groupby(by='AutoPitchType').mean().reset_index()[['AutoPitchType', 'RelSpeed', 'SpinRate', 'RelHeight', 'RelSide', 'Extension', 'InducedVertBreak', 'HorzBreak']]
    b = temp.groupby(by=['AutoPitchType','BatterSide']).count().reset_index()[['AutoPitchType','BatterSide', 'RelSpeed']]
    
    ratio_vs_right = []
    ratio_vs_left = []
    
    for i, j, k in zip(b.RelSpeed, b.BatterSide, b.AutoPitchType):
        if j == 'Left':
            length = b[b.BatterSide=='Left'].RelSpeed.sum()
            ratio = round((i/length)*100, 1)
            ratio_vs_left.append({'AutoPitchType':k, 'Ratio_vs_Left':ratio})
        elif j == 'Right':
            length = b[b.BatterSide=='Right'].RelSpeed.sum()
            ratio = round((i/length)*100, 1)    
            ratio_vs_right.append({'AutoPitchType':k, 'Ratio_vs_Right':ratio})
    
    del i, j, length, ratio, k
    
    rate_r = pd.DataFrame(ratio_vs_right)
    rate_l = pd.DataFrame(ratio_vs_left)
    
    del ratio_vs_left, ratio_vs_right
    
    temp_1 = pd.DataFrame()
    temp_1['Ptype'] = temp.AutoPitchType.drop_duplicates().to_list()
    temp_1 = pd.merge(left = temp_1, right= a, left_on='Ptype', right_on='AutoPitchType')
    temp_1 = pd.merge(temp_1,rate_r, on='AutoPitchType')
    temp_1 = pd.merge(temp_1,rate_l, on='AutoPitchType')    
    del temp, a, rate_r, rate_l 
    
    return temp_1

temp = pitcher_summary(pid = 660271)[['Ptype', 'Ratio_vs_Right', 'Ratio_vs_Left', 'RelSpeed', 'SpinRate', 'RelHeight','RelSide', 'Extension', 'InducedVertBreak', 'HorzBreak']]