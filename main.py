import pandas as pd
import requests

response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=d91ec96cdd77636f350c8675e86035d6&language=en-US&page=1')
df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
df.head()
df = pd.DataFrame()

for i in range(1,429):
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=d91ec96cdd77636f350c8675e86035d6&language=en-US&page={}'.format(i))
    temp_df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
    df = pd.concat([df, temp_df], ignore_index=True)

df.to_csv('TopMovies.csv')