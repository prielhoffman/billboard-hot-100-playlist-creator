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
