import json
from pprint import pprint


def movie_info(movies, genres):
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']
    #영화를 담을 리스트 생성
    ans = []

    for movie in movies:
        #필요 요소 추출 및 장르 값 변경
        movie_temp = {}

        for key in key_list:
            movie_temp[key] = movie[key]
        
        genre_ids = movie['genre_ids']
        gerne_names = []

        for genre in genres: 
            if genre['id'] in genre_ids:
                gerne_names.append(genre['name']) 
        # 표현된 1개의 영화 딕셔너리를 리스트에 추가함.       
        movie_temp['gerne_names'] = gerne_names
        ans.append(movie_temp)

    return ans


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))