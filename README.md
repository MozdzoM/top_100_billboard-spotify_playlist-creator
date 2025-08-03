# Top 100 Billboard - Spotify Playlist Creator 🎵

This Python script allows you to generate a Spotify playlist with the top 100 Billboard songs from a specified date.

## Features

- Scrapes the Billboard Hot 100 chart for a given date
- Searches each song on Spotify
- Creates a private Spotify playlist with found songs
- Holds environmental variables in a separate file
- Creates `.txt` files with list of song uri's that you can share

## Requirements

- Python 3.7+
- Spotify Developer account (to obtain API credentials)
- A `.env` file containing your Spotify credentials

## Setup

### 1. Create a Spotify Developer Account

If you don't already have one, create a [Spotify account](https://spotify.com/) and then:

- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Log in and click **"Create an App"**
- Give your app a name and description
- Use https://example.com/ as redirect URI
- Accept the terms and create the app
- You will now see your **Client ID** and **Client Secret**

### 2. Clone the repository

```bash
git clone https://github.com/MozdzoM/top_100_billboard-spotify_playlist-creator.git
cd top_100_billboard-spotify_playlist-creator
```

### 3. Configure .env and do a 1st run
-  Copy your **Client ID** and **Client Secret** and paste them to `.env`
```bash
echo "SPOTIFY_CLIENT_ID=your_id" >> .env
echo "SPOTIFY_CLIENT_SECRET=your_secret" >> .env
```

### 4. First run
- If configured properly, on first run you should be asked to agree that **the 
  app can take actions in Spotify on your behalf**
- Then it will take you to the page, example.com and you need to copy the 
  entire URL in the address bar and paste it to the CLI

After these steps you should be able to use the app freely

## License

MIT License
