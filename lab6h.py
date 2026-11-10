# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6h.py

# TO DO 1: Copy the code from lab6g.py and paste here.
# TO DO 2: Create function find_movie().
# TO DO 3: Call the function as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.

def add_movie(database, name, director, year, runtime):
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(movie)

def find_movie(database, search_word):
    result = []
    for movie in database:
        if search_word.lower() in movie["name"].lower():
            result.append(movie)
    return result

def main():
    movie_database = []
    add_movie(movie_database, 'Vishwanath & Sons', 'Venky Atluri', '2006', '101 minutes')
    add_movie(movie_database, 'Digger', 'Alejandro González Iñárritu', '2026', '128 minutes')
    add_movie(movie_database, 'Solo Mio', 'Charles Kinnane, Daniel Kinnane', '2026', '96 minutes')
    add_movie(movie_database, '28 Years Later: The Bone Temple', 'Nia DaCosta', '2026', '109 minutes')
    
    add_movie(movie_database, 'Gone with the wind', 'Victor Fleming', '1939', '238 minutes')
    add_movie(movie_database, 'Forever gone', 'Mikey McGregor', '2015', '3 minutes')
    print(find_movie(movie_database, 'gone'))
    print(find_movie(movie_database, "later"))

main()