#dictionary
dic = {'boy' : '소년', 'school' : '학교', 'book' : '책'} #{ key : value}
print(dic)
print(dic['boy'])
print(dic.get("student"),'사전에 없는 단어 입니다.')

dic['boy'] = '남자아이'
print(dic)

dic['girl'] = '소녀'
print(dic)

del dic['book']
print(dic)

print(dic.keys())
print(dic.values())

print(dic.items()) #튜플 형태로 출력. 수정 불가

dic2 = {'student' : '학생', 'teacher' : '선생님'}
dic.update(dic2) #dic2값을 dic에 추가

print(dic)

li = [['boy','소년'],['school', '학교'], ['book', '책']]

dic1 = dict(li) #list에서 dictionary로 변환
print(dic1)
