#주상 전치 암호

# 암호키 입력 받기(중복되는 단어가 없어야 함.)
# def Input_Key(key, PLAINTEXT): return arr
key = "BRAIN"

for i in range(len(key)-1):
    for j in range(int(i+1),len(key)):
        if(key[i] == key[j]):
            print("중복된 단어가 있습니다. \n키 값을 다시 입력해주세요.")

# 펑문 입력 받기
PLAINTEXT = "ABCDEFGHIJKLMNOPQRSTVWXYZ"

# 암호키의 알파벳에 순서 부여(dictionary 이용)
# sorted 함수를 이용해서 알파벳 정렬(dictionary key 이용)
key_dic = {}
sorted_key = sorted(key)
for i in range(1, len(key)+1):
    key_dic[i] = sorted_key[i-1]


this_keydic = {}
for i in range(len(key)):
    for j in range(1, len(key)+1):
      if(key[i] == key_dic[j]):
            this_keydic[i+1] = key_dic[j]

print(this_keydic)


# 암호키의 길이 = 평문을 배열하는 열의 개수(list? table? 이용할 예정)

if(len(PLAINTEXT)%len(key) == 0):
    row = int(len(PLAINTEXT)/len(key))
else:
    row = int(len(PLAINTEXT)/len(key))+1


column = len(key)
arr = [[None]*column for i in range(row)]

# list 행렬에 PLAINTEXT 할당하기.
k = 0
for i in range(row):
    for j in range(column):
        arr[i][j] = PLAINTEXT[k]
        k+=1


# BLOCK_SIZE, 열에 배열된 문자 갯수, 암호 블록 크기
# 각 열을 읽은 후, 붙여서 암호문 만들기
# def Cipher(arr): return






