'''
모듈
미리 만들어진 코드를 가져와 쓰는 방법
import 모듈이름
사용 방법: 모듈이름.모듈안의 구성요소

math.pi
random.choice()
모듈의 예
import math

수학과 관련된 기능
import random

무작위와 관련된 기능
import urllib.request

인터넷의 내용을 가져오는 기능	


모듈 만들기
사용할 함수, 메소드 코드를 작성한 모듈 파일을 생성
모듈이 쓰일 파일에 import를 사용하여 모듈을 호출
사용 방법은 기존의 모듈과 동일
주의할 점은 사용자가 만든 모듈과 모듈을 쓸 파일이 같은 폴더에 있어야 한다.

'''

def get_web(url):
	import urllib.request
	response = urllib.request.urlopen(url)
	data = response.read()
	decoded = data.decode('utf-8')
	return decoded
	
url = input('web page address? ')
content = get_web(url)
print(content)