# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:07:38 2018
Run movie website
Project 1 Udacity FSWD
@author: ALLAN
"""

import media
from media import get_data, apply_movie
import fresh_tomatoes

# 1. INPUT LIST OF MOVIES AND TRAILER LINKS
#input_movies = 
input_trailers = {"Frozen": "https://www.youtube.com/watch?v=-WdC4DaYIeQ", "Little+Bear":"https://www.youtube.com/watch?v=kv49vjUor6Q",
        "Cinderella": "https://www.youtube.com/watch?v=cL-RjWKtZrM", "Olaf's+Frozen": "https://www.youtube.com/watch?v=HE2Ku_o_NNE",
        "Little+Mermaid": "https://www.youtube.com/watch?v=ZGZX5-PAwR8"} 


frozen = apply_movie("Frozen", input_trailers)
cinderella = apply_movie("Cinderella", input_trailers)
little_bear = apply_movie("Little+Bear", input_trailers)
little_mermaid = apply_movie("Little+Mermaid", input_trailers)
olafs_adventures = apply_movie("Olaf's+Frozen", input_trailers)

mov_list = [frozen, cinderella, little_bear, little_mermaid, olafs_adventures]
# movies = [frozen, cinderella, olafs_adventures, little_bear]
fresh_tomatoes.open_movies_page(mov_list)
