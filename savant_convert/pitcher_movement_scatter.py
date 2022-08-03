# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:52:17 2022

@author: dlghw
"""
# input values = ['pid'='선수id', 'perspective'='시점']

def pitcher_movement_scatter(pid, perspective='pitcher'):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from db_function import db_connection
    
    conn = db_connection()
    temp = pd.read_sql_query(f'''SELECT * FROM savant_convert WHERE PitcherId = {pid}''', conn)
    conn.close()
    name = temp.Pitcher[0]
    colors = {'Slider' : 'green', 
              'Curveball' : 'orange', 
              'Four-Seam' : 'red', 
              'Sinker':'yellow', 
              'Splitter':'pink', 
              'Changeup':'blue', 
              'Cutter':'lightgreen', 
              'Knuckleball':'grey'}
    
    movement = sns.scatterplot(x='HorzBreak', 
                    y='InducedVertBreak', 
                    hue='AutoPitchType',
                    data=temp,
                    palette=colors)
    
    plt.axhline(y=0, color='grey',linewidth=1, alpha=.5)
    plt.axvline(x=0, color='grey',linewidth=1, alpha=.5)
    plt.axis([-70,70,-70,70])
    plt.title(f'{name}_movement by pitch type')
    if perspective=='catcher':
        movement.invert_xaxis()
    
pid = 660271
perspective='catcher'

pitcher_movement_scatter(pid=pid, perspective=perspective)