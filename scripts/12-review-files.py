# read in the movies.txt file and print all movies to the console, cleanly (summarized)

from classes.movie import Movie


movies_list = []
with open('./scripts/files/movies.txt') as file_in:
    movies_split_lines = file_in.read().splitlines()
    # parse each line into a movie
    for line in movies_split_lines:
        movie_raw = line.split(',')
        title = movie_raw[0]
        year = movie_raw[1]
        rating = movie_raw[2]
        director = movie_raw[3]
        movie = Movie(title, year, rating, director)
        movies_list.append(movie)
    
print("--- movies in our file ---")
for m in movies_list:
    print(m.details())