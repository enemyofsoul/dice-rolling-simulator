import random
l = [0,1,2,3,4,5,6]
n = random.choice(l)
print(n)
a = 0
while(a==0):
    b = input("do you want to get a dice roll again")
    if(b=="yes" or b =="YES" or b =="Yes"):
        n = random.choice(l)
        print(n)