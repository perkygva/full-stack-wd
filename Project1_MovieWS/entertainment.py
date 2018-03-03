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
fzn_url = "https://www.youtube.com/watch?v=-WdC4DaYIeQ"
lbr_url = "https://www.youtube.com/watch?v=kv49vjUor6Q"
cnd_url = "https://www.youtube.com/watch?v=cL-RjWKtZrM"
olf_url = "https://www.youtube.com/watch?v=HE2Ku_o_NNE"
lmer_url = "https://www.youtube.com/watch?v=ZGZX5-PAwR8"

input_trailers = {"Frozen": fzn_url, "Little+Bear": lbr_url,
                  "Cinderella": cnd_url, "Olaf's+Frozen": olf_url,
                  "Little+Mermaid": lmer_url}

# 2. Call apply_movie function from media.py
frozen = apply_movie("Frozen", input_trailers)
cinderella = apply_movie("Cinderella", input_trailers)
little_bear = apply_movie("Little+Bear", input_trailers)
little_mermaid = apply_movie("Little+Mermaid", input_trailers)
olafs_adventures = apply_movie("Olaf's+Frozen", input_trailers)

# 3. Create movie list and fresh tomatoes
mov_list = [frozen, cinderella, little_bear, little_mermaid,
            olafs_adventures]
fresh_tomatoes.open_movies_page(mov_list)
