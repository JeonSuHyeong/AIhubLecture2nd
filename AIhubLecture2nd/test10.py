import time
#tuple
score=(88,95,70,100,99)

print(score)
sum=0
for s in score:
    sum += s
print(sum)
print(sum/len(score))

#list로 여러 값 return이 가능하다

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print("지금은 %d시 %d분 입니다." %(result[0],result[1]))