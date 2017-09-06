import webbrowser

class Movie():
    '''Class movie contains movie related information: must be given 1.title, 2.storyline, 3.poster, 4.trailer, 5.length & 6.rating attributes in that order'''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_length, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.length = movie_length
        self.rating = movie_rating

    def show_trailer(self):
        '''function show_trailer() needs to be passed a class movie object and will open a web page to the movie's trailer on youtube'''
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        '''function show_poster() needs to be passed a class movie object and will open a web page to the movie's poster image'''
        webbrowser.open(self.poster_image_url)
