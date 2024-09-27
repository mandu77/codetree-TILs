# import sys

# sys.stdin = open("input.txt", "r")

dirs = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]

def in_board(R, C, N):
    return 0<=R<N and 0<=C<N


def exp_virus(board, plus_board, virus, K, N):
    # 1. 양분 섭취
    # 2. 죽은 바이러스 양분으로 변환 (나이/2)
    # 3. 5의 배수 바이러스 번식
    # 4. 양분 추가

    for _ in range(K):
        dead_virus=[]
        after_virus=[]
        for v in virus:
            if board[v[0]][v[1]]>=v[2]:
                board[v[0]][v[1]]-=v[2]
                v[2]+=1
                after_virus+=[v]
            else:
                dead_virus+=[v]
        for dv in dead_virus:
            board[dv[0]][dv[1]]+=dv[2]/2

        virus.clear()

        for av in after_virus:
            if av[2]%5==0:
                for d in dirs:
                    if in_board(av[0]+d[0], av[1]+d[1], N):
                        virus.append([av[0]+d[0], av[1]+d[1], 1])

            virus.append(av)

        virus.sort()

        for i in range(N):
            for j in range(N):
                board[i][j]+=plus_board[i][j]



    return len(virus)







if __name__=="__main__":

    N, M, K = map(int, input().split())

    board = [[5]*N for _ in range(N)]
    # print(N, M, K)
    plus_board = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    # print(*plus_board, sep='\n')

    # print(*board, sep='\n')

    # virus = [
    #     list(map(int, input().split()))
    #     for _ in range(M)
    # ]
    virus = [
        list(x-1 if idx<2 else x for idx, x in enumerate(map(int, input().split())))
        for _ in range(M)
    ]
    # print(*virus, sep='\n')

    ans = exp_virus(board, plus_board, virus, K, N)

    print(ans)