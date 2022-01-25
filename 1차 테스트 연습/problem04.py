import json


def turn(temperatures):
    dict_temp = {
        'maximum' : [],
        'minimum' : []
    }
    for i in temperatures:
        dict_temp['maximum'].append(i[0])
        dict_temp['minimum'].append(i[1])
    return dict_temp
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }
