options=["Saving","Recurring","Demat","Wallet"]

for option in options:
    print("Menu Item %s" %(option))

#nested list
assets=[12456,["apartment","Equity","bonds","shares"],482584547]
employee=[48358734,"Tarun",["C#","Java","Python","Click Sense"]]

for elem in employee:
    if(type(elem) is list):
        for skill in elem:
            print(skill)

orgList=["CITI","TCS","HCL"]
locList=["Chennai","Mumbai","Pune"]

for o,l in zip(orgList,locList):
    print(o,"-->",l)
#sorting the data
orgList.sort()
for org in orgList:
    print(org)

orgList.reverse()
for org in orgList:
    print(org)


import random

otp=[]

for i in range(1,100):
    otp.append(random.randint(9000,10000))


for num in otp[20:30]:
    print(num,end="\t")

