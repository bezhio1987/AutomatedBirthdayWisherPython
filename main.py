import os
import random
from dotenv import load_dotenv
import smtplib
import datetime as dt
import pandas as pd

load_dotenv()
today = dt.datetime.now()
today_month = today.month
today_day = today.day

data = pd.read_csv("birthdays.csv")
data_formatted = (data.to_dict(orient="records"))

person_info = [item for item in data_formatted if item["month"]== today_month and item["day"]== today_day]

file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", person_info[0]["name"])

my_email = os.getenv('MY_EMAIL_USERNAME')
mailtrap_username = os.getenv('MAIL_TRAP_USERNAME')
mailtrap_password = os.getenv('MAIL_TRAP_PASSWORD')
mailtrap_host = os.getenv('MAIL_TRAP_HOST')

message = f"Subject:Happy Birthday!\n\n{contents}"

with smtplib.SMTP(mailtrap_host, 2525) as server:
    server.login(mailtrap_username, mailtrap_password)
    server.sendmail(my_email, person_info[0]["email"], message)


