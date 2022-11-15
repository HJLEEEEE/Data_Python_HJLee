# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:09:58 2021

@author: Hojoong Lee
"""

def Normal_Batter_Stat_Crawler1(year):
    
    from selenium import webdriver
    import time
    
    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx?sort=HRA_RT'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    Season = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').text
    time.sleep(1)
    print('시즌선택 완료')
    
    # 정규시즌기록 선택
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[1]').click()
    time.sleep(1)
    print('정규시즌 기록 선택 완료')
    
    # 게임 정렬 선택(규정타석 외 기록이 나오기 위함)
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_udpContent"]/div[3]/table/thead/tr/th[5]/a').click()
    time.sleep(1)
    print('출장경기 순 정렬 완료')
    
    ## 타자 기본기록 크롤링
    # 빈 리스트 생성
    season1 = []
    player_name = []
    player_id =[]
    team = []
    avg = []
    g = []
    pa = []
    ab = []
    r = []
    h = []
    double = []
    triple = []
    hr = []
    tb = []
    rbi = []
    sac = []
    sf = []
    print('리스트 생성 완료')
    
    print('타자 기본기록 크롤링 시작')
    for i in range(1,10):
        try:
            pages = driver.find_elements_by_css_selector("div.paging > a")
            
            if len(pages) == 9:
                
                for j in range(1,len(pages)-3):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(1)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(1)
                    
                    for k in range(1, len(players)+1):
                        
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        name = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('text')
                        Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
                        AVG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
                        G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        PA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                        AB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        R = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        H = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        HH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        HHH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                        HR = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                        TB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                        RBI = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                        SAC = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                        SF = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
                        
                        pid = href[-5:]
                        
                        player_id.append(pid)
                        player_name.append(name)
                        team.append(Team)
                        if AVG == '-':
                            avg.append(float(0.000))
                        else:
                            avg.append(float(AVG))
                        g.append(int(G))
                        pa.append(int(PA))
                        ab.append(int(AB))
                        r.append(int(R))
                        h.append(int(H))
                        double.append(int(HH))
                        triple.append(int(HHH))
                        hr.append(int(HR))
                        tb.append(int(TB))
                        rbi.append(int(RBI))
                        sac.append(int(SAC))
                        sf.append(int(SF))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')                                                           
            else:
                
                for j in range(1,len(pages)-2):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(1)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(1)
                    
                    for k in range(1, len(players)+1):
                        
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        name = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('text')
                        Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
                        AVG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
                        G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        PA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                        AB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        R = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        H = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        HH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        HHH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                        HR = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                        TB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                        RBI = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                        SAC = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                        SF = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
                        
                        pid = href[-5:]
                        
                        player_id.append(pid)
                        player_name.append(name)
                        team.append(Team)
                        if AVG == '-':
                            avg.append(float(0.0))
                        else:
                            avg.append(float(AVG))
                        g.append(int(G))
                        pa.append(int(PA))
                        ab.append(int(AB))
                        r.append(int(R))
                        h.append(int(H))
                        double.append(int(HH))
                        triple.append(int(HHH))
                        hr.append(int(HR))
                        tb.append(int(TB))
                        rbi.append(int(RBI))
                        sac.append(int(SAC))
                        sf.append(int(SF))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')                        
                        
            driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_ucPager_btnNext').click()
            time.sleep(2)
            print(str(i)+'장 크롤링 완료')
        except:
            break
        
    for s in range(len(g)):
        season1.append(Season)
        
        
    
    driver.close()
         
    print(Season+'시즌 타자 기본기록1 크롤링 완료')
    
    dic1 = {'SEASON' : season1,
            'PLAYERID' : player_id,
            'PLAYER' : player_name,
            'TEAM' : team,
            'AVG' : avg,
            'G' : g,
            'PA' : pa,
            'AB' : ab,
            'R' : r,
            'H' : h,
            '2B' : double,
            '3B' : triple,
            'HR' : hr,
            'TB' : tb,
            'RBI' : rbi,
            'SAC' : sac,
            'SF' : sf}
    
    import pandas as pd
    df = pd.DataFrame(dic1)
    
    print('타자 기본기록1 데이터프레임 생성 완료')
    return df

def Normal_Batter_Stat_Crawler2(year):
    from selenium import webdriver
    import time
    
    # 시즌 기록실 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx?sort=HRA_RT'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 왼료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    #year = 2021
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    print('시즌선택 완료')
    
    # 정규시즌기록 선택
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[1]').click()
    time.sleep(1)
    print('정규시즌 기록 선택 완료')
    
    # 기록보기 2장 선택
    driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.row > div.more_record > a.next').click()
    print('기록보기 2장 선택 완료')
    
    # 볼넷으로 정렬(규정타석 이외의 선수를 보기 위함)
    driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > thead > tr > th:nth-child(5) > a').click()
    time.sleep(1)
    print('볼넷 정렬 선택 완료')
    
    ## 타자 기본기록2 크롤링
    # 빈 리스트 생성
    player_id =[]
    bb = []
    ibb = []
    hbp = []
    so = []
    gdp = []
    slg = []
    obp = []
    ops = []
    mh = []
    risp = []
    phba = []
    
    print('타자 기본기록2 크롤링 시작')
    for i in range(1,10):
      try:
          pages = driver.find_elements_by_css_selector("div.paging > a")
          
          if len(pages) == 9:
              
              for j in range(1,len(pages)-3):
                  
                  driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                  time.sleep(1)

                  players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                  time.sleep(1)
                  
                  for k in range(1, len(players)+1):
                      href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                      pid = href[-5:]
                      BB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                      IBB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                      HBP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                      SO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                      GDP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                      SLG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                      OBP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                      OPS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                      MH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                      RISP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                      PHBA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                      
                      player_id.append(pid)
                      bb.append(int(BB))
                      ibb.append(int(IBB))
                      hbp.append(int(HBP))
                      so.append(int(SO))
                      gdp.append(int(GDP))
                      if SLG == '-':
                          slg.append(float(0))
                      else:
                          slg.append(float(SLG))
                      
                      if OBP == '-':
                          obp.append(float(0))
                      else:
                          obp.append(float(OBP))
                          
                      if OPS == '-':
                          ops.append(float(0))
                      else:
                          ops.append(float(OPS))
                      
                      mh.append(int(MH))
                      
                      if RISP == '-':
                          risp.append(float(0))
                      else:
                          risp.append(float(RISP))
                          
                      if PHBA == '-':
                          phba.append(float(0))
                      else:
                          phba.append(float(PHBA))
                      print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')
          else:
              
              for j in range(1,len(pages)-2):
                  
                  driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                  time.sleep(1)
                  
                  players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                  time.sleep(1)
                  
                  for k in range(1, len(players)+1):
                      
                      href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                      pid = href[-5:]
                      BB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                      IBB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                      HBP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                      SO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                      GDP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                      SLG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                      OBP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                      OPS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                      MH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                      RISP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                      PHBA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                      
                      player_id.append(pid)
                      bb.append(int(BB))
                      ibb.append(int(IBB))
                      hbp.append(int(HBP))
                      so.append(int(SO))
                      gdp.append(int(GDP))
                      if SLG == '-':
                          slg.append(float(0))
                      else:
                          slg.append(float(SLG))
                      
                      if OBP == '-':
                          obp.append(float(0))
                      else:
                          obp.append(float(OBP))
                          
                      if OPS == '-':
                          ops.append(float(0))
                      else:
                          ops.append(float(OPS))
                      
                      mh.append(int(MH))
                      
                      if RISP == '-':
                          risp.append(float(0))
                      else:
                          risp.append(float(RISP))
                          
                      if PHBA == '-':
                          phba.append(float(0))
                      else:
                          phba.append(float(PHBA))    
                      print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')                      
                      
          driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_ucPager_btnNext').click()
          time.sleep(2)
          print(str(i)+'장 크롤링 완료')
      
      except:
          break
      

      
    print(str(year)+'시즌 타자 기본기록2 크롤링 완료')      
      
    driver.close()
       

      
    dic1 = {'PLAYERID' : player_id,
            'BB' : bb,
            'IBB' : ibb,
            'HBP' : hbp,
            'SO' : so,
            'GDP' : gdp,
            'SLG' : slg,
            'OBP' : obp,
            'OPS' : ops,
            'MH' : mh,
            'RISP' : risp,
            'PH-BA' : phba}
    
    import pandas as pd
    df = pd.DataFrame(dic1)
    print('타자 기본기록2 데이터프레임 생성 완료')
    return df

def Normal_Pitcher_Stat_Crawler1(year):
    from selenium import webdriver
    import time

    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    Season = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').text
    time.sleep(1)
    print('시즌선택 완료')
    
    # 정규시즌기록 선택
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[1]').click()
    time.sleep(1)
    print('정규시즌 기록 선택 완료')
    
    # 출장 경기 순 정렬
    driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > thead > tr > th:nth-child(5) > a').click()
    time.sleep(1)
    print('출장 경기 순 정렬 완료')
    
    # 리스트 생성
    player_id = []
    player_name = []
    team = []
    era = []
    g = []
    w = []
    l = []
    sv = []
    hld = []
    wpct = []
    ip = []
    h = []
    hr = []
    bb = []
    hbp = []
    so = []
    r = []
    er = []
    whip = []
    season1 = []
    
    
        
    print('투수 기본기록1 크롤링 시작')
    for i in range(1,10):
        try:
            pages = driver.find_elements_by_css_selector("div.paging > a")
                
            if len(pages) == 9:
                    
                for j in range(1,len(pages)-3):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(1)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(1)
                
                    for k in range(1, len(players)+1):
                                
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        name = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('text')
                        Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
                        ERA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
                        G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        W = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                        L = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        SV = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        HLD = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        WPCT = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        IP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                        H = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                        HR = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                        BB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                        HBP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                        SO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
                        R = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(17)').text
                        ER = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(18)').text
                        WHIP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(19)').text
                        
                        pid = href[-5:]
                        player_id.append(pid)
                        player_name.append(name)
                        team.append(Team)
                        if ERA == '-':
                            era.append(float(0.00))
                        else:
                            era.append(float(ERA))
                        g.append(int(G))
                        w.append(int(W))
                        l.append(int(L))
                        sv.append(int(SV))
                        hld.append(int(HLD))
                        if WPCT == '-':
                            wpct.append(int(0))
                        else:
                            wpct.append(float(WPCT))
                        ip.append(IP)
                        h.append(int(H))
                        hr.append(int(HR))
                        bb.append(int(BB))
                        hbp.append(int(HBP))
                        so.append(int(SO))
                        r.append(int(R))
                        er.append(int(ER))
                        if WHIP == '-':
                            whip.append(float(0.00))
                        else:
                            whip.append(float(WHIP))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')
            else:
                    
                for j in range(1,len(pages)-2):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(1)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(1)    
                    
                    
                    for k in range(1, len(players)+1):
                                
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        name = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('text')
                        Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
                        ERA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
                        G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        W = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                        L = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        SV = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        HLD = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        WPCT = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        IP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                        H = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                        HR = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                        BB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                        HBP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                        SO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
                        R = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(17)').text
                        ER = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(18)').text
                        WHIP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(19)').text
                        
                        pid = href[-5:]
                        player_id.append(pid)
                        player_name.append(name)
                        team.append(Team)
                        if ERA == '-':
                            era.append(float(0.00))
                        else:
                            era.append(float(ERA))
                        g.append(int(G))
                        w.append(int(W))
                        l.append(int(L))
                        sv.append(int(SV))
                        hld.append(int(HLD))
                        if WPCT == '-':
                            wpct.append(float(0.000))
                        else:
                            wpct.append(float(WPCT))
    
                        ip.append(IP)
                        h.append(int(H))
                        hr.append(int(HR))
                        bb.append(int(BB))
                        hbp.append(int(HBP))
                        so.append(int(SO))
                        r.append(int(R))
                        er.append(int(ER))
                        if WHIP == '-':
                            whip.append(float(0.00))
                        else:
                            whip.append(float(WHIP))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')
                        
            driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_ucPager_btnNext').click()
            time.sleep(2)   
            print(str(i)+'장 크롤링 완료')
        except:
            break
    print('투수 기본기록1 크롤링 완료')
    for s in range(len(g)):
        season1.append(Season)
            
    driver.close()
    
    IP1 = []
    
    for i in ip:
        if " " in i and "/" in i:
            ip1 = i.split(' ')[0]
            ip2 = i.split(' ')[1]
            ip3 = int(ip2.split('/')[0])/10
            ip4 = int(ip1)+float(ip3)
            IP1.append(ip4)
        elif " " not in i and "/" in i:
            ip3 = int(ip2.split('/')[0])/10
            IP1.append(ip3)
        else:
            IP1.append(float(i))
    
    dic1 = {'SEASON' : season1,
            'PLAYERID' : player_id,
            'PLAYER' : player_name,
            'TEAM' : team,
            'ERA' : era,
            'G' : g,
            'W' : w,
            'L' : l,
            'SV' : sv,
            'HLD' : hld,
            'WPCT' : wpct,
            'IP' : IP1,
            'H' : h,
            'HR' : hr,
            'BB' : bb,
            'HBP' : hbp,
            'SO' : so,
            'R' : r,
            'ER' : er,
            'WHIP' : whip}

    import pandas as pd

    Pitcher1 = pd.DataFrame(dic1)
    print(f'{year}시즌 투수 기본기록1 데이터프레임 생성 완료')
    return Pitcher1

def Normal_Pitcher_Stat_Crawler2(year):
    from selenium import webdriver
    import time
    
    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    print('시즌선택 완료')
    
    # 정규시즌기록 선택
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[1]').click()
    time.sleep(1)
    print('정규시즌 기록 선택 완료')
    
    
    # 다음 기록 보기
    driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.row > div.more_record > a.next').click()
    time.sleep(1)
    print('정규시즌 기록2 선택 완료')
    
    # CG 순 정렬
    driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > thead > tr > th:nth-child(5) > a').click()
    time.sleep(1)
    print('CG 순 정렬 완료')
     
    # 리스트 생성
    player_id = []
    cg = []
    sho = []
    qs = []
    bsv = []
    tbf = []
    np = []
    avg = []
    double = []
    triple = []
    sac = []
    sf = []
    ibb = []
    wp = []
    bk = []
    
    print('투수 기본기록2 크롤링 시작')
    for i in range(1,10):
        try:
            pages = driver.find_elements_by_css_selector("div.paging > a")
                
            if len(pages) == 9:
                    
                for j in range(1,len(pages)-3):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(1)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(1)
                
                    for k in range(1, len(players)+1):
                                
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        CG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        SHO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                        QS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        BSV = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        TBF = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        NP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        AVG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                        HH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                        HHH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                        SAC = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                        SF = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                        IBB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
                        WP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(17)').text
                        BK = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(18)').text
                        
                        
                        pid = href[-5:]
                        player_id.append(pid)
                        cg.append(int(CG))
                        sho.append(int(SHO))
                        qs.append(int(QS))
                        bsv.append(int(BSV))
                        tbf.append(int(TBF))
                        np.append(int(NP))
                        avg.append(float(AVG))
                        double.append(int(HH))
                        triple.append(int(HHH))
                        sac.append(int(SAC))
                        sf.append(int(SF))
                        ibb.append(int(IBB))
                        wp.append(int(WP))
                        bk.append(int(BK))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')
            else:
                    
                for j in range(1,len(pages)-2):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(1)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(1)    
                    
                    
                    for k in range(1, len(players)+1):
                                
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        CG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        SHO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                        QS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        BSV = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        TBF = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        NP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        AVG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                        HH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                        HHH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                        SAC = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                        SF = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                        IBB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
                        WP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(17)').text
                        BK = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(18)').text
                        
                        
                        pid = href[-5:]
                        player_id.append(pid)
                        cg.append(int(CG))
                        sho.append(int(SHO))
                        qs.append(int(QS))
                        bsv.append(int(BSV))
                        tbf.append(int(TBF))
                        np.append(int(NP))
                        if AVG == '-':
                            avg.append(float(0.000))
                        else:
                            avg.append(float(AVG))
                        double.append(int(HH))
                        triple.append(int(HHH))
                        sac.append(int(SAC))
                        sf.append(int(SF))
                        ibb.append(int(IBB))
                        wp.append(int(WP))
                        bk.append(int(BK))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')
                        
            
            driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_ucPager_btnNext').click()
            time.sleep(2)   
            print(f'{i}장 크롤링 완료')
            
        except:
            break
        
    
            
    
    print('투수 기본기록2 크롤링 완료')        
    driver.close()
    
    dic1 = {'PLAYERID' : player_id,
            'CG' : cg,
            'SHO' : sho,
            'QS' : qs,
            'BSV' : bsv,
            'TBF' : tbf,
            'NP' : np,
            'AVG' : avg,
            '2B' : double,
            '3B' : triple,
            'SAC' : sac,
            'SF' : sf,
            'IBB' : ibb,
            'WP' : wp,
            'BK' : bk}
    
    import pandas as pd
    
    Pitcher2 = pd.DataFrame(dic1)
    
    print(f'{year}시즌 투수 기본기록2 데이터프레임 생성 완료')
    return Pitcher2

def Normal_Defence_Stat_Crawler(year):
    from selenium import webdriver
    import time
    
    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Player/Defense/Basic.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    Season = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').text
    print('시즌선택 완료')
    
    ## 타자 기본기록 크롤링
    # 빈 리스트 생성
    season1 = []
    player_name = []
    player_id =[]
    team = []
    pos = []
    g = []
    gs = []
    ip = []
    e = []
    pko = []
    po = []
    a = []
    dp = []
    fpct = []
    pb = []
    sb = []
    cs = []
    cs_per = []
    print('리스트 생성 완료')
    
    print('수비 기본기록 크롤링 시작')
    for i in range(1,10):
        try:
            pages = driver.find_elements_by_css_selector("div.paging > a")
            
            if len(pages) == 9:
                
                for j in range(1,len(pages)-3):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(1)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(1)
                    
                    for k in range(1, len(players)+1):
    
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        name = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('text')
                        Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
                        POS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
                        G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        GS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                        IP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        E = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        PKO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        PO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        A = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                        DP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                        FPCT = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                        PB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                        SB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                        CS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
                        CS_PER = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(17)').text
                        
                        pid = href[-5:]
                        player_id.append(pid)
                        player_name.append(name)
                        team.append(Team)
                        pos.append(POS)
                        g.append(int(G))
                        gs.append(int(GS))
                        ip.append(IP)
                        e.append(int(E))
                        pko.append(int(PKO))
                        po.append(int(PO))
                        a.append(int(A))
                        dp.append(int(DP))
                        if FPCT == '-':
                            fpct.append(float(0.000))
                        else:
                            fpct.append(float(FPCT))
                        pb.append(int(PB))
                        sb.append(int(SB))
                        cs.append(int(CS))
                        
                        if CS_PER == '-':
                            cs_per.append(float(0.000))
                        else:
                            cs_per.append(float(CS_PER))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')
            else:
                
                for j in range(1,len(pages)-2):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(1)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(1)
                    
                    for k in range(1, len(players)+1):
                        
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        name = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('text')
                        Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
                        POS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
                        G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        GS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
                        IP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        E = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        PKO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        PO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        A = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
                        DP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
                        FPCT = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
                        PB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
                        SB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
                        CS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
                        CS_PER = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(17)').text
                        
                        pid = href[-5:]
                        player_id.append(pid)
                        player_name.append(name)
                        team.append(Team)
                        g.append(int(G))
                        gs.append(int(GS))
                        ip.append(IP)
                        pos.append(POS)
                        e.append(int(E))
                        pko.append(int(PKO))
                        po.append(int(PO))
                        a.append(int(A))
                        dp.append(int(DP))
                        if FPCT == '-':
                            fpct.append(float(0.000))
                        else:
                            fpct.append(float(FPCT))
                        pb.append(int(PB))
                        sb.append(int(SB))
                        cs.append(int(CS))
                        if CS_PER == '-':
                            cs_per.append(float(0.000))
                        else:
                            cs_per.append(float(CS_PER))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')
                        
            driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_ucPager_btnNext').click()
            time.sleep(2)
            print(str(i)+'장 크롤링 완료')
        except:
            break
        
    for s in range(len(g)):
        season1.append(Season)
        
        
    
    driver.close()
         
    print(Season+'시즌 수비기록 크롤링 완료')
    
    
    # 이닝 표기방식 처리
    
    IP1 = []
    
    for i in ip:
        if " " in i and "/" in i:
            ip1 = i.split(' ')[0]
            ip2 = i.split(' ')[1]
            ip3 = int(ip2.split('/')[0])/10
            ip4 = int(ip1)+float(ip3)
            IP1.append(ip4)
        elif " " not in i and "/" in i:
            ip3 = int(ip2.split('/')[0])/10
            IP1.append(ip3)
        else:
            IP1.append(float(i))
    
    dic1 = {'SEASON' : season1,
            'PLAYERID' : player_id,
            'PLAYER' : player_name,
            'TEAM' : team,
            'POS' : pos,
            'G' : g,
            'GS' : gs,
            'IP' : IP1,
            'E' : e,
            'PKO' : pko,
            'PO' : po,
            'A' : a,
            'DP' : dp,
            'FPCT' : fpct,
            'PB' : pb,
            'SB' : sb,
            'CS' : cs,
            'CS%' : cs_per}
    
    import pandas as pd
    df = pd.DataFrame(dic1)
    
    print('수비기록 데이터프레임 생성 완료')
    
    return df

def Normal_Running_Stat_Crawler(year):
    from selenium import webdriver
    import time
    
    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Player/Runner/Basic.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    Season = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').text
    print('시즌선택 완료')


    
    ## 타자 기본기록 크롤링
    # 빈 리스트 생성
    season1 = []
    player_name = []
    player_id =[]
    team = []
    g = []
    sba = []
    sb = []
    cs = []
    sb_per = []
    oob = []
    pko = []
    
    print('리스트 생성 완료')
    
    print('주루 기본기록 크롤링 시작')
    for i in range(1,10):
        try:
            pages = driver.find_elements_by_css_selector("div.paging > a")
            
            if len(pages) == 9:
                
                for j in range(1,len(pages)-3):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(2)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(2)
                    
                    for k in range(1, len(players)+1):
    
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        name = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('text')
                        Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
                        G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
                        SB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        SBA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(5)').text
                        CS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        SB_PER = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        OOB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        PKO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        
                        pid = href[-5:]
                        player_id.append(pid)
                        player_name.append(name)
                        team.append(Team)
                        g.append(int(G))
                        sba.append(int(SBA))
                        sb.append(int(SB))
                        cs.append(int(CS))
                        if SB_PER == '-':
                            sb_per.append(float(0.000))
                        else:
                            sb_per.append(float(SB_PER))
                        oob.append(int(OOB))
                        pko.append(int(PKO))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')
                                                           
            else:
                
                for j in range(1,len(pages)-2):
                    
                    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{j}').click()
                    time.sleep(2)
                    
                    players = driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')
                    time.sleep(2)
                    
                    for k in range(1, len(players)+1):
                        
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('href')
                        name = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2) > a').get_attribute('text')
                        Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
                        G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
                        SB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
                        SBA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(5)').text
                        CS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
                        SB_PER = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
                        OOB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
                        PKO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
                        
                        pid = href[-5:]
                        player_id.append(pid)
                        player_name.append(name)
                        team.append(Team)
                        g.append(int(G))
                        sba.append(int(SBA))
                        sb.append(int(SB))
                        cs.append(int(CS))
                        if SB_PER == '-':
                            sb_per.append(float(0.000))
                        else:
                            sb_per.append(float(SB_PER))
                        oob.append(int(OOB))
                        pko.append(int(PKO))
                        print(f'{i}장 {j}페이지 {k}번째 선수 크롤링 완료')
                        
            driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_ucPager_btnNext').click()
            time.sleep(2)
            print(str(i)+'장 크롤링 완료')
        except:
            break
        
    for s in range(len(g)):
        season1.append(Season)
        
        
    
    driver.close()
         
    print(Season+'시즌 주루기록 크롤링 완료')
    
    dic1 = {'SEASON' : season1,
           'PLAYERID' : player_id,
           'PLAYER' : player_name,
           'TEAM' : team,
           'G' : g,
           'SBA' : sba,
           'SB' : sb,
           'CS' : cs,
           'SB%' : sb_per,
           'OOB' : oob,
           'PKO' : pko
           }
    
    import pandas as pd
    df = pd.DataFrame(dic1)
    
    print('주루기록 데이터프레임 생성 완료')
    
    return df

def Team_Batter_Stat_Crawler1(year):
    
    from selenium import webdriver
    import time
    
    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Team/Hitter/BasicOld.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    Season = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').text
    print('시즌선택 완료')
    
    # 정규시즌기록 선택
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[1]').click()
    time.sleep(1)
    print('정규시즌 기록 선택 완료')
    
    
    ## 타자 기본기록 크롤링
    # 빈 리스트 생성
    season1 = []
    team = []
    avg = []
    g = []
    pa = []
    ab = []
    r = []
    h = []
    double = []
    triple = []
    hr = []
    tb = []
    rbi = []
    sac = []
    sf = []
    print('리스트 생성 완료')
    
    print('타자 팀기록 크롤링 시작')
    
     
    for k in range(1,11):
        Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2)').text
        AVG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
        G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
        PA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(5)').text
        AB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
        R = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
        H = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
        HH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
        HHH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
        HR = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
        TB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
        RBI = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
        SAC = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
        SF = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
        
        team.append(Team)
        if AVG == '-':
            avg.append(float(0.000))
        else:
            avg.append(float(AVG))
        g.append(int(G))
        pa.append(int(PA))
        ab.append(int(AB))
        r.append(int(R))
        h.append(int(H))
        double.append(int(HH))
        triple.append(int(HHH))
        hr.append(int(HR))
        tb.append(int(TB))
        rbi.append(int(RBI))
        sac.append(int(SAC))
        sf.append(int(SF))                                                      
        time.sleep(1)
        
        
    for s in range(1,11):
        season1.append(Season)
        
    
    driver.close()
         
    print(Season+'시즌 타자 팀기본기록1 크롤링 완료')
    
    dic1 = {'SEASON' : season1,
            'TEAM' : team,
            'AVG' : avg,
            'G' : g,
            'PA' : pa,
            'AB' : ab,
            'R' : r,
            'H' : h,
            '2B' : double,
            '3B' : triple,
            'HR' : hr,
            'TB' : tb,
            'RBI' : rbi,
            'SAC' : sac,
            'SF' : sf}
    
    import pandas as pd
    df = pd.DataFrame(dic1)
    
    print(Season+'타자 팀기본기록1 데이터프레임 생성 완료')
    return df

def Team_Batter_Stat_Crawler2(year):
    from selenium import webdriver
    import time
    
    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Team/Hitter/BasicOld.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    print('시즌선택 완료')
    
    # 정규시즌기록 선택
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[1]').click()
    time.sleep(1)
    print('정규시즌 기록 선택 완료')
    
    # 기록보기 2장 선택
    driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > div > div > a.next').click()
    time.sleep(1)
    print('기록보기 2장 선택 완료')
    
    
    ## 타자 기본기록2 크롤링
    # 빈 리스트 생성
    team =[]
    bb = []
    ibb = []
    hbp = []
    so = []
    gdp = []
    slg = []
    obp = []
    ops = []
    mh = []
    risp = []
    phba = []
    
    print('타자 팀기본기록2 크롤링 시작')
             
    for k in range(1, 11):
    
        #cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child(1) > td:nth-child(2)
        try:
            Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2)').text
            BB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
            IBB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(5)').text
            HBP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
            SO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
            GDP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
            SLG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
            OBP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
            OPS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
            MH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
            RISP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
            PHBA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
            
            team.append(Team)
            bb.append(int(BB))
            ibb.append(int(IBB))
            hbp.append(int(HBP))
            so.append(int(SO))
            gdp.append(int(GDP))
            if SLG == '-':
                slg.append(float(0))
            else:
                slg.append(float(SLG))
            
            if OBP == '-':
                obp.append(float(0))
            else:
                obp.append(float(OBP))
            
            if OPS == '-':
                ops.append(float(0))
            else:
                ops.append(float(OPS))
            
            mh.append(int(MH))
            
            if RISP == '-':
                risp.append(float(0))
            else:
                risp.append(float(RISP))
            
            if PHBA == '-':
                phba.append(float(0))
            else:
                phba.append(float(PHBA))
      
        except:
            print(str(year)+'시즌 타자 팀기본기록2 크롤링 완료')      
            break
      
    driver.close()
       
    
      
    dic1 = {'TEAM' : team,
            'BB' : bb,
            'IBB' : ibb,
            'HBP' : hbp,
            'SO' : so,
            'GDP' : gdp,
            'SLG' : slg,
            'OBP' : obp,
            'OPS' : ops,
            'MH' : mh,
            'RISP' : risp,
            'PH-BA' : phba}
    
    import pandas as pd
    df = pd.DataFrame(dic1)
    print('타자 팀기본기록2 데이터프레임 생성 완료')
    return df

def Team_Pitcher_Stat_Crawler1(year):
    from selenium import webdriver
    import time
    
    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Team/Pitcher/Basic1.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    Season = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').text
    time.sleep(1)
    print('시즌선택 완료')
    
    # 정규시즌기록 선택
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[1]').click()
    time.sleep(1)
    print('정규시즌 기록 선택 완료')

    
    # 리스트 생성
    team = []
    era = []
    g = []
    w = []
    l = []
    sv = []
    hld = []
    wpct = []
    ip = []
    h = []
    hr = []
    bb = []
    hbp = []
    so = []
    r = []
    er = []
    whip = []
    season1 = []
            
    print('투수 팀기본기록1 크롤링 시작')
    
    for k in range(1, 11):
        try:        
            Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2)').text
            ERA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
            G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
            W = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(5)').text
            L = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
            SV = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
            HLD = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
            WPCT = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
            IP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
            H = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
            HR = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
            BB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
            HBP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
            SO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
            R = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
            ER = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(17)').text
            WHIP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(18)').text
            
            team.append(Team)
            if ERA == '-':
                era.append(float(0.00))
            else:
                era.append(float(ERA))
            g.append(int(G))
            w.append(int(W))
            l.append(int(L))
            sv.append(int(SV))
            hld.append(int(HLD))
            if WPCT == '-':
                wpct.append(int(0))
            else:
                wpct.append(float(WPCT))
            ip.append(IP)
            h.append(int(H))
            hr.append(int(HR))
            bb.append(int(BB))
            hbp.append(int(HBP))
            so.append(int(SO))
            r.append(int(R))
            er.append(int(ER))
            if WHIP == '-':
                whip.append(float(0.00))
            else:
                whip.append(float(WHIP))

        except:
            break
            print('투수 팀기본기록1 크롤링 완료')
            
        
    for s in range(len(g)):
        season1.append(Season)
            
    driver.close()
    
    IP1 = []
    
    for i in ip:
        if " " in i and "/" in i:
            ip1 = i.split(' ')[0]
            ip2 = i.split(' ')[1]
            ip3 = int(ip2.split('/')[0])/10
            ip4 = int(ip1)+float(ip3)
            IP1.append(ip4)
        elif " " not in i and "/" in i:
            ip3 = int(ip2.split('/')[0])/10
            IP1.append(ip3)
        else:
            IP1.append(float(i))
    
    dic1 = {'TEAM' : team,
            'ERA' : era,
            'G' : g,
            'W' : w,
            'L' : l,
            'SV' : sv,
            'HLD' : hld,
            'WPCT' : wpct,
            'IP' : IP1,
            'H' : h,
            'HR' : hr,
            'BB' : bb,
            'HBP' : hbp,
            'SO' : so,
            'R' : r,
            'ER' : er,
            'WHIP' : whip}

    import pandas as pd
    
    Pitcher1 = pd.DataFrame(dic1)
    
    print(f'{year}시즌 투수 팀기본기록1 데이터프레임 생성 완료')
    return Pitcher1

def Team_Pitcher_Stat_Crawler2(year):
    from selenium import webdriver
    import time
    
     # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Team/Pitcher/Basic1.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    time.sleep(1)
    print('시즌선택 완료')
    
    # 정규시즌기록 선택
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeries_ddlSeries"]/option[1]').click()
    time.sleep(1)
    print('정규시즌 기록 선택 완료')
    
    
    # 다음 기록 보기
    driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > div > div > a.next').click()
    time.sleep(1)
    
    print('정규시즌 기록2 선택 완료')
     
    # 리스트 생성
    team = []
    cg = []
    sho = []
    qs = []
    bsv = []
    tbf = []
    np = []
    avg = []
    double = []
    triple = []
    sac = []
    sf = []
    ibb = []
    wp = []
    bk = []
    
    print('투수 팀기본기록2 크롤링 시작')

    for k in range(1, 11):
        try:        
            Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2)').text
            CG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
            SHO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(5)').text
            QS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
            BSV = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
            TBF = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
            NP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
            AVG = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
            HH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
            HHH = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
            SAC = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
            SF = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(14)').text
            IBB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(15)').text
            WP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(16)').text
            BK = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(17)').text
            time.sleep(1)
          
            team.append(Team)
            cg.append(int(CG))
            sho.append(int(SHO))
            qs.append(int(QS))
            bsv.append(int(BSV))
            tbf.append(int(TBF))
            np.append(int(NP))
            if AVG == '-':
                avg.append(float(0.000))
            else:
                avg.append(float(AVG))
            double.append(int(HH))
            triple.append(int(HHH))
            sac.append(int(SAC))
            sf.append(int(SF))
            ibb.append(int(IBB))
            wp.append(int(WP))
            bk.append(int(BK))


        except:
            break
            print('투수 기본기록2 크롤링 완료')
            
    
            
    driver.close()
    
    dic1 = {'TEAM' : team,
            'SHO' : sho,
            'QS' : qs,
            'BSV' : bsv,
            'TBF' : tbf,
            'NP' : np,
            'AVG' : avg,
            '2B' : double,
            '3B' : triple,
            'SAC' : sac,
            'SF' : sf,
            'IBB' : ibb,
            'WP' : wp,
            'BK' : bk}
    
    import pandas as pd
    
    Pitcher2 = pd.DataFrame(dic1)
    
    print(f'{year}시즌 투수 기본기록2 데이터프레임 생성 완료')
    return Pitcher2

def Team_Defence_Stat_Crawler(year):
    from selenium import webdriver
    import time
        
    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Team/Defense/Basic.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    Season = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').text
    print('시즌선택 완료')
    time.sleep(1)
    ## 타자 기본기록 크롤링
    # 빈 리스트 생성
    season1 = []
    team = []
    g = []
    e = []
    pko = []
    po = []
    a = []
    dp = []
    fpct = []
    pb = []
    sb = []
    cs = []
    cs_per = []
    print('리스트 생성 완료')
    
    print('수비 팀기록 크롤링 시작')
    
    for k in range(1, 11):
        try:
            Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2)').text
            G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
            E = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
            PKO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(5)').text
            PO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
            A = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
            DP = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
            FPCT = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
            PB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(10)').text
            SB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(11)').text
            CS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(12)').text
            CS_PER = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(13)').text
            
    
            team.append(Team)
            g.append(int(G))
            e.append(int(E))
            pko.append(int(PKO))
            po.append(int(PO))
            a.append(int(A))
            dp.append(int(DP))
            if FPCT == '-':
                fpct.append(float(0.000))
            else:
                fpct.append(float(FPCT))
            pb.append(int(PB))
            sb.append(int(SB))
            cs.append(int(CS))
            
            if CS_PER == '-':
                cs_per.append(float(0.000))
            else:
                cs_per.append(float(CS_PER))
                                           
        except:
            break
        
    for s in range(len(g)):
        season1.append(Season)
        
    print(f'{year}시즌 팀수비기록 크롤링 완료')    
    
    driver.close()
    
    
    dic1 = {'SEASON' : season1,
            'TEAM' : team,
            'G' : g,
            'E' : e,
            'PKO' : pko,
            'PO' : po,
            'A' : a,
            'DP' : dp,
            'FPCT' : fpct,
            'PB' : pb,
            'SB' : sb,
            'CS' : cs,
            'CS%' : cs_per}
    
    import pandas as pd
    df = pd.DataFrame(dic1)
    
    print('수비기록 데이터프레임 생성 완료')
    return df

def Team_Running_Stat_Crawler(year):
    from selenium import webdriver
    import time
    
    # 시즌 기록 사이트 접속
    URL = 'https://www.koreabaseball.com/Record/Team/Runner/Basic.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print('기록실페이지 접속 완료')
    
    # 원하는 시즌 선택(일단은 현재시즌 선택만)
    from datetime import datetime
    today_year = datetime.now().year - year
    season = len(driver.find_elements_by_css_selector('#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option'))-today_year
    driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').click()
    Season = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlSeason_ddlSeason > option:nth-child({season})').text
    print('시즌선택 완료')
    time.sleep(1)
    
    ## 타자 기본기록 크롤링
    # 빈 리스트 생성
    season1 = []
    team = []
    g = []
    sba = []
    sb = []
    cs = []
    sb_per = []
    oob = []
    pko = []
    
    print('리스트 생성 완료')
    
    print('주루 팀기록 크롤링 시작')

    for k in range(1, 11):
        try:
            Team = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(2)').text
            G = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(3)').text
            SBA = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(4)').text
            SB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td.asc').text
            CS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(6)').text
            SB_PER = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(7)').text
            OOB = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(8)').text
            PKO = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr:nth-child({k}) > td:nth-child(9)').text
            
            team.append(Team)
            g.append(int(G))
            sba.append(int(SBA))
            sb.append(int(SB))
            cs.append(int(CS))
            if SB_PER == '-':
                sb_per.append(float(0.000))
            else:
                sb_per.append(float(SB_PER))
            oob.append(int(OOB))
            pko.append(int(PKO))

        except:
            break
        
    for s in range(len(g)):
        season1.append(Season)
        
        
    
    driver.close()
         
    print(Season+'시즌 팀주루기록 크롤링 완료')
    
    dic1 = {'TEAM' : team,
           'G' : g,
           'SBA' : sba,
           'SB' : sb,
           'CS' : cs,
           'SB%' : sb_per,
           'OOB' : oob,
           'PKO' : pko
           }
    
    import pandas as pd
    df = pd.DataFrame(dic1)
    
    print('주루기록 데이터프레임 생성 완료')
    
    return df

def entry_crawler_major():
    from selenium import webdriver
    import pandas as pd
    import time
    url1 = 'https://www.koreabaseball.com/Player/Register.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=url1)
    # driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_btnPreDate').click()
    time.sleep(2)
    #teams = ['KT','두산','삼성','LG','키움','SSG','NC','롯데','KIA','한화']
    date = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_lblGameDate').text.split('.')
    date1 = date[0]+date[1]+date[2][:-3]
    date = []
    team = []
    backno = []
    playerid = []
    pos = []
    name = []
    hand = []
    birth = []
    body = []
    for t in range(2,11):    
        try:
            for i in range(2,4):
            
                POS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child({i}) > thead > tr > th:nth-child(2)').text
                time.sleep(1)
                team_name = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div.teams > ul > li.on > a > span').text
                
                for k in range(1,20):
                    try:
                        BACKNO = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(1)').text
                        #href = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(2) > a').get_attribute('href')
                        NAME = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(2)').text
                        HAND = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(3)').text
                        BIRTH = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(4)').text
                        BODY = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(5)').text
        
                        pos.append(POS)
                        backno.append(BACKNO)
                        playerid.append(POS)
                        name.append(NAME)
                        hand.append(HAND)
                        birth.append(BIRTH)
                        body.append(BODY)
                        team.append(team_name)
                        date.append(int(date1))
                        print(f'{team_name} {POS}테이블 {k}번째 코칭스탭 크롤링 완료')
                    except:
                        break
                        time.sleep(1)
                        
            for i in range(4,8):
            
                POS = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child({i}) > thead > tr > th:nth-child(2)').text
                time.sleep(1)
                team_name = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div.teams > ul > li.on > a > span').text
                
                for k in range(1,20):
                    try:
                        BACKNO = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(1)').text
                        href = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(2) > a').get_attribute('href')
                        NAME = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(2) > a').text
                        HAND = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(3)').text
                        BIRTH = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(4)').text
                        BODY = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div:nth-child(3) > table:nth-child('+str(i)+') > tbody > tr:nth-child('+str(k)+') > td:nth-child(5)').text
                        PLAYERID = href[-5:]
                        pos.append(POS)
                        backno.append(BACKNO)
                        playerid.append(PLAYERID)
                        name.append(NAME)
                        hand.append(HAND)
                        birth.append(BIRTH)
                        body.append(BODY)
                        team.append(team_name)
                        date.append(int(date1))
                        print(f'{team_name} {POS}테이블 {k}번째 선수 크롤링 완료')
            
                    except:
                        break
                        time.sleep(1)
                    
            print(f'{team_name} 팀 등록명단 크롤링 완료')
            driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > div.teams > ul > li:nth-child({t}) > a').click()
            time.sleep(2)
        except:
            pass
            driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > div.teams > ul > li:nth-child({t}) > a').click()
            time.sleep(2)
        
    player_amount = len(playerid)
    print(f'등록선수 총 {player_amount}명 크롤링 완료')
    driver.close()
    
    birth1 = []
    
    for i in birth:
        a = str(i).split('-')[0]
        b = str(i).split('-')[1]
        c = str(i).split('-')[2]
        bir = a+b+c
        birth1.append(bir)
    
    height = []
    weight = []
    
    for i in body:
        a = str(i).split(' ')[0]
        b = str(i).split(' ')[1]
        h = a[:-3]
        w = b[:-2]
        height.append(h)
        weight.append(w)
    
    dic1 = {'RDATE' : date1,
            'TEAM' : team,
            'PLAYERID' : playerid,
            'NAME' : name,
            'BACKNO' : backno,
            'POS' : pos,
            'HAND' : hand,
            'BIRTH' : birth1,
            'HEIGHT' : height,
            'WEIGHT' : weight}
        
    df = pd.DataFrame(dic1)
    print('데이터프레임 생성완료')
    return df

def KBO_Roster_Crawler():
    from selenium import webdriver
    import time
    from selenium.webdriver.support.ui import Select

    #선수별 정보창 link 크롤링
    URL = 'https://www.koreabaseball.com/Player/Search.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    ids = []
    
    for i in range(1,11):  
        select = Select(driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_ddlTeam'))
        select.select_by_index(i)
        time.sleep(2)    
        team = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpRecord > div.inquiry > table > tbody > tr:nth-child(1) > td:nth-child(3)').text                              
        print(f'{team}선택 완료')
        
        for k in range(1,20):
            try:
                for j in range(1,21):
                    try:
                        href = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > div.inquiry > table > tbody > tr:nth-child({j}) > td:nth-child(2) > a').get_attribute('href')
                        player_id = href[-5:]
                        ids.append(player_id)
                        print(f'{team} {k}페이지 {j}번째 선수id 크롤링 완료')
                    except:
                        break
                        ids = list(dict.fromkeys(ids))
                        
                driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ucPager_btnNo{k}').click()
                time.sleep(2)
            except:
                break
    
    del href, player_id, URL
    
    # 중복값 제거
    ids = list(dict.fromkeys(ids))
    ids_len = len(ids)
    print(f'모든 팀 선수 id 총 {ids_len}개 크롤링 완료')
    del ids_len
    y = []
    group = []
    team = []
    name = []
    backno = []
    birth = []
    position = []
    # throw = []
    # batterside = []
    height =[]
    weight = []
    career = []
    down_payment = []
    salary = []
    draft = []
    year = []
    hittype = []
    active = []
    lst = [' ', '년', '월', '일']
    
    from datetime import datetime
    
    for ID in ids:
        URL2 = f'https://www.koreabaseball.com/Record/Player/HitterDetail/Basic.aspx?playerId={ID}'
        driver.get(url=URL2)
        # time.sleep(1)
        TEAM = driver.find_element_by_id("h4Team").text
        NAME = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblName').text
        BACKNO = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblBackNo').text
        BIRTH = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblBirthday').text
        for i in lst:
            BIRTH = BIRTH.replace(i, '')
        POSITION = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblPosition').text[:-6]
        HAND = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblPosition').text[-5:-1]
        # THROW = HAND[0:1]
        # BATTERSIDE = HAND[2:3]
        HW = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblHeightWeight').text
        HEIGHT = HW.split('/')[0][:-2]
        WEIGHT = HW.split('/')[1][:-2]
        CAREER = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblCareer').text
        PAYMENT = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblPayment').text
        SALARY = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblSalary').text
        DRAFT = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblDraft').text
        YEAR = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_playerProfile_lblJoinInfo').text

        y.append(datetime.today().year)
        group.append('R')
        t = TEAM.split(' ')[0]
        if t == '고양':
            team.append('키움')
        else:
            team.append(t)
        name.append(NAME)
        backno.append(BACKNO)
        birth.append(BIRTH)
        position.append(POSITION)
        # 롯데 최종은 예외처리(타격방향 잘못 등록됨)
        if ID =='51574':
            hittype.append('우투좌타')
            # batterside.append('좌')
        else:
            hittype.append(HAND)
            # batterside.append(BATTERSIDE)
        # throw.append(THROW)
        height.append(HEIGHT)
        weight.append(WEIGHT)
        career.append(CAREER)
        down_payment.append(PAYMENT)
        salary.append(SALARY)
        draft.append(DRAFT)
        year.append(YEAR)
        active.append('Y')
        print(f'{TEAM} {NAME} 정보 크롤링 완료')
    
    del ID, URL2, TEAM, NAME, BACKNO, HAND, BIRTH, POSITION, HW, HEIGHT, WEIGHT, CAREER, PAYMENT, SALARY, DRAFT, YEAR
    del j, k
    
    name_len = len(name)
    print(f'{name_len}명 정보 크롤링 완료')
    del name_len
    
    name_eng = []
    
    print('영문이름 크롤링 시작')
    for ID, i in zip(ids, range(len(ids))):
        i = i+1
        per = len(ids)
        URL3 = f'http://eng.koreabaseball.com/Teams/PlayerInfoPitcher/Summary.aspx?pcode={ID}'
        driver.get(url=URL3)
        # time.sleep(1)
        NAME = driver.find_element_by_css_selector('#contents > div.inner > div.player_info > div > ul > li:nth-child(1) > span').text
        name1 = str(NAME).split(" ")
        
        if len(name1) == 2:
            name2=""
            name_eng.append(name2)
            
        elif len(name1) == 4:
            lname= name1[2]
            fname= name1[3]
            name2= lname+", "+fname
            name_eng.append(name2)
        
        else:
            lname = name1[2]
            fname = name1[3]+" "+name1[4]
            name2 = lname+", "+fname
            name_eng.append(name2)
        print(f'{i}/{per} 영문이름 크롤링 완료')
    driver.close()       
    ikv = []
    for i, k in zip(y, ids):
        a = str(i)+'-'+str(k)
        ikv.append(a)
        
    dic = {'ikv':ikv,
           'game_year':y,
           'gameGroup':group,
           'team':team,
           'ID':ids,
           'NAME':name,
           'POS':position,
           'BackNum':backno,           
           'engName':name_eng,
           'Birthday':birth,
           'Height':height,
           'Weight':weight,
           'Career':career,
           'HitType':hittype,
           'proJoinYear':draft,
           'teamDeposit':down_payment,
           'annualIncome':salary,
           'joininfo':year,
           'active':active
           }
    
    import pandas as pd
    df = pd.DataFrame(dic)
    name = []
    
    import urllib
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup    
    
    n = df[['NAME','engName']].fillna('-')
    
    for i, j in zip(n.NAME, n.engName):
        if j == '-':
            naver_url = 'https://dict.naver.com/name-to-roman/translation/?query='
            name_url = naver_url + urllib.parse.quote(i)
            
            req = Request(name_url)
            res = urlopen(req)
            
            html = res.read().decode('utf-8')
            bs = BeautifulSoup(html, 'html.parser')
            name_tags = bs.select('#container > div > table > tbody > tr > td > a')
            names = [name_tag.text for name_tag in name_tags][0]
            name.append(names)
        else:
            name.append(j)
    name1 = []
    for i in name:
        a = i.replace(',','')
        a = a.upper()
        name1.append(a)
        
    df['engName'] = name1
    
    return df

    
def kbo_schedule_crawler_major(season=2022, sm='all', em='all'):
    # sm = 조회 시작하는 달 , em = 조회 끝나는 달
    from selenium import webdriver
    import time
    stime = time.time()
    URL = 'https://www.koreabaseball.com/Schedule/Schedule.aspx?seriesId=0,9'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    time.sleep(1)
    # sm=4
    # em=10
    months = []
    if sm == 'all':
        months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    else:
        for i in range(sm,em+1):
            months.append(str(i).zfill(2))
    s = []
    t = []
    d = []
    lvl = []
    typ = []
    at = []
    ht = []
    st = []
    etc = []
    etc1 = []
    
    from datetime import datetime
    # year = datetime.today().strftime('%Y%m%d')[0:4]
    driver.find_element_by_xpath('//*[@id="ddlYear"]').send_keys(str(season))
    
    for month in months:
        
        driver.find_element_by_xpath('//*[@id="ddlMonth"]').send_keys(month)
        time.sleep(2)
        
        for i in range(1,200):
    
            try:
                TIME = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.time > b').text.replace(':','')
                ATEAM = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.play > span:nth-child(1)').text
                HTEAM = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.play > span:nth-child(3)').text
                SCORE = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.play > em > span').text
                
                try:
                    D = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.day').text.split('.')
                    DATE = str(season)+D[0]+D[1][:-3]
                    STADIUM = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(8)').text
                    ETC = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(9)').text
    
                except:
                    STADIUM = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(7)').text
                    ETC = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(8)').text
                    DATE = d[-1]
                s.append(season)    
                d.append(DATE)
                t.append(TIME)
                lvl.append('kbo1')
                if HTEAM == '나눔' or ATEAM =='나눔':
                    typ.append('AL')
                else:
                    typ.append('R')
                at.append(ATEAM)
                ht.append(HTEAM)
                st.append(STADIUM)
                etc.append(ETC)
                
                # 시즌 시작 후 한 경기 진행되면, 경기 종료 여부 처리 예정
                if ETC == '-' and SCORE == 'vs':
        
                    etc1.append('Pre_Game')
                elif ETC == '-' and SCORE != 'vs':
                    etc1.append('Final')
                else:
                    etc1.append('Postponed')
                    
                print(f'{month}월 {i}번째 일정 크롤링 완료')
    
            except:
                break
    print('전체일정 크롤링 완료')    
    del month, months, i, TIME, ATEAM, HTEAM, D, DATE, STADIUM, ETC
    driver.close()
    del URL, driver
    
    at1 = []
    ht1 = []
    
    for i in at:
        if i == '삼성':
            at1.append('SS')
        elif i == '두산':
            at1.append('OB')
        elif i == '한화':
            at1.append('HH')
        elif i == 'KIA':
            at1.append('HT')
        elif i == '키움' or i == '넥센':
            at1.append('WO')
        elif i == 'SSG':
            at1.append('SK')
        elif i == '롯데':
            at1.append('LT')
        elif i == '나눔':
            at1.append('WE')
        elif i == '드림':
            at1.append('EA')
        else:
            at1.append(i)
            
    for i in ht:
        if i == '삼성':
            ht1.append('SS')
        elif i == '두산':
            ht1.append('OB')
        elif i == '한화':
            ht1.append('HH')
        elif i == 'KIA':
            ht1.append('HT')
        elif i == '키움' or i == '넥센':
            ht1.append('WO')
        elif i == 'SSG':
            ht1.append('SK')
        elif i == '롯데':
            ht1.append('LT')
        elif i == '나눔':
            ht1.append('WE')
        elif i == '드림':
            ht1.append('EA')
        else:
            ht1.append(i)
            
    sttm = []
    
    for i in st:
        if i == '창원':
            sttm.append('NCDinosMajors')
        elif i == '잠실':
            sttm.append('Jamsil')
        elif i == '수원':
            sttm.append('Suwon')
        elif i == '고척':
            sttm.append('Gocheok')
        elif i == '문학':
            sttm.append('Incheon')
        elif i == '대전':
            sttm.append('Daejeon')
        elif i == '대구':
            sttm.append('DaeguPark')
        elif i == '사직':
            sttm.append('Sajik')
        elif i == '광주':
            sttm.append('Gwangju')
        elif i == '마산':
            sttm.append('Masan')
        else:
            sttm.append('Undefined')
    
    del i
    
    scode = []
    for i, k  in zip(st, ht1):
        if i == '잠실' and k == 'OB':
            scode.append('JSOB')
        elif i == '잠실' and k == 'LG':
            scode.append('JSLG')
        elif i == '고척':
            scode.append('GC')
        elif i == '문학':
            scode.append('MH')
        elif i == '수원':
            scode.append('SW')
        elif i == '대전':
            scode.append('DJ')
        elif i == '청주':
            scode.append('CJ')
        elif i == '대구':
            scode.append('DG')
        elif i == '포항':
            scode.append('PH')
        elif i == '사직':
            scode.append('SJ')
        elif i == '울산':
            scode.append('US')
        elif i == '창원':
            scode.append('CH')
        elif i == '광주':
            scode.append('GJ')
        elif i == '군산':
            scode.append('GS')
        elif i == '마산':
            scode.append('MS')
        else:
            scode.append('Undefined')
    del i, k
    
    import pandas as pd

    df = pd.DataFrame()
    
    df['season'] = s
    df['gamedate']= d
    df['gametime']= t
    df['level'] = lvl
    df['gametype'] = typ
    df['awayteam']= at
    df['awayteamcode']= at1
    df['hometeam']= ht
    df['hometeamcode']= ht1
    df['stadium_kor']= st
    df['stadium_tm']= sttm
    df['scode'] = scode
    # df['gameid_kbo'] = (df['date']+df['awayteamcode']+df['hometeamcode']+str(0))
    # df['gameid_tm'] = df['date']+'-'+df['stadium_tm']+'-1'
    df['kv0'] = (df['gamedate']+df['awayteamcode']+df['hometeamcode']+df['gametime'])
    df['kv1'] = (df['gamedate']+df['awayteamcode']+df['hometeamcode'])
    df['memo'] = etc
    df['status'] = etc1
    
    # 더블헤더 예외처리
    df1 = df.sort_values(by=['kv0'], axis=0).reset_index(drop=True)
    kv1 = df1.kv1.to_list()
    dhv = []
    dhv1 = []
    for i in range(len(kv1)):
        if i == 0:
            dhv.append(0)
        elif i > 0:
            if kv1[i] == kv1[i-1]:
                dhv[i-1] = 1
                dhv.append(2)
            else:
                dhv.append(0)
    df1['dh_value'] = dhv
    
    for i in dhv:
        if i == 0:
            dhv1.append(1)
        else:
            dhv1.append(i)
    df1['dh_value_tm'] = dhv1
    
    
    gameid_k = []
    gameid_t = []
    
    for i in range(len(df1)):
        gameid_k.append(df1['kv1'][i]+str(df1['dh_value'][i]))
        gameid_t.append(df1.gamedate[i]+'-'+df1['stadium_tm'][i]+'-'+str(df1['dh_value_tm'][i]))
    
    del i
    df1['gameid_kbo']=gameid_k
    df1['gameid_tm']=gameid_t
    df1['inputtime'] = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    df1['gameid_spo']=gameid_k
    del d, df, dhv, dhv1, etc, gameid_k, gameid_t, ht, ht1, at, at1, kv1, scode, sttm, t
    etime = time.time()
    
    print(f'소요시간: {etime-stime: .3f}초 소요')
    df1.to_csv(f'./result/{season}_kbo_schedule_major.csv', index=False, encoding='ANSI')
    return df1

def kbo_gamecenter_crawler():
    from selenium import webdriver
    import time
    
    URL = 'https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    time.sleep(1)
    
    st = [] #구장
    at = [] #원정팀
    ht = [] #홈팀
    ap = [] #원정투수
    hp = [] #홈투수
    se = [] #n차전
    bc = [] #방송중계
    dt = driver.find_element_by_css_selector('#lblGameDate').text
    date = dt.split('.')[0]+dt.split('.')[1]+dt.split('.')[2][:-3]
    for i in range(1,7):
        try:
            stadium = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({i}) > div > div.tit-area > h4 > span.place').text
            awayteam = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({i}) > div > div.game-cont > div.team.away > div > img').get_attribute('alt')
            hometeam = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({i}) > div > div.game-cont > div.team.home > div > img').get_attribute('alt')
            awaypit = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({i}) > div > div.game-cont > div.team.away > span.today-pitcher > span').text.split(':')[1]
            homepit = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({i}) > div > div.game-cont > div.team.home > span.today-pitcher > span').text.split(':')[1]
            temp = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({i}) > div > div.game-cont > div.broadcasting').text
            series = temp.split(' ')[0]
            broadcast = temp.split(' ')[-1]
            
            st.append(stadium)
            at.append(awayteam)
            ht.append(hometeam)
            ap.append(awaypit)
            hp.append(homepit)
            se.append(series)
            bc.append(broadcast)
            print(str(i)+'번째 경기 정보 크롤링 완료')
    
        except:
            try:
                driver.find_element_by_css_selector('#contents > div.today-game > div > div.bx-controls.bx-has-controls-direction > div > a.bx-next').click()
                time.sleep(1)
                for k in range(6,12):
                    
                        stadium = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({k}) > div > div.tit-area > h4 > span.place').text
                        awayteam = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({k}) > div > div.game-cont > div.team.away > div > img').get_attribute('alt')
                        hometeam = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({k}) > div > div.game-cont > div.team.home > div > img').get_attribute('alt')
                        awaypit = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({k}) > div > div.game-cont > div.team.away > span.today-pitcher > span').text.split(':')[1]
                        homepit = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({k}) > div > div.game-cont > div.team.home > span.today-pitcher > span').text.split(':')[1]
                        temp = driver.find_element_by_css_selector(f'#contents > div.today-game > div > div.bx-viewport > ul > li:nth-child({k}) > div > div.game-cont > div.broadcasting').text
                        series = temp.split(' ')[0]
                        broadcast = temp.split(' ')[-1]
                        
                        st.append(stadium)
                        at.append(awayteam)
                        ht.append(hometeam)
                        ap.append(awaypit)
                        hp.append(homepit)
                        se.append(series)
                        bc.append(broadcast)
                        print(str(k)+'번째 경기 정보 크롤링 완료')
            except:
                break
                del k
                             
    del stadium, awayteam, hometeam, awaypit, homepit, series, broadcast, i, temp, URL    
    driver.close()
    
    import pandas as pd
    
    df = pd.DataFrame()
    
    df['구장'] = st
    df['원정팀'] = at
    df['원정팀선발투수'] = ap
    df['홈팀'] = ht
    df['홈팀선발투수'] = hp
    df['시리즈'] = se
    df['방송중계'] = bc
    df.insert(0,'날짜', date)
    
    df.to_csv(f"./result/{date}_gamelist.csv", index=False, encoding='ANSI')
    
    del st, at, ap, ht, hp, se, bc
    return df

def kbo_trade_crawler(year=2022):
    from selenium import webdriver
    import time
    
    URL = 'https://www.koreabaseball.com/Player/Trade.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    time.sleep(1)
    
    driver.find_element_by_css_selector('#selYear').send_keys(year)
    driver.find_element_by_css_selector('#btnSearch').click()
    time.sleep(1)
    
    d=[]
    v=[]
    t=[]
    p=[]
    e=[]
    
    for k in range(1,40):
        try:
            for i in range(1,21):
    
                try:
                    D = driver.find_element_by_css_selector(f'#tblTradeList > tbody > tr:nth-child({i}) > td:nth-child(1)').text.replace('-','')
                    V = driver.find_element_by_css_selector(f'#tblTradeList > tbody > tr:nth-child({i}) > td:nth-child(2)').text
                    T = driver.find_element_by_css_selector(f'#tblTradeList > tbody > tr:nth-child({i}) > td:nth-child(3)').text
                    P = driver.find_element_by_css_selector(f'#tblTradeList > tbody > tr:nth-child({i}) > td:nth-child(4)').text
                    E = driver.find_element_by_css_selector(f'#tblTradeList > tbody > tr:nth-child({i}) > td:nth-child(5)').text
                    
                    d.append(D)
                    v.append(V)
                    t.append(T)
                    p.append(P)
                    e.append(E)
                    
                except:
                    break
                    
            driver.find_element_by_css_selector('#contents > div.sub-content > div.paging > a.pg_next').click()
            time.sleep(1)
        except:
            break
        
    driver.close()
    
    import pandas as pd
    
    df = pd.DataFrame()
    df['date'] = d
    df['contents'] = v
    df['team'] = t
    df['player'] = p
    df['etc'] = e
    df['kv'] = df['date'].astype(str)+'_'+df['contents']+'_'+df['player']
    df1 = df.drop_duplicates(subset=['kv'])
    
    df1 = df1[['date', 'contents', 'team', 'player', 'etc']]
    from datetime import datetime
    df1['upload_date'] = datetime.today().strftime('%Y%m%d')
    
    df1.to_csv(f"./result/{year}_trade_{datetime.today().strftime('%Y%m%d')}.csv", encoding='ANSI', index=False)
    
    return df1

def kbo_schedule_crawler_minor(season=2022, sm='all', em='all'):
   
    from selenium import webdriver
    import time
    # stime = time.time()
    URL = 'https://www.koreabaseball.com/Futures/Schedule/GameList.aspx'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    time.sleep(1)
    # sm=4
    # em=10
    
    if sm == 'all' and em == 'all':
        months = ['1','2','3','4','5','6','7','8','9','10','11','12']
    
    elif sm != 'all' and em == 'all':
        months = list(range(sm, 13))
    
    elif sm == 'all' and em != 'all':
        months = list(range(1, em+1))
    
    else:
        months = list(range(sm, em+1))
    
    s = []
    t = []
    d = []
    lvl = []
    typ = []
    at = []
    ht = []
    st = []
    etc = []
    etc1 = []
    #cphContents_cphContents_cphContents_ddlMonth
    #cphContents_cphContents_cphContents_ddlMonth > option:nth-child(1)
    # from datetime import datetime
    
    # year = datetime.today().strftime('%Y%m%d')[0:4]
    driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlYear"]').send_keys(str(season)+'년')
    time.sleep(1)
    
    for month in months:
        
        driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_ddlMonth > option:nth-child({month})').click()
        
        time.sleep(1)
        
        for i in range(1,200):
            try:
    
                TIME = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > table > tbody > tr:nth-child({i}) > td.time').text.replace(':','')
                ATEAM = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > table > tbody > tr:nth-child({i}) > td.play > span:nth-child(1)').text
                HTEAM = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > table > tbody > tr:nth-child({i}) > td.play > span:nth-child(3)').text
                STADIUM = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > table > tbody > tr:nth-child({i}) > td.ballpark').text
                # a = i-1
                ETC = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > table > tbody > tr:nth-child({i}) > td.etc').text
                SCORE = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_udpRecord > table > tbody > tr:nth-child({i}) > td.play > em').text
                try:
                    D = driver.find_element_by_css_selector(f'#cphContents_cphContents_cphContents_rptGameList_lblGameDate_{i-1}').text.split('.')
                    DATE = str(season)+D[0]+D[1][:-3]
    
                
                except:
                    # STADIUM = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(7)').text
                    # ETC = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(8)').text
                    DATE = d[-1]
                s.append(season)
                lvl.append('kbo2')
                typ.append('R')
                d.append(DATE)
                t.append(TIME)
                at.append(ATEAM)
                ht.append(HTEAM)
                st.append(STADIUM)
                etc.append(ETC)
                
                # 시즌 시작 후 한 경기 진행되면, 경기 종료 여부 처리 예정
                if ETC == '-' and SCORE == 'vs':
                    etc1.append('Pre_Game')
                elif ETC =='-' and SCORE != 'vs':
                    etc1.append('Final')
                elif ETC == '교류':
                    etc1.append('Final')
                else:
                    etc1.append('Postponed')
                print(f'{month}월 {i}번째 일정 크롤링 완료')
    
            except:
                break
    
    print('전체일정 크롤링 완료')    
    del month, i, TIME, ATEAM, HTEAM, D, DATE, STADIUM, ETC
    driver.close()
    del URL, driver
    
    at1 = []
    ht1 = []
    if season == 2018:      
        for i in at:
            if i == '삼성':
                at1.append('SS')
            elif i == '두산':
                at1.append('OB')
            elif i == '한화':
                at1.append('HH')
            elif i == 'KIA':
                at1.append('HT')
            elif i == '고양':
                at1.append('NC')
            elif i == '화성':
                at1.append('WO')
            elif i == 'SSG':
                at1.append('SK')
            elif i == '롯데':
                at1.append('LT')
            elif i == '상무':
                at1.append('SM')
            elif i == '경찰':
                at1.append('PL')
            else:
                at1.append(i)
          
        for i in ht:
            if i == '삼성':
                ht1.append('SS')
            elif i == '두산':
                ht1.append('OB')
            elif i == '한화':
                ht1.append('HH')
            elif i == 'KIA':
                ht1.append('HT')
            elif i == '고양':
                ht1.append('NC')
            elif i == '화성':
                ht1.append('WO')
            elif i == 'SSG':
                ht1.append('SK')
            elif i == '롯데':
                ht1.append('LT')
            elif i == '상무':
                ht1.append('SM')
            elif i == '경찰':
                ht1.append('PL')
            else:
                ht1.append(i)
    else:
        for i in at:
            if i == '삼성':
                at1.append('SS')
            elif i == '두산':
                at1.append('OB')
            elif i == '한화':
                at1.append('HH')
            elif i == 'KIA':
                at1.append('HT')
            elif i == '고양':
                at1.append('WO')
            elif i == 'SSG':
                at1.append('SK')
            elif i == '롯데':
                at1.append('LT')
            elif i == '상무':
                at1.append('SM')
            elif i == '경찰':
                at1.append('PL')                
            else:
                at1.append(i)
          
        for i in ht:
            if i == '삼성':
                ht1.append('SS')
            elif i == '두산':
                ht1.append('OB')
            elif i == '한화':
                ht1.append('HH')
            elif i == 'KIA':
                ht1.append('HT')
            elif i == '고양':
                ht1.append('WO')
            elif i == 'SSG':
                ht1.append('SK')
            elif i == '롯데':
                ht1.append('LT')
            elif i == '상무':
                ht1.append('SM')
            elif i == '경찰':
                ht1.append('PL')                  
            else:
                ht1.append(i)
            
    sttm = []
    
    for i in st:
        if i == '창원':
            sttm.append('NCDinosMajors')
        elif i == '잠실':
            sttm.append('Jamsil')
        elif i == '수원':
            sttm.append('Suwon')
        elif i == '고척':
            sttm.append('Gocheok')
        elif i == '문학':
            sttm.append('Incheon')
        elif i == '대전':
            sttm.append('Daejeon')
        elif i == '대구':
            sttm.append('DaeguPark')
        elif i == '사직':
            sttm.append('Sajik')
        elif i == '광주':
            sttm.append('Gwangju')
        elif i == '이천(두산)':
            sttm.append('DoosanMinors')
        elif i == '이천(LG)':
            sttm.append('LGMinor')
        elif i == '강화':
            sttm.append('SKFuturesPark')
        elif i == '익산':
            sttm.append('IksanStadium')
        elif i == '서산':
            sttm.append('HanwhaMinors')
        elif i == '경산':
            sttm.append('SamsungMinor')
        elif i == '상동':
            sttm.append('Gimhae')
        elif i == '마산':
            sttm.append('Masan')
        else:
            sttm.append('Undefined')
    
    del i
    
    scode = []
    for i, k  in zip(st, ht1):
        if i == '잠실' and k == 'OB':
            scode.append('JSOB')
        elif i == '잠실' and k == 'LG':
            scode.append('JSLG')
        elif i == '고척':
            scode.append('GC')
        elif i == '문학':
            scode.append('MH')
        elif i == '수원':
            scode.append('SW')
        elif i == '대전':
            scode.append('DJ')
        elif i == '청주':
            scode.append('CJ')
        elif i == '대구':
            scode.append('DG')
        elif i == '포항':
            scode.append('PH')
        elif i == '사직':
            scode.append('SJ')
        elif i == '울산':
            scode.append('US')
        elif i == '창원':
            scode.append('CH')
        elif i == '광주':
            scode.append('GJ')
        elif i == '군산':
            scode.append('GS')
        elif i == '이천(두산)':
            scode.append('ID')
        elif i == '이천(LG)':
            scode.append('IL')
        elif i == '강화':
            scode.append('GW')
        elif i == '고양':
            scode.append('GY')
        elif i == '익산':
            scode.append('IS')
        elif i == '서산':
            scode.append('SS')
        elif i == '경산':
            scode.append('GB')
        elif i == '함평':
            scode.append('HP')
        elif i == '마산':
            scode.append('MS')
        elif i == '상동':
            scode.append('GH')
        elif i == '춘천':
            scode.append('CC')
        elif i == '문경':    
            scode.append('MG')
        else:
            scode.append('Undefined')
    del i, k
    
    import pandas as pd
    
    df = pd.DataFrame()
    
    df['season'] = s
    df['gamedate']= d
    df['gametime']= t
    df['level'] = lvl
    df['gametype'] = typ
    df['awayteam']= at
    df['awayteamcode']= at1
    df['hometeam']= ht
    df['hometeamcode']= ht1
    df['stadium_kor']= st
    df['stadium_tm']= sttm
    df['scode'] = scode
    # df['gameid_kbo'] = (df['date']+df['awayteamcode']+df['hometeamcode']+str(0))
    # df['gameid_tm'] = df['date']+'-'+df['stadium_tm']+'-1'
    df['kv0'] = (df['gamedate']+df['awayteamcode']+df['hometeamcode']+df['gametime'])
    df['kv1'] = (df['gamedate']+df['awayteamcode']+df['hometeamcode'])
    df['memo'] = etc
    df['status'] = etc1
    # df['gameid_tm'] = df['date']+'-'+df['stadium_tm']+'-'
    
    # 더블헤더 예외처리
    df1 = df.sort_values(by=['kv0'], axis=0).reset_index(drop=True)
    kv1 = df1.kv1.to_list()
    dhv = []
    dhv1 = []
    for i in range(len(kv1)):
        if i == 0:
            dhv.append(5)
        elif i > 0:
            if kv1[i] == kv1[i-1]:
                dhv[i-1] = 5
                dhv.append(6)
            else:
                dhv.append(5)
    df1['dh_value'] = dhv
    
    for i in dhv:
        if i == 5:
            dhv1.append(1)
        else:
            dhv1.append(2)
    df1['dh_value_tm'] = dhv1
    
    
    gameid_k = []
    gameid_t = []
    
    for i in range(len(df1)):
        gameid_k.append(df1['kv1'][i]+str(df1['dh_value'][i]))
        
        if df1['stadium_tm'][i] != 'Undefined':
            gameid_t.append(df1.gamedate[i]+'-'+df1['stadium_tm'][i]+'-'+str(df1['dh_value_tm'][i]))
        else:
            gameid_t.append('Undefined')
    
    del i
    df1['gameid_kbo']=gameid_k
    df1['gameid_tm']=gameid_t
    
    from datetime import datetime
    df1['inputtime'] = str(datetime.today().strftime('%Y-%m-%d %T.%f'))
    
    df1.to_csv(f'./result/{season}_kbo_schedule_minor.csv', encoding='ANSI', index=False)
    return df1

# season = 2022
def kbo_schedule_crawler_sibeom(season=2022):
    # sm = 조회 시작하는 달 , em = 조회 끝나는 달
    from selenium import webdriver
    import time
    stime = time.time()
    URL = 'https://www.koreabaseball.com/Schedule/Schedule.aspx?seriesId=1'
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    time.sleep(1)

    s = []
    t = []
    d = []
    lvl = []
    typ = []
    at = []
    ht = []
    st = []
    etc = []
    etc1 = []
    
    from datetime import datetime
    # year = datetime.today().strftime('%Y%m%d')[0:4]
    driver.find_element_by_xpath('//*[@id="ddlYear"]').send_keys(str(season))    
    time.sleep(2)
        
    for i in range(1,200):

        try:
            TIME = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.time > b').text.replace(':','')
            ATEAM = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.play > span:nth-child(1)').text
            HTEAM = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.play > span:nth-child(3)').text
            SCORE = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.play > em > span').text
            
            try:
                D = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td.day').text.split('.')
                DATE = str(season)+D[0]+D[1][:-3]
                STADIUM = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(8)').text
                ETC = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(9)').text

            except:
                STADIUM = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(7)').text
                ETC = driver.find_element_by_css_selector(f'#tblSchedule > tbody > tr:nth-child({i}) > td:nth-child(8)').text
                DATE = d[-1]
            s.append(season)    
            d.append(DATE)
            t.append(TIME)
            lvl.append('kbo1')
            if HTEAM == '나눔' or ATEAM =='나눔':
                typ.append('AL')
            else:
                typ.append('S')
            at.append(ATEAM)
            ht.append(HTEAM)
            st.append(STADIUM)
            etc.append(ETC)
            
            # 시즌 시작 후 한 경기 진행되면, 경기 종료 여부 처리 예정
            if ETC == '-' and SCORE == 'vs':
    
                etc1.append('Pre_Game')
            elif ETC == '-' and SCORE != 'vs':
                etc1.append('Final')
            else:
                etc1.append('Postponed')
                
            print(f'{i}번째 일정 크롤링 완료')

        except:
            break
    print('전체일정 크롤링 완료')    
    del i, TIME, ATEAM, HTEAM, D, DATE, STADIUM, ETC
    driver.close()
    del URL, driver
    
    at1 = []
    ht1 = []
    
    for i in at:
        if i == '삼성':
            at1.append('SS')
        elif i == '두산':
            at1.append('OB')
        elif i == '한화':
            at1.append('HH')
        elif i == 'KIA':
            at1.append('HT')
        elif i == '키움' or i == '넥센':
            at1.append('WO')
        elif i == 'SSG':
            at1.append('SK')
        elif i == '롯데':
            at1.append('LT')
        elif i == '나눔':
            at1.append('WE')
        elif i == '드림':
            at1.append('EA')
        else:
            at1.append(i)
            
    for i in ht:
        if i == '삼성':
            ht1.append('SS')
        elif i == '두산':
            ht1.append('OB')
        elif i == '한화':
            ht1.append('HH')
        elif i == 'KIA':
            ht1.append('HT')
        elif i == '키움' or i == '넥센':
            ht1.append('WO')
        elif i == 'SSG':
            ht1.append('SK')
        elif i == '롯데':
            ht1.append('LT')
        elif i == '나눔':
            ht1.append('WE')
        elif i == '드림':
            ht1.append('EA')
        else:
            ht1.append(i)
            
    sttm = []
    
    for i in st:
        if i == '창원':
            sttm.append('NCDinosMajors')
        elif i == '잠실':
            sttm.append('Jamsil')
        elif i == '수원':
            sttm.append('Suwon')
        elif i == '고척':
            sttm.append('Gocheok')
        elif i == '문학':
            sttm.append('Incheon')
        elif i == '대전':
            sttm.append('Daejeon')
        elif i == '대구':
            sttm.append('DaeguPark')
        elif i == '사직':
            sttm.append('Sajik')
        elif i == '광주':
            sttm.append('Gwangju')
        elif i == '이천(두산)':
            sttm.append('DoosanMinors')
        elif i == '이천(LG)':
            sttm.append('LGMinor')
        elif i == '강화':
            sttm.append('SKFuturesPark')
        elif i == '익산':
            sttm.append('IksanStadium')
        elif i == '서산':
            sttm.append('HanwhaMinors')
        elif i == '경산':
            sttm.append('SamsungMinor')
        elif i == '상동':
            sttm.append('Gimhae')
        elif i == '마산':
            sttm.append('Masan')
        else:
            sttm.append('Undefined')
    
    del i
    
    scode = []
    for i, k  in zip(st, ht1):
        if i == '잠실' and k == 'OB':
            scode.append('JSOB')
        elif i == '잠실' and k == 'LG':
            scode.append('JSLG')
        elif i == '고척':
            scode.append('GC')
        elif i == '문학':
            scode.append('MH')
        elif i == '수원':
            scode.append('SW')
        elif i == '대전':
            scode.append('DJ')
        elif i == '청주':
            scode.append('CJ')
        elif i == '대구':
            scode.append('DG')
        elif i == '포항':
            scode.append('PH')
        elif i == '사직':
            scode.append('SJ')
        elif i == '울산':
            scode.append('US')
        elif i == '창원':
            scode.append('CH')
        elif i == '광주':
            scode.append('GJ')
        elif i == '군산':
            scode.append('GS')
        elif i == '이천(두산)':
            scode.append('ID')
        elif i == '이천(LG)':
            scode.append('IL')
        elif i == '강화':
            scode.append('GW')
        elif i == '고양':
            scode.append('GY')
        elif i == '익산':
            scode.append('IS')
        elif i == '서산':
            scode.append('SS')
        elif i == '경산':
            scode.append('GB')
        elif i == '함평':
            scode.append('HP')
        elif i == '마산':
            scode.append('MS')
        elif i == '상동':
            scode.append('GH')
        elif i == '춘천':
            scode.append('CC')
        elif i == '문경':    
            scode.append('MG')
        else:
            scode.append('Undefined')
    del i, k
    
    import pandas as pd

    df = pd.DataFrame()
    
    df['season'] = s
    df['gamedate']= d
    df['gametime']= t
    df['level'] = lvl
    df['gametype'] = typ
    df['awayteam']= at
    df['awayteamcode']= at1
    df['hometeam']= ht
    df['hometeamcode']= ht1
    df['stadium_kor']= st
    df['stadium_tm']= sttm
    df['scode'] = scode
    # df['gameid_kbo'] = (df['date']+df['awayteamcode']+df['hometeamcode']+str(0))
    # df['gameid_tm'] = df['date']+'-'+df['stadium_tm']+'-1'
    df['kv0'] = (df['gamedate']+df['awayteamcode']+df['hometeamcode']+df['gametime'])
    df['kv1'] = (df['gamedate']+df['awayteamcode']+df['hometeamcode'])
    df['memo'] = etc
    df['status'] = etc1
    
    # 더블헤더 예외처리
    df1 = df.sort_values(by=['kv0'], axis=0).reset_index(drop=True)
    kv1 = df1.kv1.to_list()
    dhv = []
    dhv1 = []
    for i in range(len(kv1)):
        if i == 0:
            dhv.append(0)
        elif i > 0:
            if kv1[i] == kv1[i-1]:
                dhv[i-1] = 1
                dhv.append(2)
            else:
                dhv.append(0)
    df1['dh_value'] = dhv
    
    for i in dhv:
        if i == 0:
            dhv1.append(1)
        else:
            dhv1.append(i)
    df1['dh_value_tm'] = dhv1
    
    
    gameid_k = []
    gameid_t = []
    
    for i in range(len(df1)):
        gameid_k.append(df1['kv1'][i]+str(df1['dh_value'][i]))
        gameid_t.append(df1.gamedate[i]+'-'+df1['stadium_tm'][i]+'-'+str(df1['dh_value_tm'][i]))
    
    del i
    df1['gameid_kbo']=gameid_k
    df1['gameid_tm']=gameid_t
    df1['inputtime'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    df1['gameid_spo'] = gameid_k   
    df1['league'] = 'kbo'
    del d, df, dhv, dhv1, etc, gameid_k, gameid_t, ht, ht1, at, at1, kv1, scode, sttm, t
    etime = time.time()


    print(f'소요시간: {etime-stime: .3f}초 소요')
    df1.to_csv(f'./result/{season}_kbo_schedule_sibeom.csv', index=False, encoding='ANSI')
    
    return df1