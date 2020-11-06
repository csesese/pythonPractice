def solution(text,key,rot):
    global len
    global encrypted

    #encrypted
    for i in range(len):
        encrypted_text=ord(text[i])
        new_key=ord(key[i])-96
        #문자를 숫자로 변환하여 더하기
        sum=encrypted_text+new_key
        #더한 숫자를 문자열로 다시 반환하여 문자열로 합치기
        encrypted=encrypted+chr(sum)

        result=list(encrypted)


    # rotation
    for i in range(rot):
        tmp = result[len - 1]
        for j in range(len-1,0,-1):
            result[j] = result[j-1]
        result[0]=tmp
    result=''.join(map(str,result))
    print(result)



#암호화 할 key 입력받기
text,key,rot = input().split()
result=[]
encrypted=''
len=len(text)
rot=int(rot)

solution(text,key,rot)
