# Music Discovery App
Project 1 for cs490 at NJIT
Made by Samuel Muller, ID: scm42
See the app at http://tranquil-brook-43836.herokuapp.com/


## How to deploy this app for yourself:
  * Sign up at https://developer.spotify.com/ and follow the steps listed there to create an app
  * Sign up to use the Genius API and get a client access token
  * Clone this repository
  * Create a file named .env in the base directory and add the three lines that say "export SPOTIFY_CLIENT='client id'", "export SPOTIFY_KEY='client secret'", and "export CLIENT_ACCESS_TOKEN='client access token'" where client id and client secret are the id and secret keys that can be found through your Spotify developer dashboard, and client access token is the access token you can get on the Genius dashboard
  * Optionally, change the artist codes on Line 28 of app.py to your favorite artists
  * run `pip install Flask` `pip install python-dotenv` and `pip install requests` to make sure you have everything installed
  * Run the application by typing `python app.py` in your terminal
  * Access the running app in your web browser '/'
## Deploy to Heroku
 * install Heroku CLI with `npm install -g heroku`
 * Create an account on signup.heroku.com
 * Create `requirements.txt` with "Flask", "requests", and "python-dotenv" on separate lines.
 * Create `Procfile` with the line `web: python app.py`
 * Login to Heroku and create a new Heroku app
 * Commit any changes you've made to the repository
 * Push the repository to Heroku
 * Add the environment variables in .env to heroku environment variables
 * Open the app with `heroku open`
## Known Problems
 * This app only works properly for songs with one artist. If there are multiple artists it will only display the first one. This could be fixed by changing the way the artist name is retrieved on Line 41 of `app.py`. It would need to get the length of the array of artists and if it contains more than one return a list of all of them. This list would then need to be handled either in `app.py` or in `index.html` to conditionally add commas and/or the word "and" between the names depending on how many names there are.
 * The link to see the lyrics will sometimes display the wrong song, especially if there's a more popular song with the same title on the Genius website. This is caused by the app searching only the title of the song and displaying the link to the first result. This could be fixed by adding the artist to the query on line 48 of app.py. It would need to be formatted in a way that the Genius API search would still work.
## Technical Problems I Encountered
 * I had trouble embedding the song preview in the web page. I've done some small stuff with HTML before but I've never had to use audio or video directly, so I googled how to embed audio in an HTML page and found a guide at https://www.w3schools.com/html/html5_video.asp which showed the basics of how to use \<video> elements. I used that to implement the preview in index.html
 * The data in the JSON object returned by the Spotify API is cluttered and it was hard to find what I needed in it. I used the Spotify API documentation to find some things, but that took a while. I decided to search for ways to display json data more nicely, so I googled it. I found and used https://jsonformatter.org/json-parser to format the data more nicely so I could read it and figure out what to extract.
 * I wasn't familiar with Markdown syntax so I didn't know how to make this README. I used https://stackedit.io/ which is an in-browser Markdown editor so I could learn formatting.
