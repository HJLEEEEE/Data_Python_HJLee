# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:52:59 2022

@author: Hojoong Lee
"""

def mlb_players(season):
    import statsapi

    players = statsapi.get('sports_players',{'sportsId':1, 'season':season})['people']
    
    length = len(players)
    
    tid = []
    pid = []
    fname = []
    lname = []
    pos = []
    phand = []
    bhand = []
    backnum = []
    active = []
    height = []
    weight = []
    birth = []
    hometown =[]
    homestate = []
    indate = []
    dyear = []
    
    for i in range(length):
        try:
            teamid = players[i]['currentTeam']['id']
            playerid = players[i]['id']
            firstn = players[i]['useName']
            lastn = players[i]['lastName']
            posi = players[i]['primaryPosition']['abbreviation']
            pitch = players[i]['pitchHand']['code']
            bat = players[i]['batSide']['code']
            try:
                num = players[i]['primaryNumber']
            except:
                num = 99999
            act = players[i]['active']
            h = players[i]['height']
            w = players[i]['weight']
            bday = players[i]['birthDate']
            try:
                htown = players[i]['birthCity']
            except:
                htown = ""
            hstate = players[i]['birthStateProvince']
            try:
                debut = players[i]['mlbDebutDate']
            except:
                debut = ""
            try:
                draft = players[i]['draftYear']
            except:
                draft = 9999
            
            tid.append(teamid)
            pid.append(playerid)
            fname.append(firstn)
            lname.append(lastn)
            pos.append(posi)
            phand.append(pitch)
            bhand.append(bat)
            backnum.append(num)
            active.append(act)
            height.append(h)
            weight.append(w)
            birth.append(bday)
            hometown.append(htown)
            homestate.append(hstate)
            indate.append(debut)
            dyear.append(draft)
            
        except:
            teamid = players[i]['currentTeam']['id']
            playerid = players[i]['id']
            firstn = players[i]['useName']
            lastn = players[i]['lastName']
            posi = players[i]['primaryPosition']['abbreviation']
            pitch = players[i]['pitchHand']['code']
            bat = players[i]['batSide']['code']
            try:
                num = players[i]['primaryNumber']
            except:
                num = 99999
            act = players[i]['active']
            h = players[i]['height']
            w = players[i]['weight']
            bday = players[i]['birthDate']
            try:
                htown = players[i]['birthCity']
            except:
                htown = ""
            hstate = players[i]['birthCountry']
            try:
                debut = players[i]['mlbDebutDate']
            except:
                debut = ""
            try:
                draft = players[i]['draftYear']
            except:
                draft = 9999
            
            tid.append(teamid)
            pid.append(playerid)
            fname.append(firstn)
            lname.append(lastn)
            pos.append(posi)
            phand.append(pitch)
            bhand.append(bat)
            backnum.append(num)
            active.append(act)
            height.append(h)
            weight.append(w)
            birth.append(bday)
            hometown.append(htown)
            homestate.append(hstate)
            indate.append(debut)
            dyear.append(draft)
    
    del act, bat, draft, i, pitch, playerid, posi, teamid, w, hstate, num, firstn, h, htown, lastn, bday, debut    
    
    # 키 몸무게 단위변환
    
    height1 = []
    weight1 = []
    
    for i, j in zip(height, weight):
        feet = i.split(' ')[0][:-1]
        inch = i.split(' ')[1][:-1]
        pound = round(j*0.453592, 0)
        newheight = int(feet)*30.48+int(inch)*2.54
        
        height1.append(round(newheight, 0))
        weight1.append(pound)
        
    del feet, inch, newheight, height, pound, weight
    
    key = []
    
    for i in pid:
        key.append(f'{season}-{i}')
    
    del i
    
    season1 = []
    
    for i in range(len(tid)):
        season1.append(season)
        
    del i, season
    
    import pandas as pd
    
    df = pd.DataFrame()
    df['SEASON'] = season1
    df['TEAMID'] = tid
    df['FIRSTNAME'] = fname
    df['LASTNAME'] = lname
    df['POS'] = pos
    df['PITCHHAND'] = phand
    df['BATSIDE'] = bhand
    df['JERSEY'] = backnum
    df['ACTIVE'] = active
    df['PLAYERID'] = pid
    df['HEIGHT'] = height1
    df['WEIGHT'] = weight1
    df['BIRTHDATE'] = birth
    df['HOMETOWN'] = hometown
    df['HOMESTATE'] = homestate
    df['INDATE'] = indate
    df['D_YEAR'] = dyear
    
    from datetime import datetime    
    df['INPUTTIME'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  
    df['KEY'] = key
    
    return df

season = 2022
res = mlb_players(season=season)

def player_info_db_upload(res = res):
    tp = [tuple(x) for x in res.values]
    
    import pymysql
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='ghwnd128',
                           db='baseball'
                           )
    
    cursor = conn.cursor()
    a = len(tp)
    
    for i, j in zip(tp, range(len(tp))):
        
        try:
            cursor.execute(f'''INSERT INTO player_info VALUES {i}''')
            conn.commit()
            
        # 키값 기준 중복 존재시 새로운 정보로 대체
        except:
            cursor.execute(f'''REPLACE INTO player_info VALUES {i}''')
            conn.commit()
                           
        print(f'{j+1}/{a} DB 업로드 완료')
        
    conn.close()    
    del a, i, j
    
player_info_db_upload(res=res)