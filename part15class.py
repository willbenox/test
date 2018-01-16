'''
자료형
type( a ) # type( 변수명 ) : 자료형
isinstance( 42, int ) # isinstance( 값, 자료형 ) : 자료형 검사

클래스
함수나 변수들을 모아 놓은 집합체
인스턴스
클래스에 의해 생성된 객체
인스턴스 각자 자신의 값을 가지고 있다.


클래스 선언
class Human( ):
    '''사람'''
인스턴스 생성
person1 = Human( )
person2 = Human( )
클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 이해하기 쉽게 포장할 수 있다.

모델링(modeling)
클래스로 현실의 개념을 표현하는 것

메소드(Method)
메소드는 함수와 비슷하다.
클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수
클래스 내부에 함수를 포함시킨 예
class Human( ):
    '''인간'''
    def create( name, weight ): # 다음 강의에서 자세히 설명
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat( self ):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

    def walk( self ):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

person = Human.create("철수", 60.5)
person.eat()
self
메소드의 첫번째 인자
인스턴스의 매개변수를 전달 할 때는 self 매개변수는 생략하고 전달


초기화 함수
__init__ : 인스턴스를 만들 때 실행되는 함수
문자열화 함수
__str__ : 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
class Human( ):
    
    def __init__( self, name, weight ):
        
        self.name = name
        self.weight = weight

    def __str__( self )
    
        return "{} ( 몸무게 {}kg )".format( self.name, self.weight )

person = Human( "사람", 60.5 ) # 초기화 함수 사용
print( person ) # 문자열화 함수 사용


상속(Inheritance)
상속하는 클래스를 부모 클래스
상속받는 클래스를 자식 클래스
자식 클래스가 부모 클래스의 내용을 가져다 쓸 수 있는 것
class Animal( ):
    def walk( self ):
        print( "걷는다" )

    def eat( self ):
        print( "먹는다" )

class Human( Animal ):
    def wave( self ):
        print( "손을 흔든다" )

class Dog( Animal ):
    def wag( self ):
        print( "꼬리를 흔든다" )


class Animal( ):
    def greet( self ):
        print( "인사한다" )

class Human( Animal ):
    def greet( self ):
        print( "손을 흔든다" )

class Dog( Animal ):
    def greet( self ):
        print( "꼬리를 흔든다" )
		
super()
자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
super().부모클래스내용
class Animal( ):
    def __init__( self, name ):
        self.name = name

class Human( Animal ):
    def __init__( self, name, hand ):
        super().__init__( name ) # 부모클래스의 __init__ 메소드 호출
        self.hand = hand

person = Human( "사람", "오른손" )


예외 정의
사용자가 직접 예외처리를 하면 코드의 직관성을 높일 수 있다.
파일을 하나 만들어 예외를 정의
Exception 클래스를 상속받아 만든다
try:
    sign_up( )
except BadUserName:
    print( "이름으로 사용할 수 없는 입력" )
except PasswordNotMatched:
    print( "입력한 패스워드 불일치")
	
	


'''

