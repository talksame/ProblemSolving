# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_password_length(password):
    # 조건문을 통해서 password 의 길이가 범위를 만족하면 True
    # 범위를 초과하거나 부족하면 False를 반환한다.
    if 8 <= len(password) <= 32:
        return True
    return False
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    password = 'q1w2e3r4'
    print(check_password_length(password)) # True
