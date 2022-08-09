# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 19:58:09 2022

@author: Hojoong Lee
"""

# 투수기준 타구 스프레이 차트

def pitcher_inplay_spray(pid, split='all'):
    
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from db_function import db_connection
    import matplotlib.patches as patches
    
    conn = db_connection()
    
    if split =='all':
        temp = pd.read_sql_query(f'''SELECT * FROM savant_convert WHERE PitcherId = {pid}''', conn)
        conn.close()
        
    elif split == 'left':
        temp = pd.read_sql_query(f'''SELECT * FROM savant_convert WHERE PitcherId = {pid} AND BatterSide = 'Left' ''', conn)
        conn.close()
        
    elif split == 'right':
        temp = pd.read_sql_query(f'''SELECT * FROM savant_convert WHERE PitcherId = {pid} AND BatterSide = 'Right' ''', conn)
        conn.close()
        
    temp = temp[(temp.PitchCall=='InPlay')&(temp.HC_Y!=0)]
    
    spary = plt.subplot()
    plt.rcParams['figure.figsize'] = [16,14]
    spray1 = sns.scatterplot(x='HC_X', 
                             y='HC_Y',
                             data=temp,
                             s=150, 
                             hue='PlayResult')
    spray1.legend(loc='lower left',
                  frameon=False, 
                  shadow=True, 
                  title='PlayResult',
                  fontsize=15,
                  markerscale=2,
                  title_fontsize=15)
    plt.xlim(-80,80)
    plt.ylim(0,140)
    
    # 펜스 그리기
    spray1.add_patch(patches.Arc((0,0),
                                 171.4985851,
                                 250,
                                 theta1=45,
                                 theta2=135,
                                 fill=False,
                                 edgecolor='brown',
                                 lw=2))
    
    # 내야 흙 그리기
    spray1.add_patch(patches.Arc((0,18.44),
                                 57.912,
                                 57.912,
                                 theta1=18,
                                 theta2=162,
                                 fill=False,
                                 edgecolor='brown',
                                 lw=2))
    
    # 베이스라인 그리기
    spray1.add_patch(patches.Polygon((
                    (0,0),
                    (-19.397353221509373,19.397353221509373),
                    (0,38.79470644),
                    (19.397353221509373,19.397353221509373)),
                    fill=False,
                    edgecolor='brown',
                    lw=2))
    
    # 파울라인 그리기
    plt.plot([0, -80], 
             [0, 80], 
             color='brown', 
             lw=2, 
             linestyle='solid')
    
    plt.plot([0, 80], 
             [0, 80], 
             color='brown', 
             lw=2, 
             linestyle='solid')

pid = 660271
split = 'all'

pitcher_inplay_spray(pid=pid, split=split)