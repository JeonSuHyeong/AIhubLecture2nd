score=[88,95,70,100,99]
a=score.index(100)
print("만점을 받은 학생은 "+str(a)+"번입니다. ")
print("만점을 받은 학생은",a,"번입니다. ")
b= score.count(100)
print("만점자 수는 "+str(b)+" 명입니다.")
print("학생 수는 %d명입니다." % len(score))
print("최고 점수는 %d입니다." % max(score))
print("최저 점수는 %d입니다." % min(score))
score.sort()
print(score)
score.reverse()
print(score)

ans = input("결제를 하시겠습니까? ")
if(ans in ["yes","y","ok","예"]):
    print("구입해 주셔서 감사합니다.")
else:
    print("안녕히 가세요")





"""
python.exe파일 설치

>> pip install pyinstaller
이후 폴더가서 pyinstaller file.py
"""