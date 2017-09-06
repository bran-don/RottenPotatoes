import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "the secret life of your toys",
                        "https://lumiere-a.akamaihd.net/v1/images/o"
                        "pen-uri20150422-20810-m8zzyx_5670999f.jpeg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc", "81 minutes", "G")

avatar = media.Movie("Avatar", "Resource Extraction 101",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "161 minutes", "PG13")

jwick = media.Movie("John Wick", "They probably shouldn't've messed with this guy",
                    "https://s-media-cache-ak0.pinimg.com/736x/03/d9/1b/03d91b0554084144eb613d6da0e8c032.jpg",
                    "https://www.youtube.com/watch?v=RllJtOw0USI", "101 minutes", "R")

arrival = media.Movie("Arrival", "First Contact",
                      "http://cdn2-www.comingsoon.net/assets/uploads/gallery/arrival/cp8v8n0vmaadzn6-jpg-large.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g", "116 minutes", "PG13")

wam = media.Movie("We Are Marshal", "Football team overcomes adversity",
                  "https://i.jeded.com/i/we-are-marshall.18837.jpg",
                  "https://www.youtube.com/watch?v=y3V6Qz3zz4s",
                  "124 minutes", "PG")

bernie = media.Movie("Bernie",
                     "A small-town mortician strikes up a friendship with a wealthy widow. When she becomes controlling, he goes to great lengths to separate himself from her grasp.",
                     "https://upload.wikimedia.org/wikipedia/en/0/04/Bernie_film_poster.jpg", "https://youtu.be/YJuhWKcY_6U?t=1m7s", "104 minutes", "PG13")

movies = [
    toy_story, avatar, jwick,
    arrival, wam, bernie
    ]

fresh_tomatoes.open_movies_page(movies)