#실수형 더 알아보기
a=0.3+0.9

if a==0.9:
    print(True)
else:
    print(False)

#round 반올림
print(round(0.123923, 3))

#리스트 자료형 : 여러개의 데이터를 연속적ㅇ로 담아 처리하기 위해 사용하는 자료형
#리스트 컴프리헨션 : 리스트를 초기화 하는 방법 중 하나 , 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 할 수 있음

#0부터 9까지의 수를 포함하는 리스트
a=[i for i in range(10)]
print(a)

#1부터 9까지의 수들의 제곱 값을 포함하는 리스트
b=[i * i for i in range(10)]
print(b)

#5번 출력하기(언더바)
for _ in range(5):
    print("hello")

#리스트에서 특정 값을 가지는 원소를 모두 제거하기
a=[1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]
print(result)

#------------------------------------------------------------

#문자열 자료형  : 문자열 변수를 초기화 할때는 큰따옴표 나 작은따옴표를 이용합니다.

data = 'hello world'
print(data)
# " 큰따옴표를 출력하기 위해서는 \ 뒤에 작성
data ="Dont you know  \"Python\" ?"
print(data)

#문자열 연산

a="String"
print(a*3)

a="abcdef"
print(a[2:4])





