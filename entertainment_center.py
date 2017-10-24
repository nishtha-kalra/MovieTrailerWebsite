import fresh_tomatoes
import media

""""Creating instances of class Movie"""

# La La Land Movie: movie title, story line, poster image and title
la_la_land = media.Movie(
    "La La Land",
    "This original musical about everyday life explores the joy and pain "
    "of pursuing your dreams.",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  # NOQA
    "https://www.youtube.com/watch?v=0pdqf4P9MB8"
    )

# Queen Movie: movie title, story line, poster image and title
queen = media.Movie(
    "Queen",
    "Journey of a heart broken girl who finds herself.",
    "https://upload.wikimedia.org/wikipedia/en/4/45/QueenMoviePoster7thMarch.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KGC6vl3lzf0&t=3s"
    )

# Planet of the Apes Movie: movie title, story line, poster image and title
planet_of_apes = media.Movie(
    "War For The Planet Of The Apes",
    "War between apes and human for survival.",
    "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=qxjPjPzQ1iU"
    )

# Rockstar Movie: movie title, story line, poster image and title
rockstar = media.Movie(
    "Rockstar",
    "Story of a person from a simple man to a rockstar.",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Rockstar-Movie-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=bD5FShPZdpw"
    )

# Dumb and Dumber Movie: movie title, story line, poster image and title
dumb_and_dumber = media.Movie(
    "Dumb And Dumber",
    "Comedy of two dumb friends.",
    "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",  # NOQA
    "https://www.youtube.com/watch?v=l13yPhimE3o"
    )

# Dangal Movie: movie title, story line, poster image and title
dangal = media.Movie(
    "Dangal",
    "Biographical sports drama film loosely based on the story of "
    "Mahavir Singh Phogat and his daughters.",
    "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=x_7YlGv9u1g"
    )

"""Creating a list of all movie instances"""
movies_list = [
    la_la_land,
    queen,
    planet_of_apes,
    rockstar,
    dumb_and_dumber,
    dangal
    ]

fresh_tomatoes.open_movies_page(movies_list)
