#기본 입출력

a = [1,2,3]
#항상 뒤에 추가되는 것
# append 는 리스트 뒤쪽에 데이터를 추가
a.append(4)
a.append(0)
print("append:",a)


b={1,2,3}
# 내부적으로 sort가 된다
b.add(4)
b.add(0)
print("add :",b)

#input() 함수는 한줄의 문자열을 입력받는 함수
#Map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용 할때 사용

#5개의 데이터를 입력 받을때
#.split() :공백기준으로 구분


a = input().split()
# 결과 : input().split() : ['1' ,'2','3','4','5']
print("a출력값:",a)

b,c,d,e,f= map(int, input().split())
print("b출력값 : " , b,c,d,e,f)

list = list(map(int,input().split()))

print("list담긴 값 출력 : ",list)

#2차원
n = int(input())
m= int (input())

arr= []
for i in range(n):
  arr.appned(list(map(int,input().split())))

#사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
#sys.stdin.readlin()
#단 , 입력 후 엔터가 줄 바꿈 기호로 입력되므로 restrip()메서드를 함께 사용

a=7
print("정답은"+str(a)+"입니다")
