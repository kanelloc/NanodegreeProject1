import media
import fresh_tomatoes

# Create 3 instances of class Movie from  media.py
toy_story = media.Movie("Toy Story",
                        "A story of a boy with his toys",
                        "https://upload.wikimedia.org/wikipedia/el/thumb/4/44/220px-Movie_poster_toy_story.jpg/250px-"
                        "220px-Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser"
                     "-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

fast_and_furious = media.Movie("Fast and the Furious 5 ",
                               "Fast Five (alternatively known as Fast & Furious 5[1] or Fast & Furious 5: Rio Heist"
                               "[4]) is a 2011 American action film directed by Justin Lin and written by Chris Morgan",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Fast_Five_poster.jpg/220px-Fast_"
                               "Five_poster.jpg",
                               "https://www.youtube.com/watch?v=bf4oDjHUmkY")

# create movies list for the fresh_tomatoes.py
movies = [toy_story, avatar, fast_and_furious]

# call open_movies_page function from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
