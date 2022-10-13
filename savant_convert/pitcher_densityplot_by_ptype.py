# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:16:30 2022

@author: Hojoong Lee
"""

def pitcher_density(pid, contents, ptype='all'):
    from db_function import db_connection
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    conn = db_connection()
    
    temp = pd.read_sql_query(f'''SELECT * FROM savant_convert WHERE PitcherId = {pid}''', conn)
    conn.close()
    
    name = temp.Pitcher[0]
    
    # ptype 필터 적용 및 결측값(0) 처리
    if ptype == 'all':
        temp1 = temp[['AutoPitchType', contents]]
        temp1 = temp1[temp1[contents]!=0]
        
    else:
        temp1 = temp[['AutoPitchType', contents]]
        temp1 = temp1[(temp1[contents]!=0)&(temp1['AutoPitchType']==ptype)]
    
    density = sns.displot(temp1, x=contents, hue='AutoPitchType', kind='kde', fill = True)
    if ptype == 'all':
        plt.title(f"2022_{name}_{contents}_by_Ptype_densityplot")  
    else:
        plt.title(f"2022_{name}_{ptype}'s_{contents}_densityplot")
    plt.ylabel('ratio')
    
    return density

pid = 660271
contents = 'RelSpeed'
ptype = 'all'

pitcher_density(pid=pid, contents=contents, ptype = ptype)