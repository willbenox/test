number = 20
greeting = 'hello'
place = 'string format'
welcome = 'welcome'


print(number, ' 번 손님', greeting, '.', place,
		'에 오신 것을', welcome, '!')
		
		
base = '{}번 손님, {}. {}에 오신 것을 {}!'

new_way = base.format(number, greeting,place,welcome)

print(base)
print(new_way)


"""
또는 "로 문자열 만들기
' 또는 "로 글의 양쪽을 감싸면 문자열로 인식
'로 감싼 문자열 안에는 "를 쓸 수 있다.
"로 감싼 문자열 안에는 '를 쓸 수 있다.

string1 = '따옴표로 싼 문자열 안에는 큰따옴표(")를 사용할 수 있다.'
string2 = "큰따옴표로 싼 문자열 안에는 따옴표(')를 사용할 수 있다."
따옴표/큰따옴표 3개로 문자열 만들기
줄 바꿈도 인식 가능
따옴표와 큰따옴표를 섞어 쓸 수 있다.
"""