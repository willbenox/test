'''
for in 반복문
코드를 필요한만큼 반복해서 실행

for pattern in patterns:
    print (pattern)
리스트 patterns의 값을 하나씩 꺼내 pattern으로 전달
리스트의 길이만큼 print (pattern) 실행

range 함수
필요한 만큼의 숫자를 만들어내는 유용한 기능
for i in range(5):
    print(i)
enumerate
리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
names = ['철수', '영희', '영수']
for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))
	
	
'''

for i in range(5):
	print(i)
	i+=2
	print(i)