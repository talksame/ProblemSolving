# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_final_position(N, mat, moves):
    dx = [1, 1, 2, 2]
    dy = [-2, 2, -1, 1]
    # 이동방향에 대한 dx, dy 값을 선언한다.

    # mat 에 담겨저 있는 1의 위치를 이중반복문으로 찾는다.
    # 이 1의 위치는 position이 된다.
    for i in range(len(mat)):
        for s in range(len(mat[i])):
            if mat[i][s] == 1:
                position = [i, s]
    
    # 움직일 때 마다, 캐릭터가 정상적인 범위 안에 있는지 확인을 하고,
    # 정상적인 범위 안에 있다면, 그때 position을 갱신한다.
    for m in moves:
        if 0<= position[1] + dx[m] < N and 0 <= position[0] + dy[m] < N:
            position[1] = position[1] + dx[m]
            position[0] = position[0] + dy[m]
        else:
            # 만약에 범위를 나간다면, None을 리턴한다.
            return "None"
    # 움직인 취종 위치를 반환한다.
    return position
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1)) # [2, 1]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2)) # [1, 2]