class Movie:
    
    # constructor
    # define the properties of a class as self._property_name
    def __init__(self, title, release_year, age_rating, director):
        self._title = title
        self._release_year = release_year
        self._age_rating = age_rating
        self._director = director
        
    def details(self):
        det_str = f"{self._title} ({self._release_year}), rated {self._age_rating}, directed by {self._director}"
        return det_str