print("Welcome to the movie app!\n")

choice = "y"

# Requirement: Add a list to store movies
# - Store movies in the list
# - Print list of movies when program ends
movie_list = []

while choice != "n":
    # Step 1: Prompt user for attributes for a movie & store them in variables: title, release year, age rating, and director
    # Star Wars, 1977, PG, George Lucas
    title = input("Enter movie title: ")
    release_year = int(input("Movie Release Year: "))
    age_rating = input("Age Rating: ")
    director = input("Director: ")
    
    # movie_tuple is a single movie
    movie_tuple = (title, release_year, age_rating, director)
    # add this movie to the list
    movie_list.append(movie_tuple)

    # Step 2: Prompt user for how many tickets to buy and store as a whole number
    num_tix = int(input("# of tickets: "))

    # Step 3: Display ticket purchase summary as follows:
    # Movie: Star Wars (1977), rated PG, directed by George Lucas
    # Tickets Purchased - 3 @ $11.75 each, total: 
    total_cost = num_tix * 11.75

    print("\n===== Movie Ticket Purchase Summary =====")
    print(f"Movie: {title} ({release_year}), rated {age_rating}, directed by {director}")
    print(f"Tickets Purchased - {num_tix} @ $11.75 each, total: ${total_cost}")
    
    choice = input("\nContinue(y/n): ")

print("\n===== Movie List ======")
# 1st - print movie list
#print(movie_list)
# 2nd - loop through movie list and print each movie
print("Title\t\tYear\t\tRating\t\tDirector")
# range for:
# for idx in range(0,len(movie_list)):
#     print(f"{movie_list[idx][0]}\t{movie_list[idx][1]}\t{movie_list[idx][2]}\t{movie_list[idx][3]}")

# for x in range(...,...)
for movie in movie_list:
    print(f"{movie[0]}\t\t{movie[1]}\t\t{movie[2]}\t\t{movie[3]}")

print("bye")