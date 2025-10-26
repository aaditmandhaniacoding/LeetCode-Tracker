import matplotlib.pyplot as plt
import datetime
import requests


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

easy = stats[1]["count"]
medium = stats[2]["count"]
hard = stats[3]["count"]


today = datetime.date.today()
with open("progress.txt","a") as f:
    f.write(f"{today},{easy},{medium},{hard}\n")


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