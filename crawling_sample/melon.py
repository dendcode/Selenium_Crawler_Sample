from selenium import webdriver
import time
import csv
chromedriver = 'C:\dev_python\Webdriver\chromedriver.exe'

print('-------------------------------------')
print(' 멜론 차트 크롤러 ')
print('-------------------------------------')


# 1. 브라우저 셋팅 함수
def open_browser():
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(10) # seconds
    driver.get("https://www.melon.com/chart/index.htm")
    print("+" * 100)
    print(driver.title)   # 크롤링한 페이지의 title 정보
    print(driver.current_url)  # 현재 크롤링된 페이지의 url
    print("-" * 100)
    return driver # 함수가 끝나며 이 함수는 driver 객체를 리턴하는 함수다


# 2. 크롤링 함수
def melon_crawling(driver):
    
    rank = 1 # 랭킹순서 초기화
    html = driver # html 결과 변수에 driver 저장
    melonRank = [] # 멜론 차트 랭킹 배열 생성

    # 정보 추출
    a1 = html.find_elements_by_css_selector(".rank01") # 노래제목 셀레늄객채 추출
    a2 = html.find_elements_by_css_selector(".rank02") # 가수 이름 셀레늄객채 추출
    a3 = html.find_elements_by_css_selector(".rank03") # 앨범 이름 셀레늄객채 추출

    # for i in a1:
    #     meloneRank[0].append(i.text)

    # for i in a2:
    #     meloneRank[1].append(i.text)

    # for i in a3:
    #     meloneRank[2].append(i.text)

    for songName, artistName, albumName in zip(a1, a2, a3):
        melonRank.append([rank, songName.text, artistName.text, albumName.text]) # 멜론 차트 랭킹 리스트에 추가
        print(f'No :{rank} SONG :{songName.text} ARTIST :{artistName.text} ALBUM :{albumName.text}') # 콘솔 출력으로 확인
        rank += 1 # 랭킹 순서 증가
        
    return save_excel(melonRank) # 함수가 끝나며 이 함수는 3번 [엑셀저장 함수]를 실행 시키면서 3번 함수 실행에 필수요소인 melonRank 데이터를 인자로 넣어서 실행시킨다.


# 3. 엑셀로 저장하는 함수
def save_excel(melonRank):
    with open('melon_chart.csv', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['순위', '곡명', '가수', '앨범'])
        for row in melonRank:
            wr.writerow(row)


# 정의
driver = open_browser() # 1번 실행
result = melon_crawling(driver) # 2번 실행