import re
p=re.compile('\d{3}[-|\.|\s]\d{3}[-|\.|\s]\d{4}')
r=p.findall('my phone number is 412-345-4545 and my ofc number is 44-344-4545 and 465-555-8989')
print(r)

regex=re.compile('\w+@\w+\.[a-z]{2,3}')
email=regex.findall('my email id is harakshitha.gmail@com and my ofc id is $harakshitha@gmail.com')
print(email)
