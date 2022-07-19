#List []
s= [88,95,70,100,99]
sum = 0
for i in s:
    sum +=i
print(s)
print(f"총점: {sum}")
print(f"평균: {sum/len(s)}")
print(s[0])
print(s[-1])
print(s[2:4])
print(s[0:5:2])

# 값 변경이 가능하다
#ex)
s[2]=55
print(s)
num = [0,1,2,3,4,5,6,7,8,9]
print(num)
num[2:5] = [20,30,40]
print(num)
num[6:8] = [90,91,92,93,94]
print(num)
num = [0,1,2,3,4,5,6,7,8,9]
del num[4]
print(num)
num.insert(4,4)
print(num)

#다른방법으로 지우기
num[2:5] = []
print(num)

#list 합치기
list1=[1,2,3,4,5]
list2=[10,11]
listadd = list1+list2
print(listadd)

#2차원 list
list1=[[1,2,3],[4,5],[6,7,8,9]]
print(list1[0]) #행 출력
print(list1[2][1]) #값 출력

for i in list1:
    for j in i:
        print(j,end="")
    print("")

num =[1,2,3,4]
num.append(5)
print(num)
num.insert(2,99)
print(num)
num.remove(99)
print(num)



#tuple {}



# dictionary{key : word}