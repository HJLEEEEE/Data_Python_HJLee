# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 20:54:58 2022

@author: Hojoong Lee
"""

# 투수 기준 스트라이크존 히트맵

def pitcher_pitchper_heatmap(pid, split='all', perspective='pitcher'):
    
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from db_function import db_connection
    
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
        
    if perspective == 'catcher':
        temp['PlateLocSide'] = temp['PlateLocSide']*-1
    name = temp.Pitcher[0]
    
    # 히트맵 생성을 위한 존 위치 컬럼 세팅
    
    zone_height = []
    zone_side = []
    
    for i in range(len(temp)):
        
        if (temp['PlateLocSide'][i]>=-0.216) and (temp['PlateLocSide'][i]<=-0.072):
            
            side = 'Left'
        
        elif (temp['PlateLocSide'][i]>-0.072) and (temp['PlateLocSide'][i]<0.072):
            
            side = 'Centre'
    
        elif (temp['PlateLocSide'][i]>=0.072) and (temp['PlateLocSide'][i]<=0.216):
             
            side = 'Right'
      
        elif (temp['PlateLocHeight'][i]>=0.833) and (temp['PlateLocHeight'][i]<=1.0):
            
            height = 'High'
        
        elif (temp['PlateLocHeight'][i]<0.833) and (temp['PlateLocHeight'][i]>0.666):
            
            height = 'Centre'
            
        elif (temp['PlateLocHeight'][i]>=0.5) and (temp['PlateLocHeight'][i]<=0.666):
    
            height = 'Low'
            
        else:
            
            side ='S99'
            height='S99'
        
        zone_height.append(height)
        zone_side.append(side)
    
    temp1 = pd.DataFrame()
       
    temp1['ptype'] = temp['AutoPitchType']
    temp1['zone_height'] = zone_height
    temp1['zone_side'] = zone_side
    array1 = ['High','Centre','Low']
    array2 = ['Left','Centre','Right']
    
    temp1 = temp1[(temp1.zone_height!='S99')&(temp1.zone_side!='S99')].reset_index(drop=True)
    
    # 스트라이크 위치 별 비율 계산
    count = temp1.groupby(by=['zone_height','zone_side']).count().reset_index()
    count['percentage'] = round(count.ptype/count.ptype.sum()*100, 1)
    temp2 = count.pivot('zone_height','zone_side','percentage')
    temp2 = pd.DataFrame(data=temp2, index = array1, columns = array2)
    
    # 컬러맵 세팅(darkblue~red)
    from matplotlib.colors import LinearSegmentedColormap
    
    colors = ['darkblue','white','red']
    cmap = LinearSegmentedColormap.from_list('my_cmap',colors,gamma=1)
    
    
    plt.figure(figsize=(6,6))
    sns.heatmap(data=temp2,
                cmap=cmap,
                annot=True,
                annot_kws={"size":10,"color":'black'},
                linewidths=3,
                fmt='.1f')
    plt.title(f'{name}_pitch% heatmap',fontsize=10)

pid=660271
split='right'
perspective = 'catcher'
pitcher_pitchper_heatmap(pid=pid, split=split, perspective='catcher')