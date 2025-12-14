import os
import pandas
import random
import smtplib
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Get environment variables
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

# Validate environment variables
if not my_email or not my_password:
    raise ValueError("MY_EMAIL and MY_PASSWORD must be set in the environment variables")

today = datetime.today()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print(birthday_person["name"])
    print(type(birthday_person["email"]))
    random_number = random.randint(a=1, b=3)
    file_path = f"letter_templates/letter_{random_number}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
