short-guide

script finds MMA(MostMentionedArtist) & counts released songs, from spotify's .CSV data
1. script finds most mentioned artist in the database
2. script counts amount of songs released in Spotify in each i-th year, from x-year to y-year

To run the script:
"python3 main.py <location of .csv> -s -m"
'-m' - to get the MMA(most mentioned artist in the database)
'-s' - to get the amount of songs released in each i-th year, from x-year to y-year in the database

.CSV should be as following:
*,year,*,*,*,*,artist_id,artist_name,*,*,...
column[1], column[6], column[7] should be filled