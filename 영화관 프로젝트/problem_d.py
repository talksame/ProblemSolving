import json


def max_revenue(movies):
    #변수 초기화 수익과 제목
    max_income = 0  
    max_title = ''

    #영화 정보 세부사항 받아오기
    for movie in movies:
        movie_list = open("data/movies/"+str(movie['id'])+".json", encoding='UTF8')
        movie_temp = json.load(movie_list) 
        # 수익을 비교해서 기존의 최대보다 크면, 최대값을 갱신하기.
        if max_income < movie_temp['revenue']:
            max_income = movie_temp['revenue']
            max_title = movie_temp['title']
    return max_title 
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))