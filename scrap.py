# reuqests 모듈 import
import requests

# bs4 모듈 import
import bs4

# 외부 파일 불러오기
import export_module

# 뉴스 저장 객체
news = {}

# crawling 하고자하는 url 지정
crawling_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EA%B8%88%EC%98%A4%EA%B3%B5%EA%B3%BC%EB%8C%80%ED%95%99%EA%B5%90&oquery=%EA%B8%88%EC%98%A4%EA%B3%B5%EA%B3%BC%EB%8C%80%ED%95%99%EA%B5%90&tqi=hXyBYwp0JywssC7KGosssssstFR-185396&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1"

# requests의 get함수로 받은 서버의 응답 값을 변수에 저장
response = requests.get(crawling_url)

# 전달받은 응답 값을 bs4 라이브러리를 통해 html로 파싱하기
result_html = bs4.BeautifulSoup(response.text,'html.parser')

# HTML 원하는 요소 찾기 (반환 : 여러가지)
contents_title = result_html.find_all("a",{"class":"news_tit"})
contents_company = result_html.find_all("a",{"class":"info press"})
contents_date = result_html.find_all("span",{"class":"info"})

# 원하는 정보 딕셔너리로 추가하기
for content in range(0,10):
    # 기사 제목에 금오공대 포함된 것만 가져오기
    if "금오공대" in contents_title[content]["title"]:
        news[str(content)] = {} 
        
        # 날짜 포맷팅
        date = export_module.date_formatting(contents_date[content].get_text())
        news[str(content)]["date"]= date
        news[str(content)]["company"] = contents_company[content].get_text()
        news[str(content)]["title"] = contents_title[content]["title"]

for new in news:
    print(news[new])