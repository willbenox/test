#콜론 뒤에는 블록이 들어갈 자리라는 선언?
#리턴 값은 여러개 받을 수 있다. 단, 리턴 수만큼 쉼표로 변수 갯수가 있어야 한다

def add(a, b):
	result = a+b
	
	return result
	
def total(a, b):
	add = a+b
	minus = a-b
	return add, minus
	
print(add(5,4))
n = add(5,3)	
print(n)

t1, t2 = total(3,3)
print('its {} {}'.format(t1,t2))
	
