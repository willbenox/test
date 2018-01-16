'''
List의 기능
list.index( value ) : 값을 이용하여 위치를 찾는 기능
list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가
list.insert( index, value ) : 원하는 위치에 값을 추가
list.sort( ) : 값을 순서대로 정렬
list.reverse( ) : 값을 역순으로 정렬


List와 String
리스트와 문자열은 유사하다.
서로 변환이 가능하다.
list = str.split( ) : 문자열에서 리스트로
" ".join( list ) : 리스트에서 문자열으로



slicing
리스트나 문자열에서 값을 여러개 가져오는 기능
text = "hello world"
text = text[ 1:5 ]

list = [ 0, 1, 2, 3, 4, 5 ]
list = list[ 1:3 ]
slice를 하면 해당하는 부분의 리스트나 문자열을 새로 만들어 준다.

시작과 끝부분을 얻어 오는 방법

list[ 2: ] : 2번째부터 끝까지 반환
list[ : 2 ] : 처음부터 2번째 까지 반환
list[ : ] : 처음부터 끝까지 전부 반환

step
slice한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능
list[ 시작값:끝값:step ]

slice 활용
삭제
del list[ :5 ] : 처음부터 5번째까지 삭제
수정
list[ 1:3 ] = [ 77, 88 ]
list[ 1:3 ] = [ 77, 88 ,99 ] : 더 많은 개수로 변환
list[ 1:4 ] = [ 8 ] : 더 적은 개수로 변환

'''

