# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:27:45 2018
Udacity FSWD Course 1 - Mini project 1: Movie Webpage
@author: ALLAN
"""

import webbrowser
from urllib import urlopen
# python 3 urllib.request
import json


# Main constructor to organize movie information and display movie trailers
class Movie():
    """Define movie parameters and open youtube trailer"""

    def __init__(self, title, plot, rating, runtime, poster, youtube_trailer):
        self.title = title
        self.storyline = plot
        self.rating = rating
        self.runtime = runtime
        self.poster_image_url = poster
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        """ Show YOUTUBE trailer for specified movie"""
        webbrowser.open(self.trailer)


# METHOD TO CALL MOVE DATA FROM OMDB
def get_data(movie):
    """fucntion calls movie data from OMDB API and returns data"""
    data = urlopen("http://www.omdbapi.com/?t=" + movie +
                   "&apikey=883d566b").read()
    raw_data = str(data)
    json_data = json.loads(raw_data)
    return(json_data)


def apply_movie(movie_title, trailers):
    """input movie title and trailer list to organize the data and
    apply the Movie class."""
    mov_data = get_data(movie_title)
    movie = Movie(mov_data["Title"], mov_data["Plot"],
                  mov_data["imdbRating"], mov_data["Runtime"],
                  mov_data["Poster"], trailers[movie_title])
    return(movie)
