# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    '''
    2가지를 우선 고려한다
    대문자는 대문자에서 순환을 하고,
    소문자는 소문자에서 순한을 한다.

    그래서 아스키 값이 97보다 큰 경우에는 소문자에서만 순환하게 하고,
    아스키 값이 90보다 작은 경우에는 대문자에서만 순환하게 한다.

    만약에, n을 더한 값이 122를 초과할 경우에는 소문자는 97로 초기화를 하고,
    대문자는 65로 초기화를 해서 다시 연산한다.

    res 라는 변수에 최종문자를 하나씩 추가한다.

    '''
    res = ''

    for i in word:
        temp = ord(i)
        if temp >= 97:
            if temp + n > 122:
                temp = 97 + (temp - 123) + n
            else:
                temp += n
        elif temp <= 90:
            if temp + n > 97:
                temp = 65 + (temp - 91) + n
            else:
                temp += n
        res += chr(temp)
    return res
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx