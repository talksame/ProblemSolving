### A. 제공되는 영화 데이터의 주요내용 수집

- **요구사항 확인**

  - 필요한 키에 해당하는 정보를 가지고 온다.
  - 데이터는 movie.json 파일을 활용하고, 이 파일은 쇼생크 탈출의 정보를 가지고 있다.

  

- **코드 및 주석**

  ```python
  def movie_info(movie):
      # 필요한 키값 저장
      key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
      ans = {}
  
      # 필요한 요소만 추출
      for key in key_list:
          ans[key] = movie[key]
      return ans
  ```

  

- **해설**

  - 우선은 추출이 필요한 키 값을 저장한 리스트를 선언한다.

  - 반복문을 통해서, 현재 movie 가 가지고 있는 키값과 필요 키 리스트를 비교를 한다.

  - movie가 가지고 있는 키가 필요 키 리스트에 있다면 최종 ans딕셔너리에 반환해준다.

    

### B. 제공되는 영화 데이터의 주요내용 수정

- **요구사항 확인**

  - 필요한 키에 해당하는 정보를 가지고 온다.
  - 데이터는 movie.json 파일을 활용하고, 이 파일은 쇼생크 탈출의 정보를 가지고 있다.
  - gener_ids를 genre_names로 바꾸고, 해당 번호의 정보를 movie에서 받아와 딕셔너리에 새롭게 추가한다.

  

- **코드 및 주석**

  ```python
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
  ```

  

- **해설**
  - 우선은 추출이 필요한 키 값을 저장한 리스트를 선언한다.
  - 반복문을 통해서, 현재 movie 가 가지고 있는 키값과 필요 키 리스트를 비교를 한다.
  - 영화가 가지고 있는 genre를 반복문으로 탐색한다.
  - 해당하는 인덱스의 장르를 genre_names 리스트에 추가하고, 딕셔너리에 추가한다.
  - ans딕셔너리에 반환해준다.



### C. 다중 데이터 분석 및 수정

- **요구사항 확인**

  - 평점이 높은 영화데이터를 모두 사용한다.
  - 평점이 높은 영화 데이터 중, 필요한 키만 반환하는 함수를 작성한다.
  - 데이터는 movie.json, genres.json 파일을 활용하고, 이 파일은 쇼생크 탈출의 정보를 가지고 있다.

  

- **코드 및 주석**

  ```python
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
  ```

  

- **해설**

  - 영화를 담을 리스트를 생성한다.

  - 반복문을 통해서 1개 영화에 대한 임시 movie dict를 생성한다.

    - 우선은 추출이 필요한 키 값을 저장한 리스트를 선언한다.
    - 반복문을 통해서, 현재 movie 가 가지고 있는 키값과 필요 키 리스트를 비교를 한다.
    - movie가 가지고 있는 키가 필요 키 리스트에 있다면 임시 movie딕셔너리에 반환해준다.

  - 생성한 임시 movie 딕셔너리를 최종 ans 리스트에 담아준다.

  - ans딕셔너리에 반환해준다.

    



### D. 알고리즘을 통한 데이터 출력

- **요구사항 확인**

  - 세부적인 영화 정보 중 수익 정보(revenue)를 이용하여 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성합니다. 
  - 영화 세부 정보는 . data/movies/ 안에 있는 파일이다.
  - movies.json과 movies폴더 내부의 파일들을 사용합니다.

  

- **코드 및 주석**

  ```python
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
  ```

  

- **해설**
  - 수입과 제목을 저장할 변수를 선언합니다.
  - 반복문을 통해서 임시 영화리스트에 각 파익들의 json 파일을 저장합니다.
  - 반복문을 통해서, 현재 movie 가 가지고 있는 수입이 기존의 max_income 보다 크다면, 그 값을 변경해줍니다.
  - max_title 도 같이 변경해줍니다.
  - 최종적인 max_title를 반환해줍니다.



### E. 알고리즘을 통한 데이터 출력

- **요구사항 확인**

  - 세부적인 영화 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성합니다.
  - 영화 세부 정보는 . data/movies/ 안에 있는 파일이다.
  - movies.json과 movies폴더 내부의 파일들을 사용합니다.

  

- **코드 및 주석**

  ```python
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
  ```

  

- **해설**
  - 결과를 담을 res 리스트를 선언합니다.
  - json 파일을 열어 리스트에 담습니다.
  - 담은 json 파일의 'release_data' 정보만 받아옵니다.
  - 개봉일의 정보가 YYYY-MM-DD 형식이기 때문에 5~7이 문자열 12라면 12월로 간주하고, 그 영화제목 정보를 추출합니다
  - 추출한 정보를 리스트에 담습니다.
  - 최종적인 res 리스트를 반환합니다.