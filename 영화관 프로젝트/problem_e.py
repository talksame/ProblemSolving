import json


def dec_movies(movies):
    #결과를 담을 리스트
    res = []

    for i in movies:
         # json 파일 열기
        movie_list = open("data/movies/"+str(i['id'])+".json", encoding='UTF8')
        movie_temp = json.load(movie_list)

    
        release_dates = movie_temp['release_date']
        # YYYY-MM-DD 이기 때문에 5~6번 글자가 12이면 결과에 추가해줌.
        if release_dates[5:7] == '12':
            res.append(movie_temp['title'])

    return res

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))