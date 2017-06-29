import webbrowser


class Movie():
    """This class provides a way of storing movie information.

    Attributes:
        movie_title     (str): Movie Title
        movie_storyline (str): Storyline of Movie
        poster_image    (str): URL of poster image
        trailer_youtube (str): URL of youtube trailer
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # This variable is in all caps
    #  because it should not change value.

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
