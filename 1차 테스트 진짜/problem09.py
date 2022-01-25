# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    # 0~3 까지 각각의 방향값을 저장한 리스트이다. 0번은 위로, 1번은 아래로를 x, y 축으로 저장했다.
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]


    # 파라미터에 있는 position 의 값에 dx, dy 의 방향을 더해준다.
    # 그리고 그 값이 0 이상 N 미만의 값인지 확인하고 x, y 축 둘다 조건에 만족한다면 True를 반환하고
    # 아니라면 False를 반환한다.
    if 0 <= position[0] + dy[M] < N and 0 <= position[1] + dx[M] < N:
        return True
    return False
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0))) # True
    print(is_position_safe(3, 0, (0, 0))) # False
