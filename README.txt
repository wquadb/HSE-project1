short-guide

script finds MMA(MostMentionedArtist) & counts released songs, from spotify's .CSV data
1. script finds most mentioned artist in the database
2. script counts amount of songs released in Spotify in each i-th year, from x-year to y-year

To run the script:
"python3 main.py <location of .csv>"

.CSV should be as following:
playlist_url,year,*,*,*,*,artist_id,artist_name,artist_genres,artist_popularity,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature

