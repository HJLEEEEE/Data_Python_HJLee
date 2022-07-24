# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:52:58 2022

Savant Data Downloader by Day

@author: Hojoong Lee
"""
def savant_downloader(first_day = '2022-04-07'):
    from datetime import date, timedelta
    import pandas as pd
    import random
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    import warnings
    import os
    # import shutil
    
    # warning 메세지 제거
    warnings.filterwarnings("ignore")    
    
    # 일자 리스트 생성
    today = date.today()
    last_day = today - timedelta(2)
    last_day = last_day.strftime('%Y-%m-%d')
    days = pd.date_range(start=first_day,end=last_day) 
    days1 = []
    
    # 날짜 리스트 텍스트 형식으로 변환 및 리스트 추가
    for i in days:
        i0 = str(i)
        i1 = i0.split(' ')[0]
        days1.append(i1)
        
    del i, i0, i1, days
    
    # 크롬드라이버 옵션 설정
    op = Options()

    # 다운로드 경로 설정
    op.add_experimental_option('prefs',{'download.default_directory':r'C:\Users\dlghw\Desktop\python_study\savant_convert\data'})
    
    # 크롬 드라이버 표시되지 않게 설정
    op.add_argument("headless")
    
    # 날짜별 데이터 다운로드
    try:
        for i in days1:
            try:
                # URL 접속
                driver = webdriver.Chrome(executable_path='chromedriver', options=op)
                URL = 'https://baseballsavant.mlb.com/statcast_search'
                driver.get(url=URL)
                time.sleep(random.uniform(0.5,2))
            
                # 시작 날짜 입력
                driver.find_element_by_css_selector('#game_date_gt').send_keys(i)
                time.sleep(random.uniform(0.5,2))
                
                # 끝 날짜 입력
                driver.find_element_by_css_selector('#game_date_lt').send_keys(i)
                time.sleep(random.uniform(0.5,2))
                
                # search 버튼 클릭
                driver.find_element_by_css_selector('#pfx_form > div.row.search-buttons > div > input.btn.btn-default.btn-search-green').click()
                time.sleep(random.uniform(2,4))
                
                # 데이터 다운로드 버튼 클릭
                driver.find_element_by_css_selector('#csv_all_pid_').click()
                time.sleep(random.uniform(2,4))
                
                print(f'{i} 데이터 다운로드 완료')
                driver.close()
                
                # 파일명 변경
                try:
                    file_oldname = os.path.join('./data', 'savant_data.csv')
                    date = i.replace('-','')
                    file_newname = os.path.join('./data', f'savant_data_{date}.csv')
                    try:
                        os.rename(file_oldname, file_newname)
                        print(f'{i} 데이터 파일명 변경 완료')
                    except:
                        os.remove(f'./data/savant_data_{date}.csv')
                        print('중복 데이터 제거 완료')
                        os.rename(file_oldname, file_newname)
                        print(f'{i} 데이터 파일명 변경 완료')                        
                except:
                    try:
                        time.sleep(5)
                        file_oldname = os.path.join('./data', 'savant_data.csv')
                        date = i.replace('-','')
                        file_newname = os.path.join('./data', f'savant_data_{date}.csv')
                        try:
                            os.rename(file_oldname, file_newname)
                            print(f'{i} 데이터 파일명 변경 완료')
                        except:
                            os.remove(f'./data/savant_data_{date}.csv')
                            print('중복 데이터 제거 완료')
                            os.rename(file_oldname, file_newname)
                            print(f'{i} 데이터 파일명 변경 완료')
                        
                    except Exception as e:
                        print(f'{i} 데이터 다운로드 중 에러발생 \n 에러내용:', e)
                        break
                        
            # 에러 발생시 에러메세지 표시 후 작업 중지
            
            except Exception as e:
                print(f'{i} 데이터 다운로드 중 에러발생 \n 에러내용:', e)
                break
        

    except:
        print(f'{i} 데이터 및 이후 다운로드 실패')
        
    del i
    
savant_downloader(first_day='2022-07-22')