# full-stack-wd
Udacity Nanodegree Projects and Files
by: Allan Perk

## Project 1: Movie Website
This is the first project of Udacity's Full Stack Nanodegree.

It is a simple script to create a webpage to host movie names, posters, and link to the movie's trailer on youtube by 
clicking on the poster.

### Running the script

1. Download and install python 2 if you do not already have it.
2. Fork this repo or download the files. (fresh_tomatoes.py, media.py, entertainment.py)
3. Open python IDLE or spyder if running Anaconda.
4. Open the file entertainment.py in IDLE or alternative python IDE (spyder, etc) and run script via RUN > RUN MODULE.

### What the code does!
- The entertainment.py file imports the methods below and applies them to the data inputted. After it creates a list of the of the "movies" and runs the fresh_tomatoes file which creates the webpage.
  - The get_data method (functions) pull all the movie information from the OMDB database.
  - The apply_movie function applies the class Movie and returns the data in the required format to run
- At the moment, a list of youtube trailer urls is required, but the intention was to have these pulled from an API as well.

That's it, your website should open with the poster of your favorite movies (or my favorite movies) and you can visualize the trailer's by clicking on the poster.
