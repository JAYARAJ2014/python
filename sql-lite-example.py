import sqlite3
import json
from pathlib import Path


def readjsondata():
    # read json file and convert it to json object
    movies = json.loads(Path("movies.json").read_text())
    print(movies)
    return movies


# db.sqlite3
def writemoviestodb():
    with sqlite3.connect("db.sqlite3") as connection:
        command = "INSERT INTO Movies VALUES(?,?,?)"
        for movie in movies:
            connection.execute(command, tuple(movie.values()))
        connection.commit()


def readmoviesfromdb():
    with sqlite3.connect("db.sqlite3") as connection:
        command = "SELECT * FROM Movies"
        cursor = connection.execute(command)
        for row in cursor:
            print(row)
        connection.commit()


readmoviesfromdb()
###
# Notes:
# sudo apt-get update
# sudo apt-get install sqlitebrowser

###
