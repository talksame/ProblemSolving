# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def dec_to_bin(n):
    #n이 0이거나 1일 경우에는 마지막에 도착한 경우이기 때문에 0또는 1을 반환한다.
    if n < 1:
        return '0'
    elif n == 1:
        return '1'

    # n이 아직 나눠질 수 있다면, 나눠지는 값에 따라서 0 또는 1을 추가해서 반환한다.
    # 다만, 반환되는 값이 문자열이기 때문에, 정수로 반환해서 재귀함수에 넣어준다.
    if n % 2 == 0:
        return dec_to_bin(int(n/2)) + '0'
    elif n % 2 == 1:
        return dec_to_bin(int(n/2)) + '1'
    
    # 여기에 코드를 작성하여 함수를 완성합니다.



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010