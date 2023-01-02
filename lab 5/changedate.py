import re
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})','\\3-\\2-\\1',dt)
dt1="2021-12-13"
print("Original date in YYYY-MM-DD format:",dt1)
print("New date in DD-MM-YYYY format:",change_date_format(dt1))
