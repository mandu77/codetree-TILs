# import sys

# sys.stdin = open("input.txt", "r")

dirs = [[-1,0], [0,-1], [1,0], [0,1]]

def in_board(pos, storm_pos, N, M):
    return 0<=pos[0]<N and 0<=pos[1]<M and pos not in storm_pos

def storm(board, storm_pos, N,M,K):
    # 1. 먼지 확산
    # 2. 돌풍의 청소

    for _ in range(K):
        tmp_board = [[0]*M for _ in range(N)]
        # print(*tmp_board, sep='\n')

        for i in range(N):
            for j in range(M):

                if board[i][j]==-1:
                    continue

                cnt =0
                tmp_dust = board[i][j]//5
                for d in dirs:
                    next_dust = [i+d[0], j+d[1]]
                    if in_board(next_dust, storm_pos, N, M):
                        cnt+=1
                        tmp_board[next_dust[0]][next_dust[1]] += tmp_dust
                board[i][j]-=(tmp_dust*cnt)

        for i in range(N):
            for j in range(M):
                if board[i][j]==-1:
                    continue
                board[i][j]+=tmp_board[i][j]

        # print(*board, sep='\n')
        # 먼지 확산 끝

        # 돌풍 청소 시작!
        end_point = storm_pos[0][0]
        start_point = storm_pos[1][0]

        for i in range(end_point-1):
            # print(end_point-i)
            board[end_point-i-1][0] = board[end_point-i-1-1][0]
        else:
            board[0][0] = board[0][1]

        # print(*board, sep='\n')
        # print()

        board[0] = board[0][1:]
        board[0].append(board[1][M-1])

        for i in range(end_point):
            # print(i)
            board[i+1][M-1] = board[i+1+1][M-1]
        else:
            board[end_point][M-1] = board[end_point][M-1-1]

        board[end_point] =[-1,0]+ board[end_point][1:M-1]


        #윗 부분 돌풍 끝

        #아랫 부분 돌풍 시작

        for i in range(start_point+1, N-1):
            # print(i)
            board[i][0] = board[i+1][0]
        else:
            board[N-1][0] = board[N-1][1]

        board[N-1] = board[N-1][1:]
        board[N-1].append(board[N-1-1][M-1])

        # print(N-1)
        # print(start_point)
        for i in range(N-1-1, start_point,-1):
            # print(i)
            board[i][M-1] = board[i-1][M-1]

        board[start_point] = [-1,0] + board[start_point][1:M-1]

        # print(*board, sep='\n')

    ans =0
    for i in range(N):
        for j in range(M):
            if board[i][j]==-1:
                continue
            ans += board[i][j]

    return ans


if __name__ == '__main__':
    N,M,K = map(int, input().split())

    # print(N, M, K)

    board = []
    storm_pos = []
    for i in range(N):
        A = list(map(int, input().split()))
        if A[0]==-1:
            storm_pos.append([i,0])
        board+=[A]

    # print(*board,sep='\n')
    # print(storm_pos)

    ans = storm(board, storm_pos, N,M,K)

    print(ans)