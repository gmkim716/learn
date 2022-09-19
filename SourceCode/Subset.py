# 부분집합 구하기
## 설명이 필요: 완벽하게 이해하기 어렵다..

arr = [1,2,3,4,5]
def Subset(arr):
    ret = []                # 생성된 부분집합을 반환할 리스트
    for i in range(1<<len(arr)):        # 부분집합의 개수 : 2**n
        subset = []                     # 부분집합을 담을 공간 마련
        for j in range(len(arr)):
            if i & (1<<j):              # '원소 i'와 '비트 연산자로 1을 이동시키는 값'을 & 연산 적용
                subset.append(arr[j])
        ret.append(subset)

    return ret

print(Subset(arr))

'''
    i      binary       1<<j
----------------------------------
    0       0000        0000
    1       0001        0001
    2       0010        0010
    3       0011        0100
    4       0100        1000
    5       0101
    6       0110
    7       0111
    8       1000 
    9       1001
    10      1010
    ..       ..

1을 왼쪽 shift하게 되면, 

[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], ...
→ 0 까지 범위에서의 부분집합
→ 1 까지 범위에서의 부분집합
→ 2 까지 범위에서의 부분집합
→ 3 까지 범위에서의 부분집합
→ 4 까지 범위에서의 부분집합 의 형태로 진행되는 것을 볼 수 있다
'''