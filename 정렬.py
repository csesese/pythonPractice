#정렬 알고리즘
#데이터를 특정한 기준에 따라 순서대로 나열 하는 것

# 1) 선택 정렬 : 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i] , array[min_index]= array[min_index], array[i] # 스와프
print("선택정렬 ->",array)

# 2) 삽입 정렬 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입합니다

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i,0,-1): #인덱스 i부터 1까지 1씩 감소하면서 반복하는 문법
        if array[j]<array[j-1]:
            array[j] ,array[j-1] = array[j-1], array[j]
        else:
            break
print("삽입정렬 ->",array)

# 3) 퀵 정렬 : 기준데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 가장 기본적인 퀵 정렬은 첫번째 데이터를 기준 데이터(Pivot)로 설정합니다.

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start,end):
    if start>=end : #원소가 1개인 경우 종료
        return
    pivot= start #피벗은 첫 번째 원소
    left = start+1
    right =end

    while(left<=right):
      #피벗보다 큰 데이터를 찾을 때까지 반복
      while(left<=end and array[left]<=array[pivot]):
          left+=1
      #피벗보다 작은 데이터를 찾을 때까지 반복
      while(right>start and array[right]>=array[pivot]):
          right -= 1
      if(left>right): #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right],array[pivot] = array[pivot],array[right]
      else : # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    #분할 이후 왼쪽 부분과 오른족 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
quick_sort(array,0,len(array)-1)
print("퀵정렬 ->",array)

# 3-1) 퀵 정렬 간결 코드
array=[5,7,9,0,3,1,6,2,4,8]

def quick_srort2(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array)<=1:
        return array
    pivot=array[0] #피벗은 첫 번째 원소
    tail=array[1:] #피벗을 제외한 리스트

    left_side=[x for x in tail if x<=pivot] #분할된 왼쪽 부분
    right_side=[x for x in tail if x>pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반화
    return quick_srort2(left_side)+[pivot]+quick_srort2(right_side)

print("간격한 퀵정렬 -> ",quick_srort2(array))

# 4) 계수 정렬 : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 대 사용 가능

array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count=[0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
print("계수 정렬 -> ",end=' ')
for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')

