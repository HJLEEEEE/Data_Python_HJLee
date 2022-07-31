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
    
    temp_1 = pd.DataFrame()
    temp_1['Ptype'] = temp.AutoPitchType.drop_duplicates().to_list()
    temp_1 = pd.merge(left = temp_1, right= a, left_on='Ptype', right_on='AutoPitchType')
    
    del temp, a
    
    return temp_1

temp = pitcher_summary(pid = 660271)[['Ptype', 'RelSpeed', 'SpinRate', 'RelHeight','RelSide', 'Extension', 'InducedVertBreak', 'HorzBreak']]