import random
l = [1,2,3,4,5,6]
h = [1,2,3,4,5]
n = random.choice(l)
print(n)
a = 0
while(a==0):
    b = input("do you want to get a dice roll again")
    if(b=="yes" or b =="YES" or b =="Yes" or b ==""):
        n = random.choice(l)
        print(n)
        if(n==6):
            n = random.choice(h)
            print(n)
            
