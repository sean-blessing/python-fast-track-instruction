fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
 "ORANGE", "lime", "Watermelon", "guava", "papaya" "FIG", "pear", "banana",
 "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
 "grape"]
print(f'fruits unsorted: {fruits}')
# fruits.sort() # sorts the list 'in place'
sorted_fruits = sorted(fruits, key=str.lower)

print(f'fruits sorted using sorted( , str.lower)')
print(f'fruits: {sorted_fruits}')

print(f'---- custom sort - using a custom function')
def ignore_case(word):
    return word.lower()
# person_name = "Robert Redford"
# print(f"{person_name}, ignore_case: {ignore_case(person_name)}")
sorted_fruits_2 = sorted(fruits, key=ignore_case)
print(f'fruits sorted 2: {sorted_fruits_2}')

# p. 168
print("-- sorting book titles but ignoring the word 'the'")
books= [
 "A Study in Scarlet",
 "The Sign of the Four",
 "The Hound of the Baskervilles",
 "The Valley of Fear",
 "The Adventures of Sherlock Holmes",
 "The Memoirs of Sherlock Holmes",
 "The Return of Sherlock Holmes",
 "His Last Bow",
 "The Case-Book of Sherlock Holmes",
 ]

print(f'books: {books}')
sort_books_1 = sorted(books, key=str.lower)
print(f'sorted books 1: {sort_books_1}')

def strip_article(title): #create function which takes element to compare and returns comparison key
    title = title.lower()
    for article in 'a ', 'an ', 'the ':
        if title.startswith(article):
            title = title.removeprefix(article) #remove article
            break
    return title

# print("test strip_article function...")
# for book in books:
#     print(f'book: {book}, article removed version: {strip_article(book)}')

# sort books using sorted function
sorted_books_2 = sorted(books, key=strip_article)
print(f'sorted books 2: {sorted_books_2}')

# one more sorting example to drive it home
people_list = ['Mr. Smith', 'Mrs. Dickerson', 'Mrs. Anderson', "Mr. Blessing", "Mrs. Peace"]
print(f'people unsorted: {people_list}')
people_sorted_1 = sorted(people_list, key=str.lower)
print(f'people sorted 1: {people_sorted_1}')

def strip_mr_mrs(person_name):
    person_name = person_name.lower();
    for salutation in 'mr. ', 'mrs. ':
        if person_name.startswith(salutation):
            person_name = person_name.removeprefix(salutation)
            break
    return person_name
people_sorted_2 = sorted(people_list, key=strip_mr_mrs)
print(f'people sorted 2: {people_sorted_2}')