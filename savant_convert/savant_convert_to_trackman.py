# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:46:25 2022

Savant data convert to Trackman Style

@author: Hojoong Lee
"""
def savant_convert():
    # 데이터 불러오기 및 합치기
    import pandas as pd
    import numpy as np
    import os
    from datetime import datetime
    import warnings
    import math
    
    warnings.filterwarnings("ignore")  
    path = "./data/"
    file_list = os.listdir(path)
    df = pd.DataFrame()
    
    for i in file_list: 
        temp = pd.read_csv(f'{path}{i}')
        df = df.append(temp)
        
    del i, temp, file_list
    
    today = datetime.today().strftime('%Y%m%d')
    df = df.dropna(subset=['game_pk'])
    df.to_csv(f'./total/savant_total_{today}.csv', index=False, encoding='utf-8-sig')
    
    print('1. 데이터 합치기 완료')
    
    # 날짜, 게임, 피치넘버순 정렬
    df_temp = df.sort_values(by=['game_date','game_pk','at_bat_number','pitch_number']).reset_index(drop=True)
    
    # 경기별 pitchno 컬럼 생성
    pitchno = []
    
    for i in df_temp.game_pk.drop_duplicates():
        
        temp = df_temp[df_temp.game_pk==i]
        
        for j in range(len(temp)):
            a = j+1
            pitchno.append(a)     
            
    del i, j, a, temp
    
    df_temp.insert(0, 'PitchNo', pitchno)
    df_temp['Time'] =''
    del pitchno
    
    print('2. PitchNo 컬럼 생성 완료')
    
    # 구종명 트랙맨 스타일 변경
    ptype = []
    
    for i in df_temp.pitch_name:
        if i == '4-Seam Fastball':
            ptype.append('Four-Seam')
        elif i == 'Slider' or i == 'Sinker' or i == 'Changeup' or i == 'Curveball' or i == 'Cutter' or i == 'Fastball' or i == 'Knuckleball':
            ptype.append(i)
        elif i == 'Split-Finger':
            ptype.append('Splitter')
        elif i == 'Knuckle Curve':
            ptype.append('Curveball')
        else:
            ptype.append('Other')
            
    del i
    
    df_temp['TaggedPitchType'] = 'Undefined'
    df_temp['AutoPitchType'] = ptype         
    del ptype
    print('3. 구종명 변경 완료')
    
    # 타자 이름 컬럼 생성(Batter)
    batter = []
    
    for i in df_temp.des:
        a = i.split(' ')
        name = f'{a[1]}, {a[0]}'
        batter.append(name)
        
    del i, a, name
    
    df_temp['Batter'] = batter
    del batter
    
    print('4. 타자이름 컬럼 생성 완료')
    
    # pitcherteam, batterteam 컬럼 생성
    pteam = []
    bteam = []
    
    for i, j, k in zip(df_temp.inning_topbot, df_temp.home_team, df_temp.away_team):
        if i == 'Top':
            pteam.append(j)
            bteam.append(k)
        else:
            pteam.append(k)
            bteam.append(j)
    del i, j, k
    
    df_temp['PitcherTeam'] = pteam
    df_temp['BatterTeam'] = bteam
    del pteam, bteam
    
    print('5. 투수팀, 타자팀 컬럼 생성 완료')
    
    # PAofInning, PitchofPA 컬럼 생성
    
    pin = []
    ppa = df_temp.pitch_number.to_list()
    
    for i, j, k in zip(range(len(df_temp)), ppa, df_temp.PitchNo):
        
        if k == 1:
            a = 1
            pin.append(a)
        
        else:
            if  j == 1:
                
                if df_temp.inning_topbot[i] == df_temp.inning_topbot[i-1]:
                   a = a+1
                   pin.append(a)
                   
                else:
                    a = 1
                    pin.append(a)
            
            else:
    
                pin.append(a)
                
    del i, j, k, a
    
    df_temp['PAofInning'] = pin
    df_temp['PitchofPA'] = ppa
    
    del pin, ppa
    
    print('6. PAofInning, PitchofPA 컬럼 생성 완료')
    
    # 투수/타자손 트랙맨 형식으로 변환
    pthrow = []
    bside = []
    for i, j in zip(df_temp.p_throws, df_temp.stand):
        
        if i == 'R':
            pthrow.append('Right')
            if j == 'R':
                bside.append('Right')
            else:
                bside.append('Left')
        else:
            pthrow.append('Left')
            if j == 'R':
                bside.append('Right')
            else:
                bside.append('Left')
    del i, j
    
    df_temp['PitcherThrows'] = pthrow
    df_temp['BatterSide'] = bside
    del pthrow, bside
    
    print('7. 투수/타자손 트랙맨 형식으로 변환 완료')
    
    # PitcherSet 컬럼 생성
    
    pset = []
    df_temp.on_1b = df_temp.on_1b.fillna('')
    df_temp.on_2b = df_temp.on_2b.fillna('')
    df_temp.on_3b = df_temp.on_3b.fillna('')
    
    for i, j, k in zip(df_temp.on_1b, df_temp.on_2b, df_temp.on_3b):
        if i == '' and j == '' and k == '':
            pset.append('Windup')
        else:
            pset.append('Stretch')
    del i, j, k
    
    df_temp['PitcherSet'] = pset
    del pset
    
    print('8. PitcherSet 컬럼 생성 완료')
    
    # inning_topbot 컬럼 수정
    Top_Bottom = []
    for i in df_temp.inning_topbot:
        if i == 'Bot':
            Top_Bottom.append('Bottom')
        else:
            Top_Bottom.append('Top')
    del i        
    df_temp['Top/Bottom'] = Top_Bottom
    del Top_Bottom
    print('9. Top/Bottom 컬럼 생성 완료')
    
    # PitchCall 컬럼 생성
    pcall = []
    
    for i, j in zip(df_temp.description, df_temp.events):
        if j == 'catcher_interf':
            pcall.append('CatcherInterference')
        elif i == 'ball' or i == 'blocked_ball' or i =='pitchout':
            pcall.append('BallCalled')
        elif i == 'called_strike':
            pcall.append('StrikeCalled')
        elif i == 'swinging_strike' or i == 'foul_tip' or i == 'swinging_strike_blocked' or i == 'missed_bunt' or i == 'bunt_foul_tip':
            pcall.append('StrikeSwinging')
        elif i == 'foul' or i == 'foul_bunt':
            pcall.append('FoulBall')
        elif i == 'hit_by_pitch':
            pcall.append('HitByPitch')
        elif i == 'hit_into_play':
            pcall.append('InPlay')
    del i
    df_temp['PitchCall'] = pcall
    del pcall
    print('10. PitchCall 컬럼 생성 완료')
    
    # KorBB 컬럼 생성
    kbb = []
    
    for i in df_temp.events:
        if i == 'strikeout' or i == 'strikeout_double_play':
            kbb.append('Strikeout')
        elif i == 'walk':
            kbb.append('Walk')
        else:
            kbb.append('Undefined')
    del i
    df_temp['KorBB'] = kbb
    del kbb
    
    print('11. KorBB 컬럼 생성 완료')
    
    # TaggedHitType, PlayResult 컬럼 생성
    htype = []
    pres = []
    
    for i, j in zip(df_temp.bb_type, df_temp.PitchCall):
        
        if j == 'InPlay':
            if i == 'line_drive':
                htype.append('LineDrive')
            elif i == 'ground_ball':
                htype.append('GroudBall')
            elif i == 'popup':
                htype.append('Popup')
            elif i == 'fly_ball':
                htype.append('FlyBall')
            else:
                htype.append('Undefined')
        else:
            htype.append('Undefined')
    del i, j
                
    for i, j in zip(df_temp.events, df_temp.PitchCall):
        
        if j == 'InPlay':
            if i == 'single':
                pres.append('Single')
            elif i == 'force_out' or i == 'field_out' or i == 'grounded_into_double_play' or i == 'fielders_choice_out' or i == 'double_play' or i == 'triple_play':
                pres.append('Out')
            elif i == 'double':
                pres.append('Double')
            elif i == 'triple':
                pres.append('Triple')
            elif i == 'home_run':
                pres.append('HomeRun')
            elif i == 'sac_fly' or i == 'sac_fly_double_play' or i == 'sac_bunt':
                pres.append('Sacrifice')
            elif i == 'field_error':
                pres.append('Error')
            elif i == 'fielders_choice':
                pres.append('FieldersChoice')
        else:
            pres.append('Undefined')
            
    del i, j
    
    df_temp['TaggedHitType'] = htype
    df_temp['PlayResult'] = pres
    del pres, htype
    
    print('12. TaggedHitType, PlayResult 컬럼 생성 완료')
    
    # RunsScored 컬럼 생성
    
    rsc = []
    
    for i, j in zip(range(len(df_temp)), df_temp['Top/Bottom']):
        
        if j == 'Top':
            
            a = df_temp.away_score[i]
            b = df_temp.post_away_score[i]
            
            rsc.append(int(b-a))
    
                
        elif j == 'Bottom':
            
            a = df_temp.home_score[i]
            b = df_temp.post_home_score[i]
            
            rsc.append(int(b-a))
    del i, j, a, b
    df_temp['RunsScored'] = rsc     
    del rsc    
    
    print('13. RunsScored 컬럼 생성 완료')
    
    # OutsOnPlay 컬럼 생성
    
    outs = []
    for gid in df_temp.game_pk.drop_duplicates():
        temp = df_temp[df_temp.game_pk==gid].reset_index(drop=True)
        
        for i, j, k in zip(range(len(temp)), temp.KorBB, temp.events):
            try:
                
                a = df_temp.outs_when_up[i]
                b = df_temp.outs_when_up[i+1]
                
                if k == 'triple_play':
                    outs.append(3)
                    
                elif a == b:
                    outs.append(0)
                    
                elif j == 'Strikeout' and b-a == 1:
                    outs.append(0)
                    
                elif j == 'Strikeout' and b-a == 2:
                    outs.append(1)
                    
                elif j == 'Strikeout' and a == 2:
                    outs.append(0)
                elif j == 'Strikeout' and b-a < 0:
                    outs.append(int(2-a))
                else:
                    if b-a > 0:
                        outs.append(int(b-a))
                    elif b-a < 0:
                        outs.append(int(3-a))
                    else:
                        outs.append(0)
            except:
                a = df_temp.outs_when_up[i]
                
                if temp['Top/Bottom'][i] == 'Top' and j == 'Strikeout':
                    outs.append(int(2-a))
                    
                elif temp['Top/Bottom'][i] == 'Top' and j != 'Strikeout':
                    outs.append(int(3-a))
                
                # 끝내기 상황에 대한 예외처리
                
                elif temp['Top/Bottom'][i] == 'Bottom':
                    
                    if df_temp.post_away_score[i] > df_temp.post_home_score[i] and j == 'Strikeout':
                        outs.append(int(2-a))
                        
                    elif df_temp.post_away_score[i] > df_temp.post_home_score[i] and j != 'Strikeout':
                        outs.append(int(3-a))
                    
                    elif df_temp.post_away_score[i] < df_temp.post_home_score[i] and df_temp.PlayResult == 'Sacrifice':
                        outs.append(1)
                    
                    elif df_temp.post_away_score[i] < df_temp.post_home_score[i] and df_temp.PlayResult != 'Sacrifice':
                        outs.append(0)
        
    del i, j, k, a, b, gid
    
    df_temp['OutsOnPlay'] = outs
    del outs
    print('14. OutsOnPlay 컬럼 생성 완료')
    
    # Notes 컬럼 생성
    df_temp['Notes'] = ''
    print('15. Notes 컬럼 생성 완료')
    
    # RelSpeed 컬럼 단위변환
    df_temp['RelSpeed'] = df_temp.release_speed * 1.60934
    print('16. RelSpeed 컬럼 생성 완료')
    
    # Vert/HorzRelAngle 0 처리
    df_temp['VertRelAngle'] = float(0)
    df_temp['HorzRelAngle'] = float(0)
    print('17. Vert/HorzRelAngle 컬럼 생성 완료')
    
    # SpinRate 컬럼 생성(컬럼명 변경)
    df_temp['SpinRate'] = df_temp['release_spin_rate']
    print('18. SpinRate 컬럼명 변경 완료')
    
    # SpinAxis, Tilt 컬럼 생성(컬럼명 변경)
    df_temp['SpinAxis'] = df_temp['spin_axis']
    
    
    tilt = []
    for i in df_temp.SpinAxis:
        try:
            if i//15 > 12:
                hour = int(i//15 - 12)
                minute = i/15 - 12 - hour
                min2 = int(minute // 0.25 * 15) 
                if min2 == 0:
                    tilt.append(f'{hour}:00')
                else:
                    tilt.append(f'{hour}:{min2}')
            else:
                hour = int(i//15)
                minute = i/15 - hour
                min2 = int(minute // 0.25 * 15)        
                if min2 == 0:
                    tilt.append(f'{hour}:00')
                else:
                    tilt.append(f'{hour}:{min2}')
        except:
            tilt.append('')
    del i, hour, minute, min2
    df_temp['Tilt'] = tilt
    del tilt
    print('19. SpinAxis 컬럼명 변경 및 Tilt 컬럼 생성 완료')
    
    
    # RelHeight, RelSide, Extension 단위 변환
    df_temp['RelHeight'] = df_temp['release_pos_z']*0.3048
    df_temp['RelSide'] = df_temp['release_pos_x']*0.3048
    df_temp['Extension'] = df_temp['release_extension']*0.3048
    
    print('20. RelHeight/Side/Extension 단위변환 완료')
    
    # 무브먼트 컬럼 단위변환(인치 to 센치)
    df_temp['VertBreak'] = float(0)
    df_temp['InducedVertBreak'] = df_temp['pfx_z']*30.48
    df_temp['HorzBreak'] = df_temp['pfx_x']*30.48
    
    print('21. Break 컬럼 단위변환 완료')
    
    # 로케이션 컬럼 단위 변환
    df_temp['PlateLocHeight'] = df_temp['plate_z']*0.3048
    df_temp['PlateLocSide'] = df_temp['plate_x']*0.3048 
    
    print('22. PlateLocHeight/ Side 컬럼 단위 변환 완료')
    
    # 타구속도, 발사각 컬럼명 변경
    df_temp['ExitSpeed'] = df_temp.launch_speed*1.609344
    df_temp['Angle'] = df_temp.launch_angle
    
    print('23. ExitSpeed, Angle 단위 변환 완료')
    
    # 비거리 단위변환
    df_temp['Distance'] = df_temp['hit_distance_sc']*0.3048
    print('24. Distance 컬럼 단위 변환 완료')
    
    # 타구 좌표를 통한 Bearing 및 새로운 타구 좌표 계산
    bearing = []
    
    df_temp['HC_X'] = (df_temp['hc_x']-125.42)
    df_temp['HC_Y'] = (198.27-df_temp['hc_y'])
    
    for i, j in zip(df_temp['HC_X'], df_temp['HC_Y']):
        try:
            # 역삼각함수 모듈 활용하여 각도 계산(아크탄젠트)
            
            a = math.degrees(np.arctan(i/j))
    
            bearing.append(a)
            
        except:
            bearing.append(np.nan)
    del i, j, a
    
    df_temp['Bearing'] = bearing
    del bearing
    print('25. Bearing 계산 완료')
    
    # 타구 좌표 계산
    df_temp['HC_X'] = np.sin(np.deg2rad(df_temp['Bearing']))*df_temp['Distance']
    df_temp['HC_Y'] = np.cos(np.deg2rad(df_temp['Bearing']))*df_temp['Distance']
    print('26. 타구 좌표 계산 완료')
    
    # 체감구속(EffectiveVelo) 단위 변환
    df_temp['EffectiveVelo'] = df_temp['effective_speed']*1.60934
    print('27. EffectiveVelo 컬럼 단위 변환 완료')
    
    # 게임 아이디(서번트의 game_pk 인용), 피치UID 간이생성
    
    df_temp['GameID'] = df_temp['game_pk']
    
    # PitchUID는 날짜-게임아이디-피치넘버 조합으로 생성
    
    uid = []
    for i, j, k in zip(df_temp.game_date, df_temp.game_pk, df_temp.PitchNo):
        uid.append(f'{i}_{j}_{k}')
        
    del i, j, k
    
    df_temp['GameUID'] = uid   
    del uid
    print('28. GameID, GameUID 컬럼 생성 완료')
    
    # 결과 컬럼 선택
    res_temp = df_temp[['PitchNo', 'game_date', 'Time', 'PAofInning',
                        'PitchofPA', 'player_name', 'pitcher',
                        'PitcherThrows','PitcherTeam', 'Batter', 
                        'batter', 'BatterSide', 'BatterTeam', 
                        'PitcherSet', 'inning', 'Top/Bottom', 
                        'outs_when_up', 'balls', 'strikes', 
                        'TaggedPitchType', 'AutoPitchType', 'PitchCall', 
                        'KorBB', 'TaggedHitType', 'PlayResult', 
                        'OutsOnPlay', 'RunsScored', 'Notes',
                        'RelSpeed', 'VertRelAngle', 'HorzRelAngle', 
                        'SpinRate', 'SpinAxis', 'Tilt',
                        'RelHeight', 'RelSide', 'Extension', 
                        'VertBreak', 'InducedVertBreak', 'HorzBreak',
                        'PlateLocHeight', 'PlateLocSide', 'ExitSpeed', 
                        'Angle', 'Distance', 'Bearing',
                        'HC_X', 'HC_Y', 'EffectiveVelo', 'GameID', 'PitchUID'
                        ]]
    
    # 컬럼명 변경
    res = res_temp.rename(columns={'game_date':'Date',
                                   'player_name':'Pitcher',
                                   'pitcher':'PitcherId',
                                   'batter':'BatterId',
                                   'inning':'Inning',
                                   'outs_when_up':'Outs',
                                   'balls':'Balls',
                                   'strikes':'Strikes',
                                   })
    print('29. 컬럼명 전체 트랙맨 스타일로 변경 완료')
    
    res.to_csv(f'./total/savant_to_trackman_{today}.csv',index=False, encoding='utf-8')
    print('30. 변환 파일 csv 저장 완료')

    return res

savant_convert()