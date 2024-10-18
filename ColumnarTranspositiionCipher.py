#주상 전치 암호

# 암호키 입력 받기(중복되는 단어가 없어야 함.)
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

# row, column = 2,3
# arr_2d = [[None]*column for i in range(row)]
# print(arr_2d)