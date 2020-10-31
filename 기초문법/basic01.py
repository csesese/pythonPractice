# 1부터 9까지의 수들의  제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# N*M 크기의 2차원 리스트를 한 번에 초기화 해야 할 때 유용
# 예시) array=[[0]*m for _in range(n)]

# _(언더바) 는 i(변수) 를 사용하지 않을 때 사용 
for i in range(10):
  print(i)

for _ in range(10):
  print("hello")

#------------------------------
#SORT

a = [5,4,3,9,10]
a.sort()
print(a)

b=[5,4,3,9,10]
result=sorted(b)
#sorted 는 사용하는 순간 정렬이 되지만 본체는 그대로 이다
#sort - 메서드 , sorted - 내장함수

print("b(변하지 않음) :" ,b)
print("result :",result)

#REMOVE
a=[1,2,3,4,5,5,5]
remove_set={3,5}

#remove_list 에 포함되지 않은 값만을 저장 
result=[i for i in a if i not in remove_set]
print(result)
