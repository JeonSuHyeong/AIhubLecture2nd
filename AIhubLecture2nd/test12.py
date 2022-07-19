import random as rd

"""
food = ["짜장면","짬뽕", "탕수육","군만두"]
print(food)
for i in range(5):
    print(rd.choice(food),end=", ")
print("")
rd.shuffle(food)
print(food)
"""

"""
num = rd.sample(range(1,46),6)
num.sort()
print(num)
"""
correct = 0
while True:
    a = rd.randint(1,9)
    b = rd.randint(1,9)
    op = rd.randint(1,2)

    if op == 1:
        ans = a+b
        mark = "+"
    else:
        ans = a*b
        mark = "*"
    
    q = f'{a} {mark} {b} = ?'
    c = int(input(q))

    if c==0:
        break
    elif (c== ans):
        print("정답")
        correct +=1
    else:
        print("오답")
    
print(f"{correct}개 맞췄습니다.")