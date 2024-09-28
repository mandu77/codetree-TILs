# import sys

# sys.stdin =open("input.txt", "r")


dirs = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

def in_board(R,C, N):
    return 0<=R<N and 0<=C<N


def simulation(board, virus_board, plus_board, N, K):
    for _ in range(K):

        for i in range(N):
            for j in range(N):
                if virus_board[i][j]:
                    virus_board[i][j].sort()
                    tmp_virus = []
                    for virus in virus_board[i][j]:
                        if board[i][j]>=virus:
                            board[i][j]-=virus
                            tmp_virus.append(virus+1)
                        else:
                            chk_left_virus = len(tmp_virus)
                            for dead_virus in virus_board[i][j][chk_left_virus:]:
                                board[i][j]+=dead_virus//2
                            break
                    virus_board[i][j]= tmp_virus



        for i in range(N):
            for j in range(N):
                if virus_board[i][j]:
                    for virus in virus_board[i][j]:
                        if virus%5==0:
                            for d in dirs:
                                nPos = [i+d[0], j+d[1]]
                                if in_board(nPos[0], nPos[1], N):
                                    virus_board[nPos[0]][nPos[1]].append(1)
                board[i][j]+=plus_board[i][j]

    ans = 0
    for i in range(N):
        for j in range(N):
            if virus_board[i][j]:
                ans+=len(virus_board[i][j])

    return ans










if __name__ == "__main__":
    # print("Hello Wolrd")

    N, M, K = map(int, input().split())

    plus_board= [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    # print(N, M, K)
    # print(*plus_board, sep='\n')

    virus_board = [
        [list() for _ in range(N)]
        for _ in range(N)
    ]

    board = [[5]*N for _ in range(N)]

    for _ in range(M):
        R, C, age = map(int, input().split())
        virus_board[R-1][C-1].append(age)

    # print(*board, sep='\n')

    ans = simulation(board, virus_board, plus_board, N, K)

    print(ans)