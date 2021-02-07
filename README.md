# Music Discovery App
Project 1 for cs490 at NJIT
Made by Samuel Muller, ID: scm42

## How to deploy this app:
  * Sign up for at https://developer.spotify.com/ and follow the steps listed there to create an app
  * Download this repository
  * Create a file named .env in the base directory and add the two lines that contain "export SPOTIFY_CLIENT='client-id'" and "export SPOTIFY_KEY='client-secret'" where client-id and client-secret are the id and secret keys that can be found through your Spotify developer dashboard
  * Optionally, change the artist codes on Line 28 of app.py to your favorite artists
  * run `pip install Flask` `pip install python-dotenv` and `pip install requests` to make sure you have everything installed
  * Run the application by typing `python app.py` in your terminal
  * Access the running app in your web browser '/'
## Known Problems
 * The styling is nonexistent on the finished web page. The preview image is much too large compared to the rest of the text and everything is made using default plain text with no specified layout horizontally or any background. This needs to be fixed by styling the page using CSS. This will be done by adding a stylesheet in a style.css file and linking to it in the header of index.html.
 * This app only works properly for songs with one artist. If there are multiple artists it will only display the first one. This could be fixed by changing the way the artist name is retrieved on Line 41 of `app.py`. It would need to get the length of the array of artists and if it contains more than one return a list of all of them. This list would then need to be handled either in `app.py` or in `index.html` to conditionally add commas and/or the word "and" between the names depending on how many names there are.
## Technical Problems I Encountered
 * I had trouble embedding the song preview in the web page. I've done some small stuff with HTML before but I've never had to use audio or video directly, so I googled how to embed audio in an HTML page and found a guide at https://www.w3schools.com/html/html5_video.asp which showed the basics of how to use video elements.
 * The JSON object returned by the Spotify API contains a lot of data and was hard to find what I needed in it. I used https://jsonformatter.org/json-parser to format the data more nicely so I could read it and figure out what to extract.
 * I wasn't familiar with Markdown syntax so I didn't know how to make this README. I used https://stackedit.io/ which is an in-browser Markdown editor so I could learn formatting.