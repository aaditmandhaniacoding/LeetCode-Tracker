import matplotlib.pyplot as plt
import datetime
import requests
import os

USERNAME = "YourUsername"

query = {
    "query":f"""
    query userProfile {{
        allQuestionsCount {{
            difficulty
            count
        }}
        matchedUser(username:"{USERNAME}"){{
            submitStats{{
                acSubmissionNum {{
                    difficulty
                    count
                }}
            }}
        }}
    }}
    """
}

response = requests.post("https://leetcode.com/graphql",json=query)
data = response.json()

stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

total_easy = stats[1]["count"]
total_medium = stats[2]["count"]
total_hard = stats[3]["count"]

prev_easy = total_easy
prev_medium = total_medium
prev_hard = total_hard
today = datetime.date.today()
with open("progress.txt","a") as f:
    f.write(f"{today},{prev_easy},{prev_medium},{prev_hard}\n")


dates = []
easy_list = []
medium_list = []
hard_list = []

with open("progress.txt","r") as f:
    for line in f:
        d,e,m,h = line.strip().split(",")
        dates.append(d)
        easy_list.append(int(e))
        medium_list.append(int(m))
        hard_list.append(int(h))

plt.plot(dates,easy_list,label = "Easy",marker = "o")
plt.plot(dates,medium_list,label = "Medium",marker = "o")
plt.plot(dates,hard_list,label = "Hard",marker = "o")

plt.xlabel("Date")
plt.ylabel("Problem Solved")
plt.title("Your LeetCode Progress")
plt.legend()
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()