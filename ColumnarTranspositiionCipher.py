#주상 전치 암호

# 암호키 입력 받기(중복되는 단어가 없어야 함.)
key = "BRAIN"

for i in range(len(key)-1):
    for j in range(int(i+1),len(key)):
        if(key[i] == key[j]):
            print("중복된 단어가 있습니다. \n키 값을 다시 입력해주세요.")