#Question 1
import re as r
e = input("enter the email ")
m = r.finditer('^[a-z][a-zA-Z0-9]*[@](gmail.com|yahoo.com)', e)
count = 0
for i in m:
    count += 1
if count == 1:
    print('email verified')
else:
    print('wrong input')


#Question 2
n= str(input('enter the phone number'))
m = r.finditer('^[+][9][1][6-9][\d]{9}', n)
count = 0
for i in m:
    count += 1
if count == 1:
    print('phone number validated')
else:
    print('wrong phone number')
