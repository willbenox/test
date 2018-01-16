'''
딕셔너리
여러 값을 저장해 두고 필요한 값을 꺼내 쓰는 기능
이름표를 이용하여 값을 꺼내 사용
사용할 때는 리스트와 비슷한 방식
wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위',
}

print(wintable['가위'])

추가
dict['three'] = 3

수정
dict['one'] = 11

삭제
del(dict['one'])

dict.pop('two')


딕셔너리 반복문 활용
경우에 따라 가져올 값을 정할 수있다.

for key in ages.keys(): # keys() 생략 가능
    print(key)
for value in ages.values():
    print(value)
key와 value 둘다 가져올 수 있다.

for key, value in ages.items():
    print('{}의 나이는 {} 입니다'.format(key, value))
딕셔너리는 값의 순서를 지키지 않는다.



공통점
        List	                               Dictionary
생성	list = [ 1, 2 ,3 ]              	dict = { 'one':1, 'two':2 }
호출	list[ 0 ]	                        dict[ 'one' ]
삭제	del( list[ 0 ] )                	del( dict[ 'one' ] )
개수 확인	len( list )	                    len( dict )
값 확인	2 in list	                    'two' in dict.keys( )
전부 삭제	list.clear( )	                dict.clear( )

차이점
         List	                               Dictionary
순서	삭제 시 순서가 바뀌기 때문에 인덱스에 대한 값이 바뀐다	       key로 값을 가져오기 때문에 삭제 여부와 상관없다
결합	list1 + list2	                           dict1.update( dict2 )


튜플
한번 정해진 순서를 바꿀 수 없다.

튜플 선언
tuple1 = (1, 2, 3, 4)
tuple2 = 1, 2, 3, 4
mylist = [1,2,3,4]
tuple3 = tuple(mylist)
튜플은 값의 변경과 삭제가 불가능


packing
하나의 변수에 여러개의 값을 넣는 것

unpacking
패킹된 변수에서 여러개의 값을 꺼내오는 것
c = (3, 4)
d, e = c    # c의 값을 언패킹하여 d, e에 값을 넣었다
f = d, e    # 변수 d와 e를 f에 패킹

튜플의 활용
두 변수의 값을 바꿀 때 임시변수가 필요 없다.
함수의 리턴 값으로 여러 값을 전달할 수 있다.


튜플 리스트 활용
for a in enumerate(list):
    print('{}번째 값: {}'.format(a[0], a[1]))

for a in enumerate(list):
    print('{}번째 값: {}'.format(*a))
튜플 딕셔너리 활용
for a in dict.items():
    print('{}의 나이는:{}'.format(a[0], a[1]))

for a in dict.items():
    print('{}의 나이는:{}'.format(*a))

'''
