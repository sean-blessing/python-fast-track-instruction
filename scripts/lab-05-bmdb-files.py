from classes.movie import Movie

print("Welcome to the movie app!\n")

choice = "y"

# Requirement: Add file io to read in a movie file at beginning, and write it out at end
movie_list = []

# read lines into a list
with open('./scripts/files/movies.txt') as file_in:
    movie_csv_list = file_in.read().splitlines()

# loop through list to create instances of movie and add to movie_list
for movie_csv in movie_csv_list:
    movie_data = movie_csv.split(",")
    movie = Movie(movie_data[0], movie_data[1], movie_data[2], movie_data[3])
    movie_list.append(movie)

print("\n==== Current Movie List ====")
for movie in movie_list:
    print(movie.details())
print()

while choice != "n":
    # Step 1: Prompt user for attributes for a movie & store them in variables: title, release year, age rating, and director
    # Star Wars, 1977, PG, George Lucas
    title = input("Enter movie title: ")
    release_year = int(input("Movie Release Year: "))
    age_rating = input("Age Rating: ")
    director = input("Director: ")
    
    # create an instance of movie
    movie = Movie(title, release_year, age_rating, director)
    # add this movie to the list
    movie_list.append(movie)

    # # Step 2: Prompt user for how many tickets to buy and store as a whole number
    # num_tix = int(input("# of tickets: "))

    # # Step 3: Display ticket purchase summary as follows:
    # # Movie: Star Wars (1977), rated PG, directed by George Lucas
    # # Tickets Purchased - 3 @ $11.75 each, total: 
    # total_cost = num_tix * 11.75

    print("\n===== Movie Summary =====")
    print(f"Movie: {title} ({release_year}), rated {age_rating}, directed by {director}")
    #print(f"Tickets Purchased - {num_tix} @ $11.75 each, total: ${total_cost}")
    
    choice = input("\nContinue(y/n): ")

print("\n===== Movie List ======")

#loop through movie_list and write to file
with open("./scripts/files/movies.txt", "w") as movies_out:
    for movie in movie_list:
        print(movie.details())
        movies_out.write(f"{movie._title},{movie._release_year},{movie._age_rating},{movie._director}\n")

print("bye")