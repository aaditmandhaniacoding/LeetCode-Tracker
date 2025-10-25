import matplotlib.pyplot as plt
import datetime

easy = int(input("How many easy problems did you solve today? "))
medium = int(input("How many medium problems did you solve today? "))
hard = int(input("How many hard problems did you solve today? "))

today = datetime.date.today()
with open("progress.txt","a") as f:
    f.write(f"{today},{easy},{medium},{hard}\n")
