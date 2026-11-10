# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

# TO DO 1: Create function add_movie(). 
# TO DO 2: Call the function 4 times.
# TO DO 3: Print the database as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.

def add_movie(database, name, director, year, runtime):
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(movie)



def main():
    movie_database = []
    add_movie(movie_database, 'Vishwanath & Sons', 'Venky Atluri', '2006', '101 minutes')
    add_movie(movie_database, 'Digger', 'Alejandro González Iñárritu', '2026', '128 minutes')
    add_movie(movie_database, 'Solo Mio', 'Charles Kinnane, Daniel Kinnane', '2026', '96 minutes')
    add_movie(movie_database, '28 Years Later: The Bone Temple', 'Nia DaCosta', '2026', '109 minutes')

    for movie in movie_database:
        print(movie)

main()
