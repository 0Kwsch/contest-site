import requests
from bs4 import BeautifulSoup
import json

url = "https://www.wevity.com/?c=find&s=1&gub=1"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".tit")
hosts = soup.select(".organ")

# 🔥 날짜 선택자 수정 (핵심)
dates = soup.select(".dday")

print("디버깅:", len(titles), len(hosts), len(dates))

contest_list = []

min_len = min(len(titles), len(hosts), len(dates))

for i in range(min_len):
    contest = {
        "title": titles[i].get_text(strip=True),
        "host": hosts[i].get_text(strip=True),
        "date": dates[i].get_text(strip=True)
    }
    contest_list.append(contest)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(contest_list, f, ensure_ascii=False, indent=4)

print(f" {len(contest_list)}개 크롤링 완료!")
