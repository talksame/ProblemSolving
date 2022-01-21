import json
from pprint import pprint


def movie_info(movie):
    # 필요한 키값 저장
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    ans = {}

    # 필요한 요소만 추출
    for key in key_list:
        ans[key] = movie[key]
    return ans
  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))