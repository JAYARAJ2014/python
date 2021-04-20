import json
from pathlib import Path


def writejson():
    movies = [
        {"id": 1, "title": "Terminator", "year": 1984},
        {"id": 2, "title": "KG Cop", "year": 1993},
        {"id": 3, "title": "Gods Must be Crazy", "year": 1984}
    ]

    data = json.dumps(movies)
    # print(data)

    Path("movies.json").write_text(data)


def readjson():
    data = Path("movies.json").read_text()

    movies = json.loads(data)
    for movie in movies:
        print(f"{movie['id']}\t{movie['title']}")


readjson()
