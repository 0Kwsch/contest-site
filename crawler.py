import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://www.wevity.com/?c=find&s=1&gub=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Referer": "https://www.wevity.com/"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".tit a")
hosts = soup.select(".organ")
dates = soup.select(".day")

print("디버깅:", len(titles), len(hosts), len(dates))

contest_list = []
min_len = min(len(titles), len(hosts), len(dates))

for i in range(min_len):
    contest = {
        "title": titles[i].get_text(strip=True),
        "host": hosts[i].get_text(strip=True),
        "date": dates[i].get_text(strip=True),
        "link": "https://www.wevity.com" + titles[i].get("href")
    }
    contest_list.append(contest)

if len(contest_list) > 0:
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(contest_list, f, ensure_ascii=False, indent=4)  # ✅ False 대문자
    print(f"저장완료 - 총 {len(contest_list)}개")
else:
    if os.path.exists("data.json"):
        print("크롤링 실패 -> 기존 데이터 유지")
    else:
        print("데이터 없음 + 기존 파일 없음")
