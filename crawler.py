import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://www.wevity.com/?c=find&s=1&gub=1"

# 🔥 User-Agent 추가 (차단 방지)
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 🔥 제목 + 링크 (a 태그 포함)
titles = soup.select(".tit a")

# 주최 / 마감일
hosts = soup.select(".organ")
dates = soup.select(".dday")

print("디버깅:", len(titles), len(hosts), len(dates))

contest_list = []

# 최소 길이 기준
min_len = min(len(titles), len(hosts), len(dates))

for i in range(min_len):
    title = titles[i].get_text(strip=True)

    # 링크 추가
    link = "https://www.wevity.com" + titles[i].get("href")

    contest = {
        "title": title,
        "host": hosts[i].get_text(strip=True),
        "date": dates[i].get_text(strip=True),
        "link": link
    }

    contest_list.append(contest)

# JSON 저장
# with open("data.json", "w", encoding="utf-8") as f:
#    json.dump(contest_list, f, ensure_ascii=False, indent=4)

if len(contest_list) > 0:
    with open("data.json", "w", encording="utf-8") as f:
        json.dump(contest_list, f, ensure_ascii=false, indent = 4)
    print("저장완료")
else:
    if os.path.exists("data.json"):
        print(" 크롤링 실패 -> 기존 데이터 유지")
    else:
        print(" 데이터 없음 + 기존 파일 없음")

# 콘솔 출력 (액션용)
print("\n 크롤링 결과\n")
for i, c in enumerate(contest_list, 1):
    print(f"{i}. {c['title']}")
    print(f"   주최: {c['host']}")
    print(f"   마감일: {c['date']}")
    print(f"   링크: {c['link']}")
    print("-" * 40)

print(f"\n 총 {len(contest_list)}개 크롤링 완료")
