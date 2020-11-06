# 순차 탐색 : 앞에서부터 데이터를 하나씩 확인 하는 방법
# 이진 탐색 : 탐색 범위를 절반식 좁혀가며 데이터를 탐색하는 방법(시작, 중간 , 끝)

def binaray_search (array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
        return binaray_search(array,target,start,mid-1)
    else:
        return binaray_search(array,target,start+1,end)

n,target=list(map(int,input().split()))
ㅎ
array=list(map(int,input.split()))

result=binaray_search(array,target,0,n-1)
if result==None:
    print("원소 존재하지 않음")
else :
    print(result+1)


#파라메트릭 서치 : 최적화 문제를 결정 문제('예' 혹은 '아니요') 로 바꾸어 해결하는 기법 -> 이진탐색으로 해결

