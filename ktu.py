import requests
from bs4 import BeautifulSoup
import re

session = requests.Session()

url = "https://app.ktu.edu.in/login.htm"
response = session.get(url, verify=False)

soup = BeautifulSoup(response.text, "html.parser")
csrf = soup.find("input", {"name": "CSRF_TOKEN"})["value"]

username = "KTU_USERNAME"
password = "KTU_PASSWORD"
semester = "B.Tech S"+"1-8 any number"
bot_token = "TELEGRAM_BOT_TOKEN"
chat_id = "TELEGRAM_CHAT_ID"

payload = {
    "username": username,
    "password": password,
    "CSRF_TOKEN": csrf
}

login = session.post(url, data=payload, verify=False)

profile = session.get("https://app.ktu.edu.in/eu/stu/studentDetailsView.htm", verify=False)
soup = BeautifulSoup(profile.text, "html.parser")
all_reval_links = soup.find_all("a", href=re.compile("viewRevaluationCoursesList"))

messages = []

for link in all_reval_links:
    label = link.find_previous("label")
    if label and semester in label.text:
        full_url = "https://app.ktu.edu.in" + link['href']
        
        reval_page = session.get(full_url, verify=False)
        soup = BeautifulSoup(reval_page.text, "html.parser")
        
        rows = soup.select("#revaluationRegisteredCoursesTable tbody tr")
        for row in rows:
            cols = [td.text.strip() for td in row.find_all("td")]
            course, prev_grade, new_grade, status = cols[0], cols[1], cols[2], cols[3]

            if status != "Not Published":
                messages.append(f"📢 {course}: Previous Grade: {prev_grade}, New Grade: {new_grade}")
            else:
                messages.append(f"❌ {course}: Not published")
        break

if messages:
    message = "\n".join(messages)
    requests.post(
        f"https://api.telegram.org/"+bot_token+"/sendMessage",
        data={"chat_id": chat_id, "text": message}
    )
