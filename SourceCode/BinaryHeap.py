# 이진 힙

H = [0] * 100       # 힙 저장 공간
hsize = 0           # 힙의 마지막 인덱스, 크기를 나타내는 값


# 이진 힙에 자료를 입력
def push(item):          # feat. 최대 힙
    # 힙에 새로운 값을 추가
    global hsize         # 힙의 마지막 인덱스(힙의 사이즈)
    hsize += 1           # 힙의 크기 += 1
    H[hsize] = item      # 힙의 마지막 인덱스에 item을 추가

    # for 추가된 값과 기존의 값을 비교, 기준 인덱스 설정(부모, 자식)
    p = hsize // 2                      # 부모 노드의 인덱스 : 현재 인덱스(마지막)의 절반 값
    c = hsize                           # 자식 노드의 인덱스 : 현재 인덱스

    # 조건에 부합할 때 까지 아래 반복
    while p and H[p] < H[c]:            ## 부모 노드가 존재하고, 자식노드 값 > 부모노드 값보다 클 때 교체 → for 최대 힙: 자식노드 값 < 부모노드 값)
        H[p], H[c] = H[c], H[p]         # 교체
        p = c // 2                      # 다음 탐색을 위해서 부모, 자식 인덱스 변경
        c = p
                                        ##1. 최소 힙을 구현할 때 부모노드 값, 자식노드 값 부등호 변경

# 이진 힙 자료에서 pop
def pop():              # feat. 최대 힙
    # 인덱스의 삭제
    global hsize            # 힙의 마지막 인덱스(힙의 사이즈)
    ret = H[1]              # 반환할 값 = 루트 노드에 위치한 값, 미리 ret에 따로 빼둠
    H[1] = H[hsize]         # 루트노드의 값에 마지막 노드의 값 입력
    hsize -= 1              # 마지막 인덱스 - 1 : 마지막 노드를 삭제

    # 힙 구조가 유지될 수 있도록 자리 배치
    p, c = 1, 2                     # 탐색의 기준이 되는 부모(1), 왼쪽 자식 노드 인덱스 (왼쪽부터 채워지는 힙 구조의 특징 이용)
                                        # 조건이 만족할 때까지 반복
    while c <= hsize:                       # 왼쪽 노드가 존재할 때 ← 마지막 노드 보다 자식 노드가 작거나 같을 때 (마지막 노드보다 자식 노드가 크면 진행x)
        if c+1 <= hsize and H[c] < H[c+1]:          # 오른쪽 노드가 존재하고, 왼쪽 노드 값 < 오른쪽 노드 값이면
            c += 1                                  # 기준이 되는 값을 오른쪽 노드로 변경
        if H[p] >= H[c]:                    # 자식노드 값보다 부모노드 값이 같거나 클 때, 원하는 정상적인 상황 (최대 힙)
            break                           # 변경 없이 break
        H[p], H[c] = H[c], H[p]             # break를 통과하지 못할 경우 교체 진행
        p = c                               # 아래 방향으로 탐색을 위해 노드 인덱스 변경
        c = p * 2

    return ret                              # print()로 불러오면 루트 노드였던 값을 반환


def empty():
    return hsize == 0
