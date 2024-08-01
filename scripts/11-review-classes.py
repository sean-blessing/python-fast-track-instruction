# prompt user for a new movie (title, year, rating, director)

from classes.movie import Movie


movies = []

title = input("Movie Name: ")
year = input("Release Year: ")
rating = input("Age Rating: ")
director = input("Director: ")
movie = Movie(title, year, rating, director)
movies.append(movie)

print(f'Movie Information: {title}, {year}, {rating}, {director}')
# another way to print this information:
# print('Movie Information (again): '+title+', '+year)

# create more movies and store in a list

