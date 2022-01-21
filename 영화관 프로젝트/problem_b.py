import json
from pprint import pprint


def movie_info(movie, genres):

    # 필요한 키값 저장
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']
    ans = {}

    # 필요한 요소만 추출
    for key in key_list:
        ans[key] = movie[key]

    # 장르 추출
    genre_ids = movie['genre_ids']
    gerne_names = []

    for genre in genres: 
        if genre['id'] in genre_ids:
            gerne_names.append(genre['name']) 

    ans['gerne_names'] = gerne_names
    return ans

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))