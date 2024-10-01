# import sys


# sys.stdin=open("input.txt", "r")

#위 아래 오른쪽 왼쪽
dirs = [[-1,0],[1,0],[0,1],[0,-1]]

def find_pos(pos, dir, size, speed):
    if dir == 1:
        if speed> size-pos-1:
            tmp = size-pos-1
            chk_dir = (speed-tmp)//(size-1)
            chk_pos = (speed-tmp)%(size-1)

            if chk_dir%2==0:
                return size-1-chk_pos, 0
            else:
                return chk_pos, 1
        else:
            return pos+speed, dir

    else:
        if pos < speed:
            chk_dir = (speed-pos)//(size-1)
            chk_pos = (speed-pos)%(size-1)

            if chk_dir%2 ==0:
                return chk_pos, 1
            else:
                return size-1-chk_pos, 0


        else:
            return pos-speed, dir



def simulate(board, N, M, K):



    ans = 0

    for student in range(M):
        tmp_board = [
            list([] for _ in range(M))
            for _ in range(N)
        ]
        for mold in range(N):
            if board[mold][student]:
                ans += board[mold][student][2]
                board[mold][student] = []
                break;

        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    speed, direction, volume = board[i][j]

                    if direction <2:
                        if direction ==0:
                            ni,d = find_pos(i, 0, N, speed)
                        else:
                            ni,d = find_pos(i,1,N, speed)

                        # if d == 0:
                        #     tmp_board[ni][j].append([speed, 0,volume])
                        # else:
                        #     tmp_board[ni][j].append([speed, 1, volume])
                        if d==0:
                            return_dir = 0
                        else:
                            return_dir =1

                        # if tmp_board[ni][j]:
                        #     if tmp_board[ni][j][2]<volume:
                        #         tmp_board[ni][nj] = [speed, return_dir, volume]
                        # else:
                        #     tmp_board[ni][nj] = [speed,return_dir,volume]

                        if tmp_board[ni][j] ==[] or tmp_board[ni][j][2]<volume:
                            tmp_board[ni][j] = [speed,return_dir,volume]


                    else:
                        if direction==3:
                            nj,d = find_pos(j, 0, M, speed)
                        else:
                            nj,d= find_pos(j, 1, M, speed)

                        # if d ==0:
                        #     tmp_board[i][nj].append([speed, 3, volume])
                        # else:
                        #     tmp_board[i][nj].append([speed, 2, volume])
                        if d == 0:
                            return_dir =3
                        else:
                            return_dir=2

                        if tmp_board[i][nj] ==[] or tmp_board[i][nj][2]<volume:
                            tmp_board[i][nj] = [speed,return_dir,volume]


        # print()
        # print(*tmp_board, sep='\n')

        for i in range(N):
            for j in range(M):
                board[i][j] = tmp_board[i][j]

    return ans

if __name__=="__main__":
    N, M, K = map(int, input().split())

    board = [
        [list() for _ in range(M)]
        for _ in range(N)
    ]

    for _ in range(K):
        x,y,s,d,b = map(int, input().split())
        # board[x-1][y-1].append([s,d-1,b])
        board[x-1][y-1] = [s,d-1,b]
    # print(*board, sep='\n')
    # print(board[1][0])

    ans = simulate(board, N, M, K)

    print(ans)