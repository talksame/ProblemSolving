# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_duplicate_id(target_username, username_list):
    # 조건문을 통해서 만들고 싶은 아이디가 기존의 유저 리스트이 있는 경우에는 true
    # 없는 경우에는 False를 반환해준다.
    if target_username in username_list:
        return True
    return False
    # 여기에 코드를 작성하여 함수를 완성합니다.
    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    target_username = 'jungssafy'
    username_list = ['kimssafy', 'jungssafy']
    print(check_duplicate_id(target_username, username_list)) # True
