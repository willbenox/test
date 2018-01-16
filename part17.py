'''
List Comprehension
파이썬의 유용한 도구
예1 [ i*i for i in range(1,11) ] # [ 계산식 for문 ]
예2 [ i*i for i in range(1,11) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]
예3 [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]
	
Dictionary Comprehension
파이썬의 유용한 도구
예 { "{}번".format(number):name for number, name in enumerate(students) } # [ 형식 for문 ]

'''

def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    list_len = len(list)
    if list_len>0:
	    total =0
		for i in list:
			total += i
		return total/list_len
	else:
		return 0