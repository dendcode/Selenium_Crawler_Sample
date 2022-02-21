from selenium import webdriver

# selenium에서 사용할 웹 드라이버 절대 경로 정보
chromedriver = 'C:\dev_python\Webdriver\chromedriver.exe'
# selenum의 webdriver에 앞서 설치한 chromedirver를 연동한다.
driver = webdriver.Chrome(chromedriver)
# driver로 특정 페이지를 크롤링한다.
driver.implicitly_wait(10) # seconds
driver.get('https://www.melon.com/search/total/index.htm?q=%EB%B9%84%EC%98%A4')

print("+" * 100)
print(driver.title)   # 크롤링한 페이지의 title 정보
print(driver.current_url)  # 현재 크롤링된 페이지의 url
print("-" * 100)



# TestElement = driver.find_elements_by_css_selector(
#     " .text > a ")

TestElement = driver.find_elements_by_css_selector(".fc_gray")

# print(TestElement)

print("+" * 100)

for TestElement in TestElement:
    print(TestElement.text)