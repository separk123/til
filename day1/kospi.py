#0 https://finance.naver.com/sise/ 에 요청해 응답 받아오기
import requests
import bs4

url = "https://finance.naver.com/sise/"
response = requests.get(url)
# print(response.text)

html = bs4.BeautifulSoup(response.text, "html.parser")
# print(html)

kospi = html.select_one("#KOSPI_now")
#span 태그 빼고 안에 있는 텍스트만 갖고 오고 싶을 때
print(kospi.text)
