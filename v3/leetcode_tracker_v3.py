import matplotlib.pyplot as plt
import datetime
import requests
import os
import sqlite3


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


db_file = "progress.db"
conn = sqlite3.connect(db_file)
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS progress(
            date TEXT PRIMARY KEY,
            total_easy INTEGER,
            total_medium INTEGER,
            total_hard INTEGER,
            daily_easy INTEGER,
            daily_medium INTEGER,
            daily_hard INTEGER
          )""")


c.execute("SELECT total_easy,total_medium,total_hard from progress ORDER BY date DESC LIMIT 1")
lastrow = c.fetchone()
if lastrow:
    prev_easy,prev_medium,prev_hard = lastrow
else:
    prev_easy = total_easy
    prev_medium = total_medium
    prev_hard = total_hard


daily_e = total_easy - prev_easy
daily_m = total_medium - prev_medium
daily_h = total_hard - prev_hard


today = str(datetime.date.today())


c.execute("""INSERT OR REPLACE INTO progress
          (date,total_easy,total_medium,total_hard,daily_easy,daily_medium,daily_hard) VALUES (?,?,?,?,?,?,?)
          """,(today,total_easy,total_medium,total_hard,daily_e,daily_m,daily_h))
conn.commit()




c.execute("SELECT date,daily_easy,daily_medium,daily_hard FROM progress ORDER BY date")
rows = c.fetchall()
conn.close()




dates = []
easy_list = []
medium_list = []
hard_list = []






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
