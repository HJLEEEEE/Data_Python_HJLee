# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 15:06:09 2022

@author: Hojoong Lee
"""

# 투수 구종별 로케이션(kde plot)
def pitcher_location_kde(pid):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from db_function import db_connection
    import matplotlib.patches as patches
    
    conn = db_connection()
    
    temp = pd.read_sql_query(f'''SELECT * FROM savant_convert WHERE PitcherId = {pid}''', conn)
    conn.close()
    ptypes = temp.AutoPitchType.drop_duplicates().to_list()
    name = temp.Pitcher[0]
    
    for i in ptypes:
        a = temp[temp.AutoPitchType==i]
        kde = plt.subplot()
        kde = sns.kdeplot(a.PlateLocSide, 
                          a.PlateLocHeight,
                          shade=True,
                          cmap = "YlOrBr",
                          shade_lowest=False,
                          n_level=20)
        
        plt.xlim(-0.7, 0.7)
        plt.xticks([-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7])
        plt.ylim(0.0,1.4)
        plt.yticks([.0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0,1.1,1.2,1.3,1.4])
        plt.title(f'{name}_{i}')
        kde.add_patch(
            patches.Rectangle((-0.216,0.5), 
                              0.4318, 
                              0.5, 
                              fill=False,
                              edgecolor='grey',
                              lw=1))
        plt.show()
        
pitcher_location_kde(pid=660271)