# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:06:42 2022

@author: Hojoong Lee
"""

def batter_avg_heatmap(pid, split='all', perspective='pitcher', ptype='all'):

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from db_function import db_connection

    conn = db_connection()

    if split == 'all':
        temp = pd.read_sql_query(
            f'''SELECT * FROM savant_convert WHERE BatterId = {pid}''', conn)
        conn.close()

    elif split == 'left':
        temp = pd.read_sql_query(
            f'''SELECT * FROM savant_convert WHERE BatterId = {pid} AND PitcherThrows = 'Left' ''', conn)
        conn.close()

    elif split == 'right':
        temp = pd.read_sql_query(
            f'''SELECT * FROM savant_convert WHERE BatterId = {pid} AND PitcherThrows = 'Right' ''', conn)
        conn.close()

    if perspective == 'catcher':
        temp['PlateLocSide'] = temp['PlateLocSide']*-1

    if ptype != 'all':
        temp = temp[temp.AutoPitchType == ptype].reset_index(drop=True)

    name = temp.Batter[0].split(',')[1][1]+'.'+temp.Pitcher[0].split(',')[0]
    print('1. 데이터 불러오기 완료')
    # 히트맵 생성을 위한 존 위치 컬럼 세팅

    zone_height = []
    zone_side = []

    for i in range(len(temp)):

        if (temp['PlateLocSide'][i] >= -0.216) and (temp['PlateLocSide'][i] <= -0.072):

            side = 'Left'

        elif (temp['PlateLocSide'][i] > -0.072) and (temp['PlateLocSide'][i] < 0.072):

            side = 'Centre'

        elif (temp['PlateLocSide'][i] >= 0.072) and (temp['PlateLocSide'][i] <= 0.216):

            side = 'Right'

        else:

            side = 'S99'

        zone_side.append(side)

    for i in range(len(temp)):

        if (temp['PlateLocHeight'][i] >= 0.833) and (temp['PlateLocHeight'][i] <= 1.0):

            height = 'High'

        elif (temp['PlateLocHeight'][i] < 0.833) and (temp['PlateLocHeight'][i] > 0.666):

            height = 'Centre'

        elif (temp['PlateLocHeight'][i] >= 0.5) and (temp['PlateLocHeight'][i] <= 0.666):

            height = 'Low'

        else:

            height = 'S99'

        zone_height.append(height)

    print('2. 존 라벨링 완료')

    temp1 = pd.DataFrame()

    temp1['ptype'] = temp['AutoPitchType']
    temp1['PitchCall'] = temp['PitchCall']
    temp1['KorBB'] = temp['KorBB']
    temp1['PlayResult'] = temp['PlayResult']
    temp1['zone_height'] = zone_height
    temp1['zone_side'] = zone_side
    array1 = ['High', 'Centre', 'Low']
    array2 = ['Left', 'Centre', 'Right']

    temp1 = temp1[(temp1.zone_height != 'S99') & 
                  (temp1.zone_side != 'S99')].reset_index(drop=True)
    temp1 = temp1[(temp1.PitchCall == 'InPlay') | 
                  (temp1.KorBB != 'Undefined')].reset_index(drop=True)

    # 타율 계산을 위한 안타 집계용 컬럼생성

    hit = []
    ab = []

    for i, j in zip(temp1.PlayResult, temp1.KorBB):
        if j != 'Walk' and i != 'Sacrifice':

            ab.append(1)

            if i == 'Out' or i == 'Error' or i == 'FieldersChoice' or i == 'Undefined':

                hit.append(0)

            else:
                hit.append(1)
        else:
            ab.append(0)
            hit.append(0)

    temp1['hit'] = hit
    temp1['ab'] = ab

    del i, j, hit, ab

    # 스트라이크 위치 별 타율 계산
    count = temp1.groupby(by=['zone_height', 'zone_side']).sum().reset_index()
    count['avg'] = round(count.hit/count.ab, 3)
    temp2 = count.pivot('zone_height', 'zone_side', 'avg')
    temp2 = pd.DataFrame(data=temp2, index=array1, columns=array2)
    temp2 = temp2.fillna(0.0)

    print('3. 존별 타율 계산 완료')

    # 컬러맵 세팅(darkblue~red)
    from matplotlib.colors import LinearSegmentedColormap

    colors = ['darkblue', 'white', 'red']
    cmap = LinearSegmentedColormap.from_list('my_cmap', colors, gamma=1)

    plt.figure(figsize=(6, 6))
    sns.heatmap(data=temp2,
                cmap=cmap,
                annot=True,
                annot_kws={"size": 10, "color": 'black'},
                linewidths=3,
                fmt='.3f')
    plt.title(f'{name}_{ptype}_avg vs {split}_{perspective} view', fontsize=10)


pid = 502671
split = 'all'
perspective = 'catcher'
ptype = 'all'

batter_avg_heatmap(pid=pid, split=split, perspective='catcher', ptype=ptype)