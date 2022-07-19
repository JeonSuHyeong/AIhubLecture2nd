file = "20200719-104830.jpg"
print(f'촬영날짜: {file[4:6]}월 {file[6:8]}일')
print(f"확장자: {file[-3:]}")

s= "python programming"
print(len(s))
print(s.find("o")) # 리스트에서 o의 위치 찾기 왼쪽부터
print(s.rfind("o")) # 리스트에서 o의 위치 찾기 오른쪽부터
print(s.count("o")) # 리스트에서 o의 갯수 찾기
print("a"in s) #리스트에서 a가 있는지 없는지 찾기 -> T/F
print(s.upper()) #s의 문자열을 대문자로 변환
print(s.lower()) #s의 문자열을 소문자로 변환