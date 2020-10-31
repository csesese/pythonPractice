#조건문 & 제어문
#블록(block) 은 들여쓰기로 한다.

##########
#조건문

a= 5
if a>10:
  print("커용")
else :
  print("작아유")
print("끝")

#여러 개의 데이터를 담는 자료형을 위해 in 연산자 가 제공된다.

score = 85
if score>=80 :
  pass # 나중에 작성할 소스코드
else :
  print("성적이 80점 미만입니다")
print('프로그램을 종료합니다')


###########
#반복문

#for 변수 in 리스트 : 실행할 소스코드
#for문에서 수를 차례대로 나열할 때는 range( ) 를 주로 사용합니다.
#range(시작 값, 끝 값)


result =0
for i in range(1,10):
  result+=i

print("1부터 9까지의 합은 : ", result)

score=[90,85,77,65,97]
black_list={2}


for i in range(5):
  if i+1 in black_list:
    continue
  if score[i]>=80:
    print(i+1,"번 학생은 합격")


#함수와 람다
#함수 : 특정한 작업을 하나의 단위로 묶어 놓은 것 

#내장 함수 : 파이썬이 기본적으로 제공하는 함수
#사용자 정의 함수 : 개발자가 직접 정의하여 사용하는 함수
#파이썬은 여러개의 반환값을 가질 수 있다.


-매개변수 : 함수 내부에서 사용할 변수
-반환 값 : 함수에서 처리 된 결과를 반환

-global 키워드로 변수를 지정하면 해당 함수에서는 지역변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.

def 함수명(매개변수):
    실행할 소스코드
    return 반환 값



def add( a, b):
  return a+b
print ("더한값은", add(3,7))

#gloabl 키워드 사용
a=0

def func():
  global a
  a+=1

for i in range(10):
  func()
print(a)

#여러개의 반환값 가능
def operator(a,b) :
  return a+b, a-b, a*b, a/b
print(operator(10,2))

#람다식 : 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다.

print((lambda a, b : a+b)(3,5))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
result = map(lambda a, b:a+b, list1, list2)
print("list1",list1)
print("list2", list2)
print("list1 과  list 2 덧셈: ", list(result))



#자주 사용되는 내장함수 
result = sum([1,2,3,4,5])
print(result)

min_result=min(7,3,5,2)
max_result=max(7,3,5,2)
print("max: ",max_result)
print("min: ",min_result)


#순열과 조합
'''
-순열 : 서로다른 n개에서 서로다른 r개를 선택하여 일렬로 나열하는 것 
-조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 
'''
#순열 
from itertools import permutations

data=['a','b','c']

result = list(permutations(data,3)) 
print("순열 : " , result)

#조합

from itertools import combinations

data2=['d','e','f']

result2= list(combinations(data2, 2)) #2개를 뽑는 모든 조합 구하기
 
print("조합",result2)
