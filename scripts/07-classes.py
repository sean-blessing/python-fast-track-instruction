# class Movie:
    
#     # constructor
#     # define the properties of a class as self._property_name
#     def __init__(self, title, release_year, age_rating, director):
#         self._title = title
#         self._release_year = release_year
#         self._age_rating = age_rating
#         self._director = director
        
#     def details(self):
#         det_str = f"{self._title} ({self._release_year}), rated {self._age_rating}, directed by {self._director}"
#         return det_str

# Create instances of the Movie class

from classes.movie import Movie


m1 = Movie("Star Wars", 1977, "PG", "George Lucas")
m2 = Movie("E.T.", 1984, "PG", "Steven Spielberg")

# Store the movies in a list
movies = [m1, m2]

print("Print movies...")
for movie in movies:
    print(movie.details())


        
        