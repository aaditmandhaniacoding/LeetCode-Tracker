# LeetCode Tracker v2
---

This is a Python program to track LeetCode problem-solving progress.



## Current functionality (v2):
---
- Automatically fetches solved counts from your LeetCode profile using the **requests** library
- Calculates progress to a text file (`progress.txt`)
- Visualizes progress over time using line charts with **Matplotlib**



## Version History
---
### v1
- Basic tracker: log easy, medium, hard problems
- Visualize progress with Matplotlib line graph

### v2
- Automatic fetching of solved problem counts from LeetCode GraphQL API
- Logs progress automatically to `progress.txt`



## Features
---
- Simple and intuitive command-line interface
- Tracks your progress over time

## Limitations
---
- The tracker **cannot fetch the exact dates of previously solved problems**.
- Only calculates daily progress from the day you start running the tracker onwards.

## Installation
---
1. Install Python
2. Install the dependencies from `requirements.txt`:


```bash
python -m pip install -r requirements.txt
```
