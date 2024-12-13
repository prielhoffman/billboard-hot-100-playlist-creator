# Billboard Hot 100 Playlist Creator

This project fetches the Billboard Hot 100 songs for a given date and creates a Spotify playlist using the Spotify API. It was created as part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu on Udemy.

## Description

This Python script allows users to:

1. Enter a date (in `YYYY-MM-DD` format).
2. Fetch the Billboard Hot 100 chart for that date.
3. Search for those songs on Spotify.
4. Create a private playlist on Spotify and add the songs to it.

## Features

- Scrapes the Billboard Hot 100 list for a specific date.
- Searches for the songs on Spotify using the Spotipy library.
- Creates a private playlist on Spotify with the found tracks.

## Installation

To run this project, you'll need the following dependencies:

1. Install the required libraries:

```bash
pip install requests beautifulsoup4 spotipy
```

2. You will also need to set up your Spotify Developer Application to get your CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI for the authentication process.

## How to Use

1. Clone this repository:
```bash
git clone https://github.com/your-username/billboard-hot-100-playlist-creator.git
```

2. Enter your Spotify API credentials in the script (CLIENT_ID, CLIENT_SECRET, REDIRECT_URI).

3. Run the script:
```bash
python playlist_creator.py
```

4. Enter a date in the YYYY-MM-DD format when prompted. For example:
```bash
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2000-08-12
```

5. A private Spotify playlist will be created with the name YYYY-MM-DD Billboard 100 containing the top songs from that day.

## Notes

- The script assumes that the songs listed on the Billboard Hot 100 are available on Spotify. If a song is not found, it will be skipped.
- Ensure that your Spotify account is linked with the application and has the necessary permissions to create playlists.

## Acknowledgements

- The Billboard Hot 100 data is fetched using BeautifulSoup.
- Spotipy is used to interact with the Spotify API.
- This project was completed as part of 100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu on Udemy.
