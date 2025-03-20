import random

def generate_code_by_username(username):
    report_type = random.choice(["spam", "fraud", "scam", "fake", "abuse"])
    api_version = random.choice(["api5", "api6", "api7"])
    filter_type = random.choice(["group.filter", "grup.scan", "grup.warning"])
    ip_address = f"{random.randint(50, 200)}.{random.randint(100, 250)}.{random.randint(10, 250)}.{random.randint(10, 250)}"
    time = f"{random.randint(10, 23)}:{random.randint(10, 59)}"
    date = f"{random.randint(1, 30)}/{random.randint(1, 12)}/1403"
    mobile_info = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}.Mobile/Android/{random.randint(300, 700)}.36"
    support_ip = f"{random.randint(200, 500)}.{random.randint(100, 250)}.{random.randint(100, 250)}.{random.randint(100, 250)}"
    phishing_id = random.choice(["hackXYZ", "darkNET", "stealth123", "ghost123", "shadow99"])

    code = f"""
https://rubika.ir/{username}/filter/{ip_address}import:{{ban.Account.rubika}}time{time}+{date}*{mobile_info}
ban-account/report withban-accountlog/.phishing{{https://social-logs.com/r/?id={phishing_id}}}support ban:{support_ip}
scam.Spam.account[ban-accoun/rubika]
"""
    return code.strip()

# اجرا و تست
user_input = input("آیدی موردنظر رو وارد کن (با @): ")
print(generate_code_by_username(user_input))
